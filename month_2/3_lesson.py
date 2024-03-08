class SmartPhone:
    def __init__(self,sim_cards,camera):
        self.__sim_cards = sim_cards
        self.camera = camera

        @property
        def sim_cards(self):
            return self.__sim_cards





class Laptop:
    def __init__(self,model,year,core, color):
        self.model = model
        self.year = year
        self.core = core
        self.color = color
    def info(self):
        print(f"модель",{self.model}) 