try:
    with open('TestData.txt','r') as file:
        content =file.read()
        print(content)
except FileNotFoundError as fnfr:
    print(fnfr)
finally:
    file.close()



try:
    with open("C:\Users\lenovo\FirstPycharmProjects\PyLearning3xATB\Ex_03062024\TestData2.txt","r") as file:
        content = file.read()
        print(content)
except FileNotFoundError as fnfr:
    print(fnfr)
finally:
    file.close()