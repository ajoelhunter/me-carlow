# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 09:43:44 2025

@author: Andrew Hunter
"""

# empty list to store all inputs
inputs = []

while True:
    
    # create menu
    print("1) Enter name")
    print("2) Quit")

    choice = input("").strip()
    
    if choice == "1":
    
        # ask user for name
        user_name = input("Please enter your name: ").strip()\
    
        # convert name into proper noun
        formatted_name = user_name.title()
        greeting = f"Hello, {formatted_name}"
        print (greeting)
    
        # store input into list
        inputs.append(greeting)
        
    if choice == "2":
        break
    
# save list to out file
with open("q5.out", "w") as file:
    for greeting in inputs:
        file.write(greeting + "\n")