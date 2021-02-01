#!/usr/bin/env python3
import sys
assert sys.version_info >= (3,9), "This script requires at least Python 3.9"
taco = 1
beef = 2
chickenpie = 3
noodles = 4
egg = 5
tastyburger = 6
burntpopcorn = 7
number = 8
pumpkinpie = 9
scone = 10
guess = input("Guess a number from 1 to 10: ")
guess = int(guess)
if guess == taco: print("You got a taco.")
if guess == number: print("Great job! You got it!")
if guess == beef: print("You got beef.")
if guess == noodles: print("You got noodles.")
if guess == egg: print("You got a dozen eggs.")
if guess == chickenpie: print("That's a Chicken Pie you just received!")
if guess == tastyburger: print("You just got one tasty burger!")
if guess == burntpopcorn: print("Oh no! You got burnt popcorn!")
if guess == pumpkinpie: print("You received a nice slice of pumpkin pie.")
if guess == scone: print("You got a handful of scones!")
else: print("Lol you got a number that was assigned to a food! I mean, that's pretty cool, but try to guess the number not assigned to food!")