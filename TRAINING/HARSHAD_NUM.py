num=int(input("enter a number:"))
temp=num
sum=0
while(num>0):
    c=num%10
    sum=sum+c
    num=num//10

if temp%sum==0:
    print("HARSHAD NUM!!")
else:
    print("NOT HARSHAD NUM!!")