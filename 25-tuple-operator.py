#Manipulating Tuple
Countries = ("Spain", "Italy", "India", "England", "Germany")
temp = list(Countries)
temp.append("Russia")
temp.pop(3)
temp[2]="Finland"
Countries = tuple(temp)
print(Countries)

Countries_1 = ("Afghanistan", "Pakistan", "Bangladesh", "Srilanka")
Countries_2 = ("Vietnam", "India", "China")
SouthEastAsia = (Countries_1 + Countries_2)
print(SouthEastAsia)

#Tuple Methods
Tuple1 = (0,1,2,3,2,3,1,3,2)
#res = Tuple1.index(3)
#res = Tuple1.count(1)
res = Tuple1.index(3,6,8)
#res = len(Tuple1)
print('count of 3 in tuple1 is:', res)