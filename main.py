def book():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    print(file_contents)
    return file_contents

def count_words(book):
    l = len(book.split())
    print(f"The book contains {l} words.")

def sort_on(dict):
    return dict["count"]

def count_characters(book):
    lowercase = book.lower()
    char_dic = {

    }

    for word in lowercase:
        for char in word:
            if char not in char_dic:
                char_dic[char]=1
            else: char_dic[char]+=1

    # sorted_dict = {key: value for key, value in sorted(char_dic.items())}

    char_list = []

    for char, count in char_dic.items():
        char_list.append({"char": char, "count": count})

    char_list.sort(reverse=True, key=sort_on)

    for c in char_list:
        if c["char"].isalpha():
            print(f"The '{c["char"]}' character was found {c["count"]} times")

    return char_list


book()

count_words(book())

count_characters(book())