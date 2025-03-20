# tuple1 = (1,2,2,3,5,4,6)
# tuple2 = ("Red", "Green", "Blue")
# print(tuple1)
# print(tuple2)
country = ("Spain", "Italy", "India", "England", "Germany")
# print(country[0])
# print(country[2])
# print(country[4])
# print(country[-1])
# print(country[-3])
# print(country[-4])
if "Germany" in country:
    print("Germany is Present")
else:
    print("Germany is absent")

if "Russia" in country:
    print("Russia is Present")
else:
    print("Russia is Abesent")

print(country[3:7])
print(country[-7:-2])
print(country[-4:])
print(country[4:])
print(country[:6])
print(country[:-3])
print(country[ ::2])
print(country[-8:-1:2])
print(country[1:8:3])