#!/usr/bin/env python3
import sys
import re
import argparse
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


def make_heading_text(stack):
    return ": ".join(text for _, text in stack)


def heading_to_filename(heading_text):
    name = re.sub(r"\s*:\s*", ":", heading_text).replace(" ", "_").replace(":", "--")
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
    leaf_sections = find_leaf_sections(sections)

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

        print(f"Created: {output_path}")

    print(f"\nDone: {len(leaf_sections)} file(s) written to {output_dir}")


if __name__ == "__main__":
    main()
