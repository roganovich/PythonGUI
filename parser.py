import requests, bs4

url = "https://market.yandex.ru/search?text=yandex%20market%20catalog%20iphone&lr=2&clid=698&onstock=0&local-offers-first=0"
r = requests.get("https://ostrov.at/b2c/catalogues/masla_motornie")
r.encoding = "UTF8"
content = r.text

b = bs4.BeautifulSoup(content, "html.parser")

items = b.select("div.block_item")
for item in items:
    a = item.find("a").getText()
    print(a)