# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 09:43:44 2025

@author: Andrew Hunter
"""

# empty list to store all inputs
inputs = []

while True:

    # ask user for name
    user_name = input("Please enter your name (or type 'quit' to exit and save): ").strip()\

    if user_name.lower() == "quit":
        break
    
    # convert name into proper noun
    formatted_name = user_name.title()
    greeting = f"Hello, {formatted_name}"
    print (greeting)
    
    # store input into list
    inputs.append(greeting)
    
# save list to out file
with open("q4.out", "w") as file:
    for greeting in inputs:
        file.write(greeting + "\n")