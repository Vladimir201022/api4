# Космический телеграмм
## Описание
Проект создан для загрузки изображений космоса, запуска космических кораблей и планеты "Земля". Программа создаёт дирректорию, в которую загружает все необходимые изображения. Для создания проекта вам также необходимо зарегистрировать телеграм бота у отца ботов и создать сов  телеграмм канал.


## Установка
Скачайте необходимые файлы, затем используйте `pip` (или `pip3`, если есть конфликт с Python2) для установки зависимостей и установить зависимости. Зависимости можно установить командой, представленной ниже.

Установите зависимости командой:
```python
  pip install -r requirements.txt
```

## Пример запуска скрипта
Для запуска скрипта у вас уже должен быть установлен Python3.

Для получения необходимых изображений необходимо написать:

```python
  python main.py
```
Чтобы загрузить фотографии из конкретного источника, нужно запустить необходимую функцию из списка: `spacex`, `nasaepic`, `nasaapod` при запуске скрипта:

```python
  python [название функции].py  
```
## Переменные окружения
Часть настроек проекта берётся из переменных окружения.
Переменные окружения - это переменные, значения которых присваиваются программе Python извне.
Чтобы их определить, создайте файл `.env` рядом с `main.py` и запишите туда данные в таком формате: ПЕРЕМЕННАЯ=значение.

Пример содержания файла `.env`:

```python


NASAAPOD_KEY = "nasa-token"
NASA_KEY = "nasa-token"
TG_TOKEN = "bot-token"
TG_CHAT_ID = "@chat_id"
FOLDER_IMAGE = "images"
TIME_BETWEEN_PHOTO_UPLOADS = 60
    
```

Получить токен  `NASA_KEY`, `NASAAPOD_KEY` и `API_KEY` можно на сайте [NASA](https://api.nasa.gov/).
Получить токен `TG_TOKEN` можно у отца ботов.
В описании канала получите название и положите в переменную `TG_CHAT_ID`.

## Цель проекта
Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org).
