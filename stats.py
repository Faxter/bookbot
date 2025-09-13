def count_words(text: str):
    return len(text.split())


def count_characters(text: str):
    char_map = {}
    for char in text.lower():
        if char in char_map:
            char_map[char] += 1
        else:
            char_map[char] = 1
    return char_map


def sort_on_count(d: dict):
    return d["num"]


def sort_characters(map: dict[str, int]):
    result = []
    for char in map:
        a = {}
        a["char"] = char
        a["num"] = map[char]
        result.append(a)
    result.sort(reverse=True, key=sort_on_count)
    return result
