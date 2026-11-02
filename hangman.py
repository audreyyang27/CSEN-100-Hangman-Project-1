import random

def header():
  print()
  print("----------------------------------------")
  print("              Hangman Game              ")
  print("----------------------------------------")
  print()

def rules():
  print()
  print("Rules: ")
  print("1. All answers in LOWERCASE")
  print("2. You get SIX lives")
  print("3. Only enter ONE letter at a time")
  print()


word_bank = ["Plant", "Cloud","Brick","Flame", "Stone", "Drift",."Crown","Maple", "Shore", ."Bloom","Crack", "Tiger", "Frost",."Brush", "Grain", "Spark", ."Wheel", "Dream", "Torch", "Plain", "Shell", ."Track", ."Ghost","Field",."Crane", "Swift","Amber","Storm","Charm","River"]


lives = 6
print ("Let's play hangman!")

nextround = True
while nextround:
  chosen_word = random.choice(word_bank)
  display = []
  for letter in chosen_word:
    display.apprend("_")
  print(" ".join(display))
  print("Lives left:", lives)


