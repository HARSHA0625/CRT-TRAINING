#printing this patterns


'''for i in range(4):
    for j in range(6):
        print("*",end="")
    print()'''


'''for i in range(6):
    for j in range(i+1):
        print("*",end="")
    print()'''


'''for i in range(6):
    for j in range(6-i+1):
        print("*",end="")
    print()'''


'''for i in range(6):
    for s in range(5-i+1):
        print("_",end="")
    for j in range(i+1):
        print("*",end="")
    print()'''


'''for i in range(1,5):
    for j in range(1,5):
        if(i==1 or i==4 or j==1 or j==4):
            print("*",end="")
        else:
            print("_",end="")
    print()'''



#doubt
'''num=1
for i in range(5):
    for j in range(i+1):
        print("num",end="")
        num=num//10
    print()'''


for i in range(4):
    for s in range(4-i+1):
        print("_",end="")
    for j in range(2*i+1):
           print(" * ",end="")
    print()
