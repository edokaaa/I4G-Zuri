# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

def read_file_content(filename):
    with open(filename) as f:
        content = f.read()
    return content


def count_words():
    text = read_file_content("./story.txt")
    my_dict = {}
    word_list = text.split()
    for word in word_list:
        if word in my_dict:
            my_dict[word] += 1
        else:
            my_dict[word] = 1
    print(my_dict)



count_words()
