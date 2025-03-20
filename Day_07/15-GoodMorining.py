import time
current_time=(time.strftime('%H:%M:%S'))
print(current_time)

current_time= int(time.strftime('%H'))
print(current_time)

if 5 <= current_time < 12:
    print("Good Morning Dear")
elif 12 <= current_time < 17:
    print("Good Afternoon")
elif 17 <= current_time < 21:
    print("Good Night")
else:
    print("Good Night")

# current_time= int(time.strftime('%M'))
# print(current_time)
# current_time= int(time.strftime('%S'))
# print(current_time)
