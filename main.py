import re


def first_task() -> int:
    input_text = input(
        "Введите текст для подсчёта смайликов типа 8-|\n").lower()
    return len(re.findall(r"8-\|", input_text))


def second_task() -> str:
    input_text = input("Введите текст для проверки на хайку\n").lower()
    if len(re.findall(r"/", input_text)) != 2:
        return "Не хайку. Должно быть 3 строки."

    if re.match(r"^(?:[^аеёиоуыэюя]*[аеёиоуыэюя]){5}[^аеёиоуыэюя]*/(?:[^аеёиоуыэюя]*[аеёиоуыэюя]){7}[^аеёиоуыэюя]*/(?:[^аеёиоуыэюя]*[аеёиоуыэюя]){5}[^аеёиоуыэюя]*$", input_text):
        return "Хайку!"
    else:
        return "Не хайку."


if __name__ == "__main__":
    choosing = input("Выберите номер таска для проверки: 1, 2, 3\n")
    match choosing:
        case "1":
            print("Ответ:", first_task())
        case "2":
            print("Ответ:", second_task())
        case "3":
            pass
        case _:
            print("Нет такого таска :(")
