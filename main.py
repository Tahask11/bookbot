import sys
from stats import word_count, stats, sorted_dict

def get_book_text(path):
    with open(path) as f:
        return f.read()

def main():
    
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    content = get_book_text(book_path)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}")
    
    wc = word_count(content)
    print("----------- Word Count ----------")
    print(f"Found {wc} total words")

    cd = stats(content)

    print("--------- Character Count -------")
    sorted_cd = sorted_dict(cd)

    for item in sorted_cd:
        print(f"{item["char"]}: {item["num"]}")
    print("============= END ===============")


main()



