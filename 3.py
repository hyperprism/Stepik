a = int(input())
b = int(input())
c = int(input())
import math
p = (a + b + c)/2
g = (p *(p - a)) * (p - b) * (p - c)
print(math.sqrt(g))