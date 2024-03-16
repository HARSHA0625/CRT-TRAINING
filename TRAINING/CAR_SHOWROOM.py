'''car showroom project'''

'''in our showroom only 3 car company : toyota,mahindra,mercedes'''

'''
take the i/p from user for the car company name and in the i/p msg give the user the option of three companies this user i/p company 
name goes as the input/argument to model name function,which welcomes the user accordingly to the company name.
Ask the user to enter the specific model name for that company.

the 2nd func whose name is variant.According to the company name and car model the user should be asked to enter the variant
he would like to choose from petrol,diesel 
 
the last display func according to the car company ,car model name and car variant 
1st it's ex showroom price should be displayed and then it's on road price should be displayed and then it's on road price 
which is clac as ex show room +cgst+5gst+insurance.
the sgst cgst and the insurance and all the have the common value throughout the car showroom

'''

class carshowroom:
    def _init_(self):
        print("welcome to the HARSHA CAR SHOWROOM")
        self.in_put()

    def variant(self,car,model):
        print(f'Select the variant for car:{car}  and modelname:{model}')
        var=input("1.Petrol\t2.Diesel \n ")
        var=var.lower()
        self.display(var,car,model)

    def in_put(self):
        print("enter one of the car name from the below\n")
        car=input("1.TOYOTA/t2.MAHINDRA/t3.MERCEDES")
        car=car.lower()
        if car.lower() == "TOYOTA" or car.lower() == "1":
            print(f"----welcome to the TOYOTA family ----")
            print("---- select the availabe models from below ----\n")
            model=input("1.PRIUS\t2.YARIS\t3.CAMRY\n")
            model=model.lower()
            self.variant(car,model)
        elif car.lower() == "MAHINDRA" or car.lower() == "2":
            print(f"---- welcome to the Mahindra family ----")
            print("---- select the availabe models from below ----")
            model=input("1.THAR\t2.BOLERO\t3.NEO\n")
            model=model.lower()
            self.variant(car,model)
        elif car.lower() == "MERCEDES" or car.lower() == "3":
            print(f"---- welcome to the Mercedes family ----")
            print("---- select the availabe models from below ----")
            model=input("1.BENZ GLS\t2.BENZ EQE SUV\t3.EQA\n")
            model=model.lower()
            self.variant(car,model)
        else:
            print("sorry customer our showroom does not have that company ")
            print()
            self.in_put()
    

    def display(self,var,car,model):
        p=self.get_price(var,car,model)
        print(f'Ex showroom price of your car is ₹ {p}')
        cgst=(p*(18/100))
        sgst=(p*(17/100))
        ins=(p*(20/100))
        op=p+cgst+sgst+ins
        print("On Road price of your car is ₹",int(op))


    def get_price(self,var,car,model):
        price=0
        if car == "toyota" or car == "1":
            if model == 'supra' or model == '1':
                if var == 'petrol' or var =='1':
                    price=9000000
                elif var =='diesel' or var=='2':
                    price=10000000
            elif model == 'fortuner' or model == '2':
                if var == 'petrol' or var =='1':
                    price=3500000
                elif var =='diesel' or var=='2':
                    price=4000000
            elif model == 'innova' or model == '3':
                if var == 'petrol' or var =='1':
                    price=3300000
                elif var =='diesel' or var=='2':
                    price=3700000
        elif car == "mahindra" or car == "2":
            if model == 'thar' or model == '1':
                if var == 'petrol' or var =='1':
                    price=2500000
                elif var =='diesel' or var=='2':
                    price=3000000
            elif model == 'scorpio' or model == '2':
                if var == 'petrol' or var =='1':
                    price=1300000
                elif var =='diesel' or var=='2':
                    price=1500000
            elif model == 'xuv700' or model == '3':
                if var == 'petrol' or var =='1':
                    price=1800000
                elif var =='diesel' or var=='2':
                    price=2200000
        elif car == "mercedes" or car == "3":
            if model == 'g-wagnor' or model == '1':
                if var == 'petrol' or var =='1':
                    price=10000000
                elif var =='diesel' or var=='2':
                    price=11400000
            elif model == 'c-class' or model == '2':
                if var == 'petrol' or var =='1':
                    price=15000000
                elif var =='diesel' or var=='2':
                    price=15300000
            elif model == 's-class' or model == '3':
                if var == 'petrol' or var =='1':
                    price=22000000
                elif var =='diesel' or var=='2':
                    price=22300000
        if price!=0:
            return price
        else:
            print(f"Sorry we dont have that model number {model} with {var} variant ")
            print("----kindly enter again----")
            self.in_put()
                
            
c=carshowroom()


