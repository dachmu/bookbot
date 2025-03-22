from stats import gen_report, get_num_words, char_count_summary, sort_chars_by_count
import sys

def get_book_text(path):
    with open(path) as book:
        book_content = book.read()
        return book_content

def main():

    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)


    content = get_book_text(sys.argv[1])
    num_words = get_num_words(content)
    char_count = char_count_summary(content)

    

    # print(char_count)
    sorted_chars = sort_chars_by_count(char_count)

    # print(sorted_chars)
    report = gen_report(sorted_chars, num_words, sys.argv[1])

main()
