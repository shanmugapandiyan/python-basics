import random
from typing import ParamSpecArgs
def get_choices():
  player_choice=input("Choose your choice in(stone,paper,sessor)")
  option=["rock","paper","sissor"]
  computer_choice=random.choice(option)
  choices={"player":player_choice,"computer":computer_choice}
  return choices
def dj(player,computer):
  print(f"you choose {player} computer choose {computer}")
  if player==computer:
    return "draw"
  elif player=="rock":
    if computer=="paper":
      return "paper will cover the rock and You lost"
    else:
      return "rock will cut the sissor and You win"
  elif player=="sissor":
    
    if computer=="paper":
      return "sissor will cut the paper,You Win"
    else:
      return "rock will broke the sissor,You lost"

  elif player=="paper":
    if computer=="sissor":
      return "sissor will cut the paper,you lost"
    else:
      return "paper will cover the stone ,you win"
a=get_choices()
result=dj(a["player"],a["computer"])
print(result)
