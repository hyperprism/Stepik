'''В институте биоинформатики по офису передвигается робот. Недавно студенты из группы программистов написали для него программу, по которой робот, когда заходит в комнату, считает количество программистов в ней и произносит его вслух: "n программистов".

Для того, чтобы это звучало правильно, для каждого n нужно использовать верное окончание слова.

Напишите программу, считывающую с пользовательского ввода целое число n (неотрицательное), выводящее это число в консоль вместе с правильным образом изменённым словом "программист", для того, чтобы робот мог нормально общаться с людьми, например: 1 программист, 2 программиста, 5 программистов.

В комнате может быть очень много программистов. Проверьте, что ваша программа правильно обработает все случаи, как минимум до 1000 человек.

Дополнительный комментарий к условию:
Обратите внимание, что задача не так проста, как кажется на первый взгляд. Если ваше решение не проходит какой-то тест, это значит, что вы не рассмотрели какой-то из случаев входных данных (число программистов 0≤n≤1000). Обязательно проверяйте свои решения на дополнительных значениях, а не только на тех, что приведены в условии задания.'''

a = int(input())
var1 = [11,111,211,311,411,511,611,711,811,911]

if a % 10 == 1 and a not in var1:
    print(a, 'программист')
elif (a % 10 == 2 and a % 100 != 12) or (a % 10 == 4 and a % 100 != 14) or (a % 10 == 3 and a % 100 != 13):
    print(a, 'программиста')
else:
    print(a, 'программистов')