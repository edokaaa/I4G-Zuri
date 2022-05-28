# A program to count the number of words in a given text
# using python's builtin len() and split() functions


text = 'I thank I4G and Zuri for this opportunity to learn.'

result = len(text.split())
# the split() will return a list containing the words of the string
# the len() with return the number of items in the list

print("There are " + str(result) + " words.")

