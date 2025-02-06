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
    
    # add the user's score to dictionary
    if name in user_scores:
        user_scores[name].append(int(score))
    else:
        user_scores[name] = [int(score)]
    
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
        print("User does not exist")
        return
    print()  

def show_total_score():
    """Display the total score for a specific user."""
    name = input("Enter the user's name to check total score: ").strip()
    
    if name in user_scores:
        total_score = sum(user_scores[name])
        print(f"Total score for {name}: {total_score}")
    else:
        print("User does not exist")
        return
    print()

def main():
    """Main menu for the application."""
    while True:
        print("Menu:")
        print("a. Add Score")
        print("b. Check Scores")
        print("c. Show Total Score")
        print("d. Exit")
        choice = input("Enter your choice: ").strip().lower()
        
        if choice == 'a':
            add_score()
        elif choice == 'b':
            check_scores()
        elif choice == 'c':
            show_total_score()
        elif choice == 'd':
            print("Exiting the application. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
            print()  
            
if __name__ == "__main__":
    main()