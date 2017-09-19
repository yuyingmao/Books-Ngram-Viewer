__author__ = 'Yuying Mao'
"""
Author: <<< Yuying Mao >>>
Language: Python 3
Purpose: uses turtle graphics to draw a box-and-whisker plot.
"""
from turtle import *

def drawBox(width):
    """
    draw a spuare.
    :param width: the width of the spuare
    :return:None
    """
    left(90)
    forward(30)
    right(90)
    forward(width*5)
    right(90)
    forward(60)
    right(90)
    forward(width*5)
    right(90)
    forward(30)
    right(90)

def boxAndWhisker(min,q1,med,q3,max):
    """
    uses turtle graphics to draw a box-and-whisker plot.
    :param min: a number the corresponds to the minimum value in a given data set.
    :param q1: a number the corresponds to the first quartile of a given data set.
    :param med: a number the corresponds to the median of a given data set.
    :param q3: a number the corresponds to the third quartile of a given data set.
    :param max: a number the corresponds to the maximum value in a given data set.
    :return: Nothing
    """
    left(90)
    forward(15)
    up()
    back(30)
    down()
    forward(15)
    right(90)
    forward((q1-min)*5)
    drawBox(med-q1)
    drawBox(q3-q1)
    up()
    forward((q3-q1)*5)
    down()
    forward((max-q3)*5)
    left(90)
    forward(15)
    up()
    back(30)
    down()
    forward(15)
    right(90)
    up()
    back((max-min)*5)
    down()
    hideturtle()
    done()

if __name__ == '__main__':
    #prompt user for the number of min, q1,median, q3 and max
    min=int(input("Enter the minimum:"))
    q1=int(input("Enter the first quartile:"))
    med=int(input("Enter the median:"))
    q3=int(input("Enter the third quartile:"))
    max=int(input("Enter the maximum:"))
    
    boxAndWhisker(min,q1,med,q3,max)