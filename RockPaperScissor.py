import random


user=input("Enter 'R' for Rock, 'P' for Paper, 'S' for Scissor: ").capitalize()
computer=random.choice(['R','P','S'])
if user==computer:
    print("Its a Tie")
elif user=='R' and computer=='S':
    print(f"You wins! because computer selected {computer} while you selected {user}")
elif user=='P' and computer=='R':
    print(f"You wins! because computer selected {computer} while you selected {user}")
elif user=='S' and computer=='P':
    print(f"You wins! because computer selected {computer} while you selected {user}")
else:
    print(f"Computer wins! because computer selected {computer} while you selected {user}")


