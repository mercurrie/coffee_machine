import json

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0
}


# report() prints the resources left in the machine
def report():
    for key, value in resources.items():
        print(key, ': ', value,)


# check_resources() checks if the current amount of resources in the machine is enough to make selected coffee.
# Returns bool
def check_resources(selection: str, coffee: dict) -> bool:
    estimated_water = resources['water'] - coffee[selection]['ingredients']['water']
    estimated_coffee = resources['coffee'] - coffee[selection]['ingredients']['coffee']
    estimated_milk = resources['milk']

    if selection != 'espresso':
        estimated_milk = resources['milk'] - coffee[selection]['ingredients']['milk']

    if estimated_milk < 0: print('Sorry there is not enough milk.')
    if estimated_coffee < 0: print('Sorry there is not enough coffee.')
    if estimated_water < 0: print('Sorry there is not enough water.')

    return True if estimated_milk > 0 and estimated_coffee > 0 and estimated_water > 0 else False


# process_coins() converts inserted coins into a dollar amount and returns total
def process_coins() -> float:
    print('Please insert coins: ')
    quarters = int(input('How many quarters?: '))
    dimes = int(input('How many dimes?: '))
    nickels = int(input('How many nickels?: '))
    pennies = int(input('How many pennies?: '))

    return (quarters * .25) + (dimes * .10) + (nickels * .05) + (pennies * .01)


# check_transaction() checks if inserted money is >= to the cost of the coffee selected. Returns bool
def check_transaction(inserted_amount: float, selection: str, coffee: dict) -> bool:
    change = inserted_amount - coffee[selection]['cost']

    if inserted_amount < coffee[selection]['cost']:
        print("Sorry that's not enough money. Money refunded.")
        return False
    else:
        if selection == 'espresso':
            resources['water'] -= coffee[selection]['ingredients']['water']
            resources['coffee'] -= coffee[selection]['ingredients']['coffee']
        else:
            resources['water'] -= coffee[selection]['ingredients']['water']
            resources['coffee'] -= coffee[selection]['ingredients']['coffee']
            resources['milk'] -= coffee[selection]['ingredients']['milk']

    resources['money'] += coffee[selection]['cost']
    if change > 0: print(f'Here is ${change} dollars in change')
    print(f'Here is your {selection}. Enjoy!!')
    return True


# process_order() takes in menu data, user selection, and calls other functions to replicate actions of a coffee maker
def process_order():
    data_file = open('data.json')
    menu = json.load(data_file)
    on = ''
    print("coffee options:\n espresso \n latte \n cappuccino")
    while on != 'off':
        user_choice = input('What would you like?')
        on = user_choice

        if user_choice == 'report':
            report()
        elif on != 'off':
            if check_resources(selection=user_choice, coffee=menu):
                coins = process_coins()
                check_transaction(inserted_amount=coins, selection=user_choice, coffee=menu)

    data_file.close()


if __name__ == '__main__':
    process_order()

# todo: 1 prompt user
# todo: 2 turn off machine by entering "off"
# todo: 3 print report
# todo: 4 check for sufficient resources
# todo: 5 process coins
# todo: 6 check if transaction was successful
# todo: 7 make coffee
