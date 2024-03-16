'''create a class f15 with functions  lights,fan and AC'''
#when lights function is called it prints out the color of the light which is taken as parameter to the function
#lights:when lights func is called it prints the color of the light whuch is taken as parameter to the func
#AC displace the room temperature and the outside temp which is taken as i/p
#write a 4th func whose name is Display which displays room temp of ac and fan speed

class F15:
    #adding CONSTRUCTOR
    def __init__(self):
         print("the college is NAAC A+")
         a=4
         b=0.8
         print(a*b)
    def  lights(self,colour):
        #self.color=colour
        print(f"I am a {colour} light !")
    def fan(self,speed):
        self.speed=speed
        print(f"fan is rotating at {speed} speed!")
    def ac(self,r_t,o_t):
            self.o_t=o_t
            self.r_t=r_t
            print(f"room temp is:{r_t} degrees and out side temp is : {o_t} degrees")
    def display(self):
         print(f"difference in the time is {self.o_t-self.r_t} degrees and fan is rotating at {self.speed} speed")
s=F15()
s.lights("white")
s.fan(4)
s.ac(25,40)
s.display()




