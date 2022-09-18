# Import a few useful containers from the typing module
from calendar import c
from typing import Dict, Union

# Imported function from procedural_resale_shop.py
from procedural_resale_shop import buy, update_price, sell, print_inventory, refurbish

class ResaleShop:

    # What attributes will it need?
    

    # - storing the inventory for the store
    # - buying a computer (add to inventory)
    # - selling a computer (remove from inventory)
    # - updating a computer's price
    # - refurbishing a computer
    
    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)
    def __init__(self, banner, inventory):
        
        
        pass # You'll remove this when you fill out your constructor

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

    def buyComputer(self, ) -> str:
        # Make sure it worked by checking inventory
        print("Checking inventory...")
        print_inventory()
        print("Done.\n")

        # Now, let's refurbish it
        new_OS = "MacOS Monterey"
        print("Refurbishing Item ID:", computer_id, ", updating OS to", new_OS)
        print("Updating inventory...")
        refurbish(computer_id, new_OS)
        print("Done.\n")

        # Make sure it worked by checking inventory
        print("Checking inventory...")
        print_inventory()
        print("Done.\n")
        
        # Now, let's sell it!
        print("Selling Item ID:", computer_id)
        sell(computer_id)
        
        # Make sure it worked by checking inventory
        print("Checking inventory...")
        print_inventory()
        print("Done.\n")

        
    # What methods will you need?
    # A method that stores the inventory of the store
    #