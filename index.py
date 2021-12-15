# Variables
name="henry" # declare string type variable with value "henry"
age=4 # type integer/number
loggedIn=False # type boolean (True OR False)
# print("Welcome " + name + "!")
users=["Remo", "Tommy", "Marie"] # decalre users variable of type array/list
# print (users) # prints the whole array
# print(users[0]) # index is based 0
# print(users[:1])
# print(users[1:]) # array slicing
session = { # python object/dict, complex data structure
    "id": 231231,
    "name": "host",
    "createdAt": 17545353
}
# print(session)
# print(session["name"]) # print just one key/entity of object/dict

# TODO
# 2. for loops and interation

# 1. conditionals

age=14

if age > 17:
    print("Welcome")
else:
    print("Too yong")


users=[14,33,52,78]
for user in users:
    print(user)
    if user > 17:
        print("Welcome")
    else:
        print("Too yong")


print(age)