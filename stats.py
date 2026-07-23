def word_count(book_content):
    return len(book_content.split())

def char_count(book_content):
    char_count = {}
    for char in book_content:
        lowered_char = char.lower()
        char_count[lowered_char] = char_count.get(lowered_char, 0) + 1
    return char_count

def sort_on(char_count_tuple):
    return char_count_tuple[1]

def chars_dict_to_sorted_list(chars_dict):
    chars_list = []
    for char in chars_dict:
        count = chars_dict[char]
        chars_list.append((char, count))
    return sorted(chars_list, key=sort_on, reverse=True)