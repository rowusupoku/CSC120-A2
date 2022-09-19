# Import a few useful containers from the typing module
from calendar import c
#from typing import Dict, Union
from cgi import print_exception
from computer import Computer


# Imported function from procedural_resale_shop.py
from procedural_resale_shop import buy, update_price, sell, print_inventory, refurbish

class ResaleShop:
    
    def __init__(self, itemID, inventory:dict, refurbish, buy, sell, updatePrice, banner):
        self.__banner = banner
        self.__refurbish = refurbish
        self.__buy = buy
        self.__sell = sell
        self.__updatePrice = updatePrice 
        self.__itemID = itemID
        self.__inventory = [int, computer] = {}
        

    def makeBanner(self, ) -> str:
        # Print a little banner
        print("-" * 21)
        print("COMPUTER RESALE STORE")
        print("-" * 21)
        
    def buyComputer(self, ) -> str:
        # Add it to the resale store's inventory
        print("Buying", computer["description"])
        print("Adding to inventory...")
        computer_id = buy(computer)
        print("Done.\n")

    def sellComputer(self, ) -> str:
        # Now, let's sell it!
        print("Selling Item ID:", computer_id)
        sell(computer_id)

    def refurbish(item_id: int, new_os: Optional[str] = None):
        if item_id in inventory:
            computer = inventory[item_id] # locate the computer
            if int(computer["year_made"]) < 2000:
                computer["price"] = 0 # too old to sell, donation only
            elif int(computer["year_made"]) < 2012:
                computer["price"] = 250 # heavily-discounted price on machines 10+ years old
            elif int(computer["year_made"]) < 2018:
                computer["price"] = 550 # discounted price on machines 4-to-10 year old machines
            else:
                computer["price"] = 1000 # recent stuff

            if new_os is not None:
                computer["operating_system"] = new_os # update details after installing new OS
        else:
            print("Item", item_id, "not found. Please select another item to refurbish.")
            
    def printRefurbish(self, ) -> str:
        # Now, let's refurbish it
        new_OS = "MacOS Monterey"
        print("Refurbishing Item ID:", computer_id, ", updating OS to", new_OS)
        print("Updating inventory...")
        refurbish(computer_id, new_OS)
        print("Done.\n")
        
    def checkInventory(self, ) -> str:
        # Make sure it worked by checking inventory
        print("Checking inventory...")
        print_inventory()
        print("Done.\n")

