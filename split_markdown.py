#!/usr/bin/env python3
import sys
import re
import argparse
import unicodedata
from pathlib import Path


def parse_heading(line):
    match = re.match(r"^(#{1,6})\s+(.+)$", line.rstrip())
    if match:
        return len(match.group(1)), match.group(2).strip()
    return None, None


def split_into_sections(lines):
    """Return list of (heading_stack, content_lines).

    heading_stack is a list of (level, text) tuples representing the full
    ancestor path to this section. content_lines is everything between this
    heading and the next one.
    """
    sections = []
    current_stack = []
    current_content = []

    for line in lines:
        level, text = parse_heading(line)
        if level is not None:
            if current_stack:
                sections.append((list(current_stack), list(current_content)))
            current_content = []
            while current_stack and current_stack[-1][0] >= level:
                current_stack.pop()
            current_stack.append((level, text))
        else:
            if current_stack:
                current_content.append(line)

    if current_stack:
        sections.append((list(current_stack), list(current_content)))

    return sections


def find_leaf_sections(sections):
    """Return only sections that have no sub-sections."""
    leaf_sections = []
    for i, (stack, content) in enumerate(sections):
        is_leaf = True
        for j, (other_stack, _) in enumerate(sections):
            if j == i or len(other_stack) <= len(stack):
                continue
            if all(other_stack[k] == stack[k] for k in range(len(stack))):
                is_leaf = False
                break
        if is_leaf:
            leaf_sections.append((stack, content))
    return leaf_sections


TAG_LINE = re.compile(r"^\s*#[^\s#]+(\s+#[^\s#]+)*\s*$")


def extract_trailing_tags(content):
    """Split trailing tag lines ("#tag1 #tag2") off the end of content.

    Returns (content_without_tags, tags). Blank lines between tag lines are
    ignored.
    """
    content = list(content)
    tag_lines = []
    while content and (content[-1].strip() == "" or TAG_LINE.match(content[-1])):
        line = content.pop()
        if line.strip():
            tag_lines.insert(0, line)
    tags = [tag[1:] for line in tag_lines for tag in line.split()]
    return content, tags


def collect_tags(sections):
    """Strip trailing tags from every section.

    Returns (sections, tag_scopes) where tag_scopes is a list of
    (scope_stack, tags). Tags apply to the section where they appear and to
    all of its sub-sections.
    """
    stripped = []
    tag_scopes = []
    for stack, content in sections:
        content, tags = extract_trailing_tags(content)
        stripped.append((stack, content))
        if tags:
            tag_scopes.append((stack, tags))
    return stripped, tag_scopes


def tags_for(stack, tag_scopes, default_tags):
    tags = list(default_tags)
    for scope, items in tag_scopes:
        if stack[: len(scope)] == scope:
            tags.extend(items)
    return list(dict.fromkeys(tags))


def make_heading_text(stack):
    return ": ".join(text for _, text in stack)


def heading_to_filename(heading_text):
    name = unicodedata.normalize("NFKD", heading_text)
    name = name.encode("ascii", "ignore").decode("ascii")
    name = re.sub(r"\s*:\s*", ":", name).replace(" ", "_").replace(":", "--")
    name = re.sub(r"[^\w\-.]", "_", name)
    name = re.sub(r"_+", "_", name)
    name = name.strip("_")
    return name + ".md"


def main():
    parser = argparse.ArgumentParser(
        description="Split a markdown file into one file per leaf section."
    )
    parser.add_argument("input", help="Input markdown file")
    parser.add_argument(
        "output_dir", help="Directory where output files will be created"
    )
    args = parser.parse_args()

    input_path = Path(args.input)
    output_dir = Path(args.output_dir)

    if not input_path.exists():
        print(f"Error: {input_path} does not exist", file=sys.stderr)
        sys.exit(1)

    output_dir.mkdir(parents=True, exist_ok=True)

    with open(input_path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    sections = split_into_sections(lines)
    sections, tag_scopes = collect_tags(sections)
    leaf_sections = find_leaf_sections(sections)
    default_tags = [output_dir.resolve().name, input_path.stem]

    for stack, content in leaf_sections:
        heading_text = make_heading_text(stack)
        filename = heading_to_filename(heading_text)
        output_path = output_dir / filename

        # Strip trailing blank lines
        while content and content[-1].strip() == "":
            content.pop()

        with open(output_path, "w", encoding="utf-8") as f:
            f.write(f"# {heading_text}\n")
            if content:
                f.write("\n")
                f.writelines(content)

            tags = tags_for(stack, tag_scopes, default_tags)
            f.write("\n## Tags\n\n")
            f.writelines(f"- {tag}\n" for tag in tags)

        print(f"Created: {output_path}")

    print(f"\nDone: {len(leaf_sections)} file(s) written to {output_dir}")


if __name__ == "__main__":
    main()
