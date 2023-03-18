


# HW-3-1-1
def func_3_1_1():
    print("HW_3-1-1")
    print("Пользователь вводит число, если оно четное - выбрасываем исключение ValueError,","\n"," если оно меньше 0 - TypeError, если оно больше 10 - IndexError. Обрабатываем ошибку, говорим пользователю, в чем его ошибка")
    number_1 = int(input('Введите число: '))
    if (number_1 % 2 == 0):
        try:
            raise ValueError("Value Error")
        except ValueError as e:
            print("Your error is:", e)

    if (number_1 < 0):
        try:
            raise TypeError("TypeError")
        except TypeError as e:
            print("Your error is:", e)
    if (number_1 > 10):
        try:
            raise IndexError("IndexError")
        except IndexError as e:
            print("Your error is:", e)






# HW-3-1-2

def func_3_1_2():
    print("Создайте список произвольной длины. Пользователь должен ввести индекс объекта, который хочет посмотреть. Если все хорошо - пишите объект в консоль.","\n","Если нет - обработайте возмозможные ошибки и скажите ему, что не так")
    list_2 = [1, 23, 4, 7, 2, 7, 87, 323476, 854, 4262, 75]
    print(list_2)
    n = input("Введите индекс объекта, который хотите посмотреть: ")
    try:
        print(list_2[int(n)])
    except TypeError as e:
        print("Ваша ошибка неверный тип запроса индекса", '\n', e)
    except IndexError as e:
        print("Вы ввели индекс не существующего обьекта листа", '\n', e)
    except ValueError as e:
        print("Запрос должен быть в формате int", '\n', e)

# HW-3-2-1

def func_3_2_1():
    print(
        "Написать функцию, которая принимает на вход два аргумента. Если аргументы больше нуля, возвращаем их сумму. Если оба меньше - разность. Если знаки разные - возвращаем 0")
    def func_2(n_1, n_2):

        if (n_1 > 0 and n_2 > 0):
            print("Cумма двух чисел: ", n_1 + n_2)
        elif (n_1 < 0 and n_2 < 0):
            print("Разность двух чисел: ", n_1 - n_2)
        elif ((n_1 < 0 and n_2 > 0) or (n_1 > 0 and n_2 < 0)):
            print("Знаки разные:", 0)

    n_1 = int(input('Введите первое число: '))
    n_2 = int(input('Введите второе число: '))
    func_2(n_1, n_2)

# HW-3-2-2

def func_3_2_2():
    print("Написать функцию, которая принимает 3 аргумента - числа, найти среди них два максимальных, вывести в консоль")
    def func_2(a, b, c):
        list_2_2 = [a, b, c]
        list_2_2.sort()
        print("Max_1: ", list_2_2[-1], '\n', "Max_2: ", list_2_2[-2])
    func_2(1, 65, 23)

#HW-3-2-3
def func_3_2_3():
    print("Написать функцию, которая принимает два аргумента. Первый - список чисел, второй - булевый флаг. Если флаг действителен - возвращаем новый список с нечетными числами из входного списка, если флаг отрицателен - возвращаем новый список с четными числами из входного списка")
    def func_3(list_f, bool):
        list_new = []
        if (bool):
            for item in list_f:
                if (item % 2 > 0):
                    list_new.append(item)
        else:
            for item in list_f:
                if not (item % 2 > 0):
                    list_new.append(item)
        return list_new


    print(func_3([1, 3, 5, 12, 7, 3, 8, 4, 25], False))

#HW-3-3-1
def func_3_3_1():
    print("Написать функцию, которая принимает любое количество аргументов чисел. Среди них она находит максимальное и минимальное. И возвращает оба")
    def func_3_1(*numbers):
        max = 0
        min = 100000000000
        for item in numbers:
            if (max < item):
                max = item
        for item in numbers:
            if (min > item):
                min = item
        print("max = ", max, '\n', "min= ", min)

    func_3_1(1, 3, 5, 34, 7, 75, 4745, 34, 76, 54, 3, 787, 94, 456, 77)


#HW-3-3-2
def func_3_3_2():
    print("Написать функцию, которая принимает два аргумента: строка и булевый флаг case по-умолчанию равный True. Если флаг действителен: возвращаем новую строку, где каждый символ входной приведен к верхнему регистру, иначе - к нижнему")
    def func_3_2(str,case=True):
        str_new = ''
        if case:
            str_new = str.upper()


        else:
            str_new = str.lower()

        return str_new
    print(func_3_2("HelLO",False))

#HW-3-3-3
def func_3_3_3():
    print("Написать функцию, которая принимает любое количество позиционных аргументов - строк и один парматер по-умолчанию glue, который равен ':'. Соединить все строки таким образом, чтобы в результат попали все строки, длинее 3 символов. Для соединения между любых двух строк вставлять glue")
    def func_3_2(*str,glue=':'):
        str_new = ''
        for item in str:
            if (len(item)>=3):
                str_new = str_new + item
                if not (item==str[-1]):
                    str_new= str_new+glue
        return str_new
    print(func_3_2("sdad","sdadasgfdsfref","dfsafretg","dfaewrerewg","fdsghh5e","vg","gr3","fdashyte4","fa","gfd5g","sdfrh",glue = " ||| "))






def main ():
    print("Задания за 3 урок:", "\n",
          "1)# HW-3-1-1", "\n",
          "2)# HW-3-1-2", "\n",
          "3)# HW-3-2-1", "\n",
          "4)# HW-3-2-2", "\n",
          "5)# HW-3-2-3", "\n",
          "6)# HW-3-3-1", "\n",
          "7)# HW-3-3-2", "\n",
          "8)# HW-3-3-3", "\n", )

    choice = int(input("Введите номер задания: "))

    if (choice == 1):
        func_3_1_1()
    elif (choice == 2):
        func_3_1_2()
    elif (choice == 3):
        func_3_2_1()
    elif (choice == 4):
        func_3_2_2()
    elif (choice == 5):
        func_3_2_3()
    elif (choice == 6):
        func_3_3_1()
    elif (choice == 7):
        func_3_3_2()
    elif (choice == 8):
        func_3_3_3()
    else:
        print("Такого задания нет!")
    print()
    print("1)Выбрать другое задание!")
    print("2)Закончить просмотр заданий!")
    choice_2 = int(input(": "))
    if choice_2 == 1:
        main()


main()