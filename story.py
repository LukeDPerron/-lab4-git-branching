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

def right_path():
    print("You walk right and encounter a talking squirrel who challenges you to a duel.")
    print("You take out a magic wand and shoot that thang")
    print("The squirrel perishes, leaving behind a note that says ('stay safe on your adventures, dad)")

def center_path():
    print("you walk the center way and meet a friend named Numair")

def center_path():
    print("you walk the center way and meet a friend named Numair")

if __name__ == "__main__":
    intro()
