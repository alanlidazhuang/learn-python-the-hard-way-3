def break_words(stuff):
    """This function will break up words for us."""
    words = stuff.split(' ')                 #通过指定的分隔符对字符中进行切片，split()有两个参数比如，str.split(" ", 2)可以这样理解，把str按空格分隔一次，返回列表格式，代码中没有数字参数，就是分隔到底
    return words

def sort_words(words):
    """Sorts the words."""
    return sorted(words)    

def print_first_word(words):
    """Prints the first word after poppong it off."""
    word = words.pop(0)
    print(word)

def print_last_word(words):
    """Prints the last word after poppong it off."""
    word = words.pop(-1)
    print(word)

def sort_sentence(sentence):
    """Takes in a full sentence and returns the sorted words."""
    words = break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence):
    """Prints the first and the last words of the sentence."""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    """Sorts the words then prints the first and last one."""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)







