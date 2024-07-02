class grandParent:

    key_gold = "1kg"
    def grandParent_method(self):
        return "Grandparet's method"


class Parent(grandParent):

    def parent_method(self):
        return "parent's method"

class child(Parent):
    mac_m3_apple ="M3 Max"

    def  child_method(self):
        return "childs method"

child = child()
print(child.grandParent_method())
print(child.parent_method())
print(child.child_method())
print(child.key_gold)
print(child.mac_m3_apple)

parent = Parent()
print(parent.grandParent_method())
print(parent.parent_method())
print(parent.key_gold)


grandParent_ref = grandParent()
grandParent_ref.grandParent_method()
grandParent_ref.key_gold


#multlevel