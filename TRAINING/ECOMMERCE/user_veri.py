import csv
class veri:
    def verify(self,uname,mail):
        with open('users.csv','r',newline="") as file:
            read=csv.DictReader(file)
            for row in read:
                if row['uname']==uname and row['mail']==mail:
                    print("user verified successfully:")
                else:
                    print("invalid user!!")    