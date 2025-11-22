from sandwich_maker import Sandwich_maker
from Data import *

### Make an instance of SandwichMachine class and write the rest of the codes ###
sandwich_machine = Sandwich_maker(resources)
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