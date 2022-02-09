
import random
from art import logo
from art import vs
import replit

from game_data import data

def random_picker(data):
  number_of_people = 0
  for people in data:
    number_of_people = number_of_people + 1
  return random.randint(0, number_of_people - 1)


  # print(f"There are {number_of_people} people")
  # print(f"The random number is {number_of_people} people")

#We pick the number for the initial character/celeb/org
a_char_num = random_picker(data)
game_over = "n"

wins = 0 

#print(a_char_num)
while game_over == "n":
  print(logo)
  if wins > 0:
    print(f"You're right! Current score: {wins}")
  print(f"Compare A: {data[a_char_num]['name']}, {data[a_char_num]['description']}, {data[a_char_num]['country']}")

  #Print the next contestant
  b_char_num = random_picker(data)
  while b_char_num == a_char_num:
    print("#Debug: They duped!\n#Debug: Re-rolling...")
    b_char_num = random_picker(data)
  print(vs)
  print(f"Against B: {data[b_char_num]['name']}, {data[b_char_num]['description']}, {data[b_char_num]['country']}")

  if data[a_char_num]['follower_count'] > data[b_char_num]['follower_count']:
    correct_answer = "a"
  elif data[a_char_num]['follower_count'] < data[b_char_num]['follower_count']:
    correct_answer = "b"

  guess = input("Who has more followers? Type 'A' or 'B': ")
  if guess.lower() == correct_answer: 
    wins = wins + 1
  else:
    game_over = "y"




  a_char_num = b_char_num
  replit.clear()


print(f"Game Over.\nFinal Score : {wins}")
