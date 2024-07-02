
class GF:

    def Car(self):
        return "old car"

class F(GF):
    def Car(self):
        return  "Honds civic"

class S(F):
    def Car(self):
        return "Lambo"  #pass

Son =S()
print(Son.Car())
gf =GF()
print(gf.Car())
# lambo , honda civic , old car