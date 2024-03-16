'''write a function which states two arguments a and b typecast the value of second argument into integer
 then multiply both arguments and print the last digit of the result '''
#pos_args
def type(a,b):
    b=int(b)
    print("last digit of mul:",(a*b)%10)
res=type(30,40)

'''def type(a,b):
    b=int(b)
#a=int(input("enter the a value:"))
#b=input("enter b value:")
res=type(20,30)
print("last digit of mul:",(a*b)%10)'''