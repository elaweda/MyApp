import random

#crew list
crew = ["Red", "Cyan", "Blue", "Lime", "Green", "White", "Black", "Purple", "Brown", "Mr. Cheese"]

impostor = "Mr. Cheese"
    
   
#prints some art, sets the atmosphere mostly
def start_screen():
    print("""

░█████╗░███╗░░░███╗░█████╗░███╗░░██╗░██████╗░░██████╗████████╗  ░█████╗░██╗░░░██╗██████╗░
██╔══██╗████╗░████║██╔══██╗████╗░██║██╔════╝░██╔════╝╚══██╔══╝  ██╔══██╗██║░░░██║██╔══██╗
███████║██╔████╔██║██║░░██║██╔██╗██║██║░░██╗░╚█████╗░░░░██║░░░  ██║░░██║██║░░░██║██████╔╝
██╔══██║██║╚██╔╝██║██║░░██║██║╚████║██║░░╚██╗░╚═══██╗░░░██║░░░  ██║░░██║██║░░░██║██╔══██╗
██║░░██║██║░╚═╝░██║╚█████╔╝██║░╚███║╚██████╔╝██████╔╝░░░██║░░░  ╚█████╔╝╚██████╔╝██║░░██║
╚═╝░░╚═╝╚═╝░░░░░╚═╝░╚════╝░╚═╝░░╚══╝░╚═════╝░╚═════╝░░░░╚═╝░░░  ░╚════╝░░╚═════╝░╚═╝░░╚═╝

░██████╗░██████╗░░█████╗░██╗░░░██╗██████╗░             *a*
██╔════╝░██╔══██╗██╔══██╗██║░░░██║██╔══██╗          **special**
██║░░██╗░██████╔╝██║░░██║██║░░░██║██████╔╝       ***adventure***
██║░░╚██╗██╔══██╗██║░░██║██║░░░██║██╔═══╝░        *****for*****
╚██████╔╝██║░░██║╚█████╔╝╚██████╔╝██║░░░░░            *Eden*
░╚═════╝░╚═╝░░╚═╝░╚════╝░░╚═════╝░╚═╝░░░░░    
    ⠀
 ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣤⣤⣤⣤⣤⣶⣦⣤⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⡿⠛⠉⠙⠛⠛⠛⠛⠻⢿⣿⣷⣤⡀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⠋⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⠈⢻⣿⣿⡄⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣸⣿⡏⠀⠀⠀⣠⣶⣾⣿⣿⣿⠿⠿⠿⢿⣿⣿⣿⣄⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣿⣿⠁⠀⠀⢰⣿⣿⣯⠁⠀⠀⠀⠀⠀⠀⠀⠈⠙⢿⣷⡄⠀
⠀⠀⣀⣤⣴⣶⣶⣿⡟⠀⠀⠀⢸⣿⣿⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣷⠀
⠀⢰⣿⡟⠋⠉⣹⣿⡇⠀⠀⠀⠘⣿⣿⣿⣿⣷⣦⣤⣤⣤⣶⣶⣶⣶⣿⣿⣿⠀
⠀⢸⣿⡇⠀⠀⣿⣿⡇⠀⠀⠀⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠃⠀
⠀⣸⣿⡇⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠉⠻⠿⣿⣿⣿⣿⡿⠿⠿⠛⢻⣿⡇⠀⠀
⠀⣿⣿⠁⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣧⠀⠀
⠀⣿⣿⠀⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⠀⠀
⠀⣿⣿⠀⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⠀⠀
⠀⢿⣿⡆⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⡇⠀⠀
⠀⠸⣿⣧⡀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⠃⠀⠀
⠀⠀⠛⢿⣿⣿⣿⣿⣇⠀⠀⠀⠀⠀⣰⣿⣿⣷⣶⣶⣶⣶⠶⠀⢠⣿⣿⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣿⣿⠀⠀⠀⠀⠀⣿⣿⡇⠀⣽⣿⡏⠁⠀⠀⢸⣿⡇⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣿⣿⠀⠀⠀⠀⠀⣿⣿⡇⠀⢹⣿⡆⠀⠀⠀⣸⣿⠇⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢿⣿⣦⣄⣀⣠⣴⣿⣿⠁⠀⠈⠻⣿⣿⣿⣿⡿⠏⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠈⠛⠻⠿⠿⠿⠿⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    """)
    input("Press ENTER to START")
    separate_events()


#prints some dashes to separate all the prints from game choices
def separate_events():
    print("*--------------------------------------------------------------------------------*")


#prints some setting for the game, presents first choice
def start():
    print("""You wake up on a large spaceship, ready to start the completing your daily tasks.
You head to the cafeteria to get some food.
When you get there, you see your crewmates having an emergency meeting.
What do you do?""")
    startcafe()


#user chooses either join meeting or eat food, calls associated function
def startcafe():
    choice = input("1. Join the meeting.\n2. Eat food.\n> ")
    print("You chose:", choice)

    if choice in ("1", "join", "Join", "one", "One"):
        separate_events()
        meeting(1)

    elif choice in ("2", "eat", "Eat", "two", "Two"):
        separate_events()
        eat(1)

    else:
        print("Pick 1 or 2.")
        startcafe()


#prints more story stuff, user chooses vote or walk somewhere else
def meeting(a):
    if a == 1:
        print("""You join the meeting.
It's pretty heated, and everyone seems to be ready to throw each other off the ship!
The crew informs you that someone was murdered and that signs of sabotage were discovered!

\"There's an IMPOSTOR among us!\"

The crew wants to vote on who the culpit could be, but you know that there are important tasks to be done.
What do you do?""")

    elif a == 2:
        print("""\"There's an IMPOSTER among us!\"

The crew wants to vote on who the culprit could be, but there are also important tasks to be done.
What do you do?""")
        
    choice = input("1. Vote for the most suspicious crewmate.\n2. Go start tasks.\n> ")
    print("You chose:", choice)

    if choice in ("1", "vote", "Vote", "one", "One"):
        separate_events()
        vote()

    elif choice in ("2", "go", "Go", "two", "Two"):
        separate_events()
        walkto()

    else:
        print("Pick 1 or 2.")
        meeting(0)


#user picks food from a list, then decides to stay in the cafe or leave
def eat(a):
    if a == 1:
        print("""You walk towards the kitchen and see that there are a few meal choices available.
What do you want to eat?""")

    choice = input("1. Spaghetti\n2. Ramen\n3. Mac & Cheese\n4. Beans\n> ")
    print("You chose:", choice)

    if choice in ("1", "one", "One", "spaghetti", "Spaghetti"):
        print("The noodles were perfectly cooked and the sauce was delicious. You finish your meal and get up to leave.")
        separate_events()
        walkto()

    elif choice in ("2", "two", "Two", "Ramen", "ramen"):
        print("The broth was hot and savory, and the noodles and toppings were very tasty. You finish your meal and get up to leave.")
        separate_events()
        walkto()

    elif choice in ("3", "three", "Three", "Mac and Cheese", "Mac & Cheese", "mac and cheese", "mac & cheese", "mac", "Mac"):
        print("The mac & cheese was warm and melty; so much yummy cheese! You finish your meal and get up to leave.")
        separate_events()
        walkto()

    elif choice in ("4", "four", "Four", "beans", "Beans"):
        print("The beans were, well, beans. They looked and smelled kinda weird so you get up, throw them away, and leave.")
        separate_events()
        walkto()

    else:
        print("Pick 1, 2, 3, or 4.")
        eat(0)


#user votes for who they think the culprit is, eliminates them
def vote():
    print("Who do you think the impostor is?")
    print("Crewmates:", crew)
    choice = input("> ")
    a = random.randint(1, 10)
    print("You chose:", choice)
    
    if choice in crew:
    
        if a < 5:
            print("The crew has chosen to eject {} from The Skeld. {} of the crewmates remain.".format(choice, len(crew)))
            crew.remove(choice)

            #win conditions            
            if impostor not in crew:
                win()
            
            separate_events()
            walkto()
    
        else:
            print("No one was ejected. {} of the crewmates remain.".format(len(crew)))
            separate_events()
            walkto()
    
    else:
        print("That's not a crew member! Try again.")
        vote()        

        
#user chooses which room to go to
def walkto():
    print("Where would you like to go?")
    choice = input("\n1. Cafeteria\n2. Weapons\n3. Navigation\n4. O2\n5. Shields\n6. Communications\n7. Storage\n8. Admin\n9. Electrical\n10. Lower Engine\n11. Security\n12. Reactor\n13. Upper Engine\n14. MedBay\n\n> ")
    print("You chose:", choice)

    if choice in ("1", "one", "One", "cafe", "Cafe", "cafeteria", "Cafeteria"):
        separate_events()
        cafeteria()

    elif choice in ("2", "two", "Two", "Weapons", "weapons"):
        separate_events()
        weapons()

    elif choice in ("3", "three", "Three", "Navigation", "navigation"):
        separate_events()
        navigation()

    elif choice in ("4", "four", "Four", "O2", "o2"):
        separate_events()
        o2()

    elif choice in ("5", "five", "Five", "shields", "Shields"):
        separate_events()
        shields()

    elif choice in ("6", "six", "Six", "Communications", "communications"):
        separate_events()
        communications()

    elif choice in ("7", "seven", "Seven", "Storage", "storage"):
        separate_events()
        storage()

    elif choice in ("8", "eight", "Eight", "admin", "Admin"):
        separate_events()
        admin()

    elif choice in ("9", "nine", "Nine", "Electrical", "electrical"):
        separate_events()
        electrical()

    elif choice in ("10", "ten", "Ten", "lower engine", "Lower Engine", "lower Engine", "Lower engine"):
        separate_events()
        lower_engine()

    elif choice in ("11", "eleven", "Eleven", "security", "Security"):
        separate_events()
        security()

    elif choice in ("12", "twelve", "Twelve", "Reactor", "reactor"):
        separate_events()
        reactor()

    elif choice in ("13", "thirteen", "Thirteen", "Upper Engine", "upper engine", "Upper engine", "upper Engine"):
        separate_events()
        upper_engine()

    elif choice in ("14", "fourteen", "Fourteen", "medbay", "MedBay", "Medbay"):
        separate_events()
        medbay()

    else:
        print("Pick one of the options listed.")
        walkto()


#tells user they are in the cafeteria, gives choices
def cafeteria():
    print("You're in the Cafeteria. What would you like to do?")
    choice = input("1. Call a meeting.\n2. Eat food.\n3. Tasks.\n4. Leave.\n> ")
    print("You chose:", choice)

    if choice in ("1", "Call", "call", "one", "One"):
        separate_events()
        meeting(2)

    elif choice in ("2", "eat", "Eat", "two", "Two"):
        separate_events()
        eat(1)

    elif choice in ("3", "three", "Three", "tasks", "Tasks"):
        separate_events()
        task(1)

    elif choice in ("4", "four", "Four", "leave", "Leave"):
        separate_events()
        walkto()

    else:
        print("Pick 1, 2, 3, or 4.")
        cafeteria()


def weapons():
    print("You're in Weapons. What would you like to do?")
    choice = input("1. Call a meeting.\n2. Tasks.\n3. Leave.\n> ")
    print("You chose:", choice)

    if choice in ("1", "Call", "call", "one", "One"):
        separate_events()
        meeting(2)

    elif choice in ("2", "tasks", "Tasks", "two", "Two"):
        separate_events()
        task(1)

    elif choice in ("3", "three", "Three", "leave", "Leave"):
        separate_events()
        walkto() 

    else:
        print("Pick 1, 2, or 3.")
        weapons()


def navigation():
    print("You're in Navigation. What would you like to do?")
    choice = input("1. Call a meeting.\n2. Tasks.\n3. Leave.\n> ")
    print("You chose:", choice)

    if choice in ("1", "Call", "call", "one", "One"):
        separate_events()
        meeting(2)

    elif choice in ("2", "tasks", "Tasks", "two", "Two"):
        separate_events()
        task(1)

    elif choice in ("3", "three", "Three", "leave", "Leave"):
        separate_events()
        walkto() 

    else:
        print("Pick 1, 2, or 3.")
        navigation()


def o2():
    print("You're in O2. What would you like to do?")
    choice = input("1. Call a meeting.\n2. Tasks.\n3. Leave.\n> ")
    print("You chose:", choice)

    if choice in ("1", "Call", "call", "one", "One"):
        separate_events()
        meeting(2)

    elif choice in ("2", "tasks", "Tasks", "two", "Two"):
        separate_events()
        task(1)

    elif choice in ("3", "three", "Three", "leave", "Leave"):
        separate_events()
        walkto() 

    else:
        print("Pick 1, 2, or 3.")
        o2()


def shields():
    print("You're in Shields. What would you like to do?")
    choice = input("1. Call a meeting.\n2. Tasks.\n3. Leave.\n> ")
    print("You chose:", choice)

    if choice in ("1", "Call", "call", "one", "One"):
        separate_events()
        meeting(2)

    elif choice in ("2", "tasks", "Tasks", "two", "Two"):
        separate_events()
        task(1)

    elif choice in ("3", "three", "Three", "leave", "Leave"):
        separate_events()
        walkto() 

    else:
        print("Pick 1, 2, or 3.")
        shield()


def communications():
    print("You're in Communications. What would you like to do?")
    choice = input("1. Call a meeting.\n2. Tasks.\n3. Leave.\n> ")
    print("You chose:", choice)

    if choice in ("1", "Call", "call", "one", "One"):
        separate_events()
        meeting(2)

    elif choice in ("2", "tasks", "Tasks", "two", "Two"):
        separate_events()
        task(1)

    elif choice in ("3", "three", "Three", "leave", "Leave"):
        separate_events()
        walkto() 

    else:
        print("Pick 1, 2, or 3.")
        communications()


def storage():
    print("You're in Storage. What would you like to do?")
    choice = input("1. Call a meeting.\n2. Tasks.\n3. Leave.\n> ")
    print("You chose:", choice)

    if choice in ("1", "Call", "call", "one", "One"):
        separate_events()
        meeting(2)

    elif choice in ("2", "tasks", "Tasks", "two", "Two"):
        separate_events()
        task(1)

    elif choice in ("3", "three", "Three", "leave", "Leave"):
        separate_events()
        walkto() 

    else:
        print("Pick 1, 2, or 3.")
        storage()


def admin():
    print("You're in Admin. What would you like to do?")
    choice = input("1. Call a meeting.\n2. Tasks.\n3. Leave.\n> ")
    print("You chose:", choice)

    if choice in ("1", "Call", "call", "one", "One"):
        separate_events()
        meeting(2)

    elif choice in ("2", "tasks", "Tasks", "two", "Two"):
        separate_events()
        task(1)

    elif choice in ("3", "three", "Three", "leave", "Leave"):
        separate_events()
        walkto() 

    else:
        print("Pick 1, 2, or 3.")
        admin()


def electrical():
    print("You're in Electrical. What would you like to do?")
    choice = input("1. Call a meeting.\n2. Tasks.\n3. Leave.\n> ")
    print("You chose:", choice)

    if choice in ("1", "Call", "call", "one", "One"):
        separate_events()
        meeting(2)

    elif choice in ("2", "tasks", "Tasks", "two", "Two"):
        separate_events()
        task(1)

    elif choice in ("3", "three", "Three", "leave", "Leave"):
        separate_events()
        walkto() 

    else:
        print("Pick 1, 2, or 3.")
        electrical()


def lower_engine():
    print("You're in Lower Engine. What would you like to do?")
    choice = input("1. Call a meeting.\n2. Tasks.\n3. Leave.\n> ")
    print("You chose:", choice)

    if choice in ("1", "Call", "call", "one", "One"):
        separate_events()
        meeting(2)

    elif choice in ("2", "tasks", "Tasks", "two", "Two"):
        separate_events()
        task(1)

    elif choice in ("3", "three", "Three", "leave", "Leave"):
        separate_events()
        walkto() 

    else:
        print("Pick 1, 2, or 3.")
        lower_engine()


def security():
    print("You're in Security. What would you like to do?")
    choice = input("1. Call a meeting.\n2. Tasks.\n3. Leave.\n> ")
    print("You chose:", choice)

    if choice in ("1", "Call", "call", "one", "One"):
        separate_events()
        meeting(2)

    elif choice in ("2", "tasks", "Tasks", "two", "Two"):
        separate_events()
        task(1)

    elif choice in ("3", "three", "Three", "leave", "Leave"):
        separate_events()
        walkto() 

    else:
        print("Pick 1, 2, or 3.")
        security()


def reactor():
    print("You're in Reactor. What would you like to do?")
    choice = input("1. Call a meeting.\n2. Tasks.\n3. Leave.\n> ")
    print("You chose:", choice)

    if choice in ("1", "Call", "call", "one", "One"):
        separate_events()
        meeting(2)

    elif choice in ("2", "tasks", "Tasks", "two", "Two"):
        separate_events()
        task(1)

    elif choice in ("3", "three", "Three", "leave", "Leave"):
        separate_events()
        walkto() 

    else:
        print("Pick 1, 2, or 3.")
        reactor()


def upper_engine():
    print("You're in Upper Engine. What would you like to do?")
    choice = input("1. Call a meeting.\n2. Tasks.\n3. Leave.\n> ")
    print("You chose:", choice)

    if choice in ("1", "Call", "call", "one", "One"):
        separate_events()
        meeting(2)

    elif choice in ("2", "tasks", "Tasks", "two", "Two"):
        separate_events()
        task(1)

    elif choice in ("3", "three", "Three", "leave", "Leave"):
        separate_events()
        walkto() 

    else:
        print("Pick 1, 2, or 3.")
        upper_engine()


def medbay():
    print("You're in MedBay. What would you like to do?")
    choice = input("1. Call a meeting.\n2. Tasks.\n3. Leave.\n> ")
    print("You chose:", choice)

    if choice in ("1", "Call", "call", "one", "One"):
        separate_events()
        meeting(2)

    elif choice in ("2", "tasks", "Tasks", "two", "Two"):
        separate_events()
        task(1)

    elif choice in ("3", "three", "Three", "leave", "Leave"):
        separate_events()
        walkto() 

    else:
        print("Pick 1, 2, or 3.")
        medbay()


#asks user to add numbers
def task(i):
    a = random.randint(1, 100)
    b = random.randint(1, 100)
    c = a + b

    if i == 1:
        print("""You go to the task console in the room. The machine needs you to add some numbers to fix some computing errors.

What is {} + {}?""".format(a, b))
    else:
        print("""The machine needs you to add some numbers to fix some computing errors.

What is {} + {}?""".format(a, b))

    answer = int(input("> "))
    print("You entered:", answer)

    if answer == c:
        print("Task completed.")
        separate_events()
        walkto()
    else:
        print("Incorrect. Try again.")
        task(0)


#win message
def win():
    print("""You found the impostor! You are awesome!
    
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣴⣶⣿⣿⣷⣶⣄⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣾⣿⣿⡿⢿⣿⣿⣿⣿⣿⣿⣿⣷⣦⡀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢀⣾⣿⣿⡟⠁⣰⣿⣿⣿⡿⠿⠻⠿⣿⣿⣿⣿⣧⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣾⣿⣿⠏⠀⣴⣿⣿⣿⠉⠀⠀⠀⠀⠀⠈⢻⣿⣿⣇⠀⠀⠀
⠀⠀⠀⠀⢀⣠⣼⣿⣿⡏⠀⢠⣿⣿⣿⠇⠀⠀⠀⠀⠀⠀⠀⠈⣿⣿⣿⡀⠀⠀
⠀⠀⠀⣰⣿⣿⣿⣿⣿⡇⠀⢸⣿⣿⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⡇⠀⠀
⠀⠀⢰⣿⣿⡿⣿⣿⣿⡇⠀⠘⣿⣿⣿⣧⠀⠀⠀⠀⠀⠀⢀⣸⣿⣿⣿⠁⠀⠀
⠀⠀⣿⣿⣿⠁⣿⣿⣿⡇⠀⠀⠻⣿⣿⣿⣷⣶⣶⣶⣶⣶⣿⣿⣿⣿⠃⠀⠀⠀
⠀⢰⣿⣿⡇⠀⣿⣿⣿⠀⠀⠀⠀⠈⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠁⠀⠀⠀⠀
⠀⢸⣿⣿⡇⠀⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠉⠛⠛⠛⠉⢉⣿⣿⠀⠀⠀⠀⠀⠀
⠀⢸⣿⣿⣇⠀⣿⣿⣿⠀⠀⠀⠀⠀⢀⣤⣤⣤⡀⠀⠀⢸⣿⣿⣿⣷⣦⠀⠀⠀
⠀⠀⢻⣿⣿⣶⣿⣿⣿⠀⠀⠀⠀⠀⠈⠻⣿⣿⣿⣦⡀⠀⠉⠉⠻⣿⣿⡇⠀⠀
⠀⠀⠀⠛⠿⣿⣿⣿⣿⣷⣤⡀⠀⠀⠀⠀⠈⠹⣿⣿⣇⣀⠀⣠⣾⣿⣿⡇⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠹⣿⣿⣿⣿⣦⣤⣤⣤⣤⣾⣿⣿⣿⣿⣿⣿⣿⣿⡟⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠻⢿⣿⣿⣿⣿⣿⣿⠿⠋⠉⠛⠋⠉⠉⠁⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠉⠁⠀⠀⠀⠀⠀⠀""")
    exit()
    
start_screen()
start()
