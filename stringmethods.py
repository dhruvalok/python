str="AbDEfghIj"
print(str.upper())
print(str.lower())
print(str.capitalize())
str1= "  Silver Spoon  "
print(str1.strip())
str2= "ALOK !!!!!"
str3="Welcome to the page !!"
str4="Welcometothepage"
print(str2.rstrip("!"))
print(str1.replace("Silver", "Gold"))
print(str2.split(" "))
print(str1.split(" "))
print(str3.center(50))
print(str3.center(50,"."))
print(str3.count("e"))
print(str3.endswith("!!!"))
print(str3.endswith("!!"))
print(str3.endswith("to", 4,10))
print(str3.find("the"))
print(str3.find("Alok"))
print(str3.index("the"))
# print(str3.index("Alok"))
print(str3.isalnum())
print(str4.isalnum()) #if string is having a space also will give you an error.
print(str3.isalpha())
print(str4.isalpha())
str5="hello alok"
print(str5.islower())
print(str5.isupper())
print(str3.isprintable())
str6="Welcome to the gaming zone\n"
print(str6.isprintable())
str7="    " #using spacebar
str8="      " #using tabs
print(str7.isspace())
print(str8.isspace())
str9="Welcome To The Nehalok Vlogs"
print(str9.istitle())
print(str5.istitle())
print(str9.startswith("Welcome"))
print(str9.swapcase())
print(str3.title())
str_a="His name is Dan. He is an honest man."  #exception value
print(str_a.find("Daniel"))