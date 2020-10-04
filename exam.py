import math
import os
import random
import re
import sys
from statistics import median, mode

n = int(input("enter data:"))
list = []
for i in range(0, n):
    e = int(input("enter number"))
    list.append(e)
avg = sum(list) / n
print("Average of data-set is", sep=" ")
print(round(avg, 2))
print("Median of data-set is % s" % (median(list))) 
print("Mode of data set  is % s" % (mode(list)))
