def vowels(word):
    number_of_vowels = 0
    the_vowels = ["a", "e", "i", "o", "u"]
    for letter in word.lower():
        if letter in the_vowels:
            number_of_vowels += 1
    return number_of_vowels







if __name__ == '__main__':

    word1 = 'saucybegger'

    count = vowels(word1)
    print(count) 



