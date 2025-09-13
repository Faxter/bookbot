import sys

from stats import count_characters, count_words, sort_characters


def get_book_text(path):
    text = ""
    with open(path) as f:
        text = f.read()
    return text


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    print("============ BOOKBOT ============")
    book = sys.argv[1]
    print(f"Analyzing book found at {book}...")
    book_text = get_book_text(book)

    print("----------- Word Count ----------")
    num_words = count_words(book_text)
    print(f"Found {num_words} total words")

    print("--------- Character Count -------")
    num_chars = count_characters(book_text)
    char_report = sort_characters(num_chars)
    for entry in char_report:
        if entry["char"].isalpha():
            print(f"{entry['char']}: {entry['num']}")

    print("============= END ===============")


if __name__ == "__main__":
    main()
