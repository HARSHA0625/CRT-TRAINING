def count(num):
    if num==0:
        return 0
    return 1+count(num//10)
def armstrong(num):
    if num==0:
        return 0
    return (((num%10)**c)+armstrong(num//10))
num=int(input("enter a number:"))
c=count(num)
if num==armstrong(num):
    print("armstrong number:")
else:
    print("not an armstrong number:")
