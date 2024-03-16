'''create a class ticket which will be the abstract class inside that create a function book ticket which 
should be the abstract method and has nothing in it.'''
'''create a class make my trip which willuse the book ticket function from ticke class to take the details such as name,ph no.,email_id,journey msg and display saying 
thank you for booking a ticket in make my trip'''
'''create a cls irctc which will use the book ticket func ticket cls to take the same details as make my trip but in the end it will give an option to the user to select
 whether it is one way or round trip if user option is round trip it again asks the user to enter te return date as well then prints disp an ing thank u for 
 chooin irctc
 else
 it prints thank u choosing irctc
 create a class indigo which takes all the details as irctc and just asks which mode of transports u want to go in displays thank u choosing indigo
 '''

from abc import ABC,abstractmethod
class ticket(ABC):
    @abstractmethod
    def book_ticket(self):
     pass
class make_mytrip(ticket):
    def book_ticket(self,name):
        print(f"welcome to make my trip,{name}")
        phn=int(input("enter your phone number:"))
        email=input("enter your mail id:")
        jd=input("enter the journey date:")
        print("---thank you for choosing make my trip---")
class IRCTC(ticket):
    def ticket(self):
        name=input("enter your name:")
        phn=int(input("enter your phone number:"))
        email=input("enter your mail ID:")
        jd=input("enter the journey date:")
        print("enter the type of journey from below:")
        n=input(("1.single trip/2.round trip"))
        n=n.lower()
        if n=="round" or n=="2":
            rd=input("enter the return journey date:")
            print("enter the mode of transport from below")
            mode=input("1.train\2.bus\3.plane\n")
            print("---thank you for choosing IRCTC---")
        else:
            print("enter the mode of transport from below")
            mode=input("1.train\2.bus\3.plane\n")
            print("---thank you for choosing IRCTC---")
class INDIGO(ticket):
    def ticket(self):
        name=input("enter your name:")
        phn=int(input("enter your phone number:"))
        email=input("enter your mail ID:")
        jd=input("enter the journey date:")
        print("enter the type of journey from below:")
        n=input(("1.single trip/2.round trip"))
        n=n.lower()
        if n=="round" or n=="2":
            rd=input("enter the return journey date:")
            print("enter the mode of transport from below")
            mode=input("1.train\2.bus\3.plane\n")
            print("---thank you for choosing INDIGO---")
        else:
            print("enter the mode of transport from below")
            mode=input("1.train\2.bus\3.plane\n")
            print("---thank you for choosing INDIGO---")
o1=make_mytrip()
o2=IRCTC()
o3=INDIGO()
o1.book_ticket(input("enter your name:"))
o2.book_ticket(input("enter your name:"))
o3.book_ticket(input("enter your name:"))
