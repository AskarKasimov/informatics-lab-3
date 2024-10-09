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


def third_task() -> bool:
    input_text = input("Введите текст для проверки cron-выражения:\n")
    if re.fullmatch(r"^((([1-5][0-9]|\d|\*)((,([1-5][0-9]|\d))*|-([1-5][0-9]|\d)))|(\*\/([1-5][0-9]|\d))) (((1\d|2[0-3]|\d|\*)((,(1\d|2[0-3]|\d))*|-(1\d|2[0-3]|\d|\*)))|(\*\/(1\d|2[0-3]|\d))) ((([1-2]\d|3[0-1]|[1-9]|L|\*)W?((,([1-2]\d|3[0-1]|[1-9]|L)W?)*|-([1-2]\d|3[0-1]|[1-9]|L)W?))|(\*\/([1-2]\d|3[0-1]|[1-9]))) (((1[0-2]|\d|\?|\*|jan|feb|mar|apr|may|jun|jul|aug|sep|oct|nov|dec)((,(1[0-2]|\d|\*|jan|feb|mar|apr|may|jun|jul|aug|sep|oct|nov|dec))*|-(1[0-2]|\d|\*|jan|feb|mar|apr|may|jun|jul|aug|sep|oct|nov|dec)))|(\*\/(1[0-2]|\d))) ((([0-6]|\?|\*|L|sun|mon|tue|wed|thu|fri|sat|sun|[0-6]\#[1-5]|\*)((,([0-6]|L|sun|mon|tue|wed|thu|fri|sat|sun|[0-6]\#[1-5]))*|-([0-6]|L|sun|mon|tue|wed|thu|fri|sat|sun|[0-6]\#[1-5])))|(\*\/([0-6]|L|sun|mon|tue|wed|thu|fri|sat|sun|[0-6]\#[1-5])))$", input_text):
        return True
    else:
        return False


if __name__ == "__main__":
    choosing = input("Выберите номер таска для проверки: 1, 2, 3\n")
    match choosing:
        case "1":
            print("Ответ:", first_task())
        case "2":
            print("Ответ:", second_task())
        case "3":
            print("Ответ:", third_task())
        case _:
            print("Нет такого таска :(")
