# -*- coding: utf-8 -*-
"""
Created on Wed Feb  5 20:14:51 2025

@author: Andrew Hunter
"""
import pandas as pd

# dictionary that stores the answers
user_scores = {}

def add_score():
    """Add a user's score to the dictionary."""
    name = input("Enter the user's name: ").strip()
    score = input("Enter the user's score: ").strip()
    
    # add the user's score to disctionary
    if name in user_scores:
        user_scores[name].append(score)
    else:
        user_scores[name] = [score]
    
    print(f"Score added for {name}!")
    print()

def check_scores():
    """Display scores for a specific user in a DataFrame."""
    name = input("Enter the user's name to check scores: ").strip()
    
    if name in user_scores:
        # create a DataFrame
        df = pd.DataFrame({"Score": user_scores[name]}, index=range(1, len(user_scores[name]) + 1))
        print(f"Scores for {name}:")
        print(df)
    else:
        print(f"No scores found for {name}.")
    print()  

def main():
    """Main menu for the application."""
    while True:
        print("Menu:")
        print("a. Add Score")
        print("b. Check Scores")
        print("c. Exit")
        choice = input("").strip().lower()
        
        if choice == 'a':
            add_score()
        elif choice == 'b':
            check_scores()
        elif choice == 'c':
            print("Exiting the application. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
            print()  
            
if __name__ == "__main__":
    main()