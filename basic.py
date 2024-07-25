import requests
from bs4 import BeautifulSoup

# ارسال درخواست به وب‌سایت
res= requests.get('https://www.opencodez.com/')
print(res.status_code)





# تجزیه محتوای HTML با BeautifulSoup
soup = BeautifulSoup(res.content, 'html.parser')
def one():
    # نمایش HTML به صورت زیبا
    pretty_html = soup.prettify()
    print(pretty_html)


def two():
    # جستجوی عنصر div با id مشخص
    test = soup.find('div', attrs={'class': 'post-content image-caption-format-1'})
    #test = soup.find('h3', attrs={'class': 'text-justify'})
    if test:
        print(test)
    else:
        print("Element not found.")

def tree():
    # جستجوی عنصر div با id مشخص
    test = soup.find('h2', attrs={'class': 'title'})
    #test = soup.find('h3', attrs={'class': 'text-justify'})
    if test:
        print(test)
    else:
        print("Element not found.")


def fwor():
    # جستجوی عنصر div با id مشخص
    test = soup.find('article', attrs={'class': 'pexcerpt6 post excerpt'}).find('p').get_text()
    # test = soup.find('h3', attrs={'class': 'text-justify'})
    if test:
        print(test)
    else:
        print("Element not found.")



def five():
    test = soup.find('article', attrs={'class': 'pexcerpt6 post excerpt'})

    test1 = test.find('span', attrs={'class': 'thetime'}).get_text().split(',')[1]
    # get attrebute
    test2 = test.find('a').get('href')
    test3 = test.find('a')['href']

    if test1:
        print(test1)
        print(test2)
        print(test3)

    else:
        print("Element not found.")


def getone():
    box = soup.find('article')

    img = box.find('div', attrs={'class': 'featured-thumbnail'}).find('img').get('src')
    print(img)
    img = box.find('div', attrs={'class': 'featured-thumbnail'}).find('img').get('src')

    titlee= box.find('h2', attrs={'class': 'title'}).find('a').get_text()
    print(titlee)
    title_link=box.find('h2', attrs={'class': 'title'}).find('a').get('href')
    print(title_link)

    text=box.find('div', attrs={'class': 'post-content image-caption-format-1'}).find('p').get_text()
    print(text)

    name=box.find('div', attrs={'class': 'post-info'}).find('span', attrs={'class': 'theauthor'}).find('a').get_text()
    print(name)

    date = box.find('div', attrs={'class': 'post-info'}).find('span', attrs={'class': 'thetime'}).get_text()
    print(date)


def getone():
    box = soup.find('article')

    img = box.find('div', attrs={'class': 'featured-thumbnail'}).find('img').get('src')
    print(img)
    img = box.find('div', attrs={'class': 'featured-thumbnail'}).find('img').get('src')

    titlee= box.find('h2', attrs={'class': 'title'}).find('a').get_text()
    print(titlee)
    title_link=box.find('h2', attrs={'class': 'title'}).find('a').get('href')
    print(title_link)

    text=box.find('div', attrs={'class': 'post-content image-caption-format-1'}).find('p').get_text()
    print(text)

    name=box.find('div', attrs={'class': 'post-info'}).find('span', attrs={'class': 'theauthor'}).find('a').get_text()
    print(name)

    date = box.find('div', attrs={'class': 'post-info'}).find('span', attrs={'class': 'thetime'}).get_text()
    print(date)



def getall2():
    box = soup.find_all('article')


    print(box)
    print(len(box))
#def active_link():



def getall():

    box = soup.find_all('article')
    for t in box:
        img = t.find('div', attrs={'class': 'featured-thumbnail'}).find('img').get('src')
        print(img)
        titlee=t.find('h2', attrs={'class': 'title'}).find('a').get_text()
        print(titlee)
        title_link=t.find('h2', attrs={'class': 'title'}).find('a').get('href')
        print(title_link)

        text=t.find('div', attrs={'class': 'post-content image-caption-format-1'}).find('p').get_text()
        print(text)

        name=t.find('div', attrs={'class': 'post-info'}).find('span', attrs={'class': 'theauthor'}).find('a').get_text()
        print(name)

        date =t.find('div', attrs={'class': 'post-info'}).find('span', attrs={'class': 'thetime'}).get_text()
        print(date)



#one()
#two()
#tree()
#fwor()
#five()
#getone

getall2()