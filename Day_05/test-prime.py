# a= int(input("Enter a number :"))
# for a in range(1, 30):

#    if (a%2 == 0):

#     print(a)
#     print("This is Prime Number")
# else:
#   if ( a%2 != 0):
#     print (a)
#     print("This is Odd Number")
x=int(input("Enter the value of x: "))

match x:


    case _ if x%2 != 0:
        print("This is prime number")
    case _ if x%2 == 0:
        print("This is Even Number")
    case _ :
        print(x)