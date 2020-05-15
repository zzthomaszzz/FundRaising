# Imports go here
from function.function_01 import not_blank
# Main routine goes here
name = not_blank("This response can not be blank or contain number", "What is your name? ", True)
print(name)

items = []
loop = True
while loop:
    response = not_blank("this cant be blank", "Items for selling? ", False)
    if response == 'xxx':
        if len(items) > 0:
            break
        else:
            print("Please add at least one item. ")
            continue
    else:
        items.append(response)
print("These are your items")
for item in items:
    loop = True
    while loop:
        quantity = input("How many of the".format(item))
        if quantity < 0:
            print("The number can't be less than 0")
            continue
        elif quantity.isdecimal():
            print("The number can't be a decimal")
            continue
        else:
            items.append(quantity)
            break
print(items)



