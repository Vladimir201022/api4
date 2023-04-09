import os
from dotenv import load_dotenv
import telegram
import random
from os import listdir
from time import sleep
from telegram.error import NetworkError


def main():
    load_dotenv()
    TG_CHAT_ID = os.environ['TG_CHAT_ID']
    TG_TOKEN = os.environ['TG_TOKEN']
    folder_images = os.environ.get("FOLDER", "images")
    time = int(os.environ.get('time', 60))
    bot = telegram.Bot(token=TG_TOKEN)
    while True:
        try:
            files = listdir(folder_images)
            random.shuffle(files)
            for file in files:
                filepath = os.path.join(folder_images, file)
                with open(filepath, 'rb') as f:
                    bot.send_document(chat_id=TG_CHAT_ID, document=f)
                sleep(time)
        except NetworkError:
            print("Ошибка сети. Перезагрузка через 5 секунд...")
            sleep(5)


if __name__ == "__main__":
    main()
