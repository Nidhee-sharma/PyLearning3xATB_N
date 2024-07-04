import os.path
try:
    file =open('Nidheesss.txt','r')
    print(file.read())
        #file.close()
except FileNotFoundError as fe:
    print("i am not able to fine the file ,please check the path")
finally:
    print("executed")
    try:
        file.close() #close has to be done
    except NameError as ne:
        print(ne)
