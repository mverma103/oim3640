def uses_only(word, letters):
    """Does word use only the allowed letters?"""
    for letter in word:
        if letter not in letters:
            return False
    return True

##print(uses_only('cake', 'kcboela'))
##print(uses_only('babson', 'kcboela'))

def must_use(word, letter):
    """Does word use the required letter?"""
    for char in word:
        if char == letter:
            return True
    return False

##print(must_use('cake', 'a'))
##print(must_use('babson', 'a'))

def is_valid(word, letters, required):
    """Is word valid?"""
    return uses_only(word, letters) and must_use(word, required) and len (word) >= 4

def find_words(letters, required):
    """print all valid words"""
    with open("data/words.txt") as word_file:
        for word in word_file:
            word = word.strip()
            if is_valid(word, letters, required):
                print(word)


def main():
    print(is_valid('cake', 'kcboela', 'a'))
    print(is_valid('babson', 'kcboela', 'a'))

if __name__ == "__main__":
    main()