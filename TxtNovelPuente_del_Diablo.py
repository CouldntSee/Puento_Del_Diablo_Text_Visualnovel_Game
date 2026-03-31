# Welcome to the Bridge of the Devil
#This is a Text based  novel, you will be the main charcater, and make choices
# This project is made for completion for my porgramming logic and design class.

# ____________________________________________________________________________________________________________________________
# |                                                                                                                           |
# | Note this it the main story, edit with caution, and make sure to test the code after every edit, to avoid bugs and errors.|
# |___________________________________________________________________________________________________________________________|

#  Lee Marc Macalanda  03/17/2026 , under 01-CPE-12 Unibersidad de Dagupan.
# Engr Sean Gabriel Macapaggal 

# The story
import time as t



def title_screen():
    print(r"""
╔══════════════════════════════════════════════════════════════════════════╗
║                                                                          ║
║    ██████╗ ██╗   ██╗███████╗███╗   ██╗████████╗███████╗                 ║
║    ██╔══██╗██║   ██║██╔════╝████╗  ██║╚══██╔══╝██╔════╝                 ║
║    ██████╔╝██║   ██║█████╗  ██╔██╗ ██║   ██║   █████╗                   ║
║    ██╔═══╝ ██║   ██║██╔══╝  ██║╚██╗██║   ██║   ██╔══╝                   ║
║    ██║     ╚██████╔╝███████╗██║ ╚████║   ██║   ███████╗                 ║
║    ╚═╝      ╚═════╝ ╚══════╝╚═╝  ╚═══╝   ╚═╝   ╚══════╝                 ║
║                                                                          ║
║           ██████╗ ███████╗██╗      ██████╗  █████╗ ██████╗              ║
║           ██╔══██╗██╔════╝██║     ██╔════╝ ██╔══██╗██╔══██╗             ║
║           ██║  ██║█████╗  ██║     ██║      ███████║██████╔╝             ║
║           ██║  ██║██╔══╝  ██║     ██║      ██╔══██║██╔══██╗             ║
║           ██████╔╝███████╗███████╗╚██████╗ ██║  ██║██║  ██║             ║
║           ╚═════╝ ╚══════╝╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝            ║
║                                                                          ║
║              ~ P U E N T E   D E L   D I A B L O ~                      ║
║                                                                          ║
║         A tale of faith, temptation, and an unfinished bridge            ║
║              Pilapila, Binangonan, Rizal — Philippines                   ║
║                                                                          ║
╚══════════════════════════════════════════════════════════════════════════╝
    """)
    
    

def GaLim():
    ascii_art = r"""
----::::::-+*******#################%%%%%%###**+++++==+++++==++==============--:::::---=============
:::::::::-+******#####**++++++++***###%%%%%%%##*+==============================--::::---============
::::::::-+******###**+========---=====+*#%%%%%##*+==============================--:::---------======
:::::--=+******#**+========-------------=+*%%#####+===========================---=--:::::-------====
=======+******#*+========-----------------=+#%%%%##+=========================----===-::::---::--====
=----=+*****#**+=======---------------------=+#%%%##+===-------------========-----====-::---::--====
=====+*******++========----------::-----------=*#####+-:::::-----------======-----=====-----::--====
=====*#####*+==========---------::::-------::::-*#####+::::::----------======-----=======--:::--====
====+*#####+=============---------::-------:::::-*####*=::::::----------=====-:::-------:::.....:---
===-=*####*+=----====----------------------:::::-+**###+-:::::-------========-:...:::::::::......:::
=====*####*+=-==========---------------===---:::-=**###*=-------------::::::::.:..::::::::::.....:::
===--=####*+=+**#####**++=========++******++=----=+####*:.....:::::::::::::::::::::::::::::::::..:::
===---*###++*********##***++===+++****++=++=++=--=+####+:....::::::::::::::::::::::::::::::::::::::-
---:::=###+++++++++++*******++++*****++===========+####+:.::::::::::::::::::::::::::::::::::::::::--
-:::::-*################%%%%############*##*#####**####=.:::::::::::::::::::::::::::::::::::::::::-=
-::::::+**#******+*###**+*#%%####++++++***+****#**+##*+:.:::::::::::::::::::::::::::::::::::::::::--
--:::::-*##++********+++++*##*##*====++++++++==+#*--**+:.:::::::::::::::::::::::::::::::::::::::::--
--::::::=#*=-=+++*****++++*#+==**======+=======+#=--+*+:.:::::::::::::::::::::::::::::::::::::::::--
--::::::-+*+=====+++++++++#*=---++===--========+*---+=-::::::::------:::::::::::::::::::::::::::::--
--:::::::-=*==========+++*#+=---=*+====----====*+---==-=====++++++++-::::=**#**+=---=*+=-::::::::::-
--::::::::=+*========++++#*+++===-=+====----==**=---==+*************--*%%%%%%%######%%%%#+-::::::::-
--::::::::-=+***++=+++*##++##***#*=+*********+=-----==++*+*****+****+#%%%%%%%%%%%%%%%%%%%#*-::::::=*
--::::::::-====+++**************+**+=+++++====------=-=********+****#%%##*****####%%%###%%%*-:::-*%%
-::::::..:-=====++=======+++=====------------------=++**+++=====++*#%%+=+++=======+#%%#*#%%%*++=+%%%
--=+---:::=+=====+================-----=======-----=+*++*===+**#*+*%%*=============*%%#**#%*=**=-+**
---=-----=**+===+++++++++****#******++=========---=**+==++++-===+**#%+=++==========+%%#*=+#+**#+=+**
---===+++**+==+++++++*####*++++++====++*+============++*+++===++=+*#*+***##*+*##**+=*#*=======*#+-=*
----=+**+++==++++++*************#**++============++++++*#++*++++***+*#**###%%####*#*++====:=+=*#+:::
==+*#+-==+===++++**************++=========+++===+%#%%#*+++=:-+++**-:=+=++*#++*++++*-=+=+=:..:-*#*-::
+++##++======+++++*****++++===++===-=====++++++==###%###**+=+++=+#-:-=+***+==+***+======:..::.:..---
==*##+========+++******+++++++++++=====+++***++==##**#####+=*#+-=#-::==+++****+++=====++:.:::::.....
*+####**=====+++++*#+************************+==*##*=-=+***++*+++*:.:-=+++*++++++===++==::.:::::::..
#==**##=-+===+++*#%%*+**##%%%##########*****+==*####=:-####+*+*#**::.:-+++***+++++=:--===-:.:::::::.
%#+==-:::++++++*#%@@%*****####%%%#####******+++#####=-:+%%##**#%%%*-::-=++++++++++=::---=--.:::::...
*:..::-=::-*++*#%@@@%%#**############******+++#####+-:-+%%%#########*=-*+++****++=+:.::-=--:::::::..
:::.:::++-=+#%@%%@@@@%%#################**++*#%###*--:=*%%%%###%%%%####***++*+++++-......:-:::::::::
....:=+*##%%%@@%%%@@@@%%%%#############**+*#%%####=-:-=#%%%%###%%%###########*++-::..:..::...::--:::
=+#%%%%%%%%%%@@%%%%@@@%%%%%%%#########*++*%%%%%%%+---=*%%%%%%##%%%%%############*=:..::.:::.....::::
%%%%%%%%%%%%@@@%%%%@@@@%%%%%%%######**++*%%%%%#%*--:-=%%%%%%%#%%%%%%%#############*+:::::::.:::::..:
%%%%%%%%%%%@@@@@%@@@@@@@@%%%%%%%###*++*#%%%%%%%#--::-+%%%%%%%#%%%%%%%%########%#####*=::::::::::::.:
%%%%%%%%%%%@@@@@@@@@@@@@@@@@%%%##*+*#%%%@%%%#%#=----=#%%%%%%%%%%%%%%%%%%%####%%#######*-::::::::::::
%%%%%%%%%%%%@@@@%#%@@@@@@@@@%%#**#@@@@*#@@%#%%*--:--*%%%%%%%%%%%%%%%%%%%%%%%%%%########*+:::::::::::
%%%%%%%%%%@%%%@@%#+#%*@@@@@@@%#%@@@@@@@@@@@%%*---:-=%%%%%%%%%%%%%%%%%%%%%%%%%%%%#%%######*=:::::::::
%%%%%%%%%%%%%%@@@%+=++#@@@@@@@@@@@@@@@@@@@@@#==-:--#%%%%%%%%%%%%%%%%%%%%%%%%%%%%#%%%##%%###+::::::::
%%%%%%%%%%%%%%%%%%*=--=%@@@@@@@@@@@@@%%@%%@%+=-:--*%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%##%%####-:::::::
%%%%%%%%%%%%%%%%%%#=---*%%@@@%##@%%%%%%%%%%*=-::=+#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%###+:::::::
%%%%%%%%%%%%%%%%%%%=---=%%%@@%*#%%%%%%%%%%#+=-:--#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%###*-::::::
%%%%%%%%%%%%%%%%%%%#----*%%%%@@%%%%%%%%%%%+=-:-=#%%%%%%%%%%%%%%%%%%%%%%%%%%%%@%%%%%%%%%%%%%%#+::::::
%%%%%%%%%%%%%%%%%%%%*---=%%%%%%%%%%%%%%%%*=---=+%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%#=:::::
%%%%%%%%%%%%%%%%%%%%%+---*%%%%%%%%%%%%%%%+=:--=#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%@%%%%%%%%%%%%%#-::::
%%%%%%%%%%%%%%%%%%%%%#=--=%%%%%%%%%%%%%%+=-:-=#%%%%%%%%%%%%%%%%%%%%%%%%%%%@%%@%@%%%%%%%%%%%%%%%*----
%%%%%%%%%%%%%%%%%%%%%%#===#%%%%%%%%%%%%#+=---*%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%@@@%%%%%%%%%%%%%%%%=--:
%%%%%%%%%%%%%%%%%%%%%%%*==*%%%%%%%%%%%%+=--=*%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%@@@%%%%%%%%%%%%%%%%%#-::
%%%%%%%%%%%%%%%%%%%%%%%%*+*#%%%%%%%%%%#+---=%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%@@@@%%%%%%%%%%%%%%%%%%+::
%%%%%%%%%%%%%%%%%%%%%%%%%%*#%@@@%%%%%%*=--=%@%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%@@@%%%%%%%%%%%%%%%%%%%#-:
%%%%%%%%%%%%%%%%%%%%%%%%@@%*#%%%%%%@%%+--=#@@%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%@@@%%%%%%%%%%%%%%%%%%%%*-
%%%%%%%%%%%%%%%%%%%%%%%%%%@@%#%@@@%@%#=-=#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%@@@@%%%%%%%%%%%%%%%%%%%%%=
%%%%%%%%%%%%%%%%%@%%%%%%%%@@@%%%@@@@%*==*%@@@%%%%%%%%%%%%%%%%%%%%%%%%%%%%@@@@@@%@@%%%%%%%%%%%%%%%@%*
%%%%%%%%%%%%%%%%%%%%%%%%%%@@@*#%%@@@%==*%@@@@@%%%%%%%%%%%%%%%%%%%%%%%%%%@@@@@@@@@@%@%%%%%%%%%%%@%@%%
%%%%%%%%%%%%%%%%%%%@@%%%%%@@@##%%%@@#+*%@%@@%%#%%%%%%%%%%%%%%%%%%%%%%%%%@@@@@@@@@@@@%%%%%%%%%%%%@@%%
%%%%%%%%%%%%%%%%@%%%%%%%%%@@@@@%%%%@*+%@@@@@@%@%%%%%%%%%%%%%%%%%%%%%%%%@@@@@@@@@@@@%%%%%%%%%%%@@@@@%
%%%%%%%%%%%%%%%%%%%%%%%%%@@@@@@%%%%%*%@@@@@@@@%%%%%%%%%%%%%%%%%%%%%%%%%@@@@@@@@@@@@%%%%%%%%%%%%@@@@@
%%%%%%%%%%%%%%%%%%%%%%%%%@@@@@@%%%%#%@@@@@@@@%%%%%%%%%%%%%%%%%%%%%%%%%%@@@@@@@@@@@@%%%%%%%%%%%@@@@@@
%%%%%%%%%%%%%%%%%%%%%%%%%@@@@@@@%%%#%@@@@@@@@%%%%%%%%%%%%%%%%%%%%%%%%%%@@@@@@@@@@@@%%%%%%%%%%%@@@@@@
%%%%%%%%%%%%%%%%%%%%%%%%%@@@@@@@%%%%%@@@@@@@@%%%%%%%%%%%%%%%%%%%%%%%%%@@@@@@@@@@@@@%@@@%%%%%%%@@@@@@
    """
    print(ascii_art)
   
# ______________________________________  
#            GAmit lang
# ________________________________________
def pause(seconds=1.5):
    t.sleep(seconds)
    
def slow_print(text, delay=0.03):
    for ch in text:
        print(ch, end='', flush=True)
        t.sleep(delay)
    print()  
    
def narrate(text):
    print()
    slow_print(f"  ✦ {text}", delay=0.025)
    print()

def bad_end(reason):
    pause(1)
    print()
    print("┌─────────────────────────────────────────────────────────────┐")
    print("│                        ~ BAD END ~                          │")
    slow_print(f"│  {reason}")
    print("└─────────────────────────────────────────────────────────────┘")
    pause(1)
    End_main()
    

    
 
def hasty_decision2(prompt, option1, option2, S1, S2, S3, S4, S5, F1, F2, F3, F4, F5, exit_action, go_action, timeout=5):
    print("╔════════════════════════════════════════════════════════════╗")
    print(f"║ {prompt}")
    print("╚════════════════════════════════════════════════════════════╝")
    print(f"1. {option1}")
    print(f"2. {option2}")
    print("\nType your choice now! Countdown:")

    start = t.time()
    choice = input("Enter choice number: ")

    success_story = [
        f"{S1}...",
        f"{S2}...",
        f"{S3}...",
        f"{S4}...",
        f"{S5}..."
    ]

    fail_story = [
        f"{F1}...",
        f"{F2}...",
        f"{F3}...",
        f"{F4}...",
        f"{F5}..."
    ]

    for i in range(timeout, 0, -1):
        if choice == "2":
            print(f"{i} - {success_story[timeout - i]}")
        elif choice == "1":
            print(f"{i} - {fail_story[timeout - i]}")
        else:
            print(f"{i} - Confusion grips you...")
        t.sleep(1)

    if choice == "1":
        exit_action()
        return option1
    elif choice == "2":
        go_action()
        return option2
    else:
        if t.time() - start > timeout:
            print("")
            return "DEFAULT"
        print("Invalid choice! You have died!")
        return "DEFAULT"
    
def hasty_decision1(prompt, option1, option2, S1, S2, S3, S4, S5, F1, F2, F3, F4, F5, exit_action, go_action, timeout=5):
    print("╔════════════════════════════════════════════════════════════╗")
    print(f"║ {prompt}")
    print("╚════════════════════════════════════════════════════════════╝")
    print(f"1. {option1}")
    print(f"2. {option2}")
    print("\nType your choice now! Countdown:")

    start = t.time()
    choice = input("Enter choice number: ")

    success_story = [
        f"{S1}...",
        f"{S2}...",
        f"{S3}...",
        f"{S4}...",
        f"{S5}..."
    ]

    fail_story = [
        f"{F1}...",
        f"{F2}...",
        f"{F3}...",
        f"{F4}...",
        f"{F5}..."
    ]

    for i in range(timeout, 0, -1):
        if choice == "1":
            print(f"{i} - {success_story[timeout - i]}")
        elif choice == "2":
            print(f"{i} - {fail_story[timeout - i]}")
        else:
            print(f"{i} - Confusion grips you...")
        t.sleep(1)

    if choice == "2":
        exit_action()
        return option1
    elif choice == "1":
        go_action()
        return option2
    else:
        if t.time() - start > timeout:
            print("")
            return "DEFAULT"
        print("Invalid choice! You have died!")
        return "DEFAULT"

    

def background_forest():
    print("🌲🌲🌲🌲🌲🌲🌲🌲🌲🌲🌲🌲🌲🌲🌲🌲",
          "🌲        DARK FOREST         🌲",
          "🌲🌲🌲🌲🌲🌲🌲🌲🌲🌲🌲🌲🌲🌲🌲🌲", sep="\n")

# Character template
def character_player():
    print("   (o_o)   ",   
          "    /|\\    ",   
          "    / \\    ", sep="\n")

def character_shadow():
    print( "   (###)   ",  
          "   /|||\\   ",  
          "   /|||\\   ", sep="\n")
def sign():
    print("╔════════════════════════════════╗")
    print("║      Puente del Diablo         ║")
    print("╚════════════════════════════════╝")

def progress_saved():
    print()
    print("  ╔════════════════════════════════╗")
    print("  ║   ✦  Progress Saved  ✦         ║")
    print("  ╚════════════════════════════════╝")

def chapter_banner(number, title):
    print()
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print(f"  CHAPTER {number}  —  {title}")
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print()
    pause(1)
    
def action_scene(text):
    print("╔══════════════════════════════════════════════════════════════════════════════╗")
    print(f"║ ⚔️ {text}")
    print("╚══════════════════════════════════════════════════════════════════════════════╝")

def dialogue(text):
    print("┌───────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐")
    slow_print(f"│ {text}")
    print("└───────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘")

def End_sc4(): # for final saved point (working)
    delay = 2

def End_sc3(): # for sc4 saved point (Working)
    delay = 2
    
def End_sc2(): # for sc3 saved point (working)
    delay = 2

def End_sc1(): # for sc2 saved point (working)
    delay = 2
    

def End_main(): #done
    delay = 2
    print("||_______________________________||")
    print("||                               ||")
    print("||         THE END               ||")
    print("||                               ||")
    print("||_______________________________||")
    t.sleep(delay)
    dialogue("you facied to unconver the mystery of the bridge.")
    t.sleep(delay)
    user = input(" try again?")
    if user.lower() == "yes":
        t.sleep(delay)
        dialogue("you woke up again.. feeling a bit disoriented, \nbut determined to uncover the secrets of the bridge once more.")
        main()
    elif user.lower() == "no":
        t.sleep(delay)
        dialogue("You perished alongside the bridge...")
        dialogue("The mystery of the bridge remains unsolved...")


def endegg():
    input("You found the easter egg! Press Enter to continue...")
    
def ecitegg():
    input("You found the easter egg! Press Enter to continue...")

def menuegg():
    input("You found the easter egg! Press Enter to continue...")



# // ______________________________________//
# ||              Story poper              ||
# // ______________________________________//

def Start():
    title_screen()
    narrate("You find yourself standing at the edge of a mysterious bridge, shrouded in darkness and mystery.")
    narrate("Do you dare to step onto the bridge and uncover its secrets, or do you choose to turn back and avoid the unknown?")
    user = input("Type 'continue' to step onto the bridge or 'no' to turn back: ")
    if user == "continue":
        narrate("You take a deep breath and step onto the bridge, feeling a sense of anticipation and curiosity.")
        main()
    elif user == "no":
        narrate("You decide to turn back, but the voice calls you again...")
        t.sleep(2)
        Path_Exit()
    
def Path_Exit():
    delay = 2
    while True:
        t.sleep(delay)
        narrate("as you leave the bridge, you see a hanging sign on the side of the road.")
        sign()
        t.sleep(delay)
        narrate("as you read the hanging sign, you see the words 'Puente del Diablo' written on it.")
        t.sleep(delay)
        print("1. go back?")
        print("2. Leave")
        t.sleep(delay)
        choice = input("Enter your choice: ")
        if choice == "1":
            main()
        elif choice == "2":
            exit()
            break
        elif choice == "3":
            menuegg()
        else:
            print("Invalid choice, please try again.")
        
def exit_():
    delay = 2
    while True:
        t.sleep(delay)
        user = input("Are you sure you want to leave? (yes/no): ")
        if user.lower() == "yes":
            t.sleep(delay)
            print("The voice fades away as you step back from the bridge. \nYou decide to leave, but the mystery of the bridge lingers in your mind...")
            break
        elif user.lower() == "no":
            Path_Exit()
        elif user.lower() == "tang ina mo sir":
            ecitegg()
        else:
            print("Invalid choice, please try again.")
            exit()
        
def main():
    chapter_banner("Prologue", "The Mysterious Bridge")
    delay = 2
    t.sleep(delay)
    narrate("Somewhere in the Town of Rizal province of Laguna.")
    while True:
        t.sleep(delay)
        narrate("You stand at the edge of the bridge. A mysterious voice whispers...")
        t.sleep(delay)
        cmd = input("Type 'continue' to proceed or 'no' to go back: ")
        if cmd.lower() == "continue":
            narrate("You step onto the bridge, and the voice grows louder, echoing in your mind...")
            t.sleep(delay)
            narrate("Your journey continues.")
            sc1()
        elif cmd.lower() == "no":
            narrate("You decide to go back, but the voice calls you again...")
            t.sleep(delay)
            Path_Exit()
            break
        else:
            print("Invalid input, please try again.")

def sc1():
    chapter_banner(1, "The Whispering Bridge")
    pause()
    progress_saved()
    delay = 2
    t.sleep(delay)
    narrate("As you walk further on the bridge, you notice the surroundings becoming more eerie.")
    t.sleep(delay)
    narrate("The voice in your mind grows stronger, urging you to continue.")
    t.sleep(delay)
    print("1. Keep walking")
    print("2. Turn back")
    print("3. Open your Phone")
    choice = input("Enter your choice: ")
    if choice == "1":
        narrate("You decide to keep walking, determined to uncover the secrets of the bridge.")
        t.sleep(delay)
        narrate("As you continue, you feel a strange sensation, as if you're being watched...")
        t.sleep(delay)
        narrate("Suddenly, you saw an amminous rock formation that resembles a face,\n and the voice becomes clearer, whispering your name...")
        t.sleep(delay)
        dialogue("You: " + "who are you? show yourself.")
        narrate("The sorrounding suddenly become more earriee silence as if wondeing what your next move is.")
        narrate("Then you glance towards the amminous rock. . .")
        dialogue("You: " + "don't tell m-")
        narrate("You collased on your own on the ground")
        t.sleep(delay)
        narrate("To be contiue. . .")
        sc2()
    elif choice == "2":
        narrate("You decide to turn back, but the voice becomes more insistent, urging you to stay...")
        t.sleep(delay)
        narrate("As you turn around, you see a shadowy figure standing at the end of the bridge, watching you...")
        t.sleep(delay)
        character_shadow()
        t.sleep(delay)
        narrate("The figure disappears as you look away, but the voice continues to haunt your thoughts...")
        t.sleep(delay)
        narrate(" You Bceome insane and you start to see things that aren't there, hearing voices that no one else can hear...")
        t.sleep(delay)
        narrate("You lose touch with reality, and the world around you becomes a blur of confusion \n You died of insanity")
        End_main()
    elif choice == "3":
        narrate("You decide to open your phone, hoping to find some answers or a way to call for help.")
        t.sleep(delay)
        narrate("As you unlock your phone, you see a message notification from an unknown number...")
        t.sleep(delay)
        narrate("The message reads: 'i know who you are. . .'")
        t.sleep(delay)
        narrate("You feel a chill run down your spine as you read the message, realizing that you're not alone on the bridge...")
        t.sleep(delay)
        narrate("Then out of nowhere, you receive another message, this time with a photo attachment...")
        t.sleep(delay)
        GaLim()
        narrate("The photo shows a two figure standing on the bridge, one of them is you, \n and the other is a shadowy figure that resembles the one you saw earlier...")
        hasty_decision2("What do you do?", "Look back and confront", "Ignore and keep Walking", "You keep walking", "Praying", "taking deep breaths", "you found yourself unbalanced","you look around, you saw an amminous rock formation","You glance around","you see nothing","you sign of relief . . . " ,"you felt diizy, the voice gwrowing louder and eriee", "you fell unconscious ",End_main,sc2,timeout=5)
def sc2():
    chapter_banner(2, "The Unfinished Mystery")
    pause()
    progress_saved()
    delay = 2
    t.sleep(delay)
    narrate("You woke up, and you find yourself in a different place. . .")
    narrate("You felt soft at your back. . .")
    dialogue("wait what just happend? Where Am I?")
    t.sleep(delay)
    dialogue("You: " + "Wait a minute, I remember falling unconscious on the bridge. . .")
    narrate("You get up from the cozy feeling bed, and you see that you're in a small room with stone walls, dimly lit by a flickering candle on a wooden table.")
    narrate("You glance around your sorrunding ")
    narrate("Still confuse how dirt road became a comfy bed inside a room, you start to look around the room,\nhoping to find some clues about where you are and how you got there.")
    narrate("Then you notice a mirror on the wall, and as you look into it, you see a reflection of yourself, but something is off...")
    narrate("Feeling bit disoriented, you strech to releive the tension of your body. . .")
    narrate("You get up from the bed, and yawn, as you stabilized your step you wonder when did you even were such a elegant white dress.")
    dialogue("You: " + "Wait, when did I even get this dress? I don't remember putting it on...")
    dialogue("You: " + "And why do I feel so... different? Like I'm not myself anymore...")
    narrate("You start pannicking, trying to piece together what just happned. . .")
    dialogue("You: " + "Right theres a mirror, maybe I can find some answers there...")
    narrate("you approach the mirror rushingly, hoping to check on yourself but. . .")
    dialogue("You: " + "wait. . . who' s this?")
    Lara()
    narrate("you see a reflection of a young girl, elegant, her skin is pale as sampaguita, her eyes is brown as the sunflower,\n her hair hold majestic dark as the night that shine like stars,\n her dress even plain, with her holds the beauty of the milky skies.")
    narrate("Star Struck by this beautiful, you wonder who is this girl.")
    dialogue("?: " + "Lara!, wake up you doze again. it's already Lunch time.")
    dialogue("You: " + "Lara? that's no-")
    narrate("suddenly the door from your room opens")
    dialogue("?: " + "Hey Lara, you're finally awake! I was getting worried about you, hurry before our lucnh get cold.")
    dialogue("You: " + "Sorry auntie, coming")
    narrate("in your mind:" + dialogue("You: " + "Wait, did I just said auntie? but i dont know her. . ."))
    narrate("You follow your 'Aunite', and you find yourself in a cozy kitchen")
    narrate("As you enter the kitchen, you are greeted by the warm aroma of freshly cooked food, and the sight of a loving family gathered around the table, sharing a meal together.")
    dialogue("Auntie: " + "Lara, you want me to do this everyday for you aren't you? Gezz you should be grateful that you have a family that loves you, unlike your parents who left you alone in the world.")
    dialogue("You: " + "But i don't even know you, and i dont even know who my parents are. . .")
    dialogue("Middle-age man: " + "Hahaha you never disspoint us to enterain us Lara, you always have a good sense of humor, just like your father.")
    dialogue("Teenager girl: " + "Geez, you seem you worship so much our heavenly father that you fogot about us, but then, how can i blame ya? \neveryday you have suitor soo envious.")
    dialogue("Auntie: " + "Stop teasing her, Lara, come one have a seat and lets eat.")
    narrate("You sit down at the table, and stared at the delicious food that your family had prepared.")
    narrate("In your mind:" + dialogue("You: " + "That middle-age man must the Uncle, and that teenager girl must be their child."))
    dialogue("Uncle: " + "Why dozing off, come on lead the prayer Lara")
    dialogue("Your: " + "Oh yea. .")
    narrate("You lead the prayer.")
    narrate("You are suprise casue you are indeed fluent at praying, eventhough you dislike GOD.\n or perhaps Lara is the one who is fluent.")
    narrate("You  enjoy the simple yet heart felt feast before the table.")
    dialogue("Uncle: " + "Lara, have you chosen your suitor?")
    dialogue("You: " + "Me chosing suito?")
    dialogue("Enenager girl: "+"AS expected to you Lara you still have not picked.")
    dialogue("You: " + "Umm")
    dialogue("Enabell: " + "Don't call me 'umm' my name is Enabell. if you're not my cousin I-")
    dialogue("Auntie: " + "Stop, Lara devoted her life to heavenly father. Lara can you go to our locat church?")
    dialogue("You:","Why?")
    dialogue("Auntie:", " Just say hi to our priest John. Enabell go with Lara")
    dialogue("Enabell:", "But i have plan thi afternoon.")
    dialogue("Auntie: ", 'No buts Enabell.')
    narrate('Enabell relucntently agrred to go with you')
    narrate('You and Enebell set out of your house')
    narrate('You openned the door and a village thriving welcomes you')
    village()
    
    t.sleep(delay)
    sc3()


def sc3():
    chapter_banner(3, "The Devil's Bargain")
    pause()
    progress_saved()
    
    
def sc4():
    chapter_banner(4, "The Final Revelation")
    pause()
    progress_saved()
    
    
def final():
    chapter_banner("Final", "The Bridge's Secret")
    pause()

    progress_saved()
    delay = 2
    
    

if __name__ == "__main__":
    Start()
    
# /// Secret ///
def show_easter_egg():
    ascii_art = r"""
...................................................................................................
.                                                                  ........                         
.                      ....................:::::::::::--------==========++-                         
.                      .=+++++++++++++++++++++++++++++++++++++++++++++++++-                         
.                      .++++++++++++++++++++++++++++++++++++++++++++++++++-.                        
.                      .++++++++++++++++++++++++++**++++++++=+++++++++++++=.                        
.                      .++++++++++++++++++++++++#%@@%*+++++++++++++++++++++.                        
.                      :*++++++==+++++++++++++++%@@@@%+++++++++++++++++++++.                        
.                      -*+++++++===+++++++++++++%@@@@%%+++++++++++++++==+++-                        
.                     .=*+++++++++++++++++++++++%@@@@@%#+++++==+++++++++=++=.                       
.                     .+*+++++++******++++++++++%@@@@@@%*+++=--=++++++++++++.                       
.                     .+**+++++*********+++++++#%@@@@@@@%*+=-==+++++++++++++:                       
.                     :+**+++++*-=---+++*++++++%@@@@@@@%#+====++++++++++++++-                       
.                     :+**+++++***++++*#*+++++*%@@@@@%%#%%%*+++=++++++++++++=.                      
.                    .=+*+++++++*#**###*++++++%@@@@%*--==-------=++++++++++++.                      
.                    .=+++++++++++*##**++++++#%@@@@=@@%-%%#*+++++++++++++++++:                      
.                    .+++==+++++++++++++++++*%@@@@#+@@%++%@@@@%*+++++++++++++-.                     
.                    :++++++++++++++++++++++%@@@@@-=@@@#:-+%@@@%#*+++++++++++=.                     
.                    :+++++++++++++++++++++%@@@@%--:%@@#:-=--=*%@%*+++++++++++.                     
.                    -++++++++++++++++++++%@@@%+::--=%%+:-===--=#%@%*+++++++++:                     
.                   .=++++++++++++++++++*%%@#+-::-==-+%-===-----=#%@@%*+++++++-.                    
.                   .=+++++++++++++++++*#%%#=::::-===-=+=-=====+*%@@@@@%*+++++=.                    
.                   .=++++++++++++++++*#%%%#-::-+=+==-:=+++++*#%@@@@@@@@@#*+++=.                    
.                   .=+++++++++++++++#%%%%%%#=-==+*++--=##%%@@@@@@@@@@@@@@@#++=.                    
.                   .=++++++++++++++#@%%%%%%@@%*====--=*@@@@@@@@@@@@@@@@@@@@@*=.                    
.                   .=++++++++++++*%%%%%%##*%@@@@@@@@@@@@@@@@@@@@@@@@@%%%%%@@%=.                    
.                   .=++++++++=++*%@*==++=+*#%@@@@@@@@@@%%*+#@%*:::+%*::::+@@#*.                    
.                   .=++++++++++*%@@%%##%*--*-::%*::::-#::-*+*=:+%=:--::-+%@@#*..                   
.                   .=++++++++++#@@@%+:--::*%+::%:::=*%#:::-=+-::-:-+#*=-::%@#*.                    
.                   .=+++++++++*@@@@@+:::-#%@*::%#+-:::+##*=:=+:-==-*+---:+@@#*..                   
.                   .=+++*+++++#%@@@@+::-::=%#-:#+===:-*-:::=#%#***#%@%#*##@@##.                    
.                   .=+++##+++*#%@@@@*::*#=-=#*+*%#**#@@@@@@@@@@@@@@@@@@@@@@@##.                    
.                   .=+++#*+++##%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%%%%%@@@@@@@##..                   
.                   .=+=++*+++%#@@@@@@@@@@@@@#%%%%%%#######****##*+*#%@@@@@@@##..                   
.                   .=+*+#*++*%#%@@@@@@@@@@@%+*##**++=#**++*****++*##%@@@@@@@%#.                    
.                   .-+*+**++*##%@@@@@@@@@@#++*#############%%%%%@@@@@@@@@@@@%*.                    
.                   .-+++**+++*#%@@@@@@@@@%#*#%%#@@@@@@@@@@@@@@@@@@@@@@@@@@@@#+.                    
.                   .-+++#*+++-*%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%+=.                    
.                   .=+++**+++==#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%++*+.                    
.                   .=+++**+++=--*%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%#*#%**.                    
.                   .=+++#*++++==+*#%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%%%%####**+++:                    
.                   .=+++**++++==*****###%%%@@@@@@@@@@@@@@%%%%##*==+*##**==++*+:                    
.                   .=++*#+++++=+**==##****++***#%%%%#+=----=+**+==+*+==-==*#*=:                    
.                   :=++**+++++*##*=*+=+=-=+*++++**##*==--===++**+*###*++***++=-.                   
.                   :=++*#++++++***+*+=--=+*#%#==++#**+==++++++*###**###*+++++=-.                   
.                   :=++**+++++++**======+++*%#=+++####*++===+********++++++++=-.                   
.                   :=++*#+++++++++++++===+++##+=-+*#*+++*####**++++++++++++++=-                    
.                   .=++#*+++++++++++++++++++***++*****++++++++++++++++++****++.                    
.                    :=+++++++++++++*****####***+*++*++++++++++++++*********++-.                    
.                    ..-++++++++++++**+++=--=+==+:=-*+++++++++++***********=-..                     
.                      ..-+++++=+++++**=-=====+++---*++*******++==-::.......                        
.                        ..-+++++++++====****##**+++==--::.......                                   
.                          ..:=++***++++==--:::.....                                                
.                            ............     
    """
    print(ascii_art)
    
def village():
    print(r"""
----------------------------------------------------------------------------------------------------------------------------------
--------------------------------------------------------------------------======--------------------------------------------------
----------------------------------------------------------------------------------------------------------------------------------
------------------------------=========-------------------------------==---------------========+----------------------------------
----------------------------+=----------=+-----------------------------------------+----------------------------------------------
--------------------====++=+-------------==--------------------------===-------------------==+==----------------------------------
-------------------------------------------------==--------+++=+++++==+++**+++=-------=+++++===========---------------------------
--------------------------=+++=------------------=+====-----------------------=++++=----------------------------------------------
-------------------------++==++====----===-----=====++----------------------------------------------------------------------------
------------------------------------------------------------------------------------------------------=====-----------------------
---------------=---------------------------------------------------------------------------------=+=------------------------------
---------------+==--------------------------------------------------------------------------=====------------=---======-----------
---------------=-------------------------------====-------------------------------------------=====-----------=--==--==-----------
---------------=----------------------------==-----=+=----------------------------------------------======------------------------
---------------==---------------------==----------+---=++=------------------------------------------------------------------------
--------------=++=-------------=+==-----------------=------==---------------------------------------------------------------------
--------------=--+----------=+-----------------------==------=+++=------------------------=+=-----+=------------------------------
-------------==--==----------------=----=+==-----------==----------+=-------------------+----==------+=---------------------------
------------==----==-------------------------------------=-----------=+++------------==-------------------=+----------------------
-----------=====-=+=+------+=---------==-----+-----------+=++-------------=-+++=-----------------=-----------=++=-----------------
----------=+===-===-=+----=++-----------==-----==+-----------======--==--------==------------------=---------------=++====--------
-----------=+=======+=---+++**=-----------==-----==------------------===-----------===----------------=-----------=++++=----------
-----------=+=+===+==---++==*===-------------=-----==-==--------------====------------==--------------=-----------==*++=----------
----+--=+=-=+======++++--=+=*+==---------------=------==-----------------====-+++=-----------------------=-------+++++++=---------
----+=+++*++=------+*+**+++=++=+=+---+=-+*=-==--------=-----------------------*+++++++*+============--------=+=--==+**+===+=------
----+++==*+==---=---+++*=+***+==+++*++++=++**++===-===++--=------------------=*++=------------------==-----=+++=+*+*++*++*+=------
----=========---=---==---===========++=--==---=--+++=-===*+==----=+=--------++*+=--------------------==----++=++=---==---==++-----
----+++-=+===---=--===--=--=--=--=-=+++====+++*++----**+=+-+*+++=+++++===++=*+--=+-+==+=+==+=+==+=+=+=-+==+=++*+++==++==+****=----
----+=+==*++=----==---------------==--+++=-=+=++++===*+==+=++=+++=--++*++++*+-++==+---------------------+*+++**++*****==-++=------
----+====+++=---===+-++-++-++-==-=--+=-=++=---++=+-+++=-------=+======++=++-+=+=++-==-=-=--=-=----=-==-=-+=+-=*=++=+++++=++++=----
----++++=+++=--==---------------=--=+=---++++--=+**+--==--------=====+*+++--+=++=+--=---------------------=+++*++*+++++++++++=----
----+++=-=+---====-==-==-==-==-+----------++==---++-++==++++++++++==++***=-----------=+++++++=======++++++++-=+-=+=+++++==+=------
----+++++++--++================----====---++==+=+==-----+*+++++++++++++=*=---=*++=---=++-===------------=+-==+*++*==+===+*+++-----
----=+++======++===============---=*+++=--==----=-------==--=-=++====-==*----+*+++---=+=--++=-==+--++=--=*=+==+=++++++=====+------
----++*+==+++=++=+--+--++-----=---+**+*=--=*+=--=-===========----==+++==*---++*+++---=+=-=++=-==+--+++---+-++++==+=+++++==+++-----
----+=++=+*++=+=--------------=---+**++=--====++=====-------==+=========+=--+=++=+--==+=-----------------+-++=+=++=+++===++++-----
----==+++++==-------==========+=-===------------------==------------==------------------====-------------------====+*+=-----------
-----=+-=+++====-===+==--------------===----------+-------------==------------+==+----------==+==--=+=------------=**+--=+=-------
----==+====------++=--------------------=-----=+-------------==------------=======-===++---==------======---------=++=------------
----++*+=+=++=--=++==-=+=++==----===-------==---===--------=--------+======------===----===--------===-----======++---------------
----*=+=--=+++++=++=+=+*=++=+-------===---=-----------=+=--=--------==-----------------++----===+++**+**===------+=---=====-------
----+++*++-=+=++=++=++=---------==--------==-------==-=-----===------------===+-------+*+----------=+=-------=++=+=---------------
----+=+===+**+++=++=+++-----------=----------===-----------------===----==-----====--=+*+----------=+=--------**=+=----=+===------
----+=++==-------+++=--------===----------------===-----------------===-------------+++**++++++==+=+++====----*+=+=--===----=-----
----++++--------------+--------------------==-----+--------------------===-------------+=----------++========+++=+=---------------
-----------===========----===-------------------===----------==------=------====-------------------==-------+++====--===----------
--------------------------+=+---------------===----------------------------------===---------==---=====-------=-------------------
-----===------------+++==++=+++=-----===-----------------------------------------------===------------====------==----------------
-------------------=*++*=+*=++++--===------------------===-----==---------------------------===----------------=++=---------------
------------------------------------------=====--------------------------------------------------=++=-----------------------------
----------------------++=-----------------------=------------=+=====++=---------------==-===------------====----------------------
--------------------------======------------------+=---------------------------------------------------------===------------------
---------------------------------=====----------------=----------------------------==-==----------------------------==------------
-------------------------------------------------------=--------------------------------------------------------------------------
    """)
    
def Lara(): # for sc2
    print(r"""
.*+========+=..=:                                                             
  =                                             +-               -=      +=                                                       
  +                                           *:                .=-==      -*+.                                                   
  +                                         *-            *.%%#         %:     :@                                                 
  =                                       --                    =.        +      -=                                               
  =                                     .     *=      #%#:#.                :                                                     
  +                                    --   -*     .*:#:@-%:-   .+-         .*     -*                                             
  +                                   :-          ..  @=@*@*%-  -==           :      -                                            
  +                                  :=    -      .   @.#:*:=:     -           %     ==                                           
  +                                      +.     .:  %              -=:          *:                                                
  +                               =*=   +:      @  --              .-+.   .      ++     *.                                        
  +                               *+-  :-     =.= #                  :-   *        #    .=                                        
  +                                ::        *.:                          #=                                                      
  =                             :+ :. =-    - =+                       .+ -   :     :%    =:                                      
  =                             *  -:-=      =-                         =  *. *      --    =:                                     
  +                             *  -#=       =-                       +@@:  *.#       =.   .:                                     
  +                            :   +.        .                  .*##+.   -. =  %       -:   :                                     
  +                                     =   +++*@+@*@*          -. .+*@=%.#-#  #        .   +:                                    
  +                          -#        -.   #:=.= +.#             *@@@@@@%@*#   #           ::                                    
  +                         *-+       :-   %@#@@@@@@@=@         :@%++*@#@=+  -  *=+          *-                                   
  +                        :  -      =-    =@%@-@#**%:@-        -#:   :+=     + = ++        .   .                                 
  +                       -+  +     .     #:   ..   . ..                      %   * #       -.  :+                                
  +                       *  *-    =:    -@#                                  @   *  +      -.   .-                               
  +                      %   %    +     ##@@:                                 @ %-  :#*     ::    -=                              
  +                     @       :     .--=*+#                                 @    =#  =:   .@=    .-                             
  =                    :   +-  *     +%##+#*@:            =   *+                   +@-#=:   .%=     .+                            
  =                   -+  :% # *    =*##@*@#@@                                %   @:@-%++   .=:    : #                            
  =                   :=  @ # :*  -   *#@*@#@%*                               @-@-@:@-%++   .=@@   =:#                            
  =                   :=   %    -*--  -=. -:-:*.         .*+%%+-++=         #+# + + - ::=   .- *   =.                             
  =                       %    .*.*  :=-+:%#@*@%*       -+-    .#=         .%.@ @:@-@=*     .- =   =.                             
  =                   -:  @   .:  *  -* :#@#@*@*@#-       ++#+*+.        .* @.@ @:@-@=*     -. =   =.                             
  =                   .  .@   %   +  .-  .%=+-#-*.%:                    :   @ % % #.#*         =   -                              
  =                    #%    :     :-      -#*%+%-@:@%               :*     %:@.@:@      -=. +=+                                  
  +                    #@   .*   * :-  -= ==##%=*.@@@-@-@-          =.      +*@.@.@*    :- :-=-+::                                
  +                     *@   *   * :-        +*:  @#@-@#  .= ====:-.         +@.@ @=   =@*++:.-+*%#:                              
  +                      %.  *                  +:      =                    .%   .   .   -.   : .*@:                             
  =                       -  -    =   .=.  .*@@#@-@-@.@.#                     @:@=@  -@+%--.   .  * #:                            
  =                       #@.     =    -#-++%+@#@+@-@.@:*                      %@=@=@%@+%.    **=.*  %                            
  =                     += :%     :*   -==@==:*=*:#.# # -                       +%@:@+#=#+:  = ==:*  %                            
  =                    #.      :       .- =*.:-..   : = =                         --*-+.=*. :..* .+  +                            
  =                   *.       *.      .=+  +@%+#   . @-@                           ++*:.:+*##+:  =  *.                           
  =                  #          -.    -:  :  .*+* %   @-@                         +-  .=%#%%@#+   =  =.                           
  =                  *          .=    =@: *=   *.                                           :#+++= .=                             
  =                  +      #.   @:    -.  +    %                    =:                            =    *     ==                  
  =               **:+     @.          -*:  -   ::                  --   +@@@@@@@@@@@@@@#=%%#.    :   @:@-@+@=%  -@*              
  +             =-**.:    @ %     :@:  -@-  -    .*                -=                           :=  +.@:@-@:=       :+            
  +                  .=   @ %     :@-  :#.  =    .*                                                 : . :             -+          
  +           .-@*@+@:%.  @ -     :%:  -         .*                                           =- :@*@:@:@-*             =         
  +           -*@%@*@. .  =  -    -=            :*                                           --  =%*@:@.@:                        
  +           .-***-#   #    #    =  :+   -.   :=                                               *++=@ @ .                =        
  +          -=+====- +.%    #   =.  -. :-    +=                                           :=  :*--:% %                  -.       
  +          +%@##*** @:     # .*    -:-=   ++                                            := .*##+#*@:@=*                =-       
  +          +%%*##**  -*   #.:+      .  *#+##.                                              -%##+**@:@                    *      
  +                    *+  :*                                                           .+                                 +      
  +          #####%+++-:  +-       -#=+=-*-+ +-+-                                      .+  :%#%*%+@#@.%                    +      
  +        -%%####%*+ *           =#*-*=-+:= +-=-                     :+=         .#%%#- .**%#@*@*@*@                             
  +        -*=--===-%-          .:  =.-. :   . .                   :            ++      ===-==+-+-=:*      .                #     
  +        -*+++=*=*=           ==-  .-.:.-                      ::        ---.      :-.+++-==*=*:#-=     =                 *     
  =        =%####**-   .     = @@#:  -+==:-                              -+         @-@=%##=**@*@=@+*     @             =-        
  =        =%#####.    #   :* .#    ---#*::                ..  .        :    -@.#:@-@=%=@#*=+*@*%=@+#   * @          .*#+:   =    
  =         .    +.   :   .=   :    .     ==               ..      .*-     :* - - : . . .     . . . . .            :+*=      :    
  +        #@@*#=+   #=   #    %.*=.@%@@@-   =#=           ..     =.    *=@-@.@ @:@-@-@+%**=**%*%=@#@ @         .#@+       +-     
  +        #@@*#=*.  #+   *     :*=.@%@@@*@#=   #*            -#.   :=%+@-@-@.@ @.@-@-@*%*+=**%+#=@*@ @        .-=    =%#+    *   
  +        :==-=:#-  =+   :       +-+=*+=:+==.++  +.
""")
    
def The_Devil():
    print(r"""
:-                                            +                                        
                                           -.+                                         -*                                         
                                          -=-=                                         .+--                                       
                                     *@+-:.--                                            =.:-#%+                                  
                                   .=-:-=::.                                              :.-+=+#:                                
                                 :@@*==                                                       +*##%.                           .  
                                #@=  .-               -+                     +=               =.  =@@                          .  
                               ##-   .-              %#:                      *%              .    .%@                         .  
                               %#    .+             =@#    .  @@@@@@@@@:      @@=             +.    *@                         .  
                               -@*:    -           * #%  :=#-@-+-+=+=*=#.@:-  #@ *           =   :* =*                         .  
                               .-+@=:-  =.         =%  %**=#-@=#=**#+*=%-@.@ @= %-.         =  -.-@+**                         .  
                               #=:#=  =.   +.   .##%@@+  ::-**+:-=+*=-=@%: -  -@@#+%-   .+   .. .=%-+@                            
                               =*-%@@#-+*=. ....  =+%@+%#@+%=%++-++#+#=+:@ @:@@@#== ..:   .-=+-*@@@-++                            
                        +        =@*#%+++*+=*+%**-%-#=@@%@+%:@#@#*#@@@#@#@=@=@@+*-*#=*+*+++==*%%@*++        =                     
                     -=. ..       :-*+#%#+%##++++%@@=+*=.*=@*@%@%*+*##=@+@-@ #+@-@@#**++#+%%#*@==#=       .. :=:               .  
                   -:  =+           -**#*%+*-#@*@@@=@+-%#@%@@@#@@%@@@%%@%@#@+@ #@=@@*@%+:*-=#%%%=           *-  :-             .  
                 .:                     .#=:@@* @@++#+@%*@@@@@@#*#*%#%%@@@#@+@*+=%*%@-+:=-#%.                :    -.           .  
                   =%@+                  -:  %+.@@=-@#+##%#@%@%@%@#%%@=%*@#@.@.@#@#++.%#. ::                 .*@*-             .  
                   =+%+                   :+-  *@:@:@@@@@@@@%@@%*##%%@@@@@@@%@@@@+*@%.  .@=                  .+%+=             .  
              .- #:=+#:-                  :#@* *@.@.@%@@@. @#@#%*#+*#%*@%@: @@@@%##-*=.=@@-                  .=%++-%.=         .  
              : .%#*+*:-                   -*%.   @=@*     -%#+#=*+*%#:*@:     =#** =  @%=:                   :%+=*@= :        .  
               =+###=*  +                  +@*  @+%:@.@      :@@#*+*@=+       @=*:#-#  +@=                  =  %=*@%#-.-       .  
            -  %#%**=@% @                    :+  =@*#*@*       -%##%**       =@=+*#+: =-                    # @@=*@@%+ -:      .  
               =-*.=-%-  +                     .*:@+##*=.=+*+= -#@@@#*+*+* =.%+%-+*=%.                     +  #%=-.*==            
          -  +**** --@ * .=                     =.@=*@%@@@@@#@%@@@@@@@@@%@+@=@#@%#@.=                     #  ==@+: =++=. --       
         - .%%=*%  @+% #   =                    -:@=#%##@@*@#@%@@@@@@@@@@@=@%@-@+*#--                    -   #+%*@ .@+=*. -       
           -++:+: =@-% @:#- #                  #-# .##+%*-=@*@#@@@@@@@#@+%#++@+@*: # +=                -@::+.@=#-@- =+=+#         
          =#=+#+ *:@:@.@# *:+%-             =.   %@.+*%@.@.=#*=@%@@@@@*%+::@@#*@= @@.   =             .*- @ @@-#-#:- =%+@#        
         ++*+%: -@-@:@.@:@.%* ##    ++      -%@@@@@@ =*#@@% +:#: .==:=% # #@@@@# @@#@@%@:      =-     % @:-%**-#-*-@. :==-=       
           --#.:=*.*.* *.-%#@@% .@@@@. =@@-   .   @@@  *%@@@@          .@@@@#@ :%@@       =@@# .@=@@: *@@@%=**:*.=.@* :-. -       
         *=#*@:.-%-@+@:@:%=*#+%@#        .=.#=@:@@@#@@==+@@@@*-*=: .:#-#+@%@.%%@@@@%#%@+*:-.       :##@.@-%+**=%=%-%- :#++-    .  
        -@+#*@:.-%:@=@.@:%=+#=%=@@@%*@@@@%@*@=@-@:@:@@@* #*@*@= .: :::--*@@@ %#@#:#*%+@=%#@@@@@@@*@@@-@ @.#+**=%=#-%- -#**-    .  
         . . =..:- = + * ==@#:-      +#*#+#*%-@-@*%+*%#@@=:%+@%@@@@@@@%@=@-=@@@%+*@*#:@*%%@@@#%=      : @@%-==.- : =:.:-.         
         *:+-#...*.%:@.*=.          :=:+@%@#@%@#@*@#@@@@@@+**@@@@@@@@@@@*@:@@@@@@@@%@#@@@@@@@+-*.          :=@:%:#-*=-:=-=.       
         *:+-#:-:*.%:%-            :%*=  :@+@-@:@:@#%++%@@%+.**@@@@@%%**:+%@@@%@#@@@@#%-%*#-  -*#             -#-#-#=#++-=.       
         : : :+%:+ #.   -.*  :+ .=-+*-%+:.  +=@ @.@-#==#+@@@%+  :==-.  .%@%@+%+@%*#+%+%-=  ::+#==+--. =-  %*@.  :%:+:#+. .        
         =*%+=+@-**    *:  .#*@#@=@=%+#+*#%=.  :@:@+##**=%=@@@@=     -@@%@=@-@-%**#**    +##@##*%=@+@*@+@  ::-    *-:@*=:+        
        -*=%*#*@=      +=@@#@#@+@=@=%+#+#*%*@@#  :*-**#%@@@@@@@@@@@@@@@@@@%@%@@%=++  .*@@*@@@@@*#=@=@=@%@+@%+@*=    .:=*:+.       
         --*=*-:-@=   :@#@+*@#@-@=%-#+#+*+#=@+@@@- - .*+-%+@*@#@@@@@@@%@@@:@ %+  ::#@@@*@%@%@%*%@+@*@%@=@.%+#%    ++%+=+.=        
             =-- +.%:#:%+*++*:%.%:#-#=#*#%@:#.% @.@-@+ --  #:#:*=***=*+. -@+ @-=#=#=#=@=#=%#@*+=*-# % @-@=*=-*=@-#-#--=*:*        
            *@#%@@@@@@@@@@@#@@@%   *@@@.   =@*@#@=@#@@%%@@@@@@%@@*@@@@@@#@+@=@@@#*@@@@@*@:   +@@@:  +@@@@@%@@@@@@@@@@@@+@@:       
            ==-%@@@@@@@@%@@@@@+     -@%      +@=@%@+@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@=     -%@.     %@@@@@@@@@@%#@@@@#++%    .  
             .:-%@:@:%.@@@@-%*.-     :*         %%#:++=+-#:#:%-+=*=+=*-%.@.@ %:#==+@%        .+      = *@-@@@%#@%#@%@@@@@@@*
                .:-%@:@:%.@@@@-%*.-     :*         %%#:++=+-#:#:%-+=*=+=*-%.@.@ %:#==+@%        .+      = *@-@@@%#@%#@%@@@@@
    """)
    
def mayor():
    ascii_art = r"""
---:..............................::-:..............................................................
................................=***#%%#*+-:.............................................:-=====-...
.............................:+*####**+####*=............................................:====--:...
............................=#####*+---=+####*:..........................................:::-------:
...........................+#####*=--:--=*##%%*:............................::::::----:::::::.......
..........................-######+=-:::-=+*#%%%*-::::::::::::------=+++:-::::::.....................
.................::::--...=#%#**+=+*******##%%%#-:.........::::=**#*+++++-.............::::::------=
.................======...:#%+*****+*+*+****#%%#-.........:=+*#######*+*###*-::-----===++*###%%%%%%%
..........................:+*-=+---=+-++===++#%#=...:..:++++#%%%%###%%#**#%%%##%%%%%%%%%%%%%%%%%%%%%
...........................-+---=+*+***+#**++*##+:..:...=**%%%%%%#%%#*+===+#%%%%%%%%%%%%%%%%%%%%%%%%
...........................:=-==++++=++++*+++*##+:..:...=*#%%%%%##*+=----==+#%%%%%%%%%%%%%%%%%%%%%%%
....:::::::::::..............====--==-=+*==++*##*......:+*#%%%%#*+=====--===*%%%%%%%%%#%###**+==--::
.......:::::::...............-+==----====++**+#%*.......:*#%%%#++=======++===**-:::-----::::---::::-
...........................:*=+***+++++******++#*........+##%%*===--++=+**#*===-:::-::::::::--=++===
.......................-==+##==++******##*#####**:.......=#**#+===++===-=---==-:.:::..:::.::--+##+++
.......:::..::-===:-=-=*####%#===++******#%#****#:.......=####*====--+=-=+*+=++++++-==++**+==+*+*++*
.......:-:....-==+**######%%%%#===++*****%%%%#*++-.......:*##*+++=++*********+==++=-=--==+===+*=---=
.....:--....:=+**######%%%%%%%%%*+++****#%%%%#%%#*-:.....:*####++++*#+===+++++*++++-===+==+=+++*##==
......--..:=+**#####%%%%%%%%%%#%%%*+++*%%%%%%%%%%%%%#+:..:*#####++++==++++++*+==++=-=+++=+++****###+
..-*=.:-+***#####%%%%%%%%%%%%%=-*%%%##%@#*%%%%%%%%%%%%%*-:+##*#*+***++==++**##*=**+-=++==+*=+++*####
..-=::-*#######%%%%%%%%%%%%%%%#--#%%%%@#:-%%%%%%%%%%%%%%%*++#*==++***********#**++===++++*++***##%%#
.::.::*###%%%%%%%%%%%%%%%%%%%%%#-=%%%%%=:+%%%%%%%%%%%%%%%#++*+====+++******+*#***+++++++===++++#%###
*+--=*##%%%%%%%%%%%%%%%%%%%%%%%%+-+%%%%-:#%%%%%%%%%%%%#+=+*****====+++***+++*%%#*+++++++++=+**+#%%#+
==+=*#%%%%%%%%%%%%%%%%%%%%%%%%%%%+=#%%#=+%%%%%%%%%%%*++++++*********=+++===+####*+++++++++++**=#%%#=
*=+*%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%=*%%*+%%%%%%%%%%%+++++++++*#%%%###*+====*##***++++++++**++++=*#%#+
*=*%%%%%%%%%%%@%%%%%%%%%%%%%%%%%%%%*%%=%%%%%%%%%%%*++++++++++*********+--+#**++++++++++++*++++=++=+=
**%%%%%%%%%%%@@@@%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%#*++++++++++++++**+++===**++++++++++++==***+++#%%#*
#%%%%%%%%%%%@@@@@%%%%%%%%%%%%%%%%%%%#%@%%%%%%%%%%*+++**+++++++++++++++++++++++++++++=::::+**++++#*--
#%%%%%%%%%@@@@@%%%%%%%%%%%%%%%%%%%%%+*%%%%%%%%%@*+++++*+==++++++++++++++++++++++++++=:.:-=***+++**==
%%%%%@%@@@@@@@%%%%%%%%%@@%%@@@@%%%%%%%%@%%%%%%%#*++++++==--+++==+++++++++++++++++++++=:::-+***++++=-
%%%%@@@@@@@@%@@@@@@@@@%%@@@@%@@@%%%%@%%@@%%%@@%#+++++++=++------====+++++++++++++++++++===*#***+++=-
%%%%@@@@@@#:#@@@@@@@%%@@@@@@@@@%%%%%#=#@@%%%@@%*+**+++++=:===+++++++++++++++++++++++++++***#******+-
+#%@@@@@@*::@@@@@@%%%%@@@@@%@@%%%%%%%=*%@@@@@@#*+++**+++*+****+++++++++++++**++++++++++++**##*****+-
==+*##%#-..=@@@%%%%%%@@@@@%@@%%%%%%%%--%@@@@@@***+***++*##**++++**++++++********++++++++++*##******=
-=+*##*:...#@@@%%%%%@@@@@%%@%%%%%%%%%#@%@@@@@%**********##**********************************%###****
-==++*-...:%%%%%%%%@@@@@%%@%%%%%%%%%%%#%@@@@@#**********##**********************************#####***
===++*:...-%%%%%%%@@@@@%%%@%%%%%%%%%%%%%%%@@@***********###********##**********************#%%####**
===+++....=%%%%%%@@@@@%%%@%%%%%%%%%##@@@@@@@%*********###%##**##**###****************#*****#%%######
==++*=....=%%%%%@@@@%%%@%%@%@@%%%%%=+%%**++##********####%#*###**###*****************##*****%%%%##*+
==++*:....=%%@%@@@@%%%@%@@@@@%@@@%%@@@@@@@@@#******######%####**###*******************##****#%%#*+=+
==+*+:....*%%%@@@@@%@@@@@@@@@@@@@@%@@@@@@@@@*********###%####**###********************###****%#**+++
==+*-....:*%%@@@@%%@@@@@@@@@@@@@@@@@@@@@@@@@################**###**********************###****%#*+++
=+++.....-#%@@@@%@@@@@@@@@@@@@@@@@@@@@@@@@@@%%%#######%%###**###************************##****#%**+*
=+*-.....+%%@@@@@@@@@@%@@@@@@@@@@@@@@@@@@@@@@@**+++==+*%#***###*************************###*****#**+
=+*......#%@@@@@@@@@%%@@@@@@@@@@@@@@@@@@@@@@@@#+++++++*##**####**************************###****#**+
=++:::...%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%++++++++##*###******************************##**+*#**
+##:....-@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@*+++++++*###****************#*##*************##*+=#**
%%%*:-+++@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#+++++++*##*********############************###=--*#*
##=---+%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@*++++++*###*****#######################*####%#=--=#*
*+===+++%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%++=+++*%%%#########################%%%%%%#****=-=**
#*+++*#@%%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#+==+++%@@%%%%%%%%%%%%%%%%%%%%%%%%%%%%##******+-=**
=*#*++++*%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%*+==++*%%%%###%#%%################*#***#**##*+--*#
+===**+=-%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#++==+*%%##########**************************+=***
=+=------@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%+===++#%%#############**********************++***
++-------@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@*+==++*%%%#############**##*#**#************+#***
#+=------%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#+++++++*############################**********#*
%#===----@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@*++++++++*#######################**************#
*+=-==--=@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@*++++++++*###################****************+**
    """
    print(ascii_art)
    
def Doton():
    ascii_art = r"""
=====+======+=+++*****###%%%#********+******************************+++++++++++++++++++=------------
++==+=======++**###%%%%%######%%#***++***************************************+++++++++++++=---------
#*+=+====+*##%%%%%#*#%%%%%##%%%#%%###**+********************************++*******++++++++++++++==---
#==*==+*##########*****#%#%%%%%%%%####%#***********************************************++++++++*++=-
====+*###*++=--==-----==---==*#%%%#%####%%%#*********************************************+++++++++++
*++-==---::---==------===-::::--+#%%%%#####%%%%#*********************************************+++++++
----::::::::::-==+==----===::::::-=*%%%######%%%%%##******************************************++++++
---::::::::::::==+*+=====++=:::::::-+#%%###*##%%%%%%%%#*********************************************
::::---:::::----=+**#*+++++++:::::::-+#%%###**#%%%%%###%##******************************************
:::--------------++*##****++*=-:::::--+#%%%##*++++++*+*#######************************************+*
---------========-=++****+++++-::::----+%%%%##*+++++++**********#***********************************
--::----:--==++++=-=+==++++**+=--::----=*%%%%#*+==+=++++++++*******##*******************************
======++==-----=+++=-::-==-:-+*+=-:-----+%%%%##++======++++++++++++****#****************************
====-==**+=-::--=+%%+=-:::-==+***=----===#%%%%#++++++===++++++++++++++++***#************************
---------=*#*+=---+++++===++*******=-===+#%%%%#*++++++=======++++++++++++++*************************
------====-=##*+=-=+*#*+==+*********====+#@%%%#+==++++++=========++++++++++++++*********************
-----=++**+==*#**==+*%%#++*+##*+++**+=++*%@%%##+-==+++*+============++++++++++++++++***************+
==---=++***+==*#*+==+**+++++*##++==+*+++#@%%##*=-====+++===============++++++++++++++***************
+==-===++****+*##*+=+**+=-++#%%#*+++**+#@%%%#*+===++++======================+++++++++++++++*********
*+=====+++*****##*+==++====+*###******#%@%%#*++=======-========================+++++++++++++++******
***++++++++++*##*++=========+*##*****##%%%%*=========----===============================+++++++++++*
****++++++*+++++*++==========+*****##*#%%#+==----------------==============================+++++++++
******++++++++==++=++=====+===+**#%%%%%%*=---------------------------==-===================+++====++
*********++++++++++++++++++++++#%%%%%%***+--=-------------------------=--=-=========================
**************++++++++++++++**%%%%%#+++++++**+=-----------------------------=-======================
#*************+**++********#%%%##*******++++++++++===--------------------------=====================
###******************####**#***************++++++**++===-----------------------------===============
####################****#**********************++++++****+=---------------------------==============
###############**#*****+**************************++++++**+--------------------------------=========
##**+++++++=++++++************************************+++++++***+=-----------------------------=-===
#****+========++++++++************************************+=++++***+------------------------------==
++**###**++=======+++++++************************************++++++**+===---------------------------
++++++**###*++======+++++++++*******+:::-+***********************++++++****+=-----------------------
+++++++++**###**++======+++++++++**=--::::-**************************+++++****+=--------------------
+++*+++++++++*###**++=======+++++=--------:+*****************************+++++****+=----------------
==+++**++++**+++**###**++=====++=---------=*********************************++++++*****+=-----------
++++==+++**+++++++++**##**++===----==+==-=++***************#*++*****************+++++*****+===------
%%#**++++++++*+++++===++***##+-=======--=++++++*************##**++*****************+++++****=-------
#%%%%%#*+=+++=++**+++===++++---==++++===+++++++++++**********#****+++******************++++++*+====-
####%%%%%%#*++===+****++++=----==++++==++====+++++++++*******************####%%%#####*****++++++**++
#######%%%%%%#*++=++=++*+----=======+***++=======+++++++++************#%%%%%%%%%%%%%#####*****++++++
############%%%%%#*+=++-----==+====++*******++======+++++++++******##%%%%%%%%%%%%%%%%%%####*******++
###############%%%%%#+--==-==+====%@%#*+####****++=====++++++++++*#%%%%%%%%%%%%%%%%%%%%%#####*******
#########***########-:----=+====+#%%#######%%%##***++======+++++*%%%%%%*++=========+*##%%%####******
-=*##*-::::::-*###+:::---=*+===+%%#***####***#%%%%#****++======*%%%%*+====-------------=+*#%###*****
:::::::::::::--*#=::::---=====+####%%%##*+*++++*#%%%%##****++=+%%#*++===-------:::::::::--=*#%##****
::-::::::::::--*=-------=----++==*%%%%%#*++*++++++**#%%%%#****%#*+++===-----::::::::::::----+####***
:--::::::::::-=+------------=-:::::+##**###*****++++++*#%%%%###*+*#*******+==------::::::----=*###**
--:::::::::::-=-----------==-::::::-*####***#*++++**+++++**#%#**#**+=====++++==--==++**++=----=+****
::::::::::::--:::--------=+-::::----*####%%#*+++++++++*+++++*****+++==---=+++=--==++++====+++=-=****
::::::::::::::::-------=++-:::------*######%%%##*+++++++++++#++++****+++++=+=--:-=++==------=+=-=***
::::::::::::::::------=++--:-------=*#########%%%%#*+++++++**+=====+++++==-=--:::-=+*++=-----==--+**
-:::::::-::::::-------=+-----------*###############%%##*+++*++==--::------=---::::::=+***++==----=++
-----------:::::------+=-:--------*####################%%##*++==---:::::---===--::::::--------:--=++
+++==-------:::::-------::------=*######################****++==---::::-++##*+=+*+---::::::::::--=+=
**+++====---::::------::-------=#######################+****++===---::--=+====+=+++=--:::::::::--===
****++++====------------------=*######################++++**+++===--------=--------:::::::::::::-=++
********+++++========---------+#######################+++***+++=========++++++===-:::::::::::::--=+*
*************+++======------==*#######################*+=***+++=====++*+=------==+==---::::::::--===
**************++++++==----==-*#########################++***++++=======+++++==----=++==-----------=+
*****************+++++=====-*#############################**+++++==+=====+++**++==---==------------=
*******************+++++==-+****##########################**+++++========--======-----==---------=--
***************++++++++=--=*********######################***+++++=====-----::::-------==---------:-
*************+++++++++==-=**************##################***+++++++=====---=--::----------------=--
**************+++++++====*******************#############*=-:----=+++++++======--------==-------=*++
**************+++++=====+***********************####*+==--==++===-:-++++++++++++==---===--------+###
*************+++++===++*********++++++++**********=-=+++++++=++===-:.-=+++++++++=...:-----------*###
***********+++++++++********+=-:.......:-=+*****==+*#####*++==+==----::-======:::::..--:::-----=****
*********++++++++++++++++++=::............:=+=-:-*####%###**+++======--::++=...:-::.:=**+=-::-=*****
*******+++++++++++++++++++=:::...................-+#####****++++++===--..:..........-+**##*+==----==
***++++++++++++++++++++++=-::::::..................:---==****+===-:..:..............:=*#####*+=====-
+++++++++++++++++*+++=--=--::::::::::...................:+******+=.............::--------==----::::.
+++++++++++++=-:-%***++::-----:::::::::::...............:=+*******=.........:-:-+-:==...............
+++++++++=-:....=****-..--------::::::::::::............:=+*******+.......:===+=:-+-................
++++++-:.......*#***=..-===-------:::::::::::...........:-==++****+:.....=::=+-:=+:.................
+++-:.........:****=..:-====--------:::::::::...........:---=+++***:...""" 
    print(ascii_art)

def THE_autor():
    ascii_art = r"""
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
:::::::::::::::::::::::::::::::::::::::::::::::::------:::::::::::::::::::::::::::::::::::::::::::::
:::::::::::::::::::::::::::::::::::::::::::::-+####****###*=-:::::::::::::::::::::::::::::::::::::::
:::::::::::----------------------:::::::::-+#*+++++=+++++++=+#+:::::::::::::::::::::::::::::::::::::
:::::::----------------------------------**++++++++++++++++++++**-::::::::::::::::::::::::::::::::::
:--------------------------------------+*++****++++=+++++++++++++*+:::::::::::::::::::::::::::::::::
--------------------------------------**+*****+++++++++++++++++++++*-:::::::::::::::::::::::::::::::
-------------------------------------##****++++++==++=+==+++++++++++*-::::::::::::::::::::::::::::::
-----------------------------------=%%*****#%%%%*++++++++*#%%#**++++*%::::::::::::::::::::::::::::::
----------------------------------=#%%**#%%##******++++++******##*+=+*#-::::::::::::::::::::::::::::
-----------------------------=====+%%**###***+***##*++++*****+++++*+=+#*::::::::::::::::::::::::::::
----------------------------======#%#**#####%%#***#*+=++*#####*++++++=+#-:::::::::::::::::::::::::::
-------------------------=========%%***#%%%#%#******+++++***##*##*++==+#=:::::::::::::::::::::::::::
---------------------============+@%*****#####******++++++++***++++++==#+:::::::::::::::::::::::::::
--------------------=============+@#*****+**********++=+++++++++++=====*=:::::::::::::::::::::::::::
----------------------============%#****++++++++*#@%#*#%#++++==========+=:::::::::::::::::::::::::::
----------------------==========*%#******++++++*###********++++========++*=:::::::::::::::::::::::::
-----------------------========+###*********++***********++++++++======++*=:::::::::::::::::::::::::
-----------------------========+**#***********#######*****+++++++==+===+=*-:::::::::::::::::::::::::
------------------------========*+#***###***###%%#*++*+**##**++++=====+++=-:::::::::::::::::::::::::
-------------------------=======******########%#####*******#**+++=====++++-:::::::::::::::::::::::::
-------------------------========*****####**********##**+++++++++++==++++=::::::::::::::::::::::::::
-------------------------==========**########******+++++++++++++++++==++=--:::::::::::::::::::::::::
-------------------------===========*########******++++++=++++++++++++==---:::::::::::::::::::::::::
----------------=-------==-=========+*############*****+++++++++++++++===--:::::::::::::::::::::::::
------------------------==-=========+*########%#######*****++++++++++====--:::::::::::::::::::::::::
---------------------=--============+*###%%%%%%%%%########*********+=====--:::::::::::::::::::::::::
----------------------------========+**##%%%%%%%%%%########******+++=====--:::::::::::::::::::::::::
----------------------------========+**####%%%%%%%%####*******++++++======-:::::::::::::::::::::::::
-------------------------------=====+**######%%%%%###*****++++++++++=====---::::::::::::::::::::::::
---------------------------------===++*########%####****+++++++++++======---::::::::::::::::::::::::
---------------------------------===++*#############****++++++++++++====----::::::::::::::::::::::::
--------------------------------=-==++*#############***++++++++++++#*===----::::::::::::::::::::::::
--------------------------------===+*#%###########*****++++++++++++%*====---::::::::::::::::::::::::
--------------------------=+++++**+***%######**********+++++++++++#%%*##++==-:::::::::::::::::::::::
------------------==+++++++++*++*++****####************+++++++++*%%%%#%%*+++++=-::::::::::::::::::::
---------==+++++++++++++++++++++*++******#@@@@@%%%%%%%%%%%%%%%%%%@%%%%%%+=++=++++++=-:::::::::::::::
-------++++++++++++++++++++++**+++*++*******#%%%@@@@%%%%%%%%%%%%%%#%%#*+++++++++++++++==-:::::::::::
-----=*++++++++=======-------------------------:::-::::::::::::----------========+++++++===-::::::::
----=**+++**+++==---------------------------------------:--------:::::::::---------------=++===-::::
--=+***++*****==------------------------------------::--::------:::::-:::::::------------+++++====-:
=+*****+******+--------------------------------------:--::---:::--::-:--:-:::------------++++++++++=
******#*******=-------*:==#==-*=+--=-+-+-=+=-+---+--==---:--------:::::::-::-:-----------=++++++++++
******#*******=-------=+*====-==+-=+:*=*-=-+-++--+--+::=-:::++-#-=+-+-=-::+------:-------=++++++++++
**##*##*******-------=-#-*-+-*-==:++:*=#-==+-=*--=--+--=-:::==+===++++::-+::--:----------=++++++++++
**#####*******::-----==--------------=---------+-=+-+===+-::=---=--===-:-==---:----------=++++++++++
#######******+::-------------------::::::::::----::::::::::::::::--:--------:--:---------=++++**++++
#######******+::::-------------------::::::----=--=-----::::-::::-:-::::----:------------=+++++**+++
#######*#****=--:::--=+:++----*-*:==-:=-===-=:=--+---+--*-=-=-----:-:::-::--:--::-:------=+++++**+++
######*#***++----::::-*===*+-:*==+-=++=-==+:=:+--++--*--*===-+=---:::-----:-:::::::::::--=*+++++*+++
######******#------::--------------::------:--=-----=+------------:-::----------:--:::----*#*+++*+++
######****%%#::-----:::----------------------------------------------:::------------------+##*+++++*
#####%###%%#*:-------::---:----=-------------------------------------:::------------------*+#%*++++*
####%%%#%%**+::---------==:++--+--+==:---+-=+=-=-++==--------------::::::--::-------------***%#*+++*
###%%%%%####+-::-------=-+-=+-*---=+--::*---=-*=--+-=-------:-------:::--::--------:-:----+**#%**+**
###%%%%%%##*=::::-------=----+---==+#+-+---+=*=+-+====---------------::::::::--::-::----::++**%##***
%%%%%%@%%%##=:::::----------=---------==---------=-=*=-------------------:---:::----::--::++**#%%***
%%%%%%%@%#**=-:::::------------------------------------------------------------:---:-:::::+++#%%#***
%%%%%@%@@%##=--:::::---------------------------------------------------------------::::---=**%%%#***
%%%%%@@@@##*=---:::::--------------------------------------------------::::::::::--:----::=*%%%#*##*
%%%%%%@@@#*+=---::::-----------------------------------------------------::--------::----:=*%%%####*
%%%%@@@@@%#*==---::::-------------------------------------------------------------------::=%%%#*###*
%%%@@@@@@%#*===---::::-------------------------------------------------------------:-----:=%%%###%#*
%%%@@@@@%%#*===---:::::-----------------------------------------------------:---::-::-:----%%%#%%#*#
@@@@@@%%%%#*===----::::--------------------------------------------------------------::----%%%%%%###
@@@@@%%%%##*====----::::-------------------------------------------------------------------#%%%%%###
%@@%%%%%###*====-----:::--------------------------------------------------------------:-:--#%%%%%%%#
%%%##%%#**+++===-----::::----------------------------------------------------------------:-*##%%%%%%
#%#**+++++++=====-----::-------------------------------------------------------------------+###%%%%%
#*+++++****++==++==----:------------------------------------------------------------====---+**###%@@
+++=+**#####**++=====---:-----::::---------::-::::--------------------------------==+***++=++****#%%
+++++++++++=+##*+===###################**********###***************************+=+*++++#**++=+++**%%
++++++++++====+*%*+*%%%%%#################*##******************################*+=+#**++***+++===+#%
++++*****++====+%%%%%%%%%###########****************************################*+=*#**+=+****++===*
=====++*#%#+====+#%%%%%#########*****************++***************#############%#+==***+==+****++===
=========+++*++++*%%%%%%#########***********************************#############*+=+***+++=*#*++===
+==++========+*+++#%%%#########************+++++++****+++++++******##############*+++**#**++==**+++=
+===+**+++====+**#%%%#########****************+++++++++*+++++++*****###############*+++##**++==+*+++
+=======++*+==+*%%%%%%%##*****##************+*++++********+++++*******##############**++##**++==+*++
*++========+**+#%%%%%%%####********************+++++++*****+++++*******###############*++*##**++==++
    """
    print(ascii_art)

def Ezekiel():
    ascii_art = r"""
+======---------=*#*###########*++*****+++++=============-==-------------------::-=::::
###*****++==---==========-----===+*++======-----------------------------------------:--
######*========================---====+==----------------------------------------------
%####***+==========--::::::::::::----=====+=------::::::::::::::::::::......:::::::----
%%######***=======--::::::::::::::---=======-::-:::::::::::::.................::::--===
%%%#######***+=======--------:-----=============-:::::::::::::::::::.......::.....:::::
%%%%%#######***+===================================-:::::::::=#+==-::.................:
%%%%%##########***=================================++-:::::::+#####***-................
%%%%%######%#####*#*+==================+++++******++++-::::::+#**####*+==-::=+++===:...
%%%%%%#####%###########*+====++++*********************-::::.::-*##***####*+==-:........
%%%%%%###################**************#####****+****+##=:::::..:-=+*****###*+==-......
%%%%%%#####################**####***########***+*##*#+#####=:.........=******###*+=-:..
%%%%%%########%################***++=+*######**#####**########=:.........-******####*+=
%%%%%#*#######%%################++####**#####*#######*###########=..........-*#*****###
%%%%%#*########################*#######*#####+####*##***############=..........:*#*****
%%%%%%##*%%####################*#####%#########**###*******############+..........:+##*
%%###%###*#%###################*##%##*##############*===+****############*+:..........=
####**####****######################################*-+---****###############+:........
**##***#%###*#*##################################**++-=*=--*****################+:.....
**###**##%###**#%################################*+=-=+=-=*+*******#################**+
*##***#########*#%%#######################*##*=======**++##++********##################
####%#####%##*###*%%####################+============*#*+*##+**********################
%####%%############*#%#####****#%#*==================+##****=*************#########%###
%%#####*#*####**####**%%%#*#*+===============++======+*+=*#*+***************##########%
%%#####***####***#####**++============++*#*=#+=======##***#=+*****************#########
%%###%#****#*#*****###***+=========+*##**#*-*========##*+***********************#######
%%###**#*********##*##****+======+***+=*+#*-*=======+###**************************#####
@@@%#####***#*+*##***#****+==========++#=#*=+=======*%###****************************##
@@@@###**###*#**####*#****+=========++*#+##++========#####****************************#
%@@@%###*####**+*###******+========+++*#**#*=*===**=--=###*****************************
%%@@%**#**##########**#***+========++++**+##+=*#%%%#*----*#****************************
%%%@%%###*########*++*#***+========++++*#**##=*%%%####*----****************************
%%%%%%%###*#**+###***##***+========++*#%%%**#*=*#%%#####*--:-+*******+---+*************
%%%%%%%#####*#**###**%###*+*#+===+#%%%%%%%#+###*=*#####*+---::-+**=-:::::::=***********
%%%%%%%%#####****###%%%%%%%%%%*+===#%%%%%%%#*#####*==*+=------:-:::::--::::::+*********
%%%%%%%%@%%####%%%%%%%%%%%%%%%%#+===+%%%%%###+#####*#+==#*=----:::-::::::::-=**********
%%%%%%%%@@@%#%@%%%%%%%%%%%%%%%%%#*====#%%%####*+#*#*#*#*****-=**----::::-=+*****+=*****
%%%%%%%%%@@@%%%%%%%%%%%%%%%%%%%%%%#+===+%*====+*+*##*****#******=-:---=+***###*****+*#*
%%%%%%%%%%%%@%%%%%%%%%%%%%%%%%%%%%%#+===========*###***********=--==+###***###*****%##*
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%#*===========+###*********#*+*++###++**************
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%##======--=+**%###***##*#####*#******+**********##
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%#+==-=====#%%#+-*##*######**###*******##*****#%%##
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%#+====-===----------+########**#*******##*++*#%%%####
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%*======-====-------=++**#*###*+*#**###********%%%%####**
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%#==========-===---=++#######*#*#***+####*##**%%%%#####****
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%*========-----==+###**#*###****##%##*****%%%%#####*******
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%#*======---==*#%###***##*##****###****#%%%%#####*********
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%##===-===*#%###***+**********####*#%%%%#######**********
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%#*++*%%######*#****=##****##**%%%%%#######************
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%###%%######*###***##*#***#**#%%%%########**************
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%#%########*####***##***#****#%%%%%#########***************
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%#%####=-*##*#########****#%%%%%##############*************
    """
    print(ascii_art)

def New_Year2026():
    ascii_art = r"""
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%##**
%%%%%%%####%%%%%%%%%%%%%#####%%%%%%%%%%%%%%%####%%%%%%##%%%%%%%%*:-..
%%%%%#*+*+*#%%%%%%%%%#*++++++#%%%%%%%%%%%%#*+*+*#%%##+++**#%%%%#*****
%%%%#+=++*********#*#++*++++**********####+*++*******++++********###*
%%#+*+*+++++++++++=+*+**+=++++++++++++***+**+++++++**+++++++++++*####
%%########**+++++++###**#########################**+++*#***##########
%%%%%%%%###++++++*##%%%%#%%#%##%%#%%%#%%%##%#%%%%#++*##%%%%%#########
%%%%%%#############%%%%#####*##%%%%%%%%%%%%%%%%%%####%%%%%%##########
%#########%%%##%%%#%%%#%#*++++#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%#######
######%%%%####%%%%%%%%%#*++++***++*********#%%%%%#*******############
##%%%##%#%%%%%%%%%%#**+====================+==+*#**************######
#%%%%%%##%%%%%%#*+-::---=+****++++++*++++**+=---==--=++***********%%%
%%%%%%%%%%%##+-:---=*****+*++++++++**+++++++++++-:::--=++*###**######
%%%%%%%%%#+::--+****+**+*#+++***+++++++*#++++*=--------=+*#########%%
%%%%%%%*-:-=+*****++#*+**+++++++++++++++++=++=---------=**##########*
%%%%%*---=***++****+*+*++++--:::::-------=+++++*++*+++++**###########
%%%*---+**+++++*+++++=:---=++************+**+*+=++*++++++**#***######
%#=--+***++**+*+*=---=***##################---+=-==-----=+++++==##%##
*--=*****+*++*+---+*#######################+==-=++=---=========+###+*
--+**+*+*+*++--+*###########################+===============-=+###*=-
=**+**+*+++=-+*##############################+======--====++**#%%#**+
**+***+++=-+*################################+=---====+++++++*####++*
***+*+*+==*########*+*##################**###*=====+++++++===+***++*+
+*#++*+-+###########+++++#+*#*+==*#####*==*****++++++++++===+++******
++++++=+##########**##++#*==*#########*=*####+*#**++++++==++*#*+++===
#++++=+############=**+#**-=**++=*###**#####*-=##**++++++***++*#*+=+=
+++*==#########***##+=*++*-=#+=++*#####=--===-:=+++**++***+++++---==+
++*==############+==--==-=-*#+=*#######+====-==-===++==+*==++=---=+++
+++-*#############==--+=*+-##+=*#####*======-+==++*#**++=++++===+++++
+*==#############++*=-*===+##*=#####+======+*+-====++=======+++++====
*+=+############*##*--**=*###*+####*+========+=====++=========++===++
*+-####################*##*########*+========-===+=-=========++==+*+=
*==###############*-=####+:-#######+--======--++============--==+#+==
*==%%%############*--****=:-*+=+##*++++=======*=-++========++=-=*====
-==%%%%%%##+--*##*+::=**#=:==-:-##**+++++====#+++*+======+**+=-++=-=*
=---=++=-----*##*=+:+-=##=-###==#++*+++++++++*#*========+***++*#+=+**
--========--*%%+:=+-=####==+=-::-=++=--=+*****+==+++====+**+**##**++*
-------=--=#%%%%##*--+=**-*=*##*-+*+-::-+***##++++=-:--+**+*###%#+###
---------+%%%%%%%%#--###*=#*=*#*+**+=--=***#%*+*+=-----+**+*#######*=
------+#%%%%%%%%%%*--#%+=####==+***+==++==+###**++=---=+**######****=
###**#%%%%%%%%%%%%##*+=*#####*=++***+==++*%%*+**++=--=++*#########*+=
%###*+#%%%%%%%%%%%%%%##%%###*++*####******##+++++=++***##########*++*
#####++*%%%%%%%%%%%%%%%%%%%#++***####****+*++******#############*****
#*##**+=*#%%%%%%%%%%%**#*#*#*+++=+*##*+==**+++***#############***+--+
**##***+=+#%%%%%%%%%%###%###+++*******++*+**+-+**#####*==+*##%#**####
*********==+#%%%%%%%%%%%#*#*=++++****+=+**+****=-+######**#####***###
+****##***+--+#%%%%%%%%%%%%#==+++**#+--=+++#**=-===*#######*+++**+++*
-=**********+--=#%%%%%%%%%%#+=--=++*=---::-##++############***+++++==
*:-+****##*****=--+#%%%%%%%#+=--=++++******########*####*+**#########
@%=:=+************=---+#%%%#+======+*###########*+=+====-=+**####**##
%%%#--=+*************+=----=*+--::--+*############*+-++=-+*******####
%%%%%#=--+******##********++++=-:::-+#########*##*+=-=+--+**+**######
%%%%%@%#=--=+***+++++++++++++++--::-=++*#####=-+*=-:---==+=--+######%
####***++=====--+#%%%%%*=======------+**##*+*=--::----==++++###***#%%
*****+======+==-==*#######======-:::-=*###+=-::-----===+++**###**#%%%
#####*+=++++++*++=+###**+++=====---::::-=-::-----===+++++**#%%%%#%#**
++++++++===--+***++=-===+++++**==-:::--=------===++++****#%%%%#*####+
+==--========-+#####+=**##*%%#+------+#%#+--==++***#%%%%###*******##*
+++=--=+*++==--+#####%%%#*%###*====--=#%%*+++#%#%%########**********#
#*++=----===+==*#########*##*+====---==+**##%%%%%%#######****#*******
=+*####+======+*****+==-----==========++***+##%@%%######***##*####***
######*+=========---:--=-----==+++++*++++++==*#*%%#####*****####%#***
######*+==--=+*+***+-===++=------=*#*++++++++*%#%#****++*****##*#****
##*#**+=--===++**++++-------=++==+##########%%####*==--=+***********#
*+++==+++==+++*******=-=++++++===+**###*##########*+=---=*##******###
    """
    print(ascii_art)
    
def forbidden_Currency():
    ascii_art = r"""
==*%@%%%%%%%####*+++++++++==-:::::-------:------====+++++****+++++++*===-------=*##+=--=*#%%%@@@@@@@@@@@@@@@@
%*+*%%%%%%%%%####*+++++++++=-::::---------------====+++****+++++==++**+====**+=-=-=+*#%%@@@@@@@@@@@@@@@@@%%%@
@@#*%@@%%%%%%%###**++++++++=::::::::----==----=====++***#+++*+==+++*#**###+---=*%%%@@@@@@@@@@@@@@@@@%%%@@@@@@
@@@%@@@@%%%%%%####****++=-.:::::::-----===--======++**#*+++*++++*##%%%%*==+#%%%@@@@@@@@@@@@@@@@@%%%@@@@@@@@@@
@@@@@%%@@%%%%%%%###**+=:...::::::-----==========++**#*++*#***#%%@@@%#*#%%%%%@@@@@@@@@@@@@@@%%%%@@@@@%@@@@@@@@
@@@@@@@@@@%%%%%%####*+....:::::------==++======++**#***###%%@@@@@@%%%%%%%@@@@@@@@@@@@@%%%%%@%@%%%%@@@@@@@@@@@
@@@@@@@@@@@%%%%%%#####+...::::-----===+*+=====+*##**#%%%@@@@@@@%%%%%%%%%%@@@@@@@@@%%%%%%%%%%@%@%%@@@@@@@@@@@@
@@@@@@@@@@@%%%%%%%####*+:::::------==+**+===+**#*#%@@%#@@@%########%%%%%%@@@%%%%%%%%%%%%%%%%@%%@@@@@@@@@@@@@@
@@@@@@@@@@@@%%%%%%#####*:::-------==+**+==+*##@@@@@#+++*%%%#*#######%%@@%%%%%%%%%%%%%%%%%%@%%%@@@%@%@@@@@@@@@
%%%%#%%%%@@@%%%%%######----------==+#%@%%%@@@@@@@#+++++++*%@#####%%%%%%%%%%%%%%%%%%%%%%%%%%@%@@@@%@%@@@%@@@@@
####%%%%@%%%%%%%%#####+-----=---==+*@@@@@@@@@@%#+++++++++++#@@%%%#%%%%%%%%%%%%%%%%%%%%%%%%%%%%@%%%@%%@@@@@@@@
#%%%%%%%%%%%%%%%%####*------====++*@@@@@@@@@@#+====++**+*+++*#####%%%#%%%%%%%%%%%%%%%%%%%@%@@%%%%%@@@@@@@@@@@
%%%%%%%%%%%%%%%%#####=--------=+#%@@@@@@@@@#+-----:-=++****++*+#####%%#%%%%%%%%%%%%%%%%%%%%@%%%%%%@@@%@@@@@@@
%%%%%%%%%%%@%%%##**#*-:-------=+#@@@@@@@@@*-----::-=--++*****+++*#####%%%%%%%%%%%%%%%%%%%@@@%%%%%@%@%%@@@@%%%
##%%%%%%%%%%%###%##*=::::----==*@@@@@@@@@%%+--::--::-:=+*++***++++*###%#%%#%%%%%%%%%%%%%%%%%%%%@@@@@@@@@%%%%%
*###%%%%########%##=::::::---=+#@@@@@@@%%%##-----===-:=+++=*#***++++######%#%%%%#%%%%%%%%%%%%%@%@@@@@@%%%%%%%
***#######%%#%###*-:::::---==+*%@@%%%%%%#%%#*+-=+*=-=++=====+*****+++*################%%%%%%@@@@@@%%%%@%%%%%%
##%%%#%%##%####*=::::::---==+*%%%%%%%%%%##%###++=-=++======+*#*#***++++*#*#####%%%%%%%%%@@@@@%%%%%%%%%@%@@@%@
%%%%%#%#######+:::::::---==+#%@@@%%%%%%###%%%%#-+++===-==+*#######*+++++*###%%%%%%%%%%%%%%%%%##%%%%%%%%%%@%%@
#%%#**########*-:::::--==*%@@@%%%%%%%%%###%%%%%%*=-=-=-===*####%%#*+==++==*%%%%%%%%%%%%%%%%#@@%%##%%%%%%%%%%%
*###############*====+*#%%%%%%%%%%@%########%%%%#+==-=--=********========-=+#%##%#%#%#%%%%###%%%%%*#%%%%%%%%%
######################%%%%%%%@@%%%%%#########%%%%#*+---=++==-===-:-==---==*############%%##%%%%@@%##%%%%%%%%%
######################%%%%%%%%%%%%#############%%%#++++=-------::------=+*#####*########%%###%%%%##%%%@%%%%%%
#############%#####%%%%%%#%%%%%%#%%#%%%%%%%####%%#%%*==---------::-:-=*#**#*##****#*##*###%%%%#%%@%%%%%%%%%%%
###*########%##%#%%##%%%%%%%#%%%%%%@%%%%%%%#####%%#%*=-----:-=:-===-*###**********########%%@%%%%%%%%%%%@@%@@
#############%###%%%%%%%%%%%%%@@%%%%%%%%%%%##########=---:-==-+***#%#%###******######%@%%%##%%%%@@@@@@@@@@%%%
#######%#######%%%%%%%%%%%%%%%%%%%%%%%%#%%#%######%##*=--=--=+***##%%%####**######%%%%%%%%%@@@@@@@@@%%%%%%%%@
#######**###%%%%%%%%%%@%%%%%%%%%%%#%%%%%%%%%#%#####%#%*-+==+*##%###%##%#######%%%%%%%@@@@@@@%%%%%%%%%@@@@@@@@
###***#####%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%#%#%######%#%*==-*%@%%%###%##%%%##%%%%@@@@@@%%%%%%%%@@@@@@@@@@@@@@@
+**######%%%%%%%#%%%%%%%%%%%%#%%%%%%%%%%#%%%%########%#%*%@@@@@%%%**##*#%%%%%@%%%%######**#%%@@@@@@@@@@@@@@@@
#########%%#####%#%%%#%#%%%%%%%%#%%#%%%#%%#%%#%######%#%@@@@@@@%@%%##%%#%%%%%#***++++++**+*#%%@@@@@@@@@@@@@@@
#####%#######%%%%%%%%#%%%%%%%%#%%%%%%#%%%%%%#%%%%#######@@@@@@@@%@@@%%%####*+++=========+*+*#%%@@@@@@@@@@@@@@
####*######%##%%#%#%%%#%#%%%%%%%%%%%%%%%%%%%%#%%%#######%@@@@@%##**#****+**##*+==========+*++#%%%@@@@@@@@@@@@
#**############%%#%%%%%#%%%%%%%%%%#%%%%#%%%%%%%%%%%####%%%@@@#++++++****+++***+++++=======+**+*#%%%@@@@@@@%%%
################%%%###%%%%%%%%%%%#%%%%#%%%%%%%%%%%%%%##%%%@@%+++*******+++++===++++++====++##*+*#%%%%@@%%#%%%
###########%#####%%%%##%#%%%#%%##%%%%%%%%%%%%%%#%%%%%%%%%%%*++++*******++++====++++++++**##%%%#++###%%%@%#%%%
##################%%###%%%%#%%#%%%#%%%%%%%%%%%%%%%%%%%%#++++++++**+**##***++===+++**########%%%#++**##%%@@%%%
###################%%##%%##%#%#%%%#%%#%#%#%%%%%%%%%#*++==++++++++*****###***++***##########%%####*=+**##%%@%%
####################%%%#####%#%%####%##%%#%%%%%#+==++++=+++++++++****++*##**+*##%%###############*+==+*###%@@
%####################%#%##########%###%%#%%#+++++==+**+++++++++++*************#############*+++==++===+**##%%
%##################################%%%%#*+=====++===+++===++++++**####*********####*******###***+*###*==**###
#%########**#*##*###########*####%%##+=++++==============++++++**#*******#*************###%%%%%%%%%%%%#===**#
##%########*####*################*+++==++=++==========+++++*******######***********##**####%%%%%%%%%%%%%*++**
##%%###########**########%###*+==++**+====+++===========++*####****####*###*####**###***####%%%%%%%%%%%%%#*+*
    """
    print(ascii_art)

def Kaldag():
    ascii_art = r"""
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#*+====+++**%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%*=-------------=++**##%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#+=--==------------------==#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%+==========------------====--*%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#===============================*@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%+===========--====================#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#+==========-----===================*@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#+===========-----===================*%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%+==============--====================*%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%=====================================*%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%=====================================+%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%+====================================*%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#+===================================*@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@*+++================================*@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%++++================================*%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%++===+==============================*@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#+==========+===+==================+#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#+=========+===++=========++======+%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%*+=======+====++++=====++++=====++%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#++++++++++++++++++++++++++++==+#%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@+==+++++++++++++++++++++++++==*@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#=++++++++++++++++++++++++++++*@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@+=+++++++++++++++++++++++++++#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%++++++++++++++++++++++++++++++#@@@@@@@@@@@@%%%%@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%++++++++++++++++++++++++++*+*+#@@@@%#*+++++++++**%@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@*+++++++++++++++++************+++===++************#@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%*+++++++++++++***************+++*****************#@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#*++++++********************************##########@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@**+***************************####################@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%#****++***************#####***#######################%@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%%%*++++*****************#####################################%@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@#*++++++++-:-+****************###*###******###########################%@@@@
@@@@@@@@@@@@@@@@@@@@@@#*+**++++***++===+++***####****###***#***+++++*******####################%@@@@
@@@@@@@@@@@@@@@@@@@@%#*+=--=+*******++++**#############*+*##*+++++++++++++**####################%@@@
@@@@@@@@@@@@@@@@@@@#**+===--====++**=+++*#****########*+*##*+++++++++++++++*#####################%@@
@@@@@@@@@@@@@@@@@%**+==++++++++======+++*****########*+*##*++++++++++++++++**####################%@@
@@@@@@@@@@@@@@@@#***=++++++++++++++++++**###########*+*##*++++++++++++*******#####################@@
@@@@@@@@@@@@@@@#*+==++++++++++++++++++***##########*+*##**++++++++++*********#####################%@
@@@@@@@@@@@@@@#**++++++++++++++++++++++**##########++##*++++++++++***********######################@
@@@@@@@@@@@@%#*****++++++++++++++++++===*#########***#**+++++++++***********##%%%%#################%
@@@@@@@@@@@%****##*+++++++++++++++**++++*############**++++++++++**********###%%%%%%%%%%%%%%%%#####%
@@@@@@@@@@%****####******++++++******################**+++++++++**********##%%%%%%%%%%%%%%%%%%%%%%#%
@@@@@@@@@@**###########*********####*#**####*#######***++++++++*******######%%%%%%%%%%%%%%%%%%%%%%%%
@@@@@@@@@**#################***#####***###**########***++++++******######%%%%%%%%%%%%%%%%%%%%%%%%%%%
@@@@@@@@**#################%#####*##********####%%###**+*********#####%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
@@@@@@@**################%%%%%%###*++++++**#####%%%##**********######%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%@
@@@@@%#*##############%%%%%##**+++++++++***####%%%%%##******####%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%@
@@@@%#*################**+++++++++++*******####%%%%%%#########%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%@@
@@@%#########****++++++=====+++++**********####%%%%%%%%###%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%@@
@@@#*#***++++===++++++++++++****************####%%%%%%%%#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%@@@
@@%*++====+++++++++++************************####%%%%%%%#%%#####%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%@@@
@%+==+++++++********************************########%%%###########%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%@@@@
@*++++************************************########################%%%%%%%%%%%%%%%%%%%%%%%%%%%%%@@@@@
#+++***********************************############################%%%%%%%%%%%%%%%%%%%%%%%%%%%%@@@@@
++***********************************#####%%########################%%%%%%%%%%%%%%%%%%%%%%%%%%@@@@@@
+*********************************######%%%%%#########################%##%%%%%%%%%%%%%%%%%%%%%@@@@@@
******************************#######%%%%%%%%%########################%#####%%%%%%%%%%%%%%%%%@@@@@@@
***************************#######%%%%%%%%%%%%%################################%%%%%%%%%%%%%%@@@@@@@
**********************##########%%%%%%%%%%%%%%%%%#################################%%%%%%%%%%%@@@@@@@
********************########%%%%%%%%%%%%%%%%%%%%%%%#################################%%%%%%%%%%@@@@@@
#*************##########%%@@@%%%%%%%%%%%%%%%%%%%%%%%###################################%%%%%%%%@@@@@
#####################%%@@@@@@%%%%%%%%%%%%%%%%%%%%%%%%%##################################%%%%%%%@@@@@
############%%%%%@@@@@@@@@@@@%%%%%%%%%%%%%%#%%%%%%%%%%%%################################%%%%%%%@@@@@
@%%%%%%@@@@@@@@@@@@@@@@@@@@@%%%%%%%%%%%%%%%%#%%%%%%%%%%%%%#############################%%%%%%%%%@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%##########################%%%%%%%%%%@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@%%%%%%%%%%%%%%%#%%%%%%%%%%%%%%%%%%######################%%%%%%%%%%%%%@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@%%%%%%%%%%%%%%%%#%%%%%%%%%%%%%%%%%%%%###################%%%%%%%%%%%%%%@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@%%%%%%%%%%%%%%%%%%#%%%%%%%%%%%%%%%%%%%%%##############%%%%%%%%%%%%%%%%@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@%%%%%%%%%%%#*#%%%#####%%%%%%%%%%%%%%%%%%%%##########%%%%%%%%%%%%%%%%%%@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@%%%%%%%%%%%%##%%%%%%%%%%#%%%%%%%%%%%%%%%%%%%####%%%%%%%%%%%%%%%%%%%%%%@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@%%%%%%%%%%###*####%######%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@%%%%%%%%%##****###%###%%##%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@%%%%%%%%%%##****###%#######%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@%%%%%%%%%%#*##*#***********%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%@@
@@@@@@@@@@@@@@@@@@@@@@@@@@%%%%%%%%%%%***********++++*%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%@@
@@@@@@@@@@@@@@@@@@@@@@@@@@%%%%%%%%%%%#######*********#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%@@
@@@@@@@@@@@@@@@@@@@@@@@@@@%%%%%%%%%%%#**#***#######%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%@@
@@@@@@@@@@@@@@@@@@@@@@@@@%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%@@
@@@@@@@@@@@@@@@@@@@@@@@@@%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%@
@@@@@@@@@@@@@@@@@@@@@@@@@%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%@
@@@@@@@@@@@@@@@@@@@@@@@@%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%@
@@@@@@@@@@@@@@@@@@@@@@@@%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%@
@@@@@@@@@@@@@@@@@@@@@@@@%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%@
    """
    print(ascii_art)

def Close_Up():
    ascii_art = r"""
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%#
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%#-::...
%%%%%%%%%%#*##**#%%%%%%%%%%%%%%%%%#***#%##%%%%%%%%%%%%%%%%%%%%%#*##**#%%%%%%%%#*#%%%%%%%%%%%%#::-:..
%%%%%%%%#*++*++*#%%%%%%%%%%%%%%#**++++*+++#%%%%%#%%%%%%%%%%%%#*++**++#%%%%%#*++=*****%%%%%%%##******
%%%%%%#**++*++*###%######%###%#*++*+++=++***######**####%%%%#*+*+*++*#######**+**++*#%###***########
%%%#**#*=**++**+=+*+++*=+******=*#***==+**++==*++*++*+=*####*=**=+++=*+**+**+=**=+*=**++**==+*******
%%%#++*=***=*+++=++=*==++=+=+**=***+=+=+=+=+++=++=++=+++**+*+***=+=++=++++**+++=++=++++++++++**#####
%%%#****#%#******+=+*=***+=*###************************###***##************++==*********************
%%%%%%%%%%%%%%##*+=+++*++=*####%%#%%%%##%%%%#%#%%%#%%###%%%%%%%##%%##%##*++*++*###%%%%%%%%%#########
%%%%%%%%%%#####*+=*++**++*##%%%%##%###%##%%###########%%#######%##%%%%%#*+++*#%%%%%%%###############
%%%%%%%%########**##*#%#####%%%%%%###%######%%%%%%%%%%%%%%%#%#%##%%%%%%####%%%%#####################
%%#%%###########%%%####%%###%%%%#%%%%#*+=+=*##%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%#######
%###########%#%#####%#%%#######%%%%#*++**+**#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%############
#########%########%####%##%####%%%#*+++++********#*********#***%%%%%%%%%##****++**%%%%%%%%%%%%%%%%%#
######%####%%###%##%#%%%%%%%%%%%%#*=+=++======+==+=+-===-==+=-+**##%%%%+=+**##*****++++***#%%%%%%%%#
%%#%%###%##%#%##%%%%%%%%%%%%#*=:..+====+==+===+====-===++=====+=-:::-+******+**##************#######
%%%%%%%%####%%%%%%%%%%%%#=:..:--:::-+****++++++++==+**++==++***+=::::-+=----=++***#************#%%%%
%##%%%%#%%%%%%%%%%%%#=:.:-----+********+++*+++++==++++=+++++++***+++*+:::::--=++++**#*#*****##**#%%%
%%%%%%%%%%%%%%%%#*-..:---=***+***+++=+***+*##++*++###+=*+*#*++*+*+=++-::::::---=+=**#####*#######%%%
%%%%%%%%%%%%%%#-.:---=**+***++**++**##=+*++**++*+++++++*+*#*+=+=+#*=------------=+**##############%%
%%%%%%%%%%%#+::---=*****+++*+##++*+++++*+++++*+++++++++++++++*+++*+--::::-------=+**##############%%
%%%%%%%%%#=.:---**+**++++**=+**+*++=+***++++************++=++**+==---=====------=+**##############*=
%%%%%%%#=:---+*+**++*+###++*+++**++**+-::::::---::::-----:::-++=++++**+************###############%%
%%%%%#=:---+*+*+++*+*++++*++*+++=::::----==++***#####***+==--+*++**+==++*#*********#####***#######%#
%%%#=:-=-**+*=*+##**+*++*++*=..----=*#########################+-=***===+*+=-------=+***+++++*####%%#
%%*----+***+**+++*+++*+*+-::--=*##############################+::--+=--=*---------=+*+=+*=-=+###%###
#=:--=*+*++++++*+*+*+*=::--+##################################*--=--===++-----======+=======*####++*
--=-***+***##+*+++*+::--+#######################################+++++++===============---=-*####*:-=
=-=*******++*+++*+:--=*#########################################*===---======--======+=--=#%%%##**-:
-***++**++*++*++---=#############################################+===++=-==----====+++**+*#%%%##*+*=
*+#+*+##+*+*+*---=###############################################*+==---==--=====++++++++*#%%%#+=+**
+*+**+++*++*+--=*################################################*=----=====+++++++++++++*######+*+*
*+=+=+*+*+*=--+#############+=+###########################**######========++++++++++=====+*#**+*=**+
**##*++***-==################+=*##**##*######*==*########*=-+#######*++++++++++++++======++****+++++
*+++*+*+*--=##########*+++++========#+==++=====+#########=--=+==+==--==++++++++++======+#*+**+***###
=**+=***-=+################+*###*=+##+==+###############==*######=-+####*++++++++===+++**##+++=====-
*+*+*+*--=#################+=*#*=*###+=-+#####*+#######=*#######*--=####**++++++++***+**++****+=+===
#++++*=-+#############***++========--=--=++=----=#####+##+=+++**+--=+=-=***++**++++**++===+*+-==+===
#*++#==-#####################+--#####+-=##+--############---+=*+==-:=++++++#*==*+***==+=+*+-:--====+
++**+--##################+++=--------=-+##+--############+-====-:--=--====+*=-==*#*--=+*+--:--==++++
**+*--+###################*+*---=+###=-+##+--##########========-=+*---#++++*====++++++++=-::-=++++++
++#==-####################=-----*=-+#--###*-=#########+========--===+++=+#%*++*+=-=+==+++==+++++==++
+**=-+###################=-+#=--+*-=+-*####-+########=========+*#*---+=====+++===+=-==+=++++++======
**+=:###################=+#*==--+##+-######=+#######===========-=+--=+====+++=-=+==========++======+
**=-=########################=--##==#######*=#######+=====-======+=======++==++===========++=====+++
+*=-*############################+#################*=====--====+=---===++=--=-=======--==++====+**=-
+*=-#######################==+#######-::*##########+---========---===+--==+=-==========--=====*#*==-
++==#######################=::=######:::*#########*=--==========--=++=-==+==============-----+#*=--*
++==#%%%###################=::+#####*::-+++=-:*##*+++++++========-++=-=++============+++=--=+**-==-=
-===#%%%%%%%%%%##+-:+#####*=::-*++*#*:::::::::+##***+++++========+#====**===========+**++=--+#----=+
----*%%%%%%%%#+---:=#####-*+:-=:=####::####*:-##*++*+++++++++++++*****+============+***+===+#*=-=+**
==----:----:---=-:-#%###--#=:=*-=####:=#####:-##==**+++==++++++++*##*==++======+==+****+=+*##+=+*#*+
---=============:=%%%%*::-#-:+*#####*-####*-::---++*+=-==++********+===++++===++=+****+++*###*##+=+*
--------======-:=%%%%%#=+##-:=:::---:---+*+-::::=***=-::--=********++++++==--===+*******#####*#++*##
-----------=--:*%%%%%%%%%%%=:-+#####-=#=*+####-=+*#+-:-::=+****#%%*+++++=--:--:=+**+++*#####%#+*###+
------------:=%%%%%%%%%%%%%=::+####*:###-=*##++*+*#+----=+=**+*%%*++**+=------:-+##+++*#####%#+*###+
------------------=+*#%%%%%%%=::+####*+###-=*##++*+*#+----=+=**+*%%*++**+=------:-+##+++*#####%#+*###+
"""
    print(ascii_art)