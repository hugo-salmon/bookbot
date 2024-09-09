def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    char_count = {}
    text = text.lower()

    for char in text:
        if char.isalpha():
            if char in char_count:
                char_count[char]+=1
            else:
                char_count[char] = 1

    sorted_char_count = sorted(char_count.items(), key=lambda x: x[1], reverse=True)
    
    for char, count in sorted_char_count:
        print(f"Le caractère '{char}' a été trouvé {count} fois")

def main():
    with open('books/frankenstein.txt', 'r') as f:
        file_contents = f.read()
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{count_words(file_contents)} mots ont été trouvés dans le document")
    count_characters(file_contents)
    print("--- End report ---")

main()
