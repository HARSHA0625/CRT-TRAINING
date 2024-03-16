#SINGLE INHERITANCE
class faculty:
    def __init__(self,f_name,department,f_id):
        self.f_name=f_name
        self.department=department
        self.f_id=f_id
    def print_info(self):
        print('faculty information=',self.f_name,self.department,self.f_id)
obj=faculty("HARSHA","computer science",4456)
obj.print_info

class cse(faculty):
    pass
obj=cse("NANDU","computer_science",4304)
obj.print_info




'''create a cls of name placemnts which has a func info which displays we have " 620 placements and still counting" '''
'''create another cls with func display which will names of depts present in clg'''
'''create a cls pragati with a func welcome which disp msg "welcome to pec we glad to have u on board" this pargati cls should also disp the details about depts & placements'''