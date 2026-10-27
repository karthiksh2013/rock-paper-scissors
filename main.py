
# ============================================================
# ROCK, PAPER, SCISSORS GAME
# Developed by: Karthik
# Description: A simple game where the user plays against
#              an opponent controlled by the computer.
# ============================================================

# Import the random module to generate random choices

import random

# ------------------------------------------------------------
# SECTION 1: DEFINE THE GAME CHOICES
# ------------------------------------------------------------

# R = Rock
# P = Paper
# S = Scissor

# Create a dictionary to map short choices to their full names
dictionary = {
    "R": "Rock",
     "P": "Paper",
    "S": "Scissor"
}


# ------------------------------------------------------------
# SECTION 2: DISPLAY THE WELCOME MESSAGE
# ------------------------------------------------------------

print("Welcome to Stone, Paper, Scissors Game!")
print("Before you play, please enter the player details.")


# ------------------------------------------------------------
# SECTION 3: GET PLAYER NAMES
# ------------------------------------------------------------

# Ask the user to enter their name
name = input("Enter your name: ")

# Ask the user to enter the opponent's name
opponent_name = input("Enter your opponent's name: ")

# Display a personalized welcome message
print(
    f"\nHello, {name}! Let's play Rock, Paper, "
    f"Scissors against {opponent_name}."
)


# ------------------------------------------------------------
# SECTION 4: INITIALIZE THE SCORES
# ------------------------------------------------------------

# Store the number of rounds won by each player
user_score = 0
opponent_score = 0

# Set the initial value to allow the game to start
play_again = "yes"


# ------------------------------------------------------------
# SECTION 5: MAIN GAME LOOP
# ------------------------------------------------------------

# Continue playing as long as the user enters "yes" or "y"
while play_again.lower() in ["yes", "y"]:

    # --------------------------------------------------------
    # STEP 1: GENERATE THE OPPONENT'S CHOICE
    # --------------------------------------------------------

    # Randomly select Rock, Paper, or Scissor for the opponent
    computer = random.choice(list(dictionary.values()))

    # --------------------------------------------------------
    # STEP 2: GET THE USER'S CHOICE
    # --------------------------------------------------------

    # Ask the user to enter R, P, or S
    # Convert the input to uppercase for consistent comparison
    you = input("\nEnter your choice (R, P, S): ").upper()

    # Display a separator between game sections
    print("***********************************")

    # Convert the user's letter into its full name
    # If the input is invalid, return "Invalid choice"
    user_choice_word = dictionary.get(you, "Invalid choice")

    # Display both players' choices
    print(f"{opponent_name} chose: {computer}")
    print(f"You chose: {user_choice_word}")

    # --------------------------------------------------------
    # STEP 3: VALIDATE THE USER'S INPUT
    # --------------------------------------------------------

    # Check whether the entered choice exists in the dictionary
    if you not in dictionary:

        # Display an error message for invalid input
        print("Input is invalid, please try again.")

    else:

        # ----------------------------------------------------
        # STEP 4: DETERMINE THE WINNER
        # ----------------------------------------------------

        # Case 1: Both players choose the same option
        if user_choice_word == computer:
            print("It's a tie!")

        # Case 2: Rock beats Scissor
        elif you == "R" and computer == "Scissor":
            print("You win!")
            user_score += 1

        # Case 3: Paper beats Rock
        elif you == "R" and computer == "Paper":
            print(f"{opponent_name} wins!")
            opponent_score += 1

        # Case 4: Paper beats Rock
        elif you == "P" and computer == "Rock":
            print("You win!")
            user_score += 1

        # Case 5: Scissor beats Paper
        elif you == "P" and computer == "Scissor":
            print(f"{opponent_name} wins!")
            opponent_score += 1

        # Case 6: Scissor beats Paper
        elif you == "S" and computer == "Paper":
            print("You win!")
            user_score += 1

        # Case 7: Rock beats Scissor
        elif you == "S" and computer == "Rock":
            print(f"{opponent_name} wins!")
            opponent_score += 1

    # --------------------------------------------------------
    # STEP 5: DISPLAY THE CURRENT SCOREBOARD
    # --------------------------------------------------------

    # Print the scores of both players after each round
    print("\n--- SCOREBOARD ---")
    print(f"{name}: {user_score} | {opponent_name}: {opponent_score}")
    print("------------------")

    # --------------------------------------------------------
    # STEP 6: ASK WHETHER THE USER WANTS TO PLAY AGAIN
    # --------------------------------------------------------

    # Accept "yes" or "y" to continue playing
    play_again = input(
        "\nDo you want to play another game? (yes/no): "
    )


# ------------------------------------------------------------
# SECTION 6: DISPLAY THE FINAL RESULTS
# ------------------------------------------------------------

# Display the final scores after the game ends
print(
    f"\nFinal Score -> {name}: {user_score} | "
    f"{opponent_name}: {opponent_score}"
)


# ------------------------------------------------------------
# SECTION 7: COLLECT THE PLAYER'S RATING
# ------------------------------------------------------------

# Thank the user for playing
print(f"Thank you for playing, {name}!")

# Ask the user to rate the game out of 5 stars
print("Rate the game out of 5 stars.")
rating = input("Enter your rating: ")

# Display the rating entered by the user
print(f"Thank you for your rating: {rating}/5")


# ------------------------------------------------------------
# SECTION 8: DEVELOPER INFORMATION
# ------------------------------------------------------------

# Display the name of the developer
print("This game is developed by: Karthik")
