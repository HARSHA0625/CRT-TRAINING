'''write a login function which accepts the user only when the user name and password are same and displace a msg login successful 
otherwise it keeps asking the user to enter their credentials until they are correct'''

#without recursion
def login():
    while(1):
      username=input("enter username:")
      password=input("enter password:")
      if username==password:
          print("Login successful:")
          break
      else:
            print("creddentials are wrong please enter again:")

login()

#with recursion
'''def login():
    username=input("enter username:")
    password=input("enter password:")
    if username==password:
        print("Login successful:")
    else:
        print("creddentials are wrong please enter again:")
        login()
login()'''

