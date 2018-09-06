# -*- coding: utf-8 -*-
"""
Created on Wed Sep  5 21:22:20 2018

@author: Harmit Jasani
"""
from random import randint
con = True

while(con):
    comp_play = True
    choice = input("\n 1) Rock \n 2) Paper \n 3) Scissors \n 4) Lizard \n 5) Spock \n Pick one: ")
    
    if choice == "1":
       print("\nYour choice is Rock")
       var = "Rock"
    elif choice == "2":
       print("\nYour choice is Paper")
       var = "Paper"
    elif choice == "3":
       print("\nYour choice is Scissors")
       var = "Scissors"
    elif choice == "4":
       print("\nYour choice is Lizard")
       var = "Lizard"
    elif choice == "5":
       print("\nYour choice is Spock")
       var = "Spock"
    else:
        print("Your choice was not recognized")
        comp_play = False
    
    if comp_play == True: 
        value = randint(1, 5)
        if value == 1:
            print("Computer chose Rock")
            comp_var = "Rock"
        elif value ==2:
            print("Computer chose Paper")
            comp_var = "Paper"
        elif value == 3:
            print("Computer chose Scissors")
            comp_var = "Scissors"
        elif value == 4:
            print("Computer chose Lizard")
            comp_var = "Lizard"
        elif value == 5:
            print("Computer chose Spock")
            comp_var = "Spock"
        else:
            print("Computer is tired!")
        if var == comp_var:
            print("\nTie")
        elif(var=="Rock" and comp_var=="Paper") or (var=="Scissors" and comp_var=="Rock") or \
        (var=="Paper" and comp_var=="Scissors") or (var=="Lizard" and comp_var=="Rock") or \
        (var=="Spock" and comp_var=="Lizard") or (var=="Scissors" and comp_var=="Spock") or \
        (var=="Lizard" and comp_var=="Scissors") or (var=="Paper" and comp_var=="Lizard") or \
        (var=="Spock" and comp_var=="Paper") or (var=="Rock" and comp_var=="Spock"):
            print("\nComputer wins!")
        else:
            print("\nYou win!")
    
        con_str = input("Do you want to continue: Y or N?\t")
        if con_str=="Y":
            con = True
        else:
            con= False
    else:
        print("Computer won't play! Try again ")