#unpacking of tuple
a , b , c  =(12,13,56)

t = (12, 13, 56)
#t.append()  # tuple are immputable in nature# tuple are immputable in nature
nae_t =t+ (4 ,)  #can only concatenate tuple (not "int") to tuple
print(nae_t)



my_list = list(t)
print(my_list)
my_list.append(5)
new_t2 =tuple(my_list)
print(new_t2)

