def calculateGmean(a, b):
    mean = (a*b)/(a+b)
    print(mean)

# # gmean1 = (a*b)/(c+d)
# # print(gmean1)
# calculateGmean(a, b)


# # gmean2 = (c*d)/(c+d)
# # print(gmean2)
# calculateGmean(c, d)

def isGreater(a, b):
    if(a>b):
        print("First number is Greater")
    else:
        print("Second number is greater or equal")

def isLesser(a, b):
    pass

a = 9
b = 8

isGreater(a, b)
calculateGmean(a, b)

c = 8
d = 74

isGreater(c, d)
calculateGmean(c, d)