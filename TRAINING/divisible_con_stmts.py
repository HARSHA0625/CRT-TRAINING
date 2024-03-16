#write a program in which you take an integer input from user 
#if that integer is divisible by 3 and 6 print good number 
#if integer is divisible by 2 and 7 then print avg number 
#if int is divisible by 4 or 9 then print awsome number
#else print a bad number



num=int(input("enter a number:"))

if num%3==0 and num%6==0:
    print("good number")
elif num%2==0 and num%7==0:
    print("avg number")
elif num%4==0 or num%9==0:
    print("bad number")
else :
    print("bad number")