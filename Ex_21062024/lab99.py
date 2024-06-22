#dict
#key and value
#name - "Pramod"
#dictionary is an unordered collection of data
#in a key value pair formate

my_dict2= {"name":"Nidhee" ,"age": 30, "city": "New York"}

print(my_dict2)
print(my_dict2['name'])
print(my_dict2.keys())
print(my_dict2.values())
print(my_dict2.items())
print(my_dict2.get('age'))
print(my_dict2.pop('age'))
print(my_dict2)
print(my_dict2.popitem())
print(my_dict2)
my_dict2.update({'age': 31})
print(my_dict2)
my_dict2.update({'age': 32, 'city': 'San Francisco'})
print(my_dict2)
my_dict2.clear()
print(my_dict2)
#del my_dict2
#print(my_dict2)

phonebook = dict(name = "Nidhee" ,age=  30, city = "New York")
print(phonebook)
print(phonebook['name'])
print(phonebook.keys())