__author__ = 'Yuying Mao'
"""
Author: <<< Yuying Mao >>>
Language: Python 3
Purpose:A supporting module, includes class definitions and utility functions
    that reads information from file and calculates the total frequency a word
    has appeared.
"""

from rit_lib import *

class YearCount(struct):
    """
    a YearCount class which has two slots:year and count.
    """
    _slots=((int,"year"),(int,"count"))

class WordTrend(struct):
    """
    a WordTrend class which has two slots: word and trend.
    """
    _slots=((str,"word"),(float,"trend"))

def readWordFile(filename):
    """
    reads the information from a file and finally returns a dictionary full filled with information.
    :param filename: a string giving the name of a unigram data file.
    :return: a dictionary mapping words to lists of YearCount object.
    """
    file=open("data/"+filename)
    map=dict()
    year=list()
    word=""
    for line in file:
        line=line.strip("\n")
        line=line.split(",")
        if len(line)==1:
            word=line[0]
            year=list()
        elif len(line)==2:
            year.append(YearCount(int(line[0]),int(line[1])))
            map[word]=year
    file.close()
    return map

def totalOccurrences(word,map):
    """
    the function that calculates the total frequency of a word.
    :param word: the word for which to calculate the count.not guaranteed to exist in words.
    :param map: a dictionary mapping words to lists of YearCount objects.
    :return: the total number of times that a word has appeared in print.
    """
    total=0
    if word in map:
        w=map[word]
        for num in w:
            total+=num.count
    else:
        total=0
    return total

if __name__ == '__main__':
    #Prompt user to enter the file name.
    file=input("Enter a file name: ")

    #prompt user to enter the word he want to search.
    word=input("Enter a word: ")

    print("Total occurrences of",word,":",totalOccurrences(word,readWordFile(file)))