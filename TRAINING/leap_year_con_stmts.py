#checking if a given year is leap or not conditions
#if the year is divisible by 4 and not by 100 or it is divisible by 400 then it is leap year


year=int(input("enter a year:"))
if year%4==0 and year%100!=0 or year%400==0:
    print("leap year:")
else:
    print("not leap year:")
