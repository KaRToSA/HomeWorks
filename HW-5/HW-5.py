class Person(object):
    def __init__(self,name,age):
        self.name = name
        self.age = age
        self.known_persons=[]
    def know(self,person):
        if not person in self.known_persons:
            self.known_persons.append(person)
        else:
            print("{} уже знает {}".format(self.name,person.name))
    def is_known(self,person):
        if person in self.known_persons:
            print("{} знаком с {}".format(self.name,person.name))
        else:
            print("{} не знаком с {}".format(self.name, person.name))
        return 1

class Printer(object):
    def __init__(self):
        self.values = []

    def log(self,*values):
        self.values = values
        str = ''
        for item in self.values:
            str = str+" "+item
        print(str)

class FormattedPrinter(Printer):
    def formated_log(self,*values):
        print("*"*30)
        self.log(*values)
        print("*"*30+"\n")
prt = Printer()
prt.log("Какой-то текст","hhj")
prt = FormattedPrinter()
prt.formated_log("Какой-то текст","hhj")

Igor = Person('Igor',20)
Valera = Person('Valera',15)
Nikita = Person('Nikita',98)
Georgiy = Person('Grisha',2)

Georgiy.is_known(Igor)
Georgiy.know(Igor)
Georgiy.is_known(Igor)

Igor.is_known(Valera)
Igor.know(Valera)
Igor.is_known(Valera)
Georgiy.know(Igor)


