#list
#list -collection of items(duplicate is allowed)

my_list=[1,2,3,4,5,6,7,8,9,10]
my_list2 =[9,'True',9,6]

#indexing

print("Element at index[0]",my_list[0])

#changing the element

my_list[1]=100
print("Element at index[0]",my_list[1])

print(my_list2[3])

#append
my_list.append(11)
print(my_list)

#exted
my_list.extend([5,6])
print(my_list)

#insert
my_list.insert(0,'a')
print(my_list)

#remove
my_list.remove('a')
print("list after removing 'a' :" ,my_list)

my_copy_list =my_list.copy()
print(my_copy_list)

#my_list clear
my_list.clear()
print("intial list:" ,my_list)
print(my_copy_list)

#print("index of 3 in the list:" ,my_list.index(3))

my_copy_list.sort()
print(my_copy_list)

my_copy_list.reverse()
print(my_copy_list)

print("length of the list:", len(my_copy_list))
print(my_copy_list[0])
print(my_copy_list[-1])
print(my_copy_list[1:3])
print(my_copy_list[:3])