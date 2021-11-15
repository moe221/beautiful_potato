import random
from PIL import Image
import requests
import webbrowser


def try_me():
    img_list = [
        "https://cdn.pixabay.com/photo/2016/08/11/08/43/potatoes-1585060_1280.jpg",
        "https://cdn.pixabay.com/photo/2014/11/24/14/39/potatoes-544073_1280.jpg",
        "https://cdn.pixabay.com/photo/2021/10/18/09/30/vegetable-6720516_1280.jpg"
    ]

    path = random.choice(img_list)
    webbrowser.open(path)

    return path

if __name__ == "__main__":

    try_me()
