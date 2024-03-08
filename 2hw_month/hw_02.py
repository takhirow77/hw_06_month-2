class Person:
    def __init__(self, fullname, age, is_married):
        self.fullname = fullname
        self.age = age
        self.is_married = is_married

    def info(self):
        print(f"Привет, меня зовут {self.fullname}. Мне {self.age} лет.")
        if self.is_married:
            print("Я состою в браке.")
        else:
            print("Я не состою в браке.")

person = Person("Рахимов Абдуллох",18,False)
person.info()

class Teacher(Person):
    salary = 0

    def __init__(self, fullname, age, is_married, experience):
        super().__init__(fullname, age, is_married)
        self.experience = experience

    def salary(self):
        self.salary = 3000 * self.experience

    def info(self):
        super().info()
        print(f"Я преподаватель с опытом работы {self.experience} лет.")
        print(f"Моя зарплата составляет {self.salary} сомов.")



teacher = Teacher("Рахимова Мубина", 25, True, 1)
teacher.salary()
teacher.info()

