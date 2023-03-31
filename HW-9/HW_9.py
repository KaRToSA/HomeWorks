import json
import re

import requests



def func_9_1_3():
    Burl = "https://habrahabr.ru/"
    response = requests.get(f"{Burl}")
    pattern_link = r'\<a href=\"(/[\w/]*)\"'
    lst = []
    for item in re.findall(pattern_link, str(response.content)):
        lst.append(item)
        with open("habr.txt", 'a') as fp:
            fp.write("%s\n" % item)
    print("Все ссылки сохранены в файле habr.txt")

def get_json(base_url):
    response = requests.get(f"{base_url}/comments")
    write_to_file_data("response.json",json.dumps(response.json(),sort_keys=True,indent=4))
    headers_dict = {}
    for key,value in response.headers.items():
        headers_dict[key] = value
        print("{}:|| {}\n".format(key,value))


def write_to_file_data(file,content,mode="w"):
    # print("Writing data!")
    with open(file,mode = mode,) as f:
        return f.write(content)
def read_the_file_data(file):
    print("Reading file!")
    with open(file) as f:
        return f.read()
def func_9_1_1():
    print("Choice process!")
    print("1) Writing")
    print("2) Reading file!")
    choice = int(input("Введите номер:"))
    if(choice == 1):
        content = str(input("Введите текст который хотите видеть в файле:"))
        сontenter = content + "a\n"
        print(сontenter)
        write_to_file_data("test.txt",сontenter)
    elif(choice == 2):
        print(read_the_file_data("test.txt"))

def other_ch():
    print("1)Выбрать другое задание!")
    print("2)Закончить просмотр заданий!")
    choice_2 = int(input(": "))
    if choice_2 == 1:
        main()

def main ():
    print("Задания за 3 урок:", "\n",
          "1)# HW-9-1-1\n",
          "2)# HW-9-1-2\n",
          "3)# HW-9-1-3\n",

         )

    choice = int(input("Введите номер задания: "))

    if (choice == 1):
        print("\n + Реализовать две функции: write_to_file(data) и read_file_data().Которые соотвественно: пишут данные в файл и читают данные из файла. \n")
        func_9_1_1()
    elif (choice == 2):
        print("\n Реализовать следующую логику: получать при помощи requests данные сервиса https://jsonplaceholder.typicode.com/(сущность можно выбрать любую, например https://jsonplaceholder.typicode.com/comments),выводить в консоль все пары заголовки, сохранять полученный json в файл на диск.\n")
        get_json("https://jsonplaceholder.typicode.com")
    elif (choice == 3):
        print("\n Обратиться с странице https://habrahabr.ru/. Получить текст страницы. При помощи регулярных выражений нужно получить все ссылки со страницы на другие.\n")
        func_9_1_3()
    elif(choice == 8):
        print("\n При помощи reduce посчитать количество букв в словах: ['some', 'other', 'value'] \n")



    else:
        print("Такого задания нет!")
        print()
    other_ch()
main()