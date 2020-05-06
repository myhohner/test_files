from bs4 import BeautifulSoup
from urllib.request import urlopen
import re


'''
# if has Chinese, apply decode()
html = urlopen("https://morvanzhou.github.io/static/scraping/table.html").read().decode('utf-8')

soup = BeautifulSoup(html, features='html.parser')

img_links = soup.find_all("img", {"src": re.compile('.*?\.jpg')})
for link in img_links:
    print(link['src'])
'''


base_url = "https://baike.baidu.com"
his = ["/item/%E7%BD%91%E7%BB%9C%E7%88%AC%E8%99%AB/5162711"]

url=base_url+his[-1]
html=urlopen(url).read().decode('utf-8')
res=BeautifulSoup(html,features='html.parser')

print(res.find('h1').get_text(),'url:',his[-1])

