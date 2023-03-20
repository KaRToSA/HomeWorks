import time
import requests
from functools import reduce
def decor_1(function):
    def func_wrapper(text):
        print("'{}' is canceled!".format(function.__name__))
        function(text)
    return func_wrapper

def decor_2(function):
    def func_wrapper(text):
        start = time.time()
        function(text)
        end = time.time()
        print (" Speed of compliting function '{}' is {} seconds".format(function.__name__ , end-start ))
    return func_wrapper

def decor_3(function):
    def func_wrapper():
        func_wrapper.counter += 1
        return function()
    func_wrapper.counter = 0
    return func_wrapper

def decor_4(function):

    def func_wrapper(text):
        print("Декоратор создан!")
        print("Начато выполнение функции! \n")
        function(text)
        print("\n Закончено выполнение функции!")
    return func_wrapper




@decor_1
def func_7_1_1(name):
    print ("My name is {}".format(name))


@decor_2
def func_7_1_2(url):
    webpage = requests.get(url)

@decor_3
def func_7_1_3():
    print("I am canceled!")

@decor_4
def func_7_1_4(url):
    webpage = requests.get(url)
    print(webpage.text)
def func_7_2_1(*args):

   print( list(map(lambda x: x % 5, args)))

def func_7_2_2(*args):

   print(list(map(str, args)))

def func_7_2_3(*args):

   print(list(filter(lambda x: type(x)!=str, args)))

def func_7_2_4(*args):
    count = 0
    counter = []
    for i in args:
        count = 0
        for j in i:
            count+=1
        counter.append(count)
    print(counter)
def other_ch():
    print("1)Выбрать другое задание!")
    print("2)Закончить просмотр заданий!")
    choice_2 = int(input(": "))
    if choice_2 == 1:
        main()

def main ():
    print("Задания за 3 урок:", "\n",
          "1)# HW-7-1-1\n",
          "2)# HW-7-1-2\n",
          "3)# HW-7-1-3\n",
          "4)# HW-7-1-4\n",
          "5)# HW-7-2-1\n",
          "6)# HW-7-2-2\n",
          "7)# HW-7-2-3\n",
          "8)# HW-7-2-4\n",
         )

    choice = int(input("Введите номер задания: "))

    if (choice == 1):
        print("\n Написать декоратор, который добавляет к выполнении любой декорированной функций и будет писать в консоль: ИМЯ_ФУНКЦИИ is canceled! \n")
        func_7_1_1("Valera")

    elif (choice == 2):
        print("\n Реализовать декоратор, который измеряет скорость выполнения функций.\n")
        func_7_1_2('https://google.com')
    elif (choice == 3):
        print("\n Реализовать декоратор, который будет считать, сколько раз выполнялась функция.\n" )
        func_7_1_3()
        func_7_1_3()
        func_7_1_3()
        func_7_1_3()
        func_7_1_3()
        print("Данная функция выполнялась {} раз".format(func_7_1_3.counter))
    elif (choice == 4):
        print("\n Реализовать декоратор, который измеряет скорость выполнения функций.\n")
        func_7_1_4('https://google.com')
    elif (choice == 5):
        print("\n При помощи map посчитать остаток от деление на 5 для чисел: [1, 4, 5, 30, 99]\n")
        func_7_2_1(1, 4, 5, 30, 99)
    elif (choice == 6):
        print("\n При помощи map превратить все числа из массива [3, 4, 90, -2] в строки\n")
        func_7_2_2(3, 4, 90, -2)
    elif (choice == 7):
        print("\n При помощи filter убрать из массива ['some', 1, 'v', 40, '3a', str] все строки \n")
        func_7_2_3('some', 1, 'v', 40, '3a', str)
    elif(choice == 8):
        print("\n При помощи reduce посчитать количество букв в словах: ['some', 'other', 'value'] \n")
        func_7_2_4('some', 'other', 'value')



    else:
        print("Такого задания нет!")
        print()
    other_ch()



main()
