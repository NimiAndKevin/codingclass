print("Welcome to the Mark App")
username=input("Username:")
address=input("Address:")
email=input("Email:")
age=int(input("Age:"))
gender=input("Gender:")
date_of_birth=input("Date Of Birth:")
def greet_user(username,email,age,gender,birth,address):
    print(f"hello {username} your email address is {email} you are {age} and you are {gender} your date of birth is {date_of_birth} your location is {address}. How can we assist you today")

greet_user(username,email,age,gender,date_of_birth,address)
