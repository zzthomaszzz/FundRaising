# Functions goes in here
def num_check(subject, error):
    loop = True
    while loop:
        check = input(subject)
        for number in check:
            if not number.isdigit():
                okay = False
        if len(check) == 0:
            print("Please enter something")
            continue
        elif not okay:
            print(error)
            print(...)
            continue
        else:
            return check


def no_num_check(subject, error="This cannot contain number"):
    loop = True
    while loop:
        check = input(subject)
        for number in check:
            if number.isdigit():
                okay = False
        if len(check) == 0:
            print("Please enter something")
            continue
        elif not okay:
            print(error)
            print(...)
            continue
        else:
            return check


def not_blank(subject, error, has_number):
    loop = True
    while loop:
        if has_number:
            response = input(subject)
        else:
            response = no_num_check(subject)
        if response == "":
            print(error)
            print(...)
            continue
        else:
            return response


def get_items(heading, list_1):
    print(heading)
    print()
    loop = True
    while loop:
        item_name = not_blank("Item: ", "The item name cannot be blank", True)
        if item_name.lower() == "xxx":
            if len(item_name) >= 1:
                break
            else:
                print("Please enter at least one item")
                print()
                continue
        else:
            item_price = num_check("Price: ", "The price cannot contain number ")
            add = ("{}, {.2f}".format(item_name, item_price))
            add = list.append()


shopping = []
get_items("*** Variables to sell ***", shopping)
print(shopping)