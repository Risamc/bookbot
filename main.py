from collections import Counter

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_of_words = get_num_of_words(text)
    num_of_chars = count_chars(text)
    
    #book report
    print(str(num_of_words)+ " words found in this document")
    for Key, Value in num_of_chars.items():
        print("The character " + "'" + Key + "'" + " is in the text " + str(Value) + " times.")
    print("----end_of_report----")
    #end of book report

def get_num_of_words(text):
    num_of_words = len(text.split())
    return num_of_words

def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_chars(text):
    lowered_text = text.lower()
    counted_chars = Counter(lowered_text)
    return counted_chars 

main()