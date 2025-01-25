def book():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    return file_contents

def count_words(book):
    l = len(book.split())
    print(f"{l} words found in the document")

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
        if c['char'].isalpha():
            print(f"The '{c['char']}' character was found {c['count']} times")

    return char_list


# print(book())

# count_words(book())

def main():
    print("--- Begin report of books/frankenstein.txt ---")
    text = book()  # store the book contents once
    count_words(text)
    print()  # blank line
    count_characters(text)  # this should print all characters including 'e'
    print("--- End report ---")

main()  # only call this once