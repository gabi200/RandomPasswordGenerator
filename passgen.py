# Random Password Generator by gabi200 @ github / (c)2019

import os
import random

words = ["cat","me","game","dog","Lol","haha","xD","x","super","royale","python","boom","math","best","riptide","loopy"]
symbols = ["!","?","@","#","&","€","_","*","^","$","\\","☼","♀"] 
bar = "-" * 32

def again():
    generate()

def generate():
   number = random.randint(36,861)
   number1 = random.randint(56,47304)
   r = random.randint(0,(len(words) - 1))
   r1 = random.randint(0,(len(symbols) - 1))
   r2 = random.randint(1,5)

   rw = words[r]
   rs = symbols[r1] 

   if r2 == 1: 	
      password = rw + rs + str(number)
   if r2 == 2: 
    	password = str(number) + rs + rw + rs
   if r2 == 3: 
      	password = rs + str(number) + rw + str(number1)
   if r2 == 4: 
      	password = rw + str(number1) + rs + str(number)
   if r2 == 5:
	    password = rw + str(number) + str(number1) + rs + rw + rs
   print("Random Password Generator v1.0.5")
   print("by gabi200")
   print(bar) 
   input("Press ENTER to generate a password...")
   os.system('cls' if os.name == 'nt' else 'clear')
   print("Here's your password:")
   print(bar)
   print(password)
   userin = input("Generate another password?(y/n) ")
   if userin == "y":
       os.system('cls' if os.name == 'nt' else 'clear')
       again()

generate()
