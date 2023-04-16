import os
from dotenv import load_dotenv
import requests
from pathlib import Path
from download_image import download_image
from urllib.parse import urlparse, unquote


def extract_link(link):
    decoding_link = unquote(link)
    parse_link = urlparse(decoding_link)
    path, fullname = os.path.split(parse_link.path)
    file_path = os.path.splitext(fullname)
    filename, extantion = file_path
    return extantion, filename


def get_apod_images(api_key, foldername, count_links):
    nasa_link_apod = "https://api.nasa.gov/planetary/apod"
    params = {"api_key": api_key, "count": count_links}

    response = requests.get(nasa_link_apod, params=params)
    response.raise_for_status()
    nasa_images = response.json()
    for image_nasa in nasa_images:
        if image_nasa.get("media_type") == "image":
            if image_nasa.get("hdurl"):
                nasa_link_image = image_nasa["hdurl"]
            else:
                nasa_link_image = image_nasa["url"]
            print(nasa_link_image)
            extantion, filename = extract_link(nasa_link_image)
            path = os.path.join(foldername, f'{filename}{extantion}')
            download_image(nasa_link_image, path)


def main():
    load_dotenv()
    
    parser = argparse.ArgumentParser(description='Загружает изображения NASA')
    parser.add_argument('count', type=int, help='Введите необходимо количество фотографий:')
    args = parser.parse_args()

    api_key = os.environ['NASAAPOD_KEY']

    foldername = "images"
    Path(foldername).mkdir(parents=True, exist_ok=True)
    get_apod_images(api_key, foldername, args.count)


if __name__ == "__main__":
    main()
