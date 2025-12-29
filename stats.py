def get_word_count(content: str):
    words = content.split()

    word_count = 0
    for word in words:
        word_count += 1

    return word_count


def get_letter_map(content: str):
    map = {}

    for char in content:
        char = char.lower()
        if char not in map:
            map[char] = 1
        else:
            map[char] += 1

    return map


def sort_map(item):
    return item["num"]


def get_report(word_count: int, map: dict):
    char_count_list = []
    print("============ BOOKBOT ============")
    print("Analyzing book found at /books/frankenstein")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")

    for key in map:
        char_count_list.append({"char": key, "num": map[key]})

    char_count_list.sort(key=sort_map, reverse=True)
    for item in char_count_list:
        if item["char"].isalpha():
            print(f"{item['char']}: {item['num']}")

    print("============= END ===============")
