#calculate the diff. of sum of num's that are divisible by 6 and not divisible by 6 in the range of 1st 30 num's
n=int(input("enter the number:"))
sum1=0
sum2=0
i=0
while(i<=n):
    if i%6==0:
        sum1+=i
    else:
        sum2+=i
    i=i+1
print(abs(sum1-sum2))