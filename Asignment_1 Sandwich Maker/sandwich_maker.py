from cashier import *
class Sandwich_maker:
    def __init__(self, machine_resources):
        self.machine_resources = machine_resources

        instance_of_cashier = Cashier(self.machine_resources)

    def check_resources(self, ingredients):
        for (ingredient) in ingredients:
            if ingredients[ingredient] > self.machine_resources[ingredient]:
                print("Sorry there is not enough " + ingredient + ".")
                return False
            else:
                self.machine_resources[ingredient] -= ingredients[ingredient]
        return True

    def make_sandwich(self, sandwich_size, order_ingredients):
        can_make = self.check_resources(order_ingredients)
        if can_make:
            if sandwich_size == "small":
                if Cashier.transaction_result(Cashier(self), Cashier.process_coins(Cashier(self)), 1.75):
                    print("Small sandwich is ready. Bon appetit!")
                else:
                    self.putBackIngredients(order_ingredients)
            elif sandwich_size == "medium":
                if Cashier.transaction_result(Cashier(self), Cashier.process_coins(Cashier(self)), 3.25):
                    print("Medium sandwich is ready. Bon appetit!")
                else:
                    self.putBackIngredients(order_ingredients)
            elif sandwich_size == "large":
                if Cashier.transaction_result(Cashier(self), Cashier.process_coins(Cashier(self)), 5.5):
                    print("Large sandwich is ready. Bon appetit!")
                else:
                    self.putBackIngredients(order_ingredients)

    def putBackIngredients(self, ingredients):
        for (ingredient) in ingredients:
            self.machine_resources[ingredient] += ingredients[ingredient]