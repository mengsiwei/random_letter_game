import random
import pyfiglet
import time

letters = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
random.shuffle(letters)
selected = letters[:5]

input(" Happy Game Time!\n In this game, you will give a random letter from A to Z.\n Each time you receive the letter, please find the item in your space beginning with this letter.\n As soon as possible!\n Press Enter to start!")

for i, letter in enumerate(selected):
    input(f" {i+1} round: Print Enter to Show Random Letter...")
    ascii_art = pyfiglet.figlet_format(letter)
    
    print(ascii_art)
