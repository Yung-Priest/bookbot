import sys
def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents

def num_words(file_contents):
    return  len(file_contents.split())

def book_dictionary(text):
    char_count = {}
    for character in text.lower():
        if character not in char_count:
            char_count[character] = 1
        else:
            char_count[character] += 1
    return char_count
def sort_on(item):
    return item["num"]

def dictionary_list(char_count):
    counts_list = []
    for char, count in char_count.items():
        counts_list.append({"char": char, "num": count})
    counts_list.sort(reverse=True, key=sort_on)
    return counts_list
   

def stats():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        text = get_book_text(sys.argv[1])
    number = num_words(text)
    dictionary = book_dictionary(text)
    sorted_list = dictionary_list(dictionary)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}")
    print("----------- Word Count ----------")
    print(f"Found {number} total words")
    print('--------- Character Count -------')
    for items in sorted_list:
        if items["char"].isalpha():
            print(f"{items['char']}: {items['num']}")
    print('============= END ===============')

stats()