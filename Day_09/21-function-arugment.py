# #default Argument
# def name (fname, mname="Kumar", lname="Singh"):
#     print("Hello", fname, mname, lname)
# name('Alok')

# #keyword Argument
# def name (fname, mname, lname):
#     print("Hello", fname, mname, lname)
# name(mname="Kumar", lname="Singh", fname='Alok')

# #Required Argument
# def name (fname, mname, lname):
#     print("Hello", fname, mname, lname)
# name("Alok", "kumar","Singh")

# #Variable-length Argument
# #1. Arbitary Argument
# def name(*name):
#     print("hello", name[0], name[1], name[2])
# name("Alok", "Kumar", "Singh")

# #keyword Arbitary Argument
# def name(**name):
#     print("hello", name["fname"], name["mname"], name["lname"])
# name(fname="Alok", mname="Kumar", lname="Singh")
#return Statemnet
def name(fname, mname, lname):
    return "Hello, " + fname + " " + mname + " " + lname
print(name("Alok", "kumar","Singh"))


# def average(a=1, b=2, c=3):
#    print("The average is: ", (a+b+c)/3)
def average(*numbers):
    print(type(numbers))
    sum = 0
    for k in numbers:
     sum =sum + k
    #  print("The average is: ", sum/len(numbers))
    # return 7
    return sum/len(numbers)

# average(2, 3, 4)
# average(b=9)
# average()
c = average(5, 6, 7, 8)
print(c)