import os

fd =os.open('testdata.txt' , os.O_RDWR)
os.write(fd,b"hello i am writing")
os.close(fd)