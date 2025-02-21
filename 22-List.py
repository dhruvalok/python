list_1=[1,2,3,4,5,6,7]
list_2=["Red","green","Yellow","Blue","Green"]
details=["Alok", 33, "SREIt", 9.8]
print(list_1)
print(list_2)
print(details)
#positive indexing
print(list_2[0])
print(list_2[4])
print(list_2[2])
print(list_2[1])
#negative indexing
print(list_2[-1])
print(list_2[-3])
print(list_2[-5])
#check whether an item present in the list
if "Yellow" in list_2:
    print("Yellow is present")
else:
    print("yellow is absent")
#example 2
if "Orange" in list_2:
    print("orange is present")
else:
    print("orange is absent")
#range of index
animals=["cats", "dog", "bat", "mouse", "pig","horse", "donkey", "goat", "cow"]
print(animals[3:7])
print(animals[-7:-2])
print(animals[4:])
print(animals[-4:])
print(animals[:6])
print(animals[:-3])
#printing alternative value
print(animals[::2])
print(animals[-8:-1:2])
print(animals[0:8:3])
#Accept item with the small letter "o" in the list
nameswith_o=[item for item in animals if "o" in item]
print(nameswith_o)
nameswith_4=[item for item in animals if (len(item))>4]
print(nameswith_4)