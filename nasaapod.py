import os
from dotenv import load_dotenv
import requests
from pathlib import Path
from download_image import download_image
from urllib.parse import urlparse, unquote


def extract_extension_from_link(link):
    decoding_link = unquote(link)
    parse_link = urlparse(decoding_link)
    path, fullname = os.path.split(parse_link.path)
    file_path = os.path.splitext(fullname)
    filename, extantion = file_path
    return extantion, filename


def get_apod_images(api_key, foldername, links_count):
    nasa_apod_link = "https://api.nasa.gov/planetary/apod"
    params = {"api_key": api_key, "count": links_count}

    response = requests.get(nasa_apod_link, params=params)
    response.raise_for_status()
    nasa_images = response.json()
    for nasa_image in nasa_images:
        if nasa_image.get("media_type") == "image":
            link_nasa_image = nasa_image.get("hdurl", nasa_image.get("url"))
        else:
            link_nasa_image = None
       extension, file_name = extract_extension_from_link(nasa_image_link)
       path = os.path.join(folder_name, f'{file_name}{extension}')
       download_image(nasa_image_link, path)


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
