import random
def guess_int ():
    print("Игра в 'Угадай число!'")
    print("Суть правил: \n Компьютером задумано рандомное число от 1 до 100, ваша задача, либо сразу отгадать число, либо при помощи подсказок компьютера сообразить, какое число было заданно!")
    number = random.randint(1,100)

    def func(number):
        user_number = int(input("Введите предполоагемое число: "))
        if  (user_number > number):
            print('Меньше!')
            return func(number)
        elif (user_number < number):
            print("Больше!")
            return func(number)
        else:
            print("Ты победил, моё число ", number)
            return 1
    func(number)

def quess_word():
    print ("Игра 'Виселица'")
    print ("Суть правил: Компьютером загаданно рандомное слово. Ваша задача: попытаться отгадать загаданное слово!")
    enc_line = []
    words = ['piece','sun','computer','python','napkin','табуретка','художник','кондиционер','нога','рефрежиратор']
    scrt_word = words[random.randint(1, len(words)-1)]
    health = int(5)


    def func_answer(scrt_word,enc_line):
        for item in scrt_word:
            enc_line.append("_")
        return enc_line


    def func_input (scrt_word,enc_line,user_letter):
        i=0
        error = True
        for item in scrt_word:
            if (user_letter == item):
                enc_line[i] = item
                i = i+1
                error = False
            else:
                i = i+1
        print(enc_line)

        check_word(scrt_word, enc_line)



    def check_word(scrt_word,enc_line):
        str_word =''.join(enc_line)
        if str_word == scrt_word:
            return 1
        else:
            user_letter = input("Введите вашу предпологаемую букву: ")
            func_input(scrt_word, enc_line, user_letter)


    print(func_answer(scrt_word,enc_line))
    check_word(scrt_word,enc_line)


def main_func():
    print("1) Игра 'Угадай число!'\n",
          "2) Игра 'Виселица'\n")
    choice = int(input("Выберите игру в которую хотели бы сыграть: "))
    if choice == 1:
        guess_int()
    if choice == 2:
        quess_word()
    print()
    print("1) Выбрать другую игру!")
    print("2) Закончить просмотр игр!")
    choice_2 = int (input(": "))
    if choice_2 == 1:
        main_func()

main_func()