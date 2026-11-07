import random

def header():
  print()
  print("----------------------------------------")
  print("              Hangman Game              ")
  print("----------------------------------------")
  print("           Let's play Hangman           ")

def rules():
  print()
  print("Rules: ")
  print("1. All answers in LOWERCASE")
  print("2. You get SIX lives")
  print("3. Only enter ONE letter at a time")
  print()

### List of possible words to pick ###
word_bank = ["Plant", "Cloud","Brick","Flame", "Stone", "Drift","Crown","Maple", "Shore", "Bloom","Crack",
             "Tiger", "Frost","Brush", "Grain", "Spark", "Wheel", "Dream", "Torch", "Plain", "Shell", "Track",
             "Ghost","Field","Crane", "Swift","Amber","Storm","Charm","River","Cream","Glass","Apple",
             "Apply","Share","Phone","Dread","Drama","Jones","Amaze","Grape","Beach","Snake","Mango","Candy",
            "Lemon","Light","Music","Storm","Green","Ocean","Chair","Crown","Nurse","Proxy","Zesty","Smile","Bread"]

### Start of Game ###
header()
rules()


#### Main game function ###
def game():
  nextround = True
  while nextround:
    
    # Choose a random word
    chosen_word = random.choice(word_bank)

    # Reset lives for each new game
    lives = 6

    # Put an underscores place holder for each letter
    # Set variable "Display" to a blank string and add underscores
    display = []
    for letter in chosen_word:
      display.append("_")

    # Keep playing while lives remaine
    while lives>0:
      print(" ".join(display))
      print("Lives remaining:", lives)

      # Check if all letters are guessed
      if "_" not in display:
          print("Congrats, you won!")
        break

      # Ask for a letter
      guess = input("Guess a letter:")
      guess = guess.lower()

      # Check for invalid inout ???

      # check for repeated letters ???

      # Check each letter in the word
      if guess in chosen_word:
          # Correct guess, look for the letter's place and put it there in Display
          # If there are multiple instances of the letter, the loop will put all of them
          for i in range(len(chosen_word)):
             if chosen_word[i] == guess:
                display[i] = guess
      else:
          # Incorrect guess, reduce one live 
          lives=lives-1
          print("You guessed a wring letter, try again!")

