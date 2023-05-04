from art import logo, vs
import random
from game_data import data
import os
from time import sleep

print(logo)


SCORE = 0

def choice_from_list():
  random_choice = (random.choice(data))
  return(random_choice)



def check_game():
  global SCORE

  choice = choice_from_list()

  name = (choice["name"])
  description = (choice["description"])
  country = (choice["country"])
  folowers = (choice["follower_count"])
  
  print(f"Compare A: {name}, a {description}, from {country}.")
  
  print(vs)
  
  choice_b = choice_from_list()
  
  name_b = (choice_b["name"])
  description_b = (choice_b["description"])
  country_b = (choice_b["country"])
  folowers_b = (choice_b["follower_count"])
  
  print(f"Against B: {name_b}, a {description_b}, from {country_b}.")
  print(f"Your current score is {SCORE}")
  
  answer = input("Who has more followers? Type 'A' or 'B': ")


  
  if answer == "A":
    if folowers > folowers_b:
      SCORE += 1
      print(f"You're right! Current score: {SCORE}.")
    if folowers_b > folowers:
      print(f"Sorry, that's wrong. Final score: {SCORE}")
  
  if answer == "B":
    if folowers > folowers_b:
      SCORE += 1
      print(f"You're right! Current score: {SCORE}.")
    if folowers_b > folowers:
      print(f"Sorry, that's wrong. Final score: {SCORE}")
  sleep(3)
  os.system('clear')


GAME_IS_ON = True

while GAME_IS_ON:
  check_game()
  
