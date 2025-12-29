from stats import get_letter_map, get_report, get_word_count


def get_file_content(path: str):
    with open(path) as file:
        content = file.read()

        return content


def main():
    path = "./books/frankenstein.txt"
    content = get_file_content(path)
    word_count = get_word_count(content)
    letter_map = get_letter_map(content)
    report = get_report(word_count, letter_map)

    # print(f"Found {word_count} total words")
    # print(f"{letter_map}")


main()
