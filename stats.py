def get_text(dir):
    file_contents = None
    with open(dir, 'r') as f:
        file_contents = f.read()
    return file_contents


def get_book_text(dir):
    book_text = get_text(dir)
    print (f"Found {len(book_text.split())} total words")


def get_character_count(dir):
    alpha_dict = {}
    book_text = get_text(dir).lower()
    for char in book_text:
        if char.isalpha() and char not in alpha_dict.keys():
            alpha_dict[char] = book_text.count(char)
    sorted_keys = sorted(alpha_dict, key=alpha_dict.get, reverse=True)
    for val in sorted_keys:
        print (f"{val}: {alpha_dict[val]}")