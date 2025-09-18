### Data ###

recipes = {
    "small": {
        "ingredients": {
            "bread": 2,  ## slice
            "ham": 4,  ## slice
            "cheese": 4,  ## ounces
        },
        "cost": 1.75,
    },
    "medium": {
        "ingredients": {
            "bread": 4,  ## slice
            "ham": 6,  ## slice
            "cheese": 8,  ## ounces
        },
        "cost": 3.25,
    },
    "large": {
        "ingredients": {
            "bread": 6,  ## slice
            "ham": 8,  ## slice
            "cheese": 12,  ## ounces
        },
        "cost": 5.5,
    }
}

resources = {
    "bread": 12,  ## slice
    "ham": 18,  ## slice
    "cheese": 24,  ## ounces
}


### Complete functions ###

class SandwichMachine:

    def __init__(self, machine_resources):
        self.machine_resources = machine_resources

    def check_resources(self, ingredients):
        for (ingredient) in ingredients:
            if ingredients[ingredient] > self.machine_resources[ingredient]:
                print("Sorry there is not enough " + ingredient + ".")
                return False
            else:
                self.machine_resources[ingredient] -= ingredients[ingredient]
        return True

    def putBackIngredients(self, ingredients):
        for (ingredient) in ingredients:
            self.machine_resources[ingredient] += ingredients[ingredient]

    def process_coins(self):
        large_dollars = input("How many large dollars?:")
        half_dollars = input("How many half dollars?:")
        quarters = input("How many quarters?: ")
        nickles = input("How many nickles?: ")
        total = float(large_dollars) + float(half_dollars)/2 + float(quarters)/4 + float(nickles)/20
        return total

    def transaction_result(self, coins, cost):
        if coins >= cost:
            coins -= cost
            if coins > 0:
                print("Here is $" + str(coins) + " in change")
            return True
        else:
            print("Sorry that's not enough money. Money refunded.")
            return False

    def make_sandwich(self, sandwich_size, order_ingredients):
        can_make = self.check_resources(order_ingredients)
        if can_make:
            if sandwich_size == "small":
                if self.transaction_result(self.process_coins(), 1.75):
                    print("Small sandwich is ready. Bon appetit!")
                else:
                    self.putBackIngredients(order_ingredients)
            elif sandwich_size == "medium":
                if self.transaction_result(self.process_coins(), 3.25):
                    print("Medium sandwich is ready. Bon appetit!")
                else:
                    self.putBackIngredients(order_ingredients)
            elif sandwich_size == "large":
                if self.transaction_result(self.process_coins(), 5.5):
                    print("Large sandwich is ready. Bon appetit!")
                else:
                    self.putBackIngredients(order_ingredients)

### Make an instance of SandwichMachine class and write the rest of the codes ###
sandwich_machine = SandwichMachine(resources)
isOff = False
while not isOff:
    mOption = input("What would you like? (small/ medium/ large/ off/ report)")
    if mOption == "report":
        print(resources)
    elif mOption == "small":
        sandwich_machine.make_sandwich("small", recipes["small"]["ingredients"])
    elif mOption == "medium":
        sandwich_machine.make_sandwich("medium", recipes["medium"]["ingredients"])
    elif mOption == "large":
        sandwich_machine.make_sandwich("large", recipes["large"]["ingredients"])
    elif mOption == "off":
        isOff = True
    else:
        print("Sorry I didn't get that.")