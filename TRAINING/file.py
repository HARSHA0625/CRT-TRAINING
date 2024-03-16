import csv
f=open("student.csv","a",newline="")
a=csv.writer(f)
a.writerow(["studentID","email","phone number","name"])
studentID=int(input("enter studentID:"))
email=input("enter email:")
phonenum=int(input("enter phone number:"))
name=input("enter name:")
a.writerow([studentID,email,phonenum,])
print("student record has save")

with open('student.csv','r',newline='') as file:
    read=csv.DictReader(file)
    for row in read:
        if row['uname']==username and row['pwd']==pass:
            return True
return False




'''import csv
f=open("Bikers.csv","a",newline="")
a=csv.writer(f)
a.writerow(["Bikeno","Bikemodel","Bikespeed"])
Bikeno=int(input("enter Bike no:"))
Bikecolor=input("enter Bike color:")
Bikemodel=int(input("enter Bike model:"))
a.writerow([Bikeno,Bikecolor,Bikemodel])
print("Bikers record has save")'''