#write a program to check on road price of a bike under the conditions
#if the price is greater than 72000 then income tax is 10% of original price and insurance will be 15% of original price
#if the price is greater than 150000 and less than 200000 rs.then tax will be 25% and insurance is 20%
#if the price is above 200000 then tax is 35% and insurance is 28%
#otherwise minimum price starts from 72000 enter a valid price


price=int(input("enter bike price:"))

if price>72000 and price<150000:
    tax=price*(10/100)
    insurance=price*(15/100)
    actual_price=price+tax+insurance
    print("on road price:₹",int(actual_price))
elif price>150000 and price<200000:
    tax=price*(25/100)
    insurance=price*(20/100)
    actual_price=price+tax+insurance
    print("on road price:₹",int(actual_price))
elif price>=200000:
    tax=price*(35/100) 
    insurance=price*(28/100)
    actual_price=price+tax+insurance
    print("on road price:₹",int(actual_price))
else:
    print("minimum price with us starts from 72000 enter a valid price") 


