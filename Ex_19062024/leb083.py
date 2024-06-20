#tuple-collection of item

my_list= [1,2,3,4,5]  #mutable
print(id(my_list))
my_list[0] =21
print(my_list)
print(id(my_list))


my_tuple = (1,2,3,4,5) #iimuatbel
#my_tuple[0] =2  TypeError: 'tuple' object does not support item assignment
print(my_tuple)