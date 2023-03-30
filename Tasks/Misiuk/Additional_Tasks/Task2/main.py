from bs4 import BeautifulSoup

with open('index.html', 'r') as file_read:

    soup = BeautifulSoup(file_read, 'lxml')
    soup.prettify()

    with open('index2.html', 'w') as file:
        for i in soup.prettify():
            file.write(str(i))
