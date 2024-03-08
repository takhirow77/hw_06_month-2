class Computer:
    def __init__(self, cpu, memory):
        self.__cpu = cpu
        self.__memory = memory

    def __make_computations(self, operation):
        if operation == '+':
            return self.__cpu + self.__memory
        elif operation == '-':
            return self.__cpu - self.__memory
        elif operation == '*':
            return self.__cpu * self.__memory
        elif operation == '/':
            if self.__memory != 0:
                return self.__cpu / self.__memory
            else:
                return "Error: Division by zero"
    @property
    def cpu(self):
        return self.__cpu
    @property
    def memory(self):
        return self.__memory

    def info(self):
        print(f"CPU: {self.__cpu}, Memory: {self.__memory}")


class Laptop(Computer):
    def __init__(self, cpu, memory, memory_card):
        super().__init__(cpu, memory)
        self.__memory_card = memory_card

    def get_memory_card(self):
        return self.__memory_card

    def info(self):
        super().info()
        print(f"Memory Card: {self.__memory_card}")



comp = Computer(cpu=2.4, memory=8)
laptop = Laptop(cpu=3.0, memory=16, memory_card="256GB SSD")

comp.info()
print()

print("Laptop info:")
laptop.info()
print()

print("Computations:")
print("2.4 + 8 =", comp._Computer__make_computations('+')) 
print("3.0 - 16 =", laptop._Computer__make_computations('-'))
print("3.0 * 16 =", laptop._Computer__make_computations('*'))
print("3.0 / 16 =", laptop._Computer__make_computations('/'))  
