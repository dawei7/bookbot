def main():
    with open("./books/frankenstein.txt") as f:
        file_contents = f.read()

    words = file_contents.split()
    dict_letters = {}

    for word in words:
        for letter in word.lower():
            if not letter.isalpha():
                continue
            if letter not in dict_letters:
                dict_letters[letter] = 1
            else:
                dict_letters[letter] += 1

    print(f"{len(words)} words found in the document")

    for k,v in sorted(dict_letters.items(), key=lambda item: item[1], reverse=True):
        print(f"The '{k}' character was found {v} times")

main()