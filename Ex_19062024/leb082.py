my_list =[1,2,3,4]
#print(list*2)
temp_list =[]
for i in my_list:
    temp_list.append(i*2)

print(temp_list)


def double_item(num):
    return num*2


#map
#1.take each item from the list
#2. execute the function on it
#3.Return the same number of elements(list)

double_item =list(map(double_item ,my_list))
print(double_item)
