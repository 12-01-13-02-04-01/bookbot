#!../.venv/bin/python

import asyncio as aio
import sys

import tts

# from stats import (  # pyright: ignore[reportUnknownVariableType]
#     get_letter_map,
#     get_report,
#     get_word_count,
# )


def get_content(path: str):
    with open(path) as file:
        content = file.read()

        return content


# Use method to get next chapter.
# - needs to track chapter of given book
def get_chapter():
    pass


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path = sys.argv[1]
    content = get_content(path)
    title = sys.argv[1].split("/")[1].split(".")
    tts.make_file(content, title[0])


main()
