'''Напишите программу, которая получает на вход три целых числа, по одному числу в строке, и выводит на консоль в три строки сначала максимальное, потом минимальное, после чего оставшееся число.

На ввод могут подаваться и повторяющиеся числа.'''

a = int(input())
b = int(input())
c = int(input())

q = [a, b, c]
qmax = max(q)
qmin = min(q)
if qmax == a and qmin == b:
    print(a)
    print(b)
    print(c)
elif qmax == a and qmin == c:
    print(a)
    print(c)
    print(b)
elif qmax == b and qmin == a:
    print(b)
    print(a)
    print(c)
elif qmax == b and qmin == c:
    print(b)
    print(c)
    print(a)
elif qmax == c and qmin == a:
    print(c)
    print(a)
    print(b)
elif qmax == c and qmin == b:
    print(c)
    print(b)
    print(a)
