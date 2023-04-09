import requests
import os
from dotenv import load_dotenv
from datetime import datetime
from pathlib import Path
from download_image import download_image


def get_epic_images(api_key, foldername, count_links):
    nasa_link_epic = "https://api.nasa.gov/EPIC/api/natural/image"
    params = {"api_key": api_key, "count": count_links}

    response = requests.get(nasa_link_epic, params=params)
    response.raise_for_status()
    nasa_images = response.json()
    for image_nasa in nasa_images:
        filename = image_nasa["image"]
        image_nasa_date = image_nasa["date"]
        image_nasa_date = datetime.fromisoformat(image_nasa_date).strftime(
            "%Y/%m/%d")
        link_path = f"https://api.nasa.gov/EPIC/archive/natural/{image_nasa_date}/png/{filename}.png"
        path = os.path.join(foldername, f'{filename}.png')
        download_image(link_path, path, params)


def main():
    load_dotenv()
    count_links = int(input("Введите число фотографий"))
    api_key = os.environ['NASA_API']
    foldername = "images"
    Path(foldername).mkdir(parents=True, exist_ok=True)
    get_epic_images(api_key, foldername, count_links)


if __name__ == "__main__":
    main()
