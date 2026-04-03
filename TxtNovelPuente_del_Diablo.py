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

def thinkblock(text):
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print('|                                                  In your Mind                                                             |')
    slow_print(f"|{text}")
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

def title_screen(): #It should named Puente DEl Diablo not DelCar.
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

#sc2 Materials
def sc2_Nun(user1):#done
    while True:
        if user1.lower() == 'yes':
            dialogue('You: '+ "Sister Jean, can I know something?")
            dialogue('Jean: '+ "Ara-ara, sure.")
            choices = input('About me/Chapel/Father/Thank you: ')
            if choices.lower() == 'about me':
                print('About me')
            elif choices.lower() == 'chapel':
                print('Chapel')
            elif choices.lower() == 'father':
                print('father')
            elif choices.lower() == 'thank you':
                print('your welcome')
                break
            else:
                dialogue("Jean" + "Speak up honey.")
        elif user1.lower() == 'no':
            dialogue('Jean: '+ "Are you sure dear?")
            l1 = input('Yes/No: ')
            if l1.lower() == 'yes':
                user1 = 'yes'
            elif l1.lower() == 'no':
                dialogue("Jean"+"Okay honey.")
                break
        else:
            user1 = input('Yes/No?: ')

def sc2_QuestionEnabell(user): #done
    while True:
        if user.lower() == 'yes':
            dialogue('You:' + 'Ena, can I ask something?')
            dialogue("Enabell:" + "What do you want to know?")
            choices1 = input('History / Suitors / the bridge / nevermind: ')
            if choices1.lower() == 'history':
                dialogue('Enabell: '"Our villiage is very old, full of secrets and life")
                dialogue('Enabell: ' + 'Just becareful Lara to whoever you choose.')
                narrate('You just nodded to her.')
            elif choices1.lower() == 'suitors':
                dialogue('Enabell: '+"Suitors? hahaha you have many. I envy that.")
                dialogue('You: '+"How? for me its a cruse. . . I just want to served god")
                narrate("You are shock, your mouth just move on its on.")
                t.sleep(2)
                dialogue('Enabell: '+"Not the crazy amount of your suitor. your resolve to serve our heavenly father.")
                narrate("A warm surge inside your body, conforting and just warm sensation. . .")
                narrate("You don't k n ow what to say.")
            elif choices1.lower() == 'the bridge':
                dialogue('Enabell: '+"Brigde?")
                dialogue('You: '+"Yes!! there's uncomplete bridge that I saw. .")
                dialogue('Enabell: '+"Well, there's no new brigde being constrcucted that I know off\n you probably dreaming again Lara.")
                narrate("Yet you still feel uneasy and grew warry.")
            elif choices1.lower() == 'nevermind':
                dialogue('Enabell:' + 'I cant really understand you sometimes')
                dialogue('Enabell:' + 'Anyway try this and shwo this to a priest')
                narrate("Enabell gave you paper, you peak inside and saw 'doton'.")
                dialogue('You: '+"The Priest? why?")
                narrate("Enabell just chuckle and wave her hand dismissively.")
                break
            else:
                dialogue("Enabell:" + "I can't hear you very well, speak up")
        elif user.lower() == 'no':
            narrate("You two continue to your journey, confident in what you have\n understood.")
            break

def check_item(inventory, target):
    """Check if item is in inventory. No 'in' keyword used."""
    index = False
    found = False
    while index < len(inventory):
        if inventory[index] == target:
            found = True
            index = len(inventory)   # early exit
        else:
            index = index + True
    return found

def hard_remove(inventory, target):
    """Return a new list with the first occurrence of target removed."""
    new_list = []
    index    = False
    while index < len(inventory):
        if inventory[index] != target:
            new_list.append(inventory[index])
        index = index + True
    return new_list

def show_inventory(inventory):
    """Print everything currently in the inventory."""
    print("\n--- Backpack ---")
    index = False
    while index < len(inventory):
        print("  - " + inventory[index])
        index = index + True
    if len(inventory) == False:
        print("  (empty)")
    print("----------------")


PAUSE = 2.0
SHORT = 1.0
LONG  = 3.0

# ── Timed countdown display ───────────────────────────────────────────────────
def timed_countdown(seconds):
    remaining = int(seconds)
    while remaining > False:
        print("  [" + str(remaining) + "]", end="\r", flush=True)
        t.sleep(SHORT)
        remaining = remaining - True
    print("     ", end="\r")

# ── Shown when player tries to leave too early ────────────────────────────────
def conviction_warning(reason):
    print()
    print("  +----------------------------------------------------------+")
    print("  |  !! " + reason)
    print("  +----------------------------------------------------------+")
    print()
    t.sleep(PAUSE)

# ── Confession booth riddle ───────────────────────────────────────────────────
# GATE: player must have events["has_lobby_hint"] == True before entering.
# RIDDLE answer is B (echo -- something that rings/repeats without a voice).
# REWARD: adds "bell_room_key" to inventory, sets events["found_bell_key"].
def puzzle_confession_booth(game_state):
    inventory = game_state["inventory"]
    events    = game_state["events"]

    print("\n" + "="*60)
    print("  The Confession Booth")
    print("="*60)
    narrate("You step inside. It smells of cedar and old paper.")
    narrate("A faded note is pinned beneath a small crucifix.")
    t.sleep(PAUSE)
    dialogue("Note: 'Only the one who listens to silence may open what rings above.'")
    t.sleep(PAUSE)
    narrate("Below the note is a wooden panel with three carved symbols:")
    print()
    print("      [ Dove ]        [ Bell ]        [ Book ]")
    print("      (  A  )         (  B  )         (  C  )")
    print()
    narrate("An inscription reads:")
    slow_print("    I speak without a mouth and hear without ears.", delay=0.04)
    slow_print("    I have no body, but I come alive with wind.", delay=0.04)
    slow_print("    What am I?", delay=0.04)
    print()

    solved   = False
    attempts = False        # False == 0

    while solved == False:
        print("\n  Attempts remaining: " + str(3 - attempts))
        print("  Enter A, B, or C.  You have 15 seconds.")
        print()
        start   = t.time()
        answer  = input("  Your answer: ").strip().upper()
        elapsed = t.time() - start

        if elapsed > 15:
            narrate("You hesitated too long. The panel resets.")
            attempts = attempts + True
        elif answer == "B":
            slow_print("  * The panel slides open with a soft click...", delay=0.05)
            t.sleep(PAUSE)
            narrate("Inside a hollow sits an old iron key. A tiny bell is etched on its head.")
            narrate("You obtained the Bell Room Key!")
            inventory.append("bell_room_key")
            events["found_bell_key"] = True
            solved = True
        else:
            narrate("Nothing happens. The panel holds firm.")
            attempts = attempts + True

        if solved == False:
            if attempts >= 3:
                narrate("The panel goes cold and locks itself.")
                dialogue("You: Maybe I need to think about this more carefully...")
                thinkblock("Lara: 'Listens to silence'... something about sound. What answers without a voice?")
                t.sleep(LONG)
                narrate("The panel warms again. You may try once more.")
                attempts = False    # reset

    game_state["inventory"] = inventory
    game_state["events"]    = events
    return game_state

# ── Bell room ─────────────────────────────────────────────────────────────────
# GATE: "bell_room_key" must be in inventory.
# SETS: events["bell_room_visited"] = True  <-- conviction gate checks this
#       events["bell_warned"]       = True  <-- sc3 can read this
# KEY is consumed on entry.
def room_bell_room(game_state):
    inventory = game_state["inventory"]
    events    = game_state["events"]

    print("\n" + "="*60)
    print("  The Bell Room")
    print("="*60)

    if check_item(inventory, "bell_room_key") == False:
        narrate("A heavy iron lock seals the door.")
        dialogue("You: I need a key for this. . .")
        thinkblock("Lara: Someone in the lobby mentioned a hidden key.")
        t.sleep(PAUSE)
        return game_state

    narrate("You insert the key into the lock.")
    slow_print("  * The lock turns...", delay=0.06)
    t.sleep(PAUSE)
    slow_print("  * The door groans open, revealing a narrow spiral staircase.", delay=0.04)
    t.sleep(PAUSE)
    narrate("You climb carefully. Each step creaks beneath your weight.")
    timed_countdown(LONG)

    print("\n" + "="*60)
    print("  At the Top  --  The Bell")
    print("="*60)
    narrate("A massive bronze bell hangs in the centre of the tower.")
    narrate("Afternoon light cuts through the slats in golden lines.")
    t.sleep(PAUSE)
    narrate("Carved into the base of the bell, barely visible under dust:")
    slow_print("  * 'He who rings me calls not the hour, but the truth.'", delay=0.06)
    print()
    t.sleep(PAUSE)
    dialogue("You: What does that mean... 'calls the truth'?")
    thinkblock("Lara: The bridge. The shadow. Father John's words. It is all connected...")
    t.sleep(PAUSE)
    narrate("A cold wind rushes through the slats -- but there is no storm outside.")
    narrate("The bell sways. Just slightly. Without anyone touching it.")
    t.sleep(LONG)
    dialogue("You: I need to leave. Now.")

    inventory = hard_remove(inventory, "bell_room_key")
    events["bell_room_visited"] = True
    events["bell_warned"]       = True

    game_state["inventory"] = inventory
    game_state["events"]    = events
    return game_state

# ── Basement ──────────────────────────────────────────────────────────────────
# GATE: events["bell_room_visited"] must be True.
# SETS: events["found_ledger_hint"] = True
def room_basement(game_state):
    events = game_state["events"]

    print("\n" + "="*60)
    print("  The Basement")
    print("="*60)

    if events.get("bell_room_visited", False) == False:
        narrate("A heavy wooden door blocks the stairwell. It will not budge.")
        thinkblock("Lara: I am not ready to go down there yet.")
        t.sleep(PAUSE)
        return game_state

    narrate("The basement door swings open -- as if it was never truly locked.")
    t.sleep(PAUSE)
    narrate("Cool, dark room. Stone shelves. The faint smell of incense.")
    narrate("One shelf holds a leather-bound ledger. The spine reads:")
    slow_print("    'Puente Del Diablo -- Construction Records, 1887'", delay=0.05)
    t.sleep(SHORT)
    dialogue("You: This is about the bridge!")
    t.sleep(PAUSE)
    narrate("You reach for it -- and the door above slams shut.")
    t.sleep(LONG)
    narrate("Footsteps. Someone walking across the floor above you.")
    t.sleep(PAUSE)
    narrate("You press yourself against the shelf. Heart hammering.")
    timed_countdown(PAUSE)
    narrate("Silence. They are gone.")
    dialogue("You: I should come back to this. Not now.")

    game_state["events"]["found_ledger_hint"] = True
    return game_state

# ── Lobby ─────────────────────────────────────────────────────────────────────
# The elderly woman NPC gives the hint that unlocks the confession booth.
# SETS: events["has_lobby_hint"] = True  (when player picks option 3)
def room_lobby(game_state):
    inventory = game_state["inventory"]
    events    = game_state["events"]

    print("\n" + "="*60)
    print("  The Church Lobby")
    print("="*60)
    narrate("Quiet. Soft light through stained glass. Candles flicker near the altar.")

    lobby_active = True
    while lobby_active == True:
        print()
        print("  1. Altar")
        print("  2. Sacristy door")
        print("  3. Talk to the people    <- hint is here")
        print("  4. Bulletin Board")
        print("  5. The Painting")
        print("  6. The Vase")
        print("  7. Go back")
        print()
        choice1 = input("  Your choice: ").strip()

        if choice1 == "1":
            narrate("You light a candle near the altar. The flame holds perfectly still.")
            thinkblock("Lara: The bell room is directly above this altar...")

        elif choice1 == "2":
            narrate("The sacristy door is ajar. Priests prepare for evening mass.")
            narrate("You decide not to disturb them.")

        elif choice1 == "3":
            narrate("An elderly woman in a blue shawl looks up at you with kind eyes.")
            dialogue("Elderly woman: Ah, you must be Lara. I have seen you with your auntie.")
            dialogue("You: Yes po. Do you know anything special about this church?")
            dialogue("Elderly woman: The bell above has not rung in forty years.")
            dialogue("Elderly woman: They say whoever unlocks that room will hear something meant only for them.")
            dialogue("You: How does one get up there?")
            t.sleep(SHORT)
            dialogue("Elderly woman: The key was hidden where people confess their sins.")
            dialogue("Elderly woman: But the booth does not simply give it up.")
            dialogue("Elderly woman: 'Only the one who listens to silence may open what rings above.'")
            dialogue("Elderly woman: Remember that, anak.")
            narrate("She turns back to her rosary.")
            events["has_lobby_hint"] = True
            thinkblock("Lara: 'Listens to silence...' -- I should check the confession booth.")
            t.sleep(SHORT)
            narrate("A young man beside her nods at you.")
            dialogue("Young man: Be careful in that bell room if you manage to get up there.")

        elif choice1 == "4":
            narrate("Among the flyers, one faded notice:")
            slow_print("    'Bell room access RESTRICTED. See Father John for inquiries.'", delay=0.04)
            thinkblock("Lara: Restricted. There must be something worth seeing up there.")

        elif choice1 == "5":
            narrate("A large painting depicts workers building a stone bridge -- clearly unfinished.")
            slow_print("    Plaque: 'Puente Del Diablo, c. 1887 -- Abandoned.'", delay=0.04)
            t.sleep(PAUSE)
            dialogue("You: This is the bridge. The same one from my vision. . .")
            events["saw_bridge_painting"] = True

        elif choice1 == "6":
            narrate("A tall ceramic vase holds fresh white sampaguita. The scent is calming.")
            if check_item(inventory, "Ceramic Vase") == False:
                take = input("\n  Take the Ceramic Vase? (yes/no): ").strip().lower()
                if take == "yes":
                    inventory.append("Ceramic Vase")
                    narrate("You carefully wrap the vase in your shawl.")
            else:
                narrate("You already have the vase.")

        elif choice1 == "7":
            lobby_active = False
        else:
            narrate("You pause, unsure what caught your attention.")

    game_state["inventory"] = inventory
    game_state["events"]    = events
    return game_state

# ── Roam_church (main hub) ────────────────────────────────────────────────────
# CONVICTION GATE: player cannot choose Leave (7) until bell_room_visited == True.
# Menu status tags update every loop so player always knows what step is next.
def Roam_church(user, game_state):
    events    = game_state["events"]
    inventory = game_state["inventory"]

    if user.strip().lower() == "no":
        dialogue("You: I think I have seen enough. I should head back to Enabell.")
        narrate("You feel you lack something. . .")
        if events.get("bell_room_visited", False) == False:
            conviction_warning("Something nags at you. You feel you are leaving something unfinished.")
            thinkblock("Lara: The old woman's words -- 'the bell above has not rung in forty years.'")
        return game_state

    narrate("You walk towards the bulletin board near the entrance.")
    dialogue("You: Hmm -- places I can look around!")

    User_Exploring = True
    conviction_met = False

    while User_Exploring == True:

        conviction_met = events.get("bell_room_visited", False)
        has_hint       = events.get("has_lobby_hint",    False)
        booth_done     = events.get("found_bell_key",    False)
        has_key        = check_item(inventory, "bell_room_key")

        # Status tags shown next to each locked option
        if booth_done == True:
            booth_tag = "[done]                                      |"
        elif has_hint == True:
            booth_tag = "[unlocked -- go try it!]                    |"
        else:
            booth_tag = "[locked -- talk to someone in lobby first]  |"

        if events.get("bell_room_visited", False) == True:
            bell_tag = "[done]                                       |"
        elif has_key == True:
            bell_tag = "[unlocked -- you have the key!]              |"
        else:
            bell_tag = "[locked -- need Bell Room Key]               |"

        if conviction_met == True:
            leave_tag = "[ready]                                      |"
        else:
            leave_tag = "[not yet -- visit the bell room first]       |"

        print()
        print("  +------------------------------------------------------------+")
        print("  |  Where do you go?                                          |")
        print("  |  1. Library                                                |")
        print("  |  2. Lobby                                                  |")
        print("  |  3. Basement                                               |")
        print("  |  4. Confession Booth  " + booth_tag +                     '|')
        print("  |  5. Bell Room         " + bell_tag +                      '|')
        print("  |  6. Check inventory                                        |")
        print("  |  7. Leave             " + leave_tag +                     '|')
        print("  +------------------------------------------------------------+")
        print()
        choice = input("  Your choice: ").strip()

        if choice == "1":
            narrate("Rows of religious texts and historical records stretch before you.")
            dialogue("You: Wow, this place is amazing!")
            t.sleep(PAUSE)
            narrate("You browse the shelves for anything about the bridge.")
            timed_countdown(PAUSE)
            narrate("You find a passage: an unfinished bridge built by monks, circa 1887.")
            dialogue("You: This must be the same bridge!")
            narrate("The pages explaining why it was abandoned are torn out.")
            dialogue("You: Of course they are. . .")
            thinkblock("Lara: The painting in the lobby and this book both say 1887. The basement ledger may have more.")
            events["read_library_book"] = True

        elif choice == "2":
            game_state["events"]    = events
            game_state["inventory"] = inventory
            game_state = room_lobby(game_state)
            events     = game_state["events"]
            inventory  = game_state["inventory"]

        elif choice == "3":
            game_state["events"]    = events
            game_state["inventory"] = inventory
            game_state = room_basement(game_state)
            events     = game_state["events"]
            inventory  = game_state["inventory"]

        elif choice == "4":
            if booth_done == True:
                narrate("You already retrieved the key. There is nothing more inside.")
            elif has_hint == False:
                narrate("You approach the booth, but stop yourself.")
                thinkblock("Lara: I feel like I am missing something. I should talk to someone first.")
                conviction_warning("You need more information before going in there.")
            else:
                game_state["events"]    = events
                game_state["inventory"] = inventory
                game_state = puzzle_confession_booth(game_state)
                events     = game_state["events"]
                inventory  = game_state["inventory"]

        elif choice == "5":
            game_state["events"]    = events
            game_state["inventory"] = inventory
            game_state = room_bell_room(game_state)
            events     = game_state["events"]
            inventory  = game_state["inventory"]

        elif choice == "6":
            show_inventory(inventory)

        elif choice == "7":
            if conviction_met == False:
                conviction_warning("You cannot bring yourself to leave yet.")
                if has_hint == False:
                    thinkblock("Lara: I have not spoken to anyone yet. I should check the lobby.")
                elif booth_done == False:
                    thinkblock("Lara: The old woman's words... I need to find the key in the confession booth.")
                elif has_key == True:
                    thinkblock("Lara: I have the key -- the bell room stairs are waiting.")
                else:
                    thinkblock("Lara: I still have not visited the bell room.")
                narrate("You stop yourself at the doorway and turn back.")
            else:
                slow_print("  * You take one last look at the church before stepping outside.", delay=0.04)
                t.sleep(PAUSE)
                dialogue("You: Goodbye, Father John. Sister Jean. Thank you.")
                narrate("You step into the fading afternoon light to find Enabell.")
                narrate("Whatever the bell whispered stays close -- like a second heartbeat.")
                User_Exploring = False
        else:
            narrate("You continue to think carefully about your options. . .")

    game_state["inventory"] = inventory
    game_state["events"]    = events
    return game_state
# // ______________________________________//
# ||              Story poper              ||
# // ______________________________________//

def Start(): # i will convert this in While loop since it bugs out when you type the other seletion lol
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
    
def Path_Exit():#done
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
            Close_Up()
        else:
            print("Invalid choice, please try again.")
        
def exit_():#done
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
        elif user.lower() == "happy newyear":
            New_Year2026()
        else:
            print("Invalid choice, please try again.")
            exit()
        
def main():#done
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

def sc1():#done
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
    narrate("You get up from the cozy feeling bed, and you see that you're\n in a small room with stone walls, dimly lit by a flickering candle on a wooden table.")
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
    thinkblock("You: " + "Wait, did I just said auntie? but i dont know her. . .")
    narrate("You follow your 'Aunite', and you find yourself in a cozy kitchen")
    narrate("As you enter the kitchen, you are greeted by the warm aroma of freshly cooked food, and the sight of a loving\n family gathered around the table, sharing a meal together.")
    dialogue("Auntie: " + "Lara, you want me to do this everyday for you aren't you? Gezz you should be grateful that you have\n a family that loves you, unlike your parents who left you alone in the world.")
    dialogue("You: " + "But i don't even know you, and i dont even know who my parents are. . .")
    dialogue("Middle-age man: " + "Hahaha you never disspoint us to enterain us Lara, you always have a good sense of humor, just like your father.")
    dialogue("Teenager girl: " + "Geez, you seem you worship so much our heavenly father that you fogot about us, but then,\n how can i blame ya? \neveryday you have suitor soo envious.")
    dialogue("Auntie: " + "Stop teasing her, Lara, come one have a seat and lets eat.")
    narrate("You sit down at the table, and stared at the delicious food \nthat your family had prepared.")
    thinkblock("You: " + "That middle-age man must the Uncle, and that \nteenager girl must be their child.")
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
    dialogue("You:" +"Why?")
    dialogue("Auntie:" + " Just say hi to our priest John. Enabell go with Lara")
    dialogue("Enabell:" + "But i have plan thi afternoon.")
    dialogue("Auntie: " + 'No buts Enabell.')
    narrate('Enabell relucntently agrred to go with you')
    narrate('You and Enebell set out of your house')
    narrate('You openned the door and a village thriving welcomes you')
    village()
    narrate("As you open the door, the Gentle breeze of afternoon brush to your skin. ")
    narrate("The Earthy scent of your coruing envelope your noustril.")
    narrate("You felt calm, restored and somewhat Familiar to this place as if. . .")
    dialogue("You: " + "Wow, I can see the whole village here.")
    dialogue("Enabell:" + "I can't get enough how beautiful our village are.")
    dialogue("This statement peak your interest once more, do you want to ask something?")
    user = input("Yes/No: ") 
    sc2_QuestionEnabell(user)
    narrate("As the both of you traverse your way down the hill you enter a forrest. ")
    narrate(" ")
    narrate(" ")
   #The Arriavl in the Village
    narrate("The Two of you quickly arrived in the village.")
    dialogue("You: " + 'The path was way too bumpy and long.')
    dialogue("Enabell:" + "have you not get used to it? hahahaha.")
    narrate("The two of you playfully teasing each other.")
    narrate("But as the two of you, make debut inside the vilage square.")
    narrate("It seems the village had froezen. ")
    narrate("Everyone gazzing towards the both of you.")
    dialogue("Enabell:" + "Everytime I'm with you, the world around us seems to stop \n just to glaze at you.")
    dialogue("You:" + "Well, that's what you get if we're fatefully serving him.")
    dialogue("Enabell:" + "Wow ms. Holy maiden.")
    dialogue("Male:" + "Umm, Ms. Lara have you received my affection Letter.")
    narrate("Soon Male sorroundes the two of you.")
    narrate("Desperately trying to get your attention with their advances.")
    narrate("You are like Field of flowers, under the swarm of bees of mens.")
    narrate("Someone grab your hand and yank you out of the swarm of men. ")
    dialogue('You:' + 'Puch who-.')
    dialogue('Enabell: '+ "Houyy, Geez come on now. Let's finish what my mother tasked us to finished. ")
    dialogue("The Group of men: "+"Where's Lara?? my lovess!!")
    dialogue('Group of Men:' + "There's she iss!! running!! away quickly.")
    narrate("With Enabell guidnace, the two of you swiftly outrun the swarm.")
    narrate("After endless of pursuit, the both of you outrun and hid in the side alley.")
    narrate("The both of you trying to grasp for air.")
    dialogue('Enabell: '+ "Lara, You should really hide your beauty hahaha.")
    dialogue('You: '+ "Shut up Ena, not funny.")
    dialogue('Enabell: '+ "Haha, I bet you do lets go and finish so we can go home. ")
    dialogue('You: '+ "True, its getting dark.")
    narrate('As the two of you arrived at church stede.')
    narrate('You felt cold wind welcomes you at the entrance of Church. ')
    dialogue('Enabell: '+ "Mom instruct me to buy some foods, so go alone inside the Church. ")
    dialogue('You: '+ "But. . . ")
    #The separation
    dialogue('Enabell: '+ "Dont worry, i'll swing by this church after I check my shopping list.")
    narrate("Enabell departs and you continue inside the church")
    narrate("You enter the chruch. you are welcome by few people of different across ages and gender,\n solomeny praying. ")
    narrate("You walk beside the altar, and a nun approaches you.")
    dialogue("Nun:" + 'Hi Lora, how are you?')
    dialogue('You: '+"I'm doing fine sister, me and Anabell just outrun my suitors.\n how about you sister?")
    dialogue('Nun: '+ "As usual are we? hahaha.")
    dialogue('You: '+ "Sister, may I know where's Father")
    dialogue('Nun: '+ "ohh my, another session?.")
    dialogue('You: '+ "My mother told me to find him.")
    dialogue('Nun: '+ "He's inside, of the usual office, I will accompanny you. ")
    narrate("You thanked her, and introduce herself as Jean.")
    narrate('As the both of you walk the silent corridor.')
    dialogue('Nun: '+ "Have any question before we arrived?")
    user1 = input("Yes/No: ")
    sc2_Nun(user1)
    narrate("As you and Sister Jean continue walking, you can't help but feel a sense of unease, as if something is lurking in the shadows, watching your every move...")
    dialogue('You: ' + "Sister Jean, do you feel like we're being watched?")
    dialogue('Jean: ' + "Oh, don't be silly, it's just your imagination.")
    narrate("But the feeling of being watched only grows stronger, and you can't shake\n the sense of dread that something is waiting for you in the darkness...")
    narrate('You and Sister Jean finally arrive at the office, and you see Father John sitting at his desk, surrounded by books and papers.')
   #Father dialogs
    dialogue('Father John: ' + "Ah, Lara, it's good to see you. What brings you here today?")
    dialogue('You: ' + "Father John, my mother sent me to find you. She said you might be able to help me with something.")
    dialogue('Father John: ' + "Of course, I'm here to help. What do you need?")
    dialogue('You: ' + "I... I don't know how to say this, but I feel like there's something wrong with me. Like I'm not myself anymore.")
    dialogue('Father John: ' + "I see. With your god given beauty, it's not suprising that you have many suitors.\n Are you perhaps turing into Age?")
    dialogue('You: ' + "Why did you asked father?")
    dialogue('Father John: ' + "Well, it's just that, you know, there's a legend a long time ago. . .")
    narrate("The Father seems a bit hesistant to say the legend, but still continue to tell you the story. . .")
    dialogue('Father John: ' + "The legend says that, there was a beautiful maiden who lived in this village long time ago, and she was so beautiful that") 
             #many suitors came to court her, but she was very devout and wanted to serve God, so she rejected all of them. One day, a mysterious figure appeared to her and offered her a deal. He said that if she agreed to be with him, he would give her eternal beauty and youth, but if she refused, he would curse her and her descendants to be forever alone and unloved.")
    dialogue('Father John: ' + "Many suitors came to court her, but she was very devout and wanted to serve God, so she rejected all of them.")
    dialogue('Father John: ' + "That's the Story of our Patron Catherine. She devoted her life under servetude to our heavenly Father.")
    dialogue('You: ' + "So, whats the connection with me and the Legend?")
    dialogue('Father John: ' + "Well, Lara. Accroding to the scripture, A women that devoted her life solely to God, will be under constant eyes of devil,\n trying to lure thy soul to earthly pleasure, this is like a trial for the soul, to test your resolve and devotion to our heavenly Father.")
    dialogue('Father John: ' + "Knowing you possesd unbound beauty and Servitude for our heavenly Father, it;s not suprising that demons are trying to lure you.\n be resilinece to whoever you choose to spend your life with.")
    dialogue('You: ' + "So, what should I do Father?")
    dialogue('Fayther John: ' + 'Well, Lara, You have to follow your heart, becasue only you with the guide of heavenly will, can choose what best for you.')
    dialogue('Father John: ' + 'anway feel free to ask me anything else, or if you need help with anything else, I am here to help you.')
    dialogue('You: ' + "Thank you Father, I will keep that in mind.")
    dialogue('Father John: ' + "You're Welcome Lara, Feel free to roam around as I will discuss something with Sister Jean.")
    user2 = input("Do you want to roam around the church? (yes/no): ") # Roam spot =
    Roam_church(user2)
    game_state = Roam_church(user2, game_state)
    t.sleep(delay)
    sc3()


def sc3(): # dont forget to use While loop at choices lol
    chapter_banner(3, "Lara's Bargain") #The night when the devil in disquise try to take Lara as his bride.+ the bidge dairing construction before the sunrise.
    narrate("As the sun falls and  the night creeps in. you and Enabell arrived home safely")
    pause()
    narrate( 'As the two of you enter the house, you are greated by the warm aroma of home-cooked food.')
    narrate("you helped Enabell to set her shopping bags down, and you both start to prepare dinner together.")
    dialogue("Enabell: " + "Lara, I know you don't like to eat with us, but can you at least stay for dinner?")
    user3 = input("Do you want to stay for dinner? (yes/no): ")
    if user3 == "yes":
        narrate("You decide to stay for dinner and enjoy a delicious meal with Enabell.")
    else:
        narrate("You politely decline the invitation and head to your room.")
    narrate("As you eat, you can't help but feel a sense of unease, as if something is lurking in the shadows, watching your every move...")
    narrate("Then, the silence is broken by a suddned knock on the main door.")
    dialogue('You: ' + "Who could that be at this hour?")
    
    progress_saved()
    
    
def sc4():# dont forget to use While loop at choices lol
    chapter_banner(4, "The Final Revelation")
    pause()
    progress_saved()
    
    
def final():# dont forget to use While loop at choices lol
    chapter_banner("Final", "The Bridge's Secret")
    pause()

    progress_saved()
    delay = 2
    
    

    
# /// Secret ///
def kiss():
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
    
def village():#done of using for demonstation of village.
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
    
def Doton():#done for sc2 interaction with enabell
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

def THE_author():
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

def New_Year2026(): #Done
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

def Close_Up(): #Done
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
    

if __name__ == "__main__": # Reminder to excecute everythin this thing should be at the very last line of the code lol or else oit wouldnt get called.
   sc2()