set1 =set(["ThtestingAcadmey","for" ,"ThtestingAcadmey."])
print(len(set1))

for i in set1:
    print(i)


set1 =set([1,2,3,4,5,6,7,8,9,10,11,12])
print(len(set1))
set1.remove(5)
print(set1)
print(len(set1))


set1.add(13)
set1.update([14, 15, 16])
print(set1)
print(len(set1))
set.pop(set1)  #remove head first value
print(set1)