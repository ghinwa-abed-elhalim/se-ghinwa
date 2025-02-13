print("welcome to the movie cinema! ")
age = int(input("please insert your age ")) 

if age <= 10:
    print("ticket price is 3$ ")

elif age <= 15 and age > 10:
    print("ticket price is 5$")

else:
    print("ticket price is 8$")

