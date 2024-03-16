'''write a function to calculate the sum of first and last digit of a number'''
def sum(num):
    ldigit=num%10
    while(num>0):
        a=num
        num=num//10
    print("sum of first and last digit of a num:",a+ldigit)
num=int(input("enter the number:"))
sum(num)