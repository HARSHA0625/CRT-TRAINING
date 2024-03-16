'''calculate the sum of digits of a number which is taken as a input from user'''

num=int(input("enter a num:"))
sum=0
while num>0:
    sum=sum+(num%10)
    num=num//10
print(sum)