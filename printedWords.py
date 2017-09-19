__author__ = 'Yuying Mao'
"""
Author: <<< Yuying Mao >>>
Language: Python 3
Purpose: computes the total number of printed words for each year.
"""
from wordData import *
from simplePlot import *

def printedWords(words):
    """
    calculates the total words printed each year, and return a list contains those data.
    :param words:  a dictionary mapping words to lists of YearCount objects.
    :return: a list containing a YearCount entry for which data exists.
    """
    map={}
    lst=[]
    values=words.values()
    for value in values:
        for v in value:
            if v.year not in map:
                map[v.year]=v.count
            else:
                map[v.year]+=v.count
    years=sorted(set(map.items()))
    for year in years:
        lst.append(YearCount(year[0],year[1]))
    return lst

def wordsForYear(year,yearList):
    for y in yearList:
        if y.year==year:
            return y.count
    return 0

if __name__ == '__main__':
    #prompt user to enter a file name.
    words = readWordFile(input("Enter a file name: "))

    #prompt user to enter a year to count.
    year=int(input("Enter year: "))

    lst=printedWords(words)
    map=wordsForYear(year,lst)
    print("Total printed words in",year,":",map)

    labels="Year","Total Words"
    plot=plot2D("Number of printed words over time",labels)
    for yc in lst:
        point=(yc.year,yc.count)
        plot.addPoint(point)
    plot.display()