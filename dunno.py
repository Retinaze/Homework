import json
import os
import sys
import time

# -------- СПІНЕР --------
def loading(text, seconds=2):
    spinner = "|/-\\"
    end_time = time.time() + seconds
    i = 0

    while time.time() < end_time:
        sys.stdout.write("\r" + text + " " + spinner[i % len(spinner)])
        sys.stdout.flush()
        time.sleep(0.1)
        i += 1

    print("\r" + text + " ✓")

# -------- КОЛЬОРИ --------
Colors = {
    "RED": "\033[91m",
    "GREEN": "\033[92m",
    "BLUE": "\033[94m",
    "YELLOW": "\033[93m",
    "PINK": "\033[95m",
    "CYAN": "\033[96m",
    "RESET": "\033[0m",
}

# -------- ОСНОВНА ПРОГРАМА --------
filename = "data.json"

loading("Запуск системи", 2)
loading("Перевірка даних", 2)

# -------- БЕЗПЕЧНЕ ЧИТАННЯ JSON --------
if os.path.exists(filename):
    try:
        with open(filename, "r") as f:
            data = json.load(f)
        name = data.get("name", "")
        user_color = data.get("color", "RESET")
        if not name:  # якщо ім’я порожнє
            raise ValueError
        print(Colors[user_color] + f"\nЛаскаво просимо назад, {name}!" + Colors["RESET"])
    except (json.JSONDecodeError, ValueError):
        # якщо файл порожній або пошкоджений
        print("Файл профілю пошкоджений або порожній. Створюємо новий профіль.")
        name = input("Як тебе звати? ")
        user_color = input("Оберіть колір (RED, GREEN, BLUE, YELLOW, PINK, CYAN): ").upper()
        if user_color not in Colors:
            user_color = "RESET"
        data = {"name": name, "color": user_color}
        with open(filename, "w") as f:
            json.dump(data, f)
else:
    name = input("Як тебе звати? ")
    user_color = input("Оберіть колір (RED, GREEN, BLUE, YELLOW, PINK, CYAN): ").upper()
    if user_color not in Colors:
        user_color = "RESET"
    data = {"name": name, "color": user_color}
    with open(filename, "w") as f:
        json.dump(data, f)

loading("Вхід у систему", 2)

print(Colors[user_color] + f"\nПривіт, {name}!" + Colors["RESET"])
print("Гарного користування терміналом!")

# -------- МЕНЮ --------
while True:
    print(Colors["CYAN"] + "\n  =-Меню-=" + Colors["RESET"])
    print(Colors["YELLOW"] + "1. Подивитись профіль" + Colors["RESET"])
    print(Colors["YELLOW"] + "2. Вийти з програми" + Colors["RESET"])
    print(Colors["YELLOW"] + "3. Видалити профіль" + Colors["RESET"])

    choice = input("Оберіть дію (1-3): ")

    if choice == "1":
        print(Colors[user_color] + f"\nПрофіль користувача:\nІм'я: {name}" + Colors["RESET"])

    elif choice == "2":
        loading("Вихід з програми", 2)
        print("До побачення!")
        break

    elif choice == "3":
        confirm = input("Ви впевнені, що хочете видалити профіль? (Y/N): ")
        if confirm.lower() == "y":
            if os.path.exists(filename):
                os.remove(filename)
            loading("Видалення профілю", 2)
            print("Профіль видалено. Перезапустіть програму для створення нового профілю.")
            break
        else:
            print("Видалення профілю скасовано.")

    else:
        print(Colors["RED"] + "Невірний вибір!" + Colors["RESET"])