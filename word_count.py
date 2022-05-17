# A function to count the number of words in a given text

def word_count(text):
    num_of_spaces = 0
    for letter in text:
        if letter == ' ':
            num_of_spaces += 1
    words = num_of_spaces + 1
    print(f"The number of words in the text is: {words}\n")

text = 'I thank I4G and Zuri for this opportunity to learn.'

word_count(text)
