# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 09:56:37 2025

@author: Andrew Hunter
"""

# ask user age then convert into integer
user_age = input("Please enter your age: ").strip()\
    
user_age = int(user_age)
        
user_ageplus = user_age + 5

# write inserted age and age + 5 to out file
with open("q2.out", "w") as file:
    file.write(f"{user_age}\n")

with open("q2.out", "a") as file:
    file.write(f"{user_ageplus}\n")