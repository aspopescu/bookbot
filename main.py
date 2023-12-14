book_path="books/frankenstein.txt"

def get_book_text(path): 
    with open(path) as f:
        return f.read()

book_text = get_book_text(book_path)

def get_num_words(text):
    words = text.split()
    return len(words)

# print(f"word count is {get_num_words(book_text)}")

def get_num_letters(text):
    count_characters = {}
    for character in text.lower():
        if character in count_characters:
            count_characters[character] += 1
        else:
            count_characters[character] = 1
    return count_characters

count_chars = get_num_letters(book_text)

# print(f"characters count dictionary is {count_chars}")

def order_dictionary(dictionary):
    list_of_characters = []
    for item in dictionary.items():
        if item[0].isalpha():
            list_of_characters.append(item)
    def get_count(e):
        return e[1]
    list_of_characters.sort(key=get_count, reverse=True)
    # print(list_of_characters)
    for character in list_of_characters:
        print(f"The '{character[0]}' character was found {character[1]} times")

def create_report():
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{get_num_words(book_text)} words found in the document")
    print()
    order_dictionary(count_chars)
    print()
    print("--- End of report of books/frankenstein.txt ---")

create_report()
