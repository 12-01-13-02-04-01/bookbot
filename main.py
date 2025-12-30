import sys

from stats import (  # pyright: ignore[reportUnknownVariableType]

    get_letter_map,
    get_report,
    get_word_count,
)


def get_file_content(path: str):
    with open(path) as file:
        content = file.read()

        return content


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path = sys.argv[1]
    content = get_file_content(path)
    word_count = get_word_count(content)
    letter_map = get_letter_map(content)  # pyright: ignore[reportUnknownVariableType]
    get_report(word_count, letter_map)  # pyright: ignore[reportUnknownArgumentType]


main()
