n=int(input("enter the number:"))
n1=n
n2=0
while(n>0):
    c=n%10
    n2=n2*10
    n2=n2+c
    n=n//10
if n2==n1:
    print("Palindrome!!")
else:
    print("Not Palindrome ")