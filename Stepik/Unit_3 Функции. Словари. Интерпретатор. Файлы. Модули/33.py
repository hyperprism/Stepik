import requests

download_link = 'https://stepic.org/media/attachments/course67/3.6.3/'
filename = '213837.txt'

while filename:
    print(filename)
    r = requests.get(download_link + filename)
    filename = None if r.text.startswith('We') else r.text

print(r.text)