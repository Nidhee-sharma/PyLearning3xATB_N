#list

numbers = [1,2,3]

#collections of items
def do_something(pramod_list):
    pramod_list.append(4)
    pramod_list[0] =100
    return pramod_list

def shanti():
 print("hello")#we hhave not called the function

numbers.append(5)
l= do_something(pramod_list=numbers)
print(l)
shanti()