#!/usr/bin/env python
# coding: utf-8

# # USE IDLE TO RUN PROGRAMS: GUESS THE NUMBER
# 
# <br>Hernan Chavez, 2024<br/>
# Ref. Michael Urban, Joel Murach, and Mike Murach. 2016. Murach's Python Programming. Mike Murach & Associates<br/>

# In[1]:


import random

LIMIT = 10

def display_title():
    print("Guess the number!")
    print()

def play_game():    
    number = random.randint(1, LIMIT)
    print(f"I'm thinking of a number from 1 to {LIMIT}\n")
    count = 1

    while (guess := int(input("Your guess: "))) != number:
        if guess < number:
            print("Too low.")
            count += 1
        elif guess > number:
            print("Too high.")
            count += 1
    print(f"You guessed it in {count} tries.\n")
     
def main():
    display_title()
    again = "y"
    while again.lower() == "y":
        play_game()
        again = input("Would you like to play again? (y/n): ")
        print()
    print("Bye!")

# if started as the main module, call the main function
if __name__ == "__main__":
    main()

