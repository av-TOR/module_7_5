import os
import time

for root, dirs, files in os.walk(r'C:\Делишки\Уроки питона\Домашние задания\Модуль 7\7.4 Форматирование строк'):
  for file in files:
    filepath = os.path.join(root, file)
    filetime = os.path.getmtime(file)
    formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
    filesize = os.path.getsize(file)
    parent_dir = os.path.dirname(file)
    print(f'Обнаружен файл: {file}, Путь: {filepath }, Размер: {filesize} байт, Время изменения: {formatted_time}, Родительская директория: {parent_dir}')