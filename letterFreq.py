__author__ = 'Yuying Mao'
"""
Author: <<< Yuying Mao >>>
Language: Python 3
Purpose: computes the relative frequency of English characters occurring in print.
"""
from wordData import *

def letterFreq(words):
    """
    computes the relative frequency of English characters occurring in print.
    :param words: a dictionary mapping words to lists of YearCount objects.
    :return: a string containing the 26 lowercase characters in the English
        alphabet, sorted in decreasing order of frequency of occurrence of each character.
    """
    map={}
    lst=[]
    most=""
    word=words.keys()
    for w in word:
        total=totalOccurrences(w,words)
        for ch in w:
            if ch not in map:
                map[ch]=1
            else:
                map[ch]+=1*total
    for key in map:
        lst.append((key,map[key]))
    lst.sort(key=lambda tup:tup[1])
    for letter in lst:
        ch=letter[0]
        most=ch+most
    return most

if __name__ == '__main__':
    #prompt user to enter a file name.
    words =readWordFile(input("Enter a file name: "))

    print("Letter sorted by decreasing frequency:",letterFreq(words))