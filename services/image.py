from random import randint

import requests


def fox():
    url = 'https://randomfox.ca/floof'

    response = requests.get(url)

    if response.status_code == 200:
        return response.json().get('image')
    else:
        return None


def duc():
    num = randint(0, 92)
    image = "images/ducks/duck_" + str(num)
    return image


def ai():
    num = randint(0, 11)
    image = "images/ai/AI_image_" + str(num) + ".png"
    return image


def person_image(person):
    if person in ("Hawking", "Socrates", "Freud"):
        image = "images/person/" + person + ".jpg"
    else:
        image = "images/person/unknown.png"
    return image


def quiz_image():
    # TODO доделать рандомный выбор нескольких картинок
    # num = randint(0, 11)
    # image = "images/quiz/AI_image_" + str(num) + ".png"
    image = "images/quiz/quiz_1.jpg"
    return image


#
# if __name__ == '__main__':
#     quiz_image()
