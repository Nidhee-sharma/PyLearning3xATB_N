#file handling
#how to Read a Text , and write into it using python code

#function-
#open("file_name","Mode")

#mode
#r = for reading (default)
#w = writing(ceate a new file and truncate an existing file)
#a = for appending
#b for binary mode . Zoom.exe -binary
#+ for updating(reading and writing)

#read and write content
#read a file
#Reading entire content: content = file_object.read()
#line = file_object_read() for a single line
#lines =file-objects.readlines() for all lines in a list
#close the file

file = open("TestData.txt", 'r')
content = file.read()
print(content)
file.close()

import os
print(os.getcwd())
ile = open("C:\Users\lenovo\FirstPycharmProjects\PyLearning3xATB\Ex_03062024\TestData2.txt", 'r')
content = file.read()
#print(content)
file.close()