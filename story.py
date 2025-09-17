def intro():
    print("You wake up in a dark forest. You can go left, center or right.")
    choice = input("Which direction do you choose? (left/center/right): ").strip().lower()
    if choice == "left":
        left_path()
    elif choice == "right":
        right_path()
    elif choice == "center":
        center_path()
    else:
        print("You stand still, unsure what to do. The forest swallows you.")

def left_path():
    print("You walk left and find a mysterious glowing sword stuck in a stone.")
    print("You grab the shaft of the sword, pulling with all your might.")
    print("The sword comes out easily, like it was made for you")
    print("You continue walking down the path and encounter a foe, Ahmad the evil, who runs towards you")
    print("You dodge Ahmad, switching to being the attacker")
    print("you jab your sword to Ahmad's chest, defeating your foe")
def right_path():
    print("You walk right and encounter a talking squirrel who challenges you to a duel.")

def center_path():
    print("you walk the center way and meet a friend named Numair")

if __name__ == "__main__":
    intro()
