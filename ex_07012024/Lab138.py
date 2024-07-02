#multiple

class Father:

    def father_money(self):
        return "This is from father"

class mother:

    def mother_money(self):
        return "2"

    def home(self):
        return "this is from the mother"

class Son(mother,Father):

    def home(self):
        return "this is from the sun"

sun = Son()
sun.father_money()
sun.mother_money()
print(sun.home())  #local has the preference #method resolution

#diamond problem - java
#python - multiple inheritance
#F,M _ S  print father method first
#M ,f - print mother method
