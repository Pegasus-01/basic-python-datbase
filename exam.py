import math
import os
import random
import re
import sys

n = int(input("enter data:"))
a = []
for i in range(0, n):
    e = int(input("enter number"))
    a.append(e)
avg = sum(a) / n
print(round(avg, 2))
