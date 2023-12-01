from data import menu

class CoffeeMaker():
    def __init__(self):
        self.resources = {
            "water": [300, "ml"],
            "milk": [200, "ml"],
            "coffee": [100, "g"],
            "money": [0, "$"]
        }

    def run(self):
        payment_successful = False
        choice = self.prompt_choice()
        if choice == "off":
            return
        else:
            self.drink_data = menu[choice]

        if self.has_resources():
            payment_successful = self.process_coins()

        if payment_successful:
            print(f"ok, here's your {choice} ☕️. Enjoy!")
            self.adjust_resources()

        self.run()

    def prompt_choice(self):
        choice = None
        while not choice:
            choice = input("What would you like? (espresso/latte/cappuccino) ")
            if choice == 'espresso' or choice == 'latte' or choice == 'cappuccino' or choice == "off":
                return choice
            else:
                print("Sorry bro that's not a thing")
                choice = None

    def print_report(self):
        for k, v in self.resources.items():
            print(f"{k}: {v[0]} {v[1]}")

    def has_resources(self):
        for ingredient in self.drink_data["ingredients"]:
            if self.resources[ingredient][0] < self.drink_data["ingredients"][ingredient]:
                print(f"Sorry, not enough {ingredient}")
                return False
        return True

    def process_coins(self):
        print(f"The price is {self.drink_data['cost']}")
        print("Please enter your payment in coins")
        quarters = int(input("How many quarters? "))
        dimes = int(input("How many dimes? "))
        nickles = int(input("How many nickles? "))
        pennies = int(input("How many pennies? "))

        total_payment = (quarters * .25) + (dimes * .1) + (nickles * .05) + (pennies * .01)
        print(f"You inserted: ${round(total_payment,2)}")

        if total_payment > self.drink_data["cost"]:
            print(f"Here's your change: ${round(total_payment - self.drink_data['cost'],2)}")
            self.resources['money'][0] += self.drink_data["cost"]
            return True
        elif total_payment == self.drink_data["cost"]:
            self.resources['money'][0] += self.drink_data["cost"]
            return True
        else:
            print("Not enough money. Refunding now.")
            return False

    def adjust_resources(self):
        for ingredient in self.drink_data["ingredients"]:
            self.resources[ingredient][0] -= self.drink_data["ingredients"][ingredient]