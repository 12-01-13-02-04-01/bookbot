def get_word_count(content: str):
    words = content.split()

    word_count = 0
    for word in words:  # pyright: ignore[reportUnusedVariable]
        word_count += 1

    return word_count


def get_letter_map(content: str):  # pyright: ignore[reportUnknownParameterType]
    map = {}

    for char in content:
        char = char.lower()
        if char not in map:
            map[char] = 1
        else:
            map[char] += 1

    return map  # pyright: ignore[reportUnknownVariableType]


def sort_key(item):  # pyright: ignore[reportUnknownParameterType, reportMissingParameterType]
    return item["num"]  # pyright: ignore[reportUnknownVariableType]


def get_report(word_count: int, map: dict[str, int]):
    char_count_list = []
    print("============ BOOKBOT ============")
    print("Analyzing book found at /books/frankenstein")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")

    for key in map:
        char_count_list.append({"char": key, "num": map[key]})  # pyright: ignore[reportUnknownMemberType]

    char_count_list.sort(key=sort_key, reverse=True)  # pyright: ignore[reportUnknownMemberType]
    for item in char_count_list:  # pyright: ignore[reportUnknownVariableType]
        if item["char"].isalpha():  # pyright: ignore[reportUnknownMemberType]
            print(f"{item['char']}: {item['num']}")

    print("============= END ===============")
