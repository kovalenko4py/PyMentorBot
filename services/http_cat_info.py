import requests
import bs4


def http_cat(http_code: str):
    http_code = http_code
    url = 'https://http.cat/status/' + http_code
    response = requests.get(url)
    if response.status_code == 200:
        image = 'https://http.cat/images/' + http_code + '.jpg'
        parser = bs4.BeautifulSoup(response.text, 'html.parser')
        code_info_raw = parser.select(
            'body > div.p-4.sm\\:px-16.sm\\:py-4.lg\\:px-32.lg\\:py-4 > main > section > div > div')
        for article in code_info_raw:
            title = article.find('h2').get_text()
            content = article.find('p').get_text()
    # отладка
        print(f'отладка: метод http_cat |')
        print(f"url : {url}", end="\n-----\n")
        print(f"image : {image}", end="\n-----\n")
        print(f"title : {title}", end="\n-----\n")
        print(f"content : {content}", end="\n-----\n")
        # print(f"data : {code_info_raw}", end="\n-----\n")
        return {"image": image, "content": content}
    elif response.status_code == 404:
        image = "https://http.cat/images/404.jpg"
        content = "There is no such HTTP code."
        return {"image": image, "content": content}
    else:
        # отладка
        print(url)
        return None

#
# if __name__ == '__main__':
#     print(http_cat('423'))
#
