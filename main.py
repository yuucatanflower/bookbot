def book():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    print(file_contents)
    return file_contents

def count_words(book):
    l = len(book)
    print(f"The book contains {l} words.")

book()

count_words(book().split())