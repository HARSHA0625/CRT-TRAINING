num=int(input("enter a number:"))
count=0
for i in range(num):
    if num%i==0:
        count+=1
if count==1:
    print("prime")
else:
    print("not a prime")