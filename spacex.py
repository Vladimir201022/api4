import requests
import os
from pathlib import Path
from download_image import download_image


def fetch_spacex_last_launch(foldername):
    image_link = "https://api.spacexdata.com/v5/launches/"
    response = requests.get(image_link)

    response.raise_for_status()
    for photo in response.json():
        if photo["links"]["flickr"]["original"]:
            urls_photo = photo["links"]["flickr"]["original"]
    for number, link in enumerate(urls_photo):
        filename = f"spacex_{number}.jpg"
        path = os.path.join(foldername, filename)
        download_image(link, path)


def main():
    foldername = "images"
    Path(foldername).mkdir(parents=True, exist_ok=True)
    fetch_spacex_last_launch(foldername)


if __name__ == "__main__":
    main()
