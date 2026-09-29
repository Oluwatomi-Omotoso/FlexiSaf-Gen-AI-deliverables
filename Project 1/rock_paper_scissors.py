import random

options = ("rock", "paper", "scissors")
player = None

bot = random.choice(options)
while player not in options:
    player = input("Enter a choice (rock, paper or scissors): ")


print(f"Player : {player}")
print(f"Bot: {bot}")


if player == bot:
    print("Tie")
elif player == "rock" and bot == "scissors":
    print("You win!")
elif player == "paper" and bot == "rock":
    print("You win!")
elif player == "scissors" and bot == "paper":
    print("You win!")
else:
    print("You lose")
