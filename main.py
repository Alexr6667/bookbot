from stats import get_book_text, get_character_count
import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        book_dir = sys.argv[1]
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_dir}...")
    print("---------- Word Count ----------")
    get_book_text(book_dir)
    print("------- Character Count -------")
    get_character_count(book_dir)

main()
