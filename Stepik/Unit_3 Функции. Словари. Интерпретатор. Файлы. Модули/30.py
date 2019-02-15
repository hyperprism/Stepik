import re

with open('dataset1.txt', 'r+') as f:
    a = re.split(r"(\d+)", f.readline())[:-1]
    result = ''.join([y * int(x) for x, y in zip(a[1::2], a[::2])])
    print(result)
    f.seek(0)
    f.write(result)