def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    char_list = get_list_chars(text)
    lowered_list = get_list_lowered(char_list)
    num_char = get_num_char(lowered_list)
    sorted_list = char_sorting(num_char)
    
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    print()

    for item in sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found '{item['num']}' times")

    print(f"--- End report ---")

def get_num_words(text):
    words = text.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_list_chars(text):
    lst = []
    for char in text:
        lst.append(char)
    return lst

def get_list_lowered(char_list):
    lowered_list = []
    for char in char_list:
        lowered_list.append(char.lower())
    return lowered_list

def get_num_char(lowered_list):
    char_dict = {}
    for char in lowered_list:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    return char_dict

def sort_on(d):
    return d["num"]

def char_sorting(num_char):
    sorted_list = []
    for ch in num_char:
        sorted_list.append({"char": ch, "num": num_char[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list





if __name__ == "__main__":
    main()