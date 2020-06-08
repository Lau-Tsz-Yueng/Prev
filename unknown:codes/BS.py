from bs4 import BeautifulSoup
import requests
import re


def Setpage():
    print("正在爬取链家网...")
    print("Location : Beijing")
    number = str(input("Please input how many pages you want to search:\n"
                       "请输入想要查找的页面数字\n"
                       "正在查找相关名称...\n"))
    start_url = 'https://bj.lianjia.com/ershoufang/'
    try:
        if number == 1:
            url = start_url + "rs/"
        else:
            url = start_url + "pg" + number + "/"
    except:
        print("Please input a valid page number")
    return url

url = Setpage()
try:
    kv = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) Appl'
          'eWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'}
    r = requests.get(url, headers=kv)
    r.raise_for_status()
    r.encoding = r.apparent_encoding

except:
    print("Failed Crawling")

demo = r.text
soup = BeautifulSoup(demo, "html.parser")
infoList = []
for link in soup.find_all('ul'):
    link.prettify()
    for lines in link:
        txt = str(lines)
        data = re.findall('[\u4e00-\u9fa5]+', txt)
        if len(data) >= 30:
            print(data[4])
            infoList.append(data)

