import sys

from stats import word_count, char_count, chars_dict_to_sorted_list

def get_book_text(book_path):
    with open(book_path, 'r') as f:
        return f.read()

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    book_content = get_book_text(book_path)
    chars_counted = char_count(book_content)
    sorted_chars = chars_dict_to_sorted_list(chars_counted)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count(book_content)} total words")
    print("--------- Character Count -------")
    for char, count in sorted_chars:
        if char.isalpha():
            print(f"{char}: {count}")
    print("============= END ===============")

if __name__ == '__main__':
    main()
