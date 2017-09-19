__author__ = 'Yuying Mao'
"""
Author: <<< Yuying Mao >>>
Language: Python 3
Purpose: computes the top and bottom trending words between a given
    starting and ending year.
"""
from wordData import *

def trending(words,startYr,endYr):
    """
    calculates the ratio of the number of times the word appeared in the ending year
        and the number of times the word appeared in the starting year.
    :param words: a dictionary mapping wordsto lists of YearCount objects.
    :param startYr: an integer, the starting year for the computation of the trending words,
    :param endYr: an integer, the ending year for the computation of the tredning words.
    :return: a list containng a WordTrend entry for each word for which qualifying data exists.
    """
    if startYr>=endYr:
        print("startYear is equal or larger than the endYear!")
        exit()
    lst=[]
    yearList=[]
    for word in words:
        w=words[word]
        k=1
        j=0
        hasEnough = True
        for i in w:
            if (i.year==startYr or i.year==endYr) and i.count<1000:
                hasEnough=False
            elif i.year==startYr:
                k=i.count
            elif i.year==endYr:
                j=i.count
        if hasEnough==True and j!=0 and k!=1:
            lst.append((word,j/k))
    lst.sort(key=lambda tup:tup[1])
    while len(lst)>0:
        yearList.append(WordTrend(str(lst[-1][0]),float(lst[-1][1])))
        lst=lst[:-1]
    return yearList

if __name__ == '__main__':
    #prompt the user to enter the file name.
    file=input("Enter a file name: ")

    #prompt the user to enter the starting year and ending year.
    startYr=int(input("Enter the starting year: "))
    endYr=int(input("Enter the ending year: "))

    words = readWordFile(file)
    lst=trending(words,startYr,endYr)
    print(lst)
    i=0
    #output the top 10 trending words in that timespan.
    print("The top 10 trending words from",startYr,"to",endYr,":")
    while i<10:
        print(lst[i].word)
        i+=1

    i=-1
    #output the bottom 10 trending words in that timespan.
    print("\nThe bottom 10 trending words from",startYr,"to",endYr,":")
    while i>-11:
        print(lst[i].word)
        i-=1



