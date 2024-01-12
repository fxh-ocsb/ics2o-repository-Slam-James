# NAME OF AUTHOR: Isaac Beaupre
# NAME OF THE PROGRAM: RST - HeroQuest
# DATE OF CREATION: June 15, 2023
# PURPOSE OF PROGRAM: Make the user enjoys a fun adventure game!

# Setup
from pygame import mixer
import random
yes_no = ["yes", "no"]
directions = ["left", "right", "forward"]
charge_defend = ["charge", "defend"]

# Music
mixer.init() # Instantiate mixer

mixer.music.load('AdventureMusic.mp3') # Load audio file

mixer.music.set_volume(1) # Volume

mixer.music.play() # Play the music

#Rules
print("This is a text based game. Make sure you type in one of the options provided with no spelling mistakes or capitals. Exception - when the program asks for your name.")

# Introduction
name = input("What is your name, adventurer?\n")
print("Greetings, " + name + ". Let us go on a quest!")
print("You find yourself waking up on the edge of a dark forest equipped with some armour and a sword. You then remember you are a knight who was part of a battalion that was wiped out by an army of barbarians.")
print("You realized you were given a crucial quest of warning your kingdom about the brutal barbarians attacking. The fate of the land depends on you!")
print("Can you be the hero of this story?\n")
 
# Start of game
Timer = 0
HasLegendarySword = "False"
LeaderIsDead = "False"
response = ""
while response not in yes_no:
    response = input("Would you like to step into the forest?\nyes/no\n")
    if response == "yes":
        print("You head into the forest. You hear wolves howling in the distance.\n")
    elif response == "no":
        print("You decide that you are not ready for this quest and you wonder why you must be the hero of this story. Before you can react a giant tree falls on your face crushing your skull.\nYou were too lazy to be a hero. This story ends here.")
        quit()
    else:
        print("That is an invalid response. Make sure you check for spelling mistakes and no capitals when writing.\n")
 
# Next part of game (Area with choices)
response = ""
while response not in directions:
    print("To your left, you see a bear blocking the path to the fastest route back to your kingdom.")
    print("To your right, there is more forest.")
    print("There is a rock wall directly in front of you.\n")
    response = input("What direction do you move?\nleft/right/forward\n")
    if response == "left":
        Timer = Timer + 1
        print("Somehow you were foolish enough to walk directly towards a bear, but warning everyone you love is of utmost importance and getting there as fast as you can seems to be your only choice.")
        print("The bear notices you immediately. You have no choice but to fight.\n")
        response1 = ""
        while response1 not in charge_defend:
            response1 = input("Would you like to charge or defend against this enemy?\ncharge/defend\n")
            if response1 == "charge":
                WinOrLose = random.randint(1,2)
                if WinOrLose == 2:
                    print("You decide to run right at the bear with no fear and stab the it repeatedly slaughtering the bear!\n")
                    BearIsDead = "True"
                elif WinOrLose != 2:
                    print("You decide to run right at the bear. The bear tore you into a thousand shreds...\nYou failed your quest. This story ends here.")
                    quit()
            elif response1 == "defend":
                WinOrLose = random.randint(1,4)
                if WinOrLose == 2:
                    print("You decide to defend yourself against the bear blocking and dodging each attack. You strike the bear when is is weak form exhaustion killing is successfully!\n")
                    BearIsDead = "True"
                elif WinOrLose != 2:
                    print("You try to defend against the bear, however it is too strong and too fast. The bear rips you apart...\nYou failed your quest. This story ends here.")
                    quit()
            else:
                print("That is a invalid response. Make sure you check for spelling mistakes and no capitals when writing.\n")
    elif response == "right":
        Timer = Timer + 1
        print("You head deeper into the forest deciding to avoid the dangerous bear.\n")
    elif response == "forward":
        print("You cannot scale the wall.\n")
        response = ""
    else:
        print("That is an invalid response. Make sure you check for spelling mistakes and no capitals when writing.\n")

# Next part of game (Another area with choices)
if response == "right":
    response2 = ""
    while response2 not in directions:
        print('You see a message carved on the trunk of a dead tree. It reads, "L, F, R" Who knows what it could mean?')
        print("To your left, you see a cliff.")
        print("To your right, you see a path that leads deeper into the forest.")
        print("In front of you see a very large field.\n")
        response2 = input("What direction do you move?\nleft/right/forward\n")
        if response2 == "left":
            print("You head left towards the cliff. As you arrive you look down and realize falling down this cliff means certain death. All of a sudden, you feel someone shove you. Before you know it, you are falling down a deep pit. You reflect on your life choices and then SPLAT!\nYou failed your quest. This story ends here.")
            quit()
        elif response2 == "right":
            print("You follow the path that leads you deeper into the forest. After some time you find yourself getting shorter. You look down and realize you are in quicksand. Your armour is too heavy which prevents you from escaping. You accept your fate.\nYou failed your quest. This story ends here.")
            quit()
        elif response2 == "forward":
            Timer = Timer + 1
            print("You walk into the field. You appear to be lost because there seems to be an endless plain around you.")
            InField = 1
        else:
            print("That is an invalid response. Make sure you check for spelling mistakes and no capitals when writing.\n")
    while InField == 1:
        CorrectDirection = 0
        HasMovedRight = "False"
        HasMovedLeft = "False"
        HasMovedForward = "False"
        HasMovedLeftTwice = "False"
        Counter = 0
        while CorrectDirection != 3:
            response3 = input("What direction do you move?\nleft/right/forward\n")
            if response3 == "right":
                Timer = Timer + 1
                if HasMovedLeft == "True" and HasMovedForward == "True":
                    CorrectDirection = CorrectDirection + 1
                    response3 == ""
                else:
                    print("You head right. You are still lost in the field.\n")
                    CorrectDirection = 0
                    HasMovedLeft = "False"
                    HasMovedForward = "False"
            elif response3 == "left":
                Timer = Timer + 1
                print("You head left. You are still lost in the field.\n")
                Counter = Counter + 1
                if HasMovedLeft == "False":
                    CorrectDirection = CorrectDirection + 1
                    HasMovedLeft = "True"
            elif response3 == "forward":
                Timer = Timer + 1
                print("You head forward. You are still lost in the field.\n")
                if HasMovedLeft == "True" and HasMovedRight == "False":
                    HasMovedForward = "True"
                    if Counter <= 1:
                        CorrectDirection = CorrectDirection + 1
                else:
                    CorrectDirection = 0
                    HasMovedLeft = "False"
                    HasMovedRight = "False"
            else:
                print("That is an invalid response. Make sure you check for spelling mistakes and no capitals when writing.\n")
        InField = 2
        BearIsDead = "False"
    print("You find your way out of the field and continue on your journey!\n")
    NextArea = "True"

# Next part of game (Another area with choices)
if response  == "left" or NextArea == "True":
    if BearIsDead == "True":
        print("After defeating the bear in combat, you continue to pursue your quest. Some time passes and you find yourself on top of a hill.\n")
    else:
        print("After some time you find yourself on top of a hill.\n")
    response = ""
    while response not in directions:
        print("To your left, you an entrance to a cave.")
        print("To your right, you see smoke.")
        print("The path to your kingdom is directly in front of you.")
        response = input("What direction do you move?\nleft/right/forward\n")
        if response == "left":
            Timer = Timer + 1
            print("You head into the cave, realizing it was a lot more scary and dark than you thought.\n")
            InCave = "True"
        elif response == "right":
            print("You go towards the smoke walking right into a barbarian outpost. They spot you and before you know it, over an army of 100 barbarians are charging you and surrounding you. The barbarians slaughter you...\nYou failed your quest. This story ends here.\n")
            quit()
        elif response == "forward":
            Timer = Timer + 1
            print("You decide to take the fastest route back to your kingdom. While making your way along the path, you encounter a barbarian scout! Prepare to fight!\n")
            response1 = ""
            while response1 not in charge_defend:
                response1 = input("Would you like to charge or defend against this enemy?\ncharge/defend\n")
                if response1 == "charge":
                    WinOrLose = random.randint(1,4)
                    if WinOrLose == 2:
                        print("You decide to charge at the barbarian! Before he can react, you cut him with your sword in several places. The barbarian is dead. You continue your way along the path to warn your kingdom.\n")
                        InCave = "False"
                        SkeletonsAreDead = "False"
                        BarbarianScoutIsDead = "True"
                    elif WinOrLose != 2:
                        print("You decide to charge at the barbarian! However, he swings his massive club knocking you right into the head and crushing your skull...\nYou failed your quest. This story ends here.\n")
                        quit()
                elif response1 == "defend":
                    WinOrLose = random.randint(1,4)
                    if WinOrLose <= 3:
                        print("You decide to defend yourself against the barbarian. The barbarian charges at you and swings his massive club. You successfully parry his attack and inflict a heavy blow with your sword. The barbarian is dead.\nYou continue your way along the path to warn your kingdom.\n")
                        InCave = "False"
                        SkeletonsAreDead = "False"
                        BarbarianScoutIsDead = "True"
                    elif WinOrLose == 4:
                        print("You try to defend against the barbarian, however he is too strong. He clubs you repeatedly until you're dead. You failed your quest. This story ends here.")
                        quit()
        else:
            print("That is an invalid response. Make sure you check for spelling mistakes and no capitals when writing.\n")

# Next part of game (Another area with choices)
if InCave == "True":
    print("Inside the cave you see different pathways.")
    response = ""
    while response not in directions:
        print("A large pile of rocks blocks your way to the left.")
        print("To your right, you see light.")
        print("In front of you, you see a tunnel that leads deeper into the cave.")
        response = input("What direction do you move?\nleft/right\n")
        if response == "left":
            print("You cannot go this way. A large pile of rocks block your path.\n")
            response = ""
        elif response == "right":
            Timer = Timer + 1
            print("You decide to follow the light and hope for the best. As the light gets brighter, you see a legendary sword stuck in a stone.\nBefore you can investigate, a horde of undead skeletons emerge. They seem to be clumsy and weak, however they can easily kill you in numbers. They block all exits surrounding you. You need to fight!\n")
            response1 = ""
            while response1 not in charge_defend:
                response1 = input("Would you like to charge or defend against these enemies?\ncharge/defend\n")
                if response1 == "charge":
                    WinOrLose = random.randint(1,1)
                    if WinOrLose == 1:
                        print("You decide to strike first charging at the skeletons taking them down one at a time! They are too clumsy to attack. After hacking and slashing with your sword for about 10 minutes, the entire horde of skeletons are in pieces.\n")
                        SkeletonsAreDead = "True"
                elif response1 == "defend":
                    WinOrLose = random.randint(1,1)
                    if WinOrLose != 0:
                        print("You stand your ground but the horde of skeletons slowly surround and enclose on your position. You parry some attacks and block others, however there are too many skeletons around you. They start to stab and cut you! You slowly fall to the ground. You lose too much blood to stand back up, rendering you vulnerable...\nYou failed your quest. This story ends here.\n")
                        quit()
        elif response == "forward":
            Timer = Timer + 1
            print("You go deeper into the cave following multiple strands of tunnels. After wandering around aimlessly, you recognize many webs all around you. All of a sudden a giant spider as big as an elephant jumps out. You must fight for your life!\n")
            response1 = ""
            while response1 not in charge_defend:
                response1 = input("Would you like to charge or defend against this enemy?\ncharge/defend\n")
                if response1 == "charge":
                    WinOrLose = random.randint(1,1)
                    if WinOrLose != 0:
                        print("You decide to charge at the spider! However, you were too stupid to realize that there were spider webs everywhere. After a few seconds, you find yourself caught in a sticky spider web. The spider bites you, injecting poison into your body. Your body feels weaker as time passes until you rot away...\nYou failed your quest. This story ends here.\n")
                        quit()
                elif response1 == "defend":
                    WinOrLose = random.randint(1,1)
                    if WinOrLose == 1:
                        print("You take your time focusing your skills to dodge the spider at any time. The spider lunges at you and you easily dodge the attack! The spider goes flying into an underground river, drowning to death.\n You make the decision to follow the underground river. Surprisingly it leads you out of the cave and directly towards your kingdom.")
                        SpiderIsDead = "True"
        else:
            print("That is an invalid response. Make sure you check for spelling mistakes and no capitals when writing.\n")

# Next part of game (Another area with choices)
if SkeletonsAreDead == "True":
    print("After defeating all the skeletons you investigate the legendary sword stuck in a large smooth stone. You also realize the exit of the cave which directly leads you back to your kingdom. You could try to pull the legendary sword out of the stone, however this may take some time, and you may not be able to warn you kingdom in time.\n")
    response = ""
    while response not in yes_no:
        response = input("Would you like to attempt to pull the legendary sword out of the stone? \nyes/no\n")
        if response == "yes":
            Timer = Timer + 1
            Successful = random.randint(1,3)
            if Successful == 2:
                print("You successfully pull the legendary sword out of the stone!\n")
                HasLegendarySword = "True"
            elif Successful != 2:
                print("You failed to pull the sword out of the stone. Should you try again or not waste anymore time?\n")
                response = ""
                HasTried = "True"
        elif response == "no":
            print("You decide there is no time to waste and head directly towards your kingdom.\n")
            HasLegendarySword = "False"
        else:
            print("That is an invalid response. Make sure you check for spelling mistakes and no capitals when writing.\n")

# Next part of game (Another area with a choice)
if Timer < 9:
    response = ""
    while response not in yes_no:
        print("You have finally made it to your kingdom.\n")
        response = input("Would you like to warn the King immediately?\nyes/no\n")
        if response == "yes":
            print("You barge in the King's throne room wasting no time. You warn him of the barbarian army and explain we need to defend ourselves immediately. The King listens to you and prepares the defences. He says that the barbarians must have some sort of leader and gives you a new quest of defeating him. You prepare for war.\n")
        elif response == "no":
            print("You decide that you deserve some time to relax and catch your breath. You sit down and reflect upon how far you came. Then all of a sudden you hear the sound of a bow and arrow. You look in the direction of the noise and HEADSHOT! It was probably a barbarian scout who fired the arrow. The arrow hits you right in the brain and you drop dead...\nYou were too lazy to be a hero and failed your quest. This story ends here.")
            quit()
        else:
            print("That is an invalid response. Make sure you check for spelling mistakes and no capitals when writing.\n")
elif Timer >= 9:
    print("As you continue on your journey you see your kingdom being burned down into flames. You were too late to warn your kingdom. Before you can process that everyone you loved is now dead, a barbarian stabs you...\nYou failed your quest. This story ends here.")
    quit()

# Dialogue
print("You now stand on the front lines waiting for the barbarians to arrive. As you wait you hear someone shout. You look forward and you see the massive army of bloodthirsty barbarians charging. Before you know it you are standing right in the middle of the battle. You spot out the leader of the barbarians. The leader seems to be the largest barbarian and wields an enormous club. Without a second thought you challenge him!\n")

mixer.init() # Instantiate mixer
mixer.music.load('BossFightMusic.mp3') # Load audio file
mixer.music.set_volume(1) # Volume
mixer.music.play() # Play the music
response = ""
response1 = ""
# Next part of game (The boss battle with legendary sword)
if HasLegendarySword == "True":
    print("You pull out your legendary sword you found.\n")
    while response1 not in charge_defend:
        response1 = input("Would you like to charge or defend against this enemy?\ncharge/defend\n")
        if response1 == "charge":
            WinOrLose = random.randint(1,1)
            if WinOrLose == 1:
                print("You decide to charge at the leader. Wielding the legendary blade, you feel faster and stronger. He swings his massive club meeting your sword. You think about all the people you love and how your life has come down to this moment. With your legendary sword you blow right through his club and decapitate him. The barbarian leader is dead.\n")
                LeaderIsDead = "True"
        elif response1 == "defend":
            WinOrLose = random.randint(1,1)
            if WinOrLose == 1:
                print("You decide to wait for the leader to make the first move. Wielding the legendary blade, you feel more precise and focused. The leader runs at you with his enormous club swinging it like a wild animal. You easily parry and dodge his attacks. He winds up to try and hit you one more time. You think about all the people you love and how your life has come down to this moment. Before he swings you stab him right in the heart with your legendary sword. The barbarian leader is dead.\n")
                LeaderIsDead = "True"
    else:
        print("That is an invalid response. Make sure you check for spelling mistakes and no capitals when writing.\n")

# Next part of game (The boss battle - Part 1)
if HasLegendarySword == "False":
        while response1 not in charge_defend:
            LeaderIsDead = "False"
            response1 = input("Would you like to charge or defend against this enemy?\ncharge/defend\n")
            if response1 == "charge":
                WinOrLose = random.randint(1,1)
                if WinOrLose != 0:
                    print("You make the first move and decide to charge at the leader. By the time you are near him, he bashes you with his enormous club crushing every bone in your body...\nYou failed your quest. This story ends here.")
                    quit()
            elif response1 == "defend":
                WinOrLose = random.randint(1,1)
                if WinOrLose == 1:
                    print("You decide to wait for the leader to make the first move. The leader runs at you with his enormous club swinging it like a wild animal. You use your agility and dodge every attack causing the leader to be off balance. You realize this is your opportunity to strike. You make several cuts on his right arm.\nWhat is your next move?\n")
            else:
                print("That is an invalid response. Make sure you check for spelling mistakes and no capitals when writing.\n")
response = ""
response1 = ""
# Next part of game (The boss battle - Part 2)
if LeaderIsDead == "False":
    while response1 not in charge_defend:
        LeaderIsDead = "False"
        response1 = input("Would you like to charge or defend against this enemy?\ncharge/defend\n")
        if response1 == "charge":
            WinOrLose = random.randint(1,1)
            if WinOrLose != 0:
                print("You charge the leader thinking he is a little weaker due to the wounds you inflicted earlier. By the time you are near him, he finds the strength to swing the club bashing you brains out of your head...\nYou failed your quest. This story ends here.")
                quit()
        elif response1 == "defend":
            WinOrLose = random.randint(1,1)
            if WinOrLose == 1:
                print("You decide to again wait for the leader to charge at you. He seems a little weaker after attacking his right arm. The leader is to hasty and charges you like a fool. You once again dodge his attack using your agility. This time you inflict several flesh wounds and deliver a massive blow to his leg.\nWhat is your next move?\n")
        else:
            print("That is an invalid response. Make sure you check for spelling mistakes and no capitals when writing.\n")
response = ""
response1 = ""
# Next part of game (The boss battle - Part 3)
if LeaderIsDead == "False":
    while response1 not in charge_defend:
        LeaderIsDead = "False"
        response1 = input("Would you like to charge or defend against this enemy?\ncharge/defend\n")
        if response1 == "charge":
            WinOrLose = random.randint(1,1)
            if WinOrLose == 1:
                print("The barbarian seems to be too weak to stand. You decide to charge at him, not letting him have any chance to react. He grabs a random blade to throw at you, however it is already too late and you stab him right in the heart. The barbarian leader dies on the spot. letting him have no chance make the first move and decide to charge at the leader.\n")
                LeaderIsDead = "True"
        elif response1 == "defend":
            WinOrLose = random.randint(1,1)
            if WinOrLose != 0:
                print("You decide to wait once again waiting for the leader to make the first move. He seems to be too weak to stand. For a few seconds you let your guard down. Before you can react, he throws a blade directly at you. It pierces right through your heart...\nYou failed your quest. This story ends here.")
                quit()
        else:
            print("That is an invalid response. Make sure you check for spelling mistakes and no capitals when writing.\n")

# Outro
if LeaderIsDead == "True":
    print("You defeated the barbarian leader! All the other barbarians fear you and without a leader, they all become cowards and retreat! As you return back to inform everyone about the victory against the barbarians, you see everyone cheering for you! The King throws you a parade and invites you to a feast. Congratulations! You completed your quest and became the hero of this story!\n")
    print("Farewell, " + name + ".")