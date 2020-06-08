import requests
from bs4 import BeautifulSoup


header = {
        'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac O'
        'S X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chr'
        'ome/76.0.3809.100 Safari/537.36'
        }
url = 'http://image.baidu.com/search/index?tn=baiduimage&ct=201326592&lm=-1&cl=2&ie=gb18030&word=%CD%BC%C6%AC&fr=ala&ala=1&alatpl=others&pos=0'


def download(url, header):
    try:
     #   header = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'}
        r = requests.get(url, headers=header)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
    except:
        print("Failed Crawling")

    return r.text


def get_img_url(url):

    html = download(url, header)
    url_str = BeautifulSoup(html, 'lxml').find('div', id="wrapper").select('div', class_="imgpage")

    page_url = []
    for i in url_str:
        print(i)
    
   # for i in url_str.find_all('li'):
   #     print(i)



def save(url, path):
    html = download(url, header)

    img_src = BeautifulSoup(html, 'lxml').select('img')['src']
    return img_src


def main():
    get_img_url(url)


if __name__ == '__main__':
    main()
