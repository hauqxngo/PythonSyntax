# 1. For a list of words, print out each word on a separate line, but in all uppercase. How can you change a word to uppercase? Ask Python for help on what you can do with strings!

# 2. Turn that into a function, print_upper_words. Test it out. (Don’t forget to add a docstring to your function!)

def print_upper_words(words):
    """Print out each word on a separate line in all uppercase."""

    for word in words:
        print(word.upper())

# 3. Change that function so that it only prints words that start with the letter ‘e’ (either upper or lowercase).

def print_upper_words_e(words):
    """Print words that start with the letter ‘e’ (either upper or lowercase) on a separate line in all uppercase."""

    for word in words:
        if word.startswith("E") or word.startswith("e"):
            print(word.upper())

# 4. Make your function more general: you should be able to pass in a set of letters, and it only prints words that start with one of those letters.

def print_upper_words_x(words, must_start_with):
    """You should be able to pass in a set of letters, and it only prints words that start with one of those letters on a separate line in all uppercase."""

    for word in words:
        for letter in must_start_with:
            if word.startswith(letter):
                print(word.upper())
                break
