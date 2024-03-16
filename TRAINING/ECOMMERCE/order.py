import csv 
class Order:
    def oitems(self,item,quan,uname):
        with open("items.csv",'a+',newline="") as file: 
            read=csv.DictReader(file)
            write=csv.DictWriter(file)
            for row in read:
                if row['item'] == item :
                    row['quan']-=quan
                    price=row['price']
            price*=quan
        
        return price 
        