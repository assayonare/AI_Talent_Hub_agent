import requests
from bs4 import BeautifulSoup

NEWS_URL = "https://news.itmo.ru/"


def get_latest_news():
    try:
        response = requests.get(NEWS_URL)

        print(response.status_code)  # Проверяем статус ответа
        print(response.text[:10000])
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")

        # news_item1 = soup.select(".splitter .wrapper main .contentbox .accent .side h3 a")
        # news_item2 = soup.find_all(".splitter .wrapper main .contentbox .triplet li h4 a")[:]
        news_items = soup.select("ul.triplet li")[:3]
        titles = []
        urls = []
        k = 0
        for item in news_items:
            k += 1
            title = item.find("h4").get_text(strip=True)
            url = item.find("a")["href"]
            titles.append(f"{k}. {title}")
            urls.append(f"Ссылка {k}: {url}")

        # news_links = []
        # news_links.extend({"title": news_item1.get_text(strip=True), "url": news_item1['href']} )
        # for item in news_item2:
        #     news_links.extend({"title": item.get_text(strip=True), "url": item['href']} )

        # news_titles = [item.get_text(strip=True) for item in news_items]
        # news_links = [item['href'] for item in news_items]

        return titles, urls

    except requests.exceptions.RequestException as e:
        print(f"Ошибка при запросе новостей с сайта ИТМО: {e}")
        return []
