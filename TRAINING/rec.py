'''write a recursive program to print digits of a number in reverse order'''
def rev(num):
    c=num%10
    print(c)
    num=num//10
    if num==0:
        return 0
    else:
        rev(num)
n=int(input("enter the number:"))
rev(n)