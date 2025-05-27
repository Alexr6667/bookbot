from stats import get_book_text, get_character_count

def main():
    book = "frankenstein.txt"
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at books/{book}...")
    print("---------- Word Count ----------")
    get_book_text(f"./books/{book}")
    print("------- Character Count -------")
    get_character_count(f"./books/{book}")

main()
