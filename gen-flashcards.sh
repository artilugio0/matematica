#!/usr/bin/env sh

decks=(
    "teoria_numeros"
    "algebra_lineal"
)


for DECK in ${decks[@]}
do
    rm -fr "./flashcards/${DECK}"
    mkdir "./flashcards/${DECK}"

    for F in $(ls "${DECK}"/*.md)
    do
        python split_markdown.py "${F}" "flashcards/${DECK}/"
    done
done
