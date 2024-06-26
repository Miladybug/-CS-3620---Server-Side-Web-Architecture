def find_the_treasure():
    print("Congradulations! You found the treasure!")
    f = open("adventure_outcomes.txt", "w")
    f.write("Found the treasure!\n")
    print("Play again?")
    f.close()
    print("\t1: Yes")
    print("\t2: No")
    choice = input()
    if choice == "1":
        main()
    if choice == "2":
        print("Thanks for playing!")
        print("Outcomes: ")
        read_outcomes()

def leave_the_forest():
    print("You left the forest.")
    f = open("adventure_outcomes.txt", "w")
    f.write("Left the forest.\n")
    print("Play again?")
    f.close()
    print("Play again?")
    print("\t1: Yes")
    print("\t2: No")
    choice = input()
    if choice == "1":
        main()
    if choice == "2":
        print("Thanks for playing!")
        print("Outcomes: ")
        read_outcomes()

def read_outcomes():
    f = open("adventure_outcomes.txt", "r")
    print(f.read())
    f.close()

def main():
    print("You find yourself at the edge of an ancient, enchanted grove. Legends say that deep within this forest lies a hidden treasure guarded by mystical creatures. As you step into the grove, you feel a tingle of magic in the air. Your adventure begins now.")
    # Decision Point 1
    print("\t1: Follow the Overgrown Path")
    print("\t2: Venture into the Dense Thicket.")
    choice = input()
    if choice == "1":
        print("You decide to follow the overgrown path. The path winds through the trees, and you soon come across a fork in the road.")
        # Decision Point 2
        print("\t1: Take the left fork")
        print("\t2: Take the right fork")
        choice = input()
        if choice == "1":
            print("Taking the left fork, you soon find yourself at a clearing with a sparkling stream. A beautiful, ethereal figure appears before you.")
            # Decision Point 4
            print("\t1: Speak to the Figure")
            print("\t2: Ignore the figure and follow the stream")
            choice = input()
            if choice == "1":
                print("You speak to the ethereal figure, who introduces herself as Elara, the guardian of the grove. She offers you a magical charm for protection.")
                # Decision Point 8
                print("\t1: Accept the charm")
                print("\t2: Decline the charm")
                choice = input()
                if choice == "1":
                    print("Accepting the charm from Elara, you feel a surge of magical energy. She guides you to a secret grove where the treasure is said to be hidden.")
                    find_the_treasure()
                if choice == "2":
                    print("Declining the charm, you continue your journey and find the edge of the forest.")
                    leave_the_forest()
            if choice == "2":
                print("Ignoring the figure, you follow the stream and find a shimmering portal at the water's edge.")
                # Decision Point 9
                print("\t1: Enter the portal")
                print("\t2: Turn back and explore another path")
                if choice == "1":
                    print("Entering the portal, you find yourself in a mystical realm filled with floating islands and magical creatures.")
                    find_the_treasure()
                if choice == "2":
                    print("Turning back, you retrace your steps and choose another path, eventually finding the edge of the forest")
                    leave_the_forest()
        if choice == "2":
            print("Taking the right fork, you encounter a group of friendly forest creatures. They offer to guide you through the grove.")
            # Decision Point 5
            print("\t1: Accept their help")
            print("\t2: Politely decline and continue alone")
            choice = input()
            if choice == "1":
                print("Accepting the creatures' help, they lead you to a hidden glade filled with rare flowers and magical herbs.")
                # Decision Point 10
                print("\t1: Collect some herbs")
                print("\t2: Thank the creatures and continue on")
                if choice == "1":
                    print("Collecting herbs from the hidden glade, you feel their magical properties and decide to use them later. You continue on, and find the edge of the forest.")
                    leave_the_forest()
                if choice == "2":
                    print("Thanking the creatures, you continue on your way and eventually find the hidden treasure of the grove.")
                    find_the_treasure()
            if choice == "2":
                print("Declining their help, you wander deeper into the forest and stumble upon an old, mysterious chest.")
                find_the_treasure()
    if choice == "2":
        print("You choose to venture into the dense thicket. The foliage is thick, and you have to push through the underbrush. Suddenly, you hear a rustling noise behind you.")
        # Decision Point 3
        print("\t1: Investigate the noise")
        print("\t2: Keep moving forward")
        choice = input()
        if choice == "1":
            print("You decide to investigate the noise and find a lost, injured fawn. It looks at you with pleading eyes.")
            # Decision Point 6
            print("\t1: Help the fawn")
            print("\t2: Leave the fawn and continue on")
            choice = input()
            if choice == "1":
                print("You help the fawn, and it transforms into a grateful fairy. She offers you a boon.")
                find_the_treasure()
            if choice == "2":
                print("Leaving the fawn, you proceed and find the edge of the woods.")
                leave_the_forest()
        if choice == "2":
            print("You choose to keep moving forward and eventually come across an ancient tree with a door carved into its trunk.")
            # Decision Point 7
            print("\t1: Enter the door")
            print("\t2: Examine the area around the tree")
            choice = input()
            if choice == "1":
                print("Entering the door in the tree, you discover a hidden underground library filled with ancient scrolls and books.")
                find_the_treasure()
            if choice == "2":
                print("Examining the area around the tree, you find a hidden map etched into the bark.")
                find_the_treasure()

main()
