# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 13:12:26 2025

@author: Andrew Hunter
"""

import random

class DungeonCrawler:
    def __init__(self):
        # creation of dungeon
        self.dungeon = [[(x, y) for y in range(2)] for x in range(4)]
        
        #random assignment of position for entrance and exit
        self.start = (random.randint(0, 3), random.randint(0, 1))
        self.exit = (random.randint(0, 3), random.randint(0, 1))

        while self.exit == self.start:
            self.exit = (random.randint(0, 3), random.randint(0, 1))
            
        # setup
        self.position = self.start
        self.moves = 0
    
    #display of dungeon
    def display(self):
        for y in range(2):
            for x in range(4):
                if (x, y) == self.position:
                    print("P", end=" ")  # player
                elif (x, y) == self.exit:
                    print("E", end=" ")  # exit
                else:
                    print(".", end=" ")  # empty space 
            print()
        print(f"Current Position: {self.position}, Moves: {self.moves}")
        
    # movement system
    def move(self, direction):
        x, y = self.position
        if direction == 'up' and y > 0:
            self.position = (x, y - 1)
        elif direction == 'down' and y < 1:
            self.position = (x, y + 1)
        elif direction == 'left' and x > 0:
            self.position = (x - 1, y)
        elif direction == 'right' and x < 3:
            self.position = (x + 1, y)
        else:
            print("Invalid move")
            return False
        
        self.moves += 1
        return True

    # shows the display, along with some text
    def play(self):
        print("You've been dropped into a dungeon!")
        print("You are P, and you must reach E to escape!")
        self.display()
        
        while self.position != self.exit:
            direction = input("Move (up/down/left/right) or 'exit' to quit: ").lower()
            
            if direction == 'exit':
                print(f"You left early! Success=False, Moves={self.moves}")
                break
            
            if self.move(direction):
                self.display()
            else:
                print("Try again.")
        
        if self.position == self.exit:
            print(f"Congratulations! You've reached the exit! Success=True, Moves={self.moves}")

# Start the game
game = DungeonCrawler()
game.play()