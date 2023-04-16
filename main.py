import os
from dotenv import load_dotenv
import telegram
import random
from os import listdir
from time import sleep
from telegram.error import NetworkError


def main():
    load_dotenv()
    tg_chat_id = os.environ['TG_CHAT_ID']
    tg_token = os.environ['TG_TOKEN']
    folder_images = os.environ.get("FOLDER", "images")
    time_between_photo_uploads = int(os.environ.get('TIME', 60))
    bot = telegram.Bot(token=tg_token)
    while True:
        try:
            files = listdir(folder_images)
            random.shuffle(files)
            for file in files:
                filepath = os.path.join(folder_images, file)
                with open(filepath, 'rb') as f:
                    bot.send_document(chat_id=tg_chat_id, document=f)
                sleep(time_between_photo_uploads)
        except NetworkError:
            print("Ошибка сети. Перезагрузка через 5 секунд...")
            sleep(5)


if __name__ == "__main__":
    main()
