class Car:
    name  = None
    make = None
    model =None

    def __init__(self,o_name,O_make,o_model):
        self.name = o_name
        self.make =O_make
        self.model =o_model

    def start_engine(self):
        print("starting the car wit the name ---" + self.name)
        print("starting the car wit the model  " + self.model)
        print("starting the car wit the make  " + self.make)


lambergoni = Car('kia', "v2" ,"v1")
lambergoni.start_engine()

lambergoni = Car('i20', "v2" ,"v0")
lambergoni.start_engine()