#printing digits in reverse order:
'''num=int(input("enter a number:"))
while(num>0):
    temp=num%10
    print(temp)
    num=num//10'''

#number of digits:
'''num=int(input("enter a number:"))
count=0
while(num>0):
    count=count+1
    num=num//10
print("no of digits",count)'''

#sum of digits:
num=int(input("enter a number:"))
sum=0
while(num>0):
    temp=num%10
    sum=sum+temp
    num=num//10
print("sum of digits:")

#multiplication of digits: