# Создаем файл с точкой в начале
import os
import time

print("Напишите название каталога: ")
file = str(input())

os.mkdir(f".{file}")
print("файл готов")
time.sleep(2)
