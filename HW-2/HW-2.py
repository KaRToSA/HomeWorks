#HW2-1
def func_2_1():
    List = [3, 6, 1, 21, 456, 2, 0, 54]
    List.sort()
    print(List, '\n')


#HW2-2
def func_2_2():
    Dict = {30390: 'Ivan Iriskin ',30391: 'Bakhdaulet Ramazanov', 30312: 'Levchenko Kirrill',30021: "Georgiy Barvenuk",}
    for key in Dict:

        print(key,Dict[key])

#HW2-3
def func_2_3():

    Tuple = (10.2, 3.5, 19.23, 78.3, 69.2,43.21,432.7,654.0, 56.3,231.0)
    print()
    max = 0
    min = 100000000;
    for item in Tuple:
        if (max<item):
            max=item
        if (min>item):
            min=item
    print(max,min)
    str1 = ""

#HW2-4
def func_2_4():
    str1=''
    List = ["Earth","Russia",'Moscow']
    # str =  List[0],List[1],List[2]
    for i in List:
        str1 = str1+i
        if not i == List[-1]:
            str1 = str1 + '->'
    print(str1)

#HW2-5

def func_2_5():
    str = '/bin:/usr/bin:/usr/local/bin'
    print(str)
    LisT = str.split(":")
    print(LisT)

#HW2-6
def func_2_6():
    L_ter7 = []
    L_notter7 = []
    for i in range(1,100):
        if i%7==0:
            L_ter7.append(i)
        else:
            L_notter7.append(i)
    print("Делятся на 7: {}".format(L_ter7))
    print ("Не деляться на 7: {}".format(L_notter7))
    print()
#HW2-7
def func_2_7():
    rows = []
    List_7 = [
        [1,2,3],
        [4,5,6],
        [7,8,9],
        [10,11,12]
    ]

    i = 0
    n=0
    while not i == len(List_7[0]):
        for row in List_7:
            rows.append(row[i])
        i += 1
        print("Столбец ",i,":",rows)
        rows.clear()
        print()

    for i in List_7:
        n = n+1
        print("Строка", n,":",i)
#HW2-8
def func_2_8():
    print()

    List_8 = [None,"Yeap",2,True,93.5, ]
    index=0
    for item in List_8:
        index+=1
        print("index","(",index-1,"): ", "item: ",item )

#HW2-9
def func_2_9():
    print()
    i=0
    List_9 = ['to-delete',None,'to-delete',"Hello",'to-delete']
    for item in List_9:
        if (item=='to-delete'):
            List_9.pop(i)
        i+=1
    print(List_9)
#HW2-10
def func_2_10():
    print()
    for i in reversed(range(1,11)):
        print(i)

def main ():
    print("Задания за 2 урок:", "\n",
          "1)# HW-2-1", "\n",
          "2)# HW-2-2", "\n",
          "3)# HW-2-3", "\n",
          "4)# HW-2-4", "\n",
          "5)# HW-2-5", "\n",
          "6)# HW-2-6", "\n",
          "7)# HW-2-7", "\n",
          "8)# HW-2-8", "\n",
          "9)# HW-2-9", "\n",
          "10)# HW-2-10", "\n",

          )

    choice = int(input("Введите номер задания: "))

    if (choice == 1):
        print("Создать лист из 6 любых чисел. Отсортировать его по возрастанию")
        func_2_1()
    elif (choice == 2):
        print("Cоздать словарь из 5 пар: int -> str, например {6: '6'}, вывести его в консоль попарно")
        func_2_2()
    elif (choice == 3):
        print("Создать лист из 3 слов: ['Earth', 'Russia', 'Moscow'], соеденить все слова в единую строку,чтобы получилось: 'Earth -> Russia -> Moscow'")
        func_2_3()
    elif (choice == 4):
        print("Взять строку '/bin:/usr/bin:/usr/local/bin' и разбить ее в список по символу ':'")
        func_2_4()
    elif (choice == 5):
        print("Пройти по всем числам от 1 до 100, написать в консоль, какие из них делятся на 7, а какие - нет")
        func_2_5()
    elif (choice == 6):
        print("Создать матрицу любых чисел 3 на 4, сначала вывести все строки, потом все столбцы")
        func_2_6()
    elif (choice == 7):
        print("Создать список любых объектов, в цикле напечатать в консоль: объект и его индекс")
        func_2_7()
    elif (choice == 8):
        print("Создать список с тремя значениями 'to-delete' и нескольми любыми другими, удалить из него все значения 'to-delete'")
        func_2_8()
    elif (choice == 9):
        print("Пройти по всем числам от 1 до 10 в обратную сторону (то есть: от 10 до 1), напечатать их в консоль")
        func_2_9()
    elif (choice == 10):
        print("")
        func_2_10()
    else:
        print("Такого задания нет!")
    print()
    print("1)Выбрать другое задание!")
    print("2)Закончить просмотр заданий!")
    choice_2 = int(input(": "))
    if choice_2 == 1:
        main()


main()