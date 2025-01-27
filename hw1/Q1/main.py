# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 09:43:44 2025

@author: Andrew Hunter
"""

while True:

    # ask user for name
    user_name = input("Please enter your name (or type 'quit' to exit and save): ").strip()\
        
    if user_name.lower() == "quit":
        break
    
    # convert name into proper noun
    formatted_name = user_name.title()
    greeting = f"Hello, {formatted_name}"
    print (greeting)

    # save the greeting as a file
    with open("q1.out", "w") as file:
            file.write(greeting)