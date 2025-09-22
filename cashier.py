class Cashier:
    def __init__(self, machine_resources):
        self.machine_resources = machine_resources

    def process_coins(self):
        large_dollars = input("How many large dollars?:")
        half_dollars = input("How many half dollars?:")
        quarters = input("How many quarters?: ")
        nickles = input("How many nickles?: ")
        total = float(large_dollars) + float(half_dollars) / 2 + float(quarters) / 4 + float(nickles) / 20
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