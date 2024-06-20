#*args
print("pramod","amit","SB")


def sum3(a=12,b=22,c=77):
    return a+b+c


result1=sum3()
result2=sum3(a=1,b=2)
result3=sum3(a=4,b=6,c=3)
result4=sum3(c=4, a=5,b=6)
print(result1,result3,result4,result2)
