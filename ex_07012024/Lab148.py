from abc import ABC, abstractmethod


class PyATB(ABC):

    @abstractmethod
    def payFee(self):
        pass

    @abstractmethod
    def enrolled(self):
        print("enrolled")

class Shubham(PyATB):

    def payFee(self):
        print("paid")

shubham = Shubham()
shubham.enrolled()
shubham.payFee()

