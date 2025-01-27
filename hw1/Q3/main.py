# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 09:56:37 2025

@author: Andrew Hunter
"""

# ask user age then convert into integer
user_age = input("Please enter your age: ").strip()\
    
user_age = int(user_age)

# check user age to see if passed or fail, then write to out file
if user_age < 20 or user_age > 30:
    with open("q3.out", "w") as file:
        file.write("fail")
        
else:
    with open("q3.out", "w") as file:
        file.write("pass")