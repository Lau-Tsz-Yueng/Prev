import requests
from bs4 import BeautifulSoup


header = {
		'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36',
        'Referer': 'https://www.mzitu.com/197786'}
url = 'https://www.mzitu.com'


def download(url, header):
    try:
        header = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'}
        r = requests.get(url, headers=header)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
    except:
        print("Failed Crawling")

    return r.text


def get_img_url(url):

	html = download(url, header)
	url_str = BeautifulSoup(html, 'lxml').find('ul', id='pins')
	page_url = []
	for i in url_str.find_all('li'):
		page_url.append([i.find('a')['href'], i.find('img')['alt']])

	return page_url


def save_img(url, path):
	html = download(url, header)
	count = int(BeautifulSoup(html, 'lxml').find('div', class_='pagenavi').find_all("span")[-2].string)
	
	img_src = BeautifulSoup(html, 'lxml').find('p').select('img')[0]['src']
	
	file = open("./test.jpg", 'wb')
	file.write(download(img_src, header))
	file.flush()
	file.close()




def main():
	for i in get_img_url(url):
		print(i[0])
		print(i[1])
	#save_img('https://www.mzitu.com/197786', '/Users/mac/Desktop')

if __name__ == '__main__':
	main()







