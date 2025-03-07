marks = [3, 5, 6, "Alok", True, 6, 7, 8, 32, 56, 1000, 2]
print(marks)
print(type(marks))
print(marks[0])
print(marks[9])
print(marks[-3])
print(len(marks))
print(marks[5-3])
print(marks[10])

if "1000" in marks:
    print("yes")
else:
    print("No")

if 32 in marks:
    print("Yes, Its there")

if "A" in "Alok":
    print("Yes")

print(marks[0:7])
print(marks[1:9])
print(marks[1:9:3])

lst=[i*i for i in range(10)]
print(lst)
lst=[i*i for i in range(10) if i%2==0]
print(lst)
