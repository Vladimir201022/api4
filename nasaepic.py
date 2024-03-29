import requests
import os
from dotenv import load_dotenv
from datetime import datetime
from pathlib import Path
from download_image import download_image


def get_epic_images(api_key, foldername, links_count):
    nasa_epic_link = "https://api.nasa.gov/EPIC/api/natural/image"
    params = {"api_key": api_key, "count": links_count}

    response = requests.get(nasa_epic_link, params=params)
    response.raise_for_status()
    nasa_images = response.json()
    for nasa_image in nasa_images:
        filename = nasa_image["image"]
        image_nasa_date = nasa_image["date"]
        image_nasa_date = datetime.fromisoformat(image_nasa_date).strftime(
            "%Y/%m/%d")
        link_path = f"https://api.nasa.gov/EPIC/archive/natural/{image_nasa_date}/png/{filename}.png"
        path = os.path.join(foldername, f'{filename}.png')
        download_image(link_path, path, params)


def main():
    load_dotenv()
    parser = argparse.ArgumentParser(description='Загружает изображения NASA')
    parser.add_argument('count', type=int, help='Введите необходимо количество фотографий:')
    args = parser.parse_args()
    api_key = os.environ['NASA_KEY']
    foldername = "images"
    Path(foldername).mkdir(parents=True, exist_ok=True)
    get_epic_images(api_key, foldername, args.count)


if __name__ == "__main__":
    main()
