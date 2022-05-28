# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}


def read_file_content(filename):
    with open(filename) as f:
        content = f.read()
    return content


# a function to remove any puntuation in our text

def remove_punctuations(text):
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    for x in text:
        if x in punctuations:
            text = text.replace(x, '')
    return text

def count_words():
    text = read_file_content("./story.txt")
    cleaned_text = remove_punctuations(text)
    my_dict = {}
    word_list = cleaned_text.split()
    for word in word_list:
        my_dict[word] = word_list.count(word)
    print(my_dict)

count_words()
