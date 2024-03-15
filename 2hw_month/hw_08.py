import sqlite3

conn = sqlite3.connect("Bank.db")
cur = conn.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS clients(
               id INTEGER PRIMARY KEY,
               name VARCHAR(100) NOT NULL,
               surname VARCHAR(100) NOT NULL,
               age INTEGER NOT NULL,
               email TEXT NOT NULL,
               balance DOUBLE (5,2) DEFAULT 0.0,
               props VARCHAR (100) NOT NULL,
               is_active BOOLEAN DEFAULT FALSE
);
""")

class Bank:
    def __init__(self):
        self.name = None
        self.surname = None
        self.age = None
        self.email = None
        self.balance = 0
        self.props = None
        self.is_active = False

    def register(self, name, surname, age, email):
        self.name = name
        self.surname = surname
        self.age = age
        self.email = email
        cur.execute(f"""INSERT INTO clients (name, surname, age, email, balance, props, is_active)
                       VALUES ('{name}', '{surname}', '{age}', '{email}', 0, 11111, True);""")
        
        conn.commit()

    def deposit(self, amount):
        cur.execute(f"""UPDATE clients SET balance = balance + {amount} WHERE email = '{self.email}'""")
        conn.commit()
        self.balance += amount

    def withdraw(self, amount):
        cur.execute(f"""SELECT balance FROM clients WHERE email = '{self.email}'""")
        balance = cur.fetchone()[0]
        if balance >= amount:
            cur.execute(f"""UPDATE clients SET balance = balance - {amount} WHERE email = '{self.email}'""")
            conn.commit()
            self.balance -= amount
            print(f"Сумма {amount} сом успешно выведена.")
        else:
            print("У вас недостаточно средств.")

    def check_balance(self):
        cur.execute(f"""SELECT balance FROM clients WHERE email = '{self.email}'""")
        balance = cur.fetchone()[0]
        print(f"Ваш текущий баланс: {balance} сом")

    def exit_program(self):
        print("До свидания!")
        conn.close()
        exit()

    def main(self):
        while True:
            print("Выберите действие:")
            print("1-Регистрация, 2-Пополнить баланс, 3-Вывести деньги, 4-Проверить баланс, 5-Выйти")
            command = int(input("Введите цифру: "))
            if command == 1:
                name = input("Введите ваше имя:")
                surname = input("Введите вашу фамилию:")
                age = int(input("Введите ваш возраст: "))
                email = input("Введите вашу почту: ")
                self.register(name, surname, age, email)
            elif command == 2:
                if self.email:
                    amount = int(input("Введите сумму: "))
                    self.deposit(amount)
                else:
                    print("Пройдите регистрацию!")
            elif command == 3:
                if self.email:
                    amount = int(input("Введите сумму: "))
                    self.withdraw(amount)
                else:
                    print("Пройдите регистрацию!")
            elif command == 4:
                self.check_balance()
            elif command == 5:
                self.exit_program()
            else:
                print("Выберите действие:")
                print("1-Регистрация, 2-Пополнить баланс, 3-Вывести деньги, 4-Проверить баланс, 5-Выйти")

bank = Bank()
bank.main()

