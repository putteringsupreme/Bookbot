def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    lower_case = convert_lower(text)
    num_words = get_num_words(text)
    word_list = lower_case.split()
    letter_counts = {"a": 0,"b": 0,"c": 0,"d": 0,"e": 0,"f": 0,"g": 0,"h": 0,"i": 0,"j": 0,"k": 0,
                     "l": 0,"m": 0,"n": 0,"o": 0,"p": 0,"q": 0,"r": 0,"s": 0,"t": 0,"u": 0,"v": 0,
                     "w": 0,"x": 0,"y": 0,"z": 0}
    for word in word_list: 
        letters = list(word)
        for letter in letters:
            if letter in letter_counts:
                letter_counts[letter] += 1
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{num_words} words found in the document")
    print("")
    for key in letter_counts:
        print(f"The '{key}' character was found {letter_counts[key]} times")
    print("--- End report ---")


def get_num_words(text):
    words = text.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()
        
def convert_lower(string):
    lower_string = string.lower()
    return lower_string


main()
