

# EXERCISE 2

"""
Congratulations, you've got a job at Python Pizza. Your first job is to build an automatic pizza order program.

Based on user's order, work out their final bill.
 ---------------------------------------------
|                                             |
| Small Pizza : $15                           |
| Medium Pizza : $20                          |
| Large Pizza : $25                           |
|                                             |
| Pepperoni for Small Pizza: +$2              |
| Pepperoni for Medium or Large Pizza: + $3   |
|                                             |
| Extra cheese for any size pizza: +$1        |
|                                             |
 ---------------------------------------------

EXAMPLE INPUT:
|------------------------|
| size = "L"             |
| add_pepperoni = "Y"    |
| extra_cheese = "N"     |
|------------------------|

EXAMPLE OUTPUT:
|--------------------------|
| Your final bill is: $29. |
|--------------------------|
"""
# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
money = 0

# selecting size
if size == "S" or size == "s":
    money = 15
elif size == "M" or size == "m":
    money = 20
else:
    money = 25

# adding pepperoni
if add_pepperoni == "Y" or add_pepperoni == "y" and money == 15:
    money += 2
elif add_pepperoni == "Y" or add_pepperoni == "y" and money == 20 or money == 25:
    money += 3
else:
    money += 0

# extra cheese
if extra_cheese == "Y" or extra_cheese == "y":
    money += 1
else:
    money += 0

print(f"Your final bill is {money}")