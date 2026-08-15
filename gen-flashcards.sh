#!/usr/bin/env sh

rm -f flashcards/teoria_numeros/*.md

for F in $(ls teoria_numeros/*.md)
do
    python split_markdown.py $F flashcards/teoria_numeros/
done
