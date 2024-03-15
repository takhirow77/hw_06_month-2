# class BankAccount:
#     def __init__(self, account_number, initial_balance=0):
#         self.account_number = account_number
#         self.balance = initial_balance

#     def deposit(self, amount):
#         if amount > 0:
#             self.balance += amount
#             print(f"Средства в размере {amount} успешно зачислены на счет {self.account_number}.")
#         else:
#             print("Невозможно зачислить отрицательную сумму.")

#     def withdraw(self, amount):
#         if 0 < amount <= self.balance:
#             self.balance -= amount
#             print(f"Сумма {amount} успешно снята со счета {self.account_number}.")
#         else:
#             print("Недостаточно средств на счете или указана отрицательная сумма.")

#     def check_balance(self):
#         print(f"Баланс счета {self.account_number}: {self.balance}")


# class User:
#     def __init__(self, first_name, last_name, age, status):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.age = age
#         self.status = status
#         self.bank_account = None

#     def register_bank_account(self, account_number):
#         self.bank_account = BankAccount(account_number)
#         print(f"Счет {account_number} успешно зарегистрирован на пользователя {self.first_name} {self.last_name}.")



# first_name = input("Введите имя: ")
# last_name = input("Введите фамилию: ")
# age = input("Введите возраст: ")
# status = input("Введите статус: ")

# user = User(first_name, last_name, age, status)


# account_number = input("Введите номер счета: ")
# user.register_bank_account(account_number)


# user.bank_account.deposit(1000)
# user.bank_account.check_balance()
# user.bank_account.withdraw(500)
# user.bank_account.check_balance()


# ganeral_age = 27
# age_difference = 3


# age_jr = (ganeral_age - age_difference) / 2
# age_senior = age_jr  + age_difference


# print(f"Возраст младшего человека: {age_jr} лет")
# print(f"Возраст старшего человека: {age_senior} лет")
   