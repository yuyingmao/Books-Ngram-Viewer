__author__ = 'Yuying Mao'
"""
Author: <<< Yuying Mao >>>
Language: Python 3
Purpose:compute the distribution of word lengths and the five
    number summary of those word lengths.
"""
from wordData import *
from boxAndWhisker import *

def findNum(lst,num):
    """
    finds the length of words in particular amount of words is given.
    :param lst:the lst with the length of word and the counts of times it appears.
    :param num: the particular amount of words.
    :return: the length of words in particular amount of words is given.
    """
    if num>lst[0][1]:
        num-=lst[0][1]
        return findNum(lst[1:],num)
    else:
        return lst[0][0]

def summaryFromWords(words,year):
    """
    compute the distribution of word lengths and the five number summary of
        those word lengths.
    :param words: a dictionary mapping words to lists of YearCount objects.
    :param year: a natural number representing the year of interest.
    :return: a five-tuple containing five numbers representing the five number summary.
    """
    has=False
    lst=[]
    map={}
    num=0
    for word in words:
        w=words[word]
        for yc in w:
            if yc.year==year:
                has=True
                num=yc.count
        if has==True and num!=0:
            lst.append((word,num))
        has=False
    for ch in lst:
        if len(ch[0]) not in map:
            map[len(ch[0])]=ch[1]
        else:
            map[len(ch[0])]+=ch[1]
    items=sorted(set(map.items()))
    total=0
    for value in map:
        total+=map[value]
    min=items[0][0]
    q1=findNum(items,total//4)
    med=findNum(items,total//2)
    q3=findNum(items,total//4*3)
    max=items[-1][0]
    fiveList=(min,q1,med,q3,max)
    return fiveList

if __name__ == '__main__':
    #prompt user for a file name and year.
    file=input("Enter a file name: ")
    year=int(input("Enter a year: "))

    words =readWordFile(file)
    lst=summaryFromWords(words,year)
    #display the five number summary of the distribution of lengths for that year.
    print("minimum:",lst[0])
    print("first quartile:",lst[1])
    print("median:",lst[2])
    print("third quartile:",lst[3])
    print("maximum:",lst[4])

    #generate the associated box-and-whisker plot.
    boxAndWhisker(lst[0],lst[1],lst[2],lst[3],lst[4])

