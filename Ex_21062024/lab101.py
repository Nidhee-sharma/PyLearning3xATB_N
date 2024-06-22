Prmod_details2 = {
    "name": "Prmod_details2",
    "operation": "like",
    "details": {
        "text": "Prmod_details2",
        "view": "Prmod_details2",
        "delete": "Prmod_details2"
    }
}

print(Prmod_details2.get("details").get("text"))
print(Prmod_details2.get("details").get("view"))
print(Prmod_details2.get("details").get("delete"))
print(Prmod_details2.get("name"))
print(Prmod_details2.get("operation"))
print(Prmod_details2.get("details"))
print(Prmod_details2)
print(Prmod_details2.keys())
print(Prmod_details2.values())
print(Prmod_details2.items())
print(Prmod_details2.pop("name"))
print(Prmod_details2)


my_dict = {'a' :1 ,'b':2 , 'c':3 , 'd':4,'a':2}

print(my_dict)
print(my_dict.keys())
print(my_dict.values())
print(my_dict.items())
print(len(my_dict))
for i in list(my_dict.keys()):
    print(i)

for i in list(my_dict.values()):
    print(i)

for k,v in list(my_dict.items()):
    print(k,v)
