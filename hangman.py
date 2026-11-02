import random

def header():
  print()
  print("----------------------------------------")
  print("              Hangman Game              ")
  print("----------------------------------------")
  print("           Let's play Hangman!          ")
  print()

def rules():
  print()
  print("Rules: ")
  print("1. All answers in LOWERCASE")
  print("2. You get SIX lives")
  print("3. Only enter ONE letter at a time")
  print()

def setup():
  word_bank = ["Plant", "Cloud","Brick","Flame", "Stone", "Drift",."Crown","Maple", "Shore", ."Bloom","Crack", "Tiger", "Frost",."Brush", "Grain", "Spark", ."Wheel", "Dream", "Torch", "Plain", "Shell", ."Track", ."Ghost","Field",."Crane", "Swift","Amber","Storm","Charm","River"]

  chosen_word = random.choice(word_bank)
  lives = 6
  guesses = []


def game()"
  display = ""

  for character in word:
      if character in guesses:
          display += character + " "
      else:
          display += "_ "






