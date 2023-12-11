# Import random module
import random

# Define the minimum and maximum values of the dice
min_value = 1
max_value = 6

# Ask the user how many dice they want to roll
num_dice = int(input("How many dice do you want to roll? "))

# Validate the user input
if num_dice < 1 or num_dice > 6:
  print("Invalid number of dice. Please enter a number between 1 and 6.")
else:
  # Loop through the number of dice
  for i in range(num_dice):
    # Generate a random number between the minimum and maximum values
    dice = random.randint(min_value, max_value)
    # Print the dice value
    print(f"Dice {i+1}: {dice}")
