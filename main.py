def main():
    with open('books/frankenstein.txt') as f:
        file_contents = f.read()
    print(file_contents)

def get_book_text(path):
    with open(path) as f:
        return f.read()
        
main()