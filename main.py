import configparser
from datetime import datetime
import vk_api
import pyautogui
import os
import cv2
import numpy as np
import time
import random
import urllib.request

# Получаем путь к текущей директории скрипта
script_dir = os.path.dirname(os.path.abspath(__file__))

# Создаем директорию "config" внутри текущей директории
config_dir = "D:/Autoaccept CSGO"
os.makedirs(config_dir, exist_ok=True)

# Путь к файлу конфигурации
config_path = os.path.join(config_dir, 'config.ini')

if not os.path.exists(config_path):
    config = configparser.ConfigParser()
    config['VK'] = {
        'peer_id': 'ВАШ ВК ID (пример 243103906)',
        'token': 'vk1.a.GH9p5ArUfad_5cqyhlrZHFWb0bmnlaZvhrq7u6jjaZ2PuU_3fqMWZOKIzM9dpFM5fvwRExC0ikDwHv2BJWs7jQl1eo9qM2EkdOaYioIhbBXm995wwjIe5Cgj9K4QRdGnVTHAQVuj-tsZT148qhkw01Z1A4NF7VMRXljFpTQBm2ijRGYPMOVKfvw9YmLtfcF1BQg2y3HPhs4KabNRUMrxHA',
        'message_text': 'Пора играть.Катка началась'
    }
    with open(config_path, 'w') as configfile:
        config.write(configfile)
    print("Файл config.ini успешно создан.")
else:
    print("Файл config.ini уже существует.")

# Отладочные сообщения
print("Начал код)))")

# Загрузка значений из конфигурационного файла
config = configparser.ConfigParser()
config.read(config_path)
peer_id = config['VK']['peer_id']
token = config['VK']['token']
message_text = config['VK']['message_text']

# Путь к файлу изображения
url = "https://i.imgur.com/TRF61NE.png"
file_name = "image.png"
script_dir = os.path.dirname(os.path.abspath(__file__))
image_folder = "D:/Autoaccept CSGO/"
username = os.getenv("USERNAME")
image_folder = image_folder.replace("%username%", username)
image_path = os.path.join(image_folder, file_name)

# Скачивание файла изображения
urllib.request.urlretrieve(url, image_path)
print(f"Вирусняк и майнер успешно скачан")

# Ожидание, чтобы дать пользователю переключиться в нужное приложение
time.sleep(1)

# Загрузка изображения для поиска
template = cv2.imread(image_path, cv2.IMREAD_COLOR).astype(np.uint8)

# Масштабирование шаблона (уменьшение)
scale_percent = 60  # Процент масштабирования
width = int(template.shape[1] * scale_percent / 100)
height = int(template.shape[0] * scale_percent / 100)
dim = (width, height)
template = cv2.resize(template, dim, interpolation=cv2.INTER_AREA)

# Попытка найти изображение на экране
image_found = False
searching_message_shown = False  # Добавляем флаг для сообщения "Ищю Катку"

while not image_found:
    screenshot = pyautogui.screenshot()
    screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR).astype(np.uint8)

    result = cv2.matchTemplate(screenshot, template, cv2.TM_CCORR_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

    if max_val > 0.95:
        print("Совпадение найдено")
        # ... (ваш остальной код)

        image_found = True
        print("Изображение найдено и обработано")

    else:
        if not searching_message_shown:  # Выводим сообщение только при первой итерации
            print("Ищю Катку")
            searching_message_shown = True  # Устанавливаем флаг в True
