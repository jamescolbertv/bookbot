def main():
    print("--- Begin report of books/frankenstein.txt ---")
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    count_words(file_contents)
    count_letters(file_contents)
    print("--- End report ---")
    
def count_words(text):
    word_list = text.split()
    print(f"{len(word_list)} words found in the document\n")
    
def count_letters(text):
    letter_count = {}
    for letter in text:
        if letter.isalpha():
            if letter.lower() in letter_count.keys():
                letter_count[letter.lower()] += 1
            else:
                letter_count[letter.lower()] = 1
    counts_only = list(letter_count.values())
    counts_only.sort(reverse=True)
    for count in counts_only:
        for letter in letter_count:
            if count == letter_count[letter]:
                print(f"The '{letter}' character was found {count} times")

if __name__=="__main__":
    main()