import os

script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)

print("Сейчас вы находитесь в главной папке. На выбор у вас есть несколько действий:\n1. Создать новую папку.\n2. Создать новый файл\n3. Перейти в папку или файл\n")
print(f"Вот весь лист текущий файлов и папок: {os.listdir()}")
choose = input("Введите свой выбор: ")

if choose == "1":
    os.makedirs("Новая_папка", exist_ok=True)
    