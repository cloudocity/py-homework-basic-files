import bs4
import requests

url ='https://habr.com/ru/all/'
KEYWORDS = ['DevOps', 'Microsoft', 'python', 'React', 'Java']
url_u ='https://habr.com'
HEADERS = {
    'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Cookie': '_ga=GA1.2.383019504.1659511736; _ym_d=1659511736; _ym_uid=1659511736645201628; hl=ru; fl=ru; _gid=GA1.2.155037354.1667909334; visited_articles=110731:319876:661795:63539:684244:126810:658981:690230:137122:537874; habr_web_home_feed=/all/; _ym_isad=2',
    'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
    'sec-ch-ua-platform': '"Windows"',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
}

response = requests.get(url,headers=HEADERS)
text = response.text
soup = bs4.BeautifulSoup(text, features='html.parser')
articles = soup.find_all('article')

for article in articles:
    dict = {}
    href = article.find(class_='tm-article-snippet__readmore').attrs['href']
    full_href = f"{url_u}{href}"
    datetime = article.find(class_='tm-article-snippet__datetime-published').find('time')
    datetime = datetime.get('datetime')
    hubs = article.find_all(class_='tm-article-snippet__hubs-item')
    hubs = [hub.text.strip(' *') for hub in hubs]
    title = article.find(class_='tm-article-snippet__title-link').find('span').text
    for hub in hubs:
        if hub in KEYWORDS:
            dict['title'] = title
            dict['datetime'] = datetime
            dict['url'] = full_href

    for key in KEYWORDS:
        if key in title:
            dict['title'] = title
            dict['datetime'] = datetime
            dict['url'] = full_href
    bodys = article.find_all(class_='tm-article-body tm-article-snippet__lead')
    bodys = [body.text.strip() for body in bodys]
    for keys in KEYWORDS:
        for body in bodys:
            if keys in body:
                dict['title'] = title
                dict['datetime'] = datetime
                dict['url'] = full_href

    if dict:
        print(f"{dict['datetime']} - {dict['title']} - {dict['url']}")
