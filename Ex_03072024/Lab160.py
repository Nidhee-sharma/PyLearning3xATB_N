#finally
#File IO

with open('Nidhee.txt','r') as file:
    print(file.read())
    file.close()

#with open('Nidhees.txt','r') as file:
 #   print(file.read()) #FileNotFoundError: [Errno 2] No such file or directory: 'Nidhees.txt'
   # file.close()

