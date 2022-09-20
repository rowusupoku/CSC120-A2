from typing import Dict, Union
from typing import Dict, Union, Optional


# Import the functions we wrote in procedural_resale_shop.py
from procedural_resale_shop import buy, update_price, sell, print_inventory, refurbish
class Computer:

    # What attributes will it need?
    # What to store:
    # - storing information about a specific computer
    # - updating a computer's OS


    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)
    def __init__(self, description: str,
                 processor_type: str,
                 hard_drive_capacity: int,
                 memory: int,
                 operating_system: str,
                 year_made: int,
                 price: int):
        
        self.__description = description
        self.__processor_type = processor_type
        self.__hard_drive_capacity = hard_drive_capacity
        self.__memory = memory
        self.__operating_system = operating_system
        self.__year_made = year_made
        self.__price = price
        
        def create_computer(description: str,
                            processor_type: str,
                            hard_drive_capacity: int,
                            memory: int,
                            operating_system: str,
                            year_made: int,
                            price: int):
            return {'description': description,
                    'processor_type': processor_type,
                    'hard_drive_capacity': hard_drive_capacity,
                    'memory': memory,
                    'operating_system': operating_system,
                    'year_made': year_made,
                    'price': price
            }
            
            # First, let's make a computer
            computer = create_computer(
                "Mac Pro (Late 2013)",
                "3.5 GHc 6-Core Intel Xeon E5",
                1024, 64,
                "macOS Big Sur", 2013, 1500
            )
            
        def update_price(inventory, item_id: int, new_price: int):
            if item_id in inventory:
                inventory[item_id]["price"] = new_price
            else:
                print("Item", item_id, "not found. Cannot update price.")

        def refurbish(inventory, item_id: int, new_os: Optional[str] = None):
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


    