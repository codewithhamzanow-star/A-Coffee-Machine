# MENU contains all available drinks, their ingredients, and their prices.
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}


# coins contains the value of each type of coin.
coins = {
    "quarters": 0.25,
    "dimes": 0.10,
    "nickels": 0.05,
    "pennies": 0.01
}


# resources represents the current state of the coffee machine.
resources = {
    "water": 500,
    "milk": 500,
    "coffee": 760,
    "money": 0,
}


def process_payment(drink):
    """
    Ask the customer for the number of each type of coin,
    calculate the total payment, and compare it with the
    drink's price.

    Returns True if enough money was inserted.
    Returns False if the payment was insufficient.
    """

    price = drink["cost"]
    total = 0

    print("Please insert coins.")

    for coin, value in coins.items():
        while True:
            try:
                amount = float(input(f"How many {coin}? "))

                if amount < 0:
                    print("Enter a positive number!")
                    continue

                break

            except ValueError:
                print("Enter a valid number!")

        total += amount * value

    if total < price:
        print("Sorry that's not enough money. Money refunded.")
        return False

    if total > price:
        print(f"Here is ${total - price:.2f} in change.")

    return True


def check_resources(drink):
    """
    Check whether the machine has enough resources
    to make the selected drink.

    Returns True if all required resources are available.
    Returns False and identifies the insufficient resource otherwise.
    """

    resources_needed = drink["ingredients"]

    for resource, amount in resources_needed.items():
        if resources[resource] < amount:
            print(f"Sorry, there isn't enough {resource}.")
            return False

    return True


def change_resources(drink):
    """
    Subtract the ingredients used by the selected drink
    from the machine's resources and add the drink's
    price to the machine's money.
    """

    resources_needed = drink["ingredients"]

    for resource, amount in resources_needed.items():
        resources[resource] -= amount

    resources["money"] += drink["cost"]


def make_coffee(drink_name):
    """
    Coordinate the process of making a coffee.

    Checks the available resources and processes the payment.
    If both succeed, the machine's resources are updated
    and the coffee is served.
    """

    drink = MENU[drink_name]

    if check_resources(drink) and process_payment(drink):
        change_resources(drink)
        print(f"Here is your {drink_name} ☕ Enjoy!")


def report():
    """
    Display the current amount of each resource
    and the amount of money inside the coffee machine.
    """

    print(f'Water: {resources["water"]}ml')
    print(f'Milk: {resources["milk"]}ml')
    print(f'Coffee: {resources["coffee"]}g')
    print(f'Money: ${resources["money"]:.2f}')


def coffee_machine():
    """
    Run the main coffee machine loop.

    The user can order a drink, request a report,
    or turn the machine off.
    """

    while True:
        choice = input(
            "What would you like? (espresso/latte/cappuccino): "
        ).lower()

        if choice not in (
            "espresso",
            "latte",
            "cappuccino",
            "off",
            "report"
        ):
            print("Please enter a valid choice!")
            continue

        if choice == "off":
            break

        elif choice == "report":
            report()

        else:
            make_coffee(choice)


coffee_machine()
