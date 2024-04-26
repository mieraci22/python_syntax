def print_upper_words(words):
    """Returns Words in ALL CAPS"""
    for word in words:
        print(word.upper())

def print_upper_words2(words):
    """print each word on new line, uppercased, if starts with E or e"""
    for word in words:
        if word.startsswith('e') or word.startswith('E'):
            print(word.upper())

def print_upper_words3(words, must_start_with):
    """Print each word on new line, uppercased, if starts with given letter"""
    for word in words:
        for letter in must_start_with:
            if word.startswith(letter):
                print(word.upper())
                break
    
