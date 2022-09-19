from calendar import c
from typing import Dict, Union

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
        self.__hard_drive_capacity= hard_drive_capacity
        self.__memory = memory
        self.__operating_system = operating_system
        self.__year_made = year_made
        self.__price = price
        
    def createComputer(self, )
        return {'description': description,
            'processor_type': processor_type,
            'hard_drive_capacity': hard_drive_capacity,
            'memory': memory,
            'operating_system': operating_system,
            'year_made': year_made,
            'price': price
    }

    # What methods will you need?
    # A method that stores information about the Computer
    # A method that updates the computer's OS
    