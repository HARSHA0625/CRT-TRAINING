#take a num i/p from user check if the sum of factors of the num is greater than original num..
#if yes print yes if no print no

num=int(input("enter the number:"))
sum=0
for i in range(1,num//2+1):
    if num%i==0:
        print(i,end="")
        sum=sum+i
if sum>num:
    print("yes")
else:
    print("no")