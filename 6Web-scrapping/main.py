import bs4
import requests

url ='https://habr.com/ru/all/'
response = requests.get(url)
text = response.text
soup = bs4.BeautifulSoup(text, features='html.parser')
post = soup.find(class_='tm-article-snippet__title tm-article-snippet__title_h2')
print(post)