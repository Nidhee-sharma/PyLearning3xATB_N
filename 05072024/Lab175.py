#os Moduel
#os module use to interact with the operating system
#get working dic , change dir, file exists ,file name ,size file ,envir

import os
import math

print(os.name) # nt - window
print(os.getcwd())
print(math.pi)

#os.chdir("C:\Users\lenovo\FirstPycharmProjects\PyLearning3xATB\05072024")

#print(os.listdir("C:\Users\lenovo\FirstPycharmProjects\PyLearning3xATB\05072024"))
#os.mkdir("pramod")
#read a fiel ,you want if exists or not
#poch to time


size = os.path.getsize('testdata.txt')
print(size)

if size !=0:
    print("file exists and has content")
else:
    print("not exists")

#modify check for file
mtime = os.path.getmtime('testdata.txt')
print(mtime)



#print(os.remove())

import time
print(time.gmtime(mtime))

print(time.localtime())

