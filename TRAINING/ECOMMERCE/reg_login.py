import csv
class RandL:
    def register(self,uname,password,email,city,phno):
        self.uname=uname
        self.password=password
        self.email=email
        self.city=city
        self.phno=phno
        with open('users.csv','r',newline="") as file:
            store=csv.writer(file)
            store.writerow([self.uname,self.password,self.email,self.city,self.phno])
    def login(self,uname,password):
        with open('users.csv','r',newline='') as file:
            read=csv.DictReader(file)
            for row in read:
                if row['uname']==uname and row['password']==password:
                    return True
        return False