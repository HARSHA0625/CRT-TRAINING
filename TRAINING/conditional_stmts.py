#write a program to accept maths marks from user and check marksgreater than 35 print cheated if marks=35 pass and marks less is fail

marks=int(input("enter your marks:"))
if marks>35:
    print("cheated")
elif marks==35:
    print("pass")
else:
    print("fail")