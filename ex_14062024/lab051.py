break - based on the condition
#out of the loop
#continue - based on the condition
#skip the statements inside loop for the current iteration and go to the next iteration
#pass do nothing skip the execution
for i in range(1,11):
    if i==5:
        break
    print(i)

for i in range(10):
    if i == 5:
        pass
    else:
        print(i)
