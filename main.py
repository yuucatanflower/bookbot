def book():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    print(file_contents)
    return file_contents

def count_words(book):
    l = len(book.split())
    print(f"The book contains {l} words.")

def count_characters(book):
    lowercase = book.lower()
    char_dic = {

    }

    for word in lowercase:
        for char in word:
            if char not in char_dic:
                char_dic[char]=1
            else: char_dic[char]+=1
    return char_dic


book()

count_words(book())

print(count_characters(book()))