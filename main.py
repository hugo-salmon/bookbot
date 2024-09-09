def count_words(text):
    words = text.split()  
    return len(words)    

def count_characters(text):
    char_count = {}  
    text = text.lower()  
    
    for char in text:
        if char.isalpha():  
            if char in char_count:
                char_count[char] += 1  
            else:
                char_count[char] = 1   

    sorted_char_count = sorted(char_count.items(), key=lambda x: x[1], reverse=True)

    return sorted_char_count  

def main():
    with open('books/frankenstein.txt', 'r') as f:
        file_contents = f.read()

    word_count = count_words(file_contents)
    print(f"Le livre 'Frankenstein' contient {word_count} mots.")
    
    character_count = count_characters(file_contents)
    print("Nombre d'occurrences de chaque caractère (trié par ordre décroissant) :")
    print(character_count)

if __name__ == "__main__":
    main()
