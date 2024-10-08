import re


def first_task() -> int:
    input_text = input("Введите текст для подсчёта смайликов типа 8-|\n")
    return len(re.findall(r"8-\|", input_text))


if __name__ == "__main__":
    choosing = input("Выберите номер таска для проверки: 1, 2, 3")
    match choosing:
        case "1":
            first_task()
        case "2":
            pass
        case "3":
            pass
        case _:
            print("Нет такого таска :(")
