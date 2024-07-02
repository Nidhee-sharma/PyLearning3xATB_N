from abc import abstractmethod, ABC


class father(ABC):

    def __init__(self,name):
        self.name = name

    @abstractmethod
    def loan(self):
        pass

class Pramod(father):

    def loan(self):
        print("loan given")

pramod =Pramod("rancho")
pramod.loan()


