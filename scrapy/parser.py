import requests
from bs4 import BeautifulSoup
from django.views.decorators.csrf import csrf_exempt

HOST = "https://chasy.kg/"
HOST3 = "https://new.technodom.kg/category/229"


HEADERS = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36",
}


@csrf_exempt
def get_html(url):
    req = requests.get(url=url, headers=HEADERS)
    return req


@csrf_exempt
def get_data_watch(html):
    soup = BeautifulSoup(html, "html.parser")
    items = soup.find_all("div", class_="col-6 col-md-4 col-lg-4 col-xl-3 fm-item")
    watch = []

    for item in items:
        watch.append(
            {
                "link": item.find("div").find("a").get("href"),
                "image": item.find("div").find("img").get("src"),
                "title": item.find("div", class_="fm-module-title").get_text(
                    strip=True
                ),
            }
        )
    return watch


@csrf_exempt
def parser_func_watch():
    html = get_html(HOST)
    if html.status_code == 200:
        watch = []
        for i in range(0, 1):
            watch.extend(get_data_watch(html.text))
            return watch
    else:
        raise Exception("Error in parsr function")


# html = get_html(HOST2)
# get_data_lalafo(html.text)


@csrf_exempt
def get_data_tehnodom(html):
    soup = BeautifulSoup(html, "html.parser")
    items = soup.find_all("div", class_="common__recommendations__list__item one-four")
    tehnodom = []

    for item in items:
        tehnodom.append(
            {
                "image": item.find("div").find("a").get("data-background-image"),
                "title": item.find(
                    "div", class_="common__recommendations__list__item__title"
                ).get_text(strip=True),
                "price": item.find(
                    "div", class_="common__recommendations__list__item__price"
                ).get_text(strip=True),
            }
        )
    return tehnodom


@csrf_exempt
def parser_func_technodom():
    html = get_html(HOST3)
    if html.status_code == 200:
        tehnodom = []
        for i in range(0, 1):
            tehnodom.extend(get_data_tehnodom(html.text))
            return tehnodom
    else:
        raise Exception("Error in parsr function technodom")
