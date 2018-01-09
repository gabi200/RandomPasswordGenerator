import os,random

words = ["cat","me","game","dog","Lol","haha","xD","x"]
number = random.randint(36,861)
symbols = ["!","?","@","#","&","€","_"]
bar = "-" * 32

r = random.randint(0,7)
r1 = random.randint(0,6)
r2 = random.randint(1,3)

if r in [0,1,2,3,4,5,6,7]:
	rw = words[r]
if r1 in [0,1,2,3,4,5,6]:
	rs = symbols[r1]

if r2 == 1:
	password = rw + rs + str(number)
if r2 == 2:
	password = str(number) + rs + rw + rs
if r2 == 3:
	password = rs + str(number) + rw + str(number)

print("Random Password Generator v1.0.1")
print(bar)
input("Press ENTER to generate a password...")
os.system("clear")
print("Here's your password:")
print(bar)
print(password)
