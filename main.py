from win32 import win32gui
import win32ui
import time


def League_Running():
    
    if win32ui.FindWindow(None, "League of Legends (TM) Client"):
        return True
    
    else:
        print("Client window not found")
        return False
   
flashtimer = 5
barriertimer = 180
healtimer = 240
teleporttimer = 340
ignitetimer = 180
cleansetimer = 210

summtimer1 = 0
summtimer2 = 0
summtimer3 = 0
summtimer4 = 0
summtimer5 = 0
summtimer6 = 0

Spell1 = None
Spell2 = None
Spell3 = None
Spell4 = None
Spell5 = None
Spell6 = None

Role1 = None
Role2 = None
Role3 = None
Role4 = None
Role5 = None
Role6 = None

oneclosed = False
twoclosed = False
threeclosed = False
fourclosed = False
fiveclosed = False
sixclosed = False

timer1 = 0
timer2 = 0
timer3 = 0
timer4 = 0
timer5 = 0
timer6 = 0

while League_Running():

    if not oneclosed or timer1 >= timer1 + summtimer1:
        summtimer1 = None
        linenumber = {4}
        for i, row in enumerate(open(r'C:\Riot Games\League of Legends\MyNotes.txt', "r")):
            if i in linenumber:

                if "-f" in str(row):
                    summtimer1 = flashtimer
                    Spell1 = "FLASH"
                    if "adc" in str(row):
                        Role1 = "ADC"
                        timer1 = time.time()
                        print("ADC FLASH DOWN")
                        oneclosed = True
                    elif "supp" in str(row):
                        Role1 = "SUPPORT"
                        timer1 = time.time()
                    elif "jg" in str(row):
                        Role1 = "JUNGLE"
                        timer1 = time.time()
                    elif "mid" in str(row):
                        Role1 = "MID"
                        timer1 = time.time()
                    elif "top" in str(row):
                        Role1 = "TOP"
                        timer1 = time.time()
                    else:
                        print("Something went wrong at 1 ROLEASSINGMENT, or invalid input.")
                elif "-b" in str(row):
                    summtimer1 = barriertimer
                    Spell1 = "BARRIER"
                    if "adc" in str(row):
                        Role1 = "ADC"
                        timer1 = time.time()
                    elif "supp" in str(row):
                        Role1 = "SUPPORT"
                        timer1 = time.time()
                    elif "jg" in str(row):
                        Role1 = "JUNGLE"
                        timer1 = time.time()
                    elif "mid" in str(row):
                        Role1 = "MID"
                        timer1 = time.time()
                    elif "top" in str(row):
                        Role1 = "TOP"
                        timer1 = time.time()
                    else:
                        print("Something went wrong at 1 ROLEASSINGMENT, or invalid input.")
                elif "-h" in str(row):
                    summtimer1 = healtimer
                    Spell1 = "HEAL"
                    if "adc" in str(row):
                        Role1 = "ADC"
                        timer1 = time.time()
                    elif "supp" in str(row):
                        Role1 = "SUPPORT"
                        timer1 = time.time()
                    elif "jg" in str(row):
                        Role1 = "JUNGLE"
                        timer1 = time.time()
                    elif "mid" in str(row):
                        Role1 = "MID"
                        timer1 = time.time()
                    elif "top" in str(row):
                        Role1 = "TOP"
                        timer1 = time.time()
                    else:
                        print("Something went wrong at 1 ROLEASSINGMENT, or invalid input.")
                elif "-t" in str(row):
                    summtimer1 = teleporttimer
                    Spell1 = "TELEPORT"
                    if "adc" in str(row):
                        Role1 = "ADC"
                        timer1 = time.time()
                    elif "supp" in str(row):
                        Role1 = "SUPPORT"
                        timer1 = time.time()
                    elif "jg" in str(row):
                        Role1 = "JUNGLE"
                        timer1 = time.time()
                    elif "mid" in str(row):
                        Role1 = "MID"
                        timer1 = time.time()
                    elif "top" in str(row):
                        Role1 = "TOP"
                        timer1 = time.time()
                    else:
                        print("Something went wrong at 1 ROLEASSINGMENT, or invalid input.")
                elif "-i" in str(row):
                    summtimer1 = ignitetimer
                    Spell1 = "Ignite"
                    if "adc" in str(row):
                        Role1 = "ADC"
                        timer1 = time.time()
                    elif "supp" in str(row):
                        Role1 = "SUPPORT"
                        timer1 = time.time()
                    elif "jg" in str(row):
                        Role1 = "JUNGLE"
                        timer1 = time.time()
                    elif "mid" in str(row):
                        Role1 = "MID"
                        timer1 = time.time()
                    elif "top" in str(row):
                        Role1 = "TOP"
                        timer1 = time.time()
                    else:
                        print("Something went wrong at 1 ROLEASSINGMENT, or invalid input.")
                elif "-c" in str(row):
                    summtimer1 = cleansetimer
                    Spell1 = "CLEANSE"
                    if "adc" in str(row):
                        Role1 = "ADC"
                        timer1 = time.time()
                    elif "supp" in str(row):
                        Role1 = "SUPPORT"
                        timer1 = time.time()
                    elif "jg" in str(row):
                        Role1 = "JUNGLE"
                        timer1 = time.time()
                    elif "mid" in str(row):
                        Role1 = "MID"
                        timer1 = time.time()
                    elif "top" in str(row):
                        Role1 = "TOP"
                        timer1 = time.time()
                    else:
                        print("Something went wrong at 1 ROLEASSINGMENT, or invalid input.")
                else:
                    print("Something went wrong at summtimer1 assignment, or there was invalid input")



    elif not twoclosed:
        linenumber = {5}
        for i, row in enumerate(open(r'C:\Riot Games\League of Legends\MyNotes.txt', "r")):
            if i in linenumber:
                if "-f" in str(row):
                    summtimer2 = flashtimer
                    Spell2 = "FLASH"
                    if "adc" in str(row):
                        Role2 = "ADC"
                        timer2 = time.time()
                        print("ADC FLASH DOWN")
                        twoclosed = True
                    elif "supp" in str(row):
                        Role2 = "SUPPORT"
                        timer2 = time.time()
                    elif "jg" in str(row):
                        Role2 = "JUNGLE"
                        timer2 = time.time()
                    elif "mid" in str(row):
                        Role2 = "MID"
                        timer2 = time.time()
                    elif "top" in str(row):
                        Role2 = "TOP"
                        timer2 = time.time()
                    else:
                        print("Something went wrong at 2 ROLEASSINGMENT, or invalid input.")
                elif "-b" in str(row):
                    summtimer2 = barriertimer
                    Spell2 = "BARRIER"
                    if "adc" in str(row):
                        Role2 = "ADC"
                        timer2 = time.time()
                    elif "supp" in str(row):
                        Role2 = "SUPPORT"
                        timer2 = time.time()
                    elif "jg" in str(row):
                        Role2 = "JUNGLE"
                        timer2 = time.time()
                    elif "mid" in str(row):
                        Role2 = "MID"
                        timer2 = time.time()
                    elif "top" in str(row):
                        Role2 = "TOP"
                        timer2 = time.time()
                    else:
                        print("Something went wrong at 2 ROLEASSINGMENT, or invalid input.")
                elif "-h" in str(row):
                    summtimer2 = healtimer
                    Spell2 = "HEAL"
                    if "adc" in str(row):
                        Role2 = "ADC"
                        timer2 = time.time()
                    elif "supp" in str(row):
                        Role2 = "SUPPORT"
                        timer2 = time.time()
                    elif "jg" in str(row):
                        Role2 = "JUNGLE"
                        timer2 = time.time()
                    elif "mid" in str(row):
                        Role2 = "MID"
                        timer2 = time.time()
                    elif "top" in str(row):
                        Role2 = "TOP"
                        timer2 = time.time()
                    else:
                        print("Something went wrong at 2 ROLEASSINGMENT, or invalid input.")
                elif "-t" in str(row):
                    summtimer2 = teleporttimer
                    Spell2 = "TELEPORT"
                    if "adc" in str(row):
                        Role2 = "ADC"
                        timer2 = time.time()
                    elif "supp" in str(row):
                        Role2 = "SUPPORT"
                        print("SUPPORT TELEPORT DOWN")
                        timer2 = time.time()
                    elif "jg" in str(row):
                        Role2 = "JUNGLE"
                        timer2 = time.time()
                    elif "mid" in str(row):
                        Role2 = "MID"
                        timer2 = time.time()
                    elif "top" in str(row):
                        Role2 = "TOP"
                        timer2 = time.time()
                    else:
                        print("Something went wrong at 2 ROLEASSINGMENT, or invalid input.")
                elif "-i" in str(row):
                    summtimer2 = ignitetimer
                    Spell2 = "Ignite"
                    if "adc" in str(row):
                        Role2 = "ADC"
                        timer2 = time.time()
                    elif "supp" in str(row):
                        Role2 = "SUPPORT"
                        timer2 = time.time()
                    elif "jg" in str(row):
                        Role2 = "JUNGLE"
                        timer2 = time.time()
                    elif "mid" in str(row):
                        Role2 = "MID"
                        timer2 = time.time()
                    elif "top" in str(row):
                        Role2 = "TOP"
                        timer2 = time.time()
                    else:
                        print("Something went wrong at 2 ROLEASSINGMENT, or invalid input.")
                elif "-c" in str(row):
                    summtimer2 = cleansetimer
                    Spell2 = "CLEANSE"
                    if "adc" in str(row):
                        Role2 = "ADC"
                        timer2 = time.time()
                    elif "supp" in str(row):
                        Role2 = "SUPPORT"
                        timer2 = time.time()
                    elif "jg" in str(row):
                        Role2 = "JUNGLE"
                        timer2 = time.time()
                    elif "mid" in str(row):
                        Role2 = "MID"
                        timer2 = time.time()
                    elif "top" in str(row):
                        Role2 = "TOP"
                        timer2 = time.time()
                    else:
                        print("Something went wrong at 2 ROLEASSINGMENT, or invalid input.")
                else:
                    print("Something went wrong at summtimer2 assignment, or there was invalid input")


    elif not threeclosed:
        linenumber = {6}
        for i, row in enumerate(open(r'C:\Riot Games\League of Legends\MyNotes.txt', "r")):
            if i in linenumber:
                if "-f" in str(row):
                    summtimer3 = flashtimer
                    Spell3 = "FLASH"
                    if "adc" in str(row):
                        Role3 = "ADC"
                        timer3 = time.time()
                        print("ADC FLASH DOWN")
                        threeclosed = True
                    elif "supp" in str(row):
                        Role3 = "SUPPORT"
                        timer3 = time.time()
                    elif "jg" in str(row):
                        Role3 = "JUNGLE"
                        timer3 = time.time()
                    elif "mid" in str(row):
                        Role3 = "MID"
                        timer3 = time.time()
                    elif "top" in str(row):
                        Role3 = "TOP"
                        timer3 = time.time()
                    else:
                        print("Something went wrong at 3 ROLEASSINGMENT, or invalid input.")
                elif "-b" in str(row):
                    summtimer3 = barriertimer
                    Spell3 = "BARRIER"
                    if "adc" in str(row):
                        Role3 = "ADC"
                        timer3 = time.time()
                    elif "supp" in str(row):
                        Role3 = "SUPPORT"
                        timer3 = time.time()
                    elif "jg" in str(row):
                        Role3 = "JUNGLE"
                        timer3 = time.time()
                    elif "mid" in str(row):
                        Role3 = "MID"
                        timer3 = time.time()
                    elif "top" in str(row):
                        Role3 = "TOP"
                        timer3 = time.time()
                    else:
                        print("Something went wrong at 3 ROLEASSINGMENT, or invalid input.")
                elif "-h" in str(row):
                    summtimer3 = healtimer
                    Spell3 = "HEAL"
                    if "adc" in str(row):
                        Role3 = "ADC"
                        timer3 = time.time()
                    elif "supp" in str(row):
                        Role3 = "SUPPORT"
                        timer3 = time.time()
                    elif "jg" in str(row):
                        Role3 = "JUNGLE"
                        timer3 = time.time()
                    elif "mid" in str(row):
                        Role3 = "MID"
                        timer3 = time.time()
                    elif "top" in str(row):
                        Role3 = "TOP"
                        timer3 = time.time()
                    else:
                        print("Something went wrong at 3 ROLEASSINGMENT, or invalid input.")
                elif "-t" in str(row):
                    summtimer3 = teleporttimer
                    Spell3 = "TELEPORT"
                    if "adc" in str(row):
                        Role3 = "ADC"
                        timer3 = time.time()
                    elif "supp" in str(row):
                        Role3 = "SUPPORT"
                        timer3 = time.time()
                    elif "jg" in str(row):
                        Role3 = "JUNGLE"
                        timer3 = time.time()
                    elif "mid" in str(row):
                        Role3 = "MID"
                        timer3 = time.time()
                    elif "top" in str(row):
                        Role3 = "TOP"
                        timer3 = time.time()
                    else:
                        print("Something went wrong at 3 ROLEASSINGMENT, or invalid input.")
                elif "-i" in str(row):
                    summtimer3 = ignitetimer
                    Spell3 = "Ignite"
                    if "adc" in str(row):
                        Role3 = "ADC"
                        timer3 = time.time()
                    elif "supp" in str(row):
                        Role3 = "SUPPORT"
                        timer3 = time.time()
                    elif "jg" in str(row):
                        Role3 = "JUNGLE"
                        timer3 = time.time()
                    elif "mid" in str(row):
                        Role3 = "MID"
                        timer3 = time.time()
                    elif "top" in str(row):
                        Role3 = "TOP"
                        timer3 = time.time()
                    else:
                        print("Something went wrong at 3 ROLEASSINGMENT, or invalid input.")
                elif "-c" in str(row):
                    summtimer3 = cleansetimer
                    Spell3 = "CLEANSE"
                    if "adc" in str(row):
                        Role3 = "ADC"
                        timer3 = time.time()
                    elif "supp" in str(row):
                        Role3 = "SUPPORT"
                        timer3 = time.time()
                    elif "jg" in str(row):
                        Role3 = "JUNGLE"
                        timer3 = time.time()
                    elif "mid" in str(row):
                        Role3 = "MID"
                        timer3 = time.time()
                    elif "top" in str(row):
                        Role3 = "TOP"
                        timer3 = time.time()
                    else:
                        print("Something went wrong at 3 ROLEASSINGMENT, or invalid input.")
                else:
                    print("Something went wrong at summtimer3 assignment, or there was invalid input")


    elif not fourclosed:
        linenumber = {7}
        for i, row in enumerate(open(r'C:\Riot Games\League of Legends\MyNotes.txt', "r")):
            if i in linenumber:
                if "-f" in str(row):
                    summtimer4 = flashtimer
                    Spell4 = "FLASH"
                    if "adc" in str(row):
                        Role4 = "ADC"
                        timer4 = time.time()
                        print("ADC FLASH DOWN")
                        fourclosed = True
                    elif "supp" in str(row):
                        Role4 = "SUPPORT"
                        timer4 = time.time()
                    elif "jg" in str(row):
                        Role4 = "JUNGLE"
                        timer4 = time.time()
                    elif "mid" in str(row):
                        Role4 = "MID"
                        timer4 = time.time()
                    elif "top" in str(row):
                        Role4 = "TOP"
                        timer4 = time.time()
                    else:
                        print("Something went wrong at 4 ROLEASSINGMENT, or invalid input.")
                elif "-b" in str(row):
                    summtimer4 = barriertimer
                    Spell4 = "BARRIER"
                    if "adc" in str(row):
                        Role4 = "ADC"
                        timer4 = time.time()
                    elif "supp" in str(row):
                        Role4 = "SUPPORT"
                        timer4 = time.time()
                    elif "jg" in str(row):
                        Role4 = "JUNGLE"
                        timer4 = time.time()
                    elif "mid" in str(row):
                        Role4 = "MID"
                        timer4 = time.time()
                    elif "top" in str(row):
                        Role4 = "TOP"
                        timer4 = time.time()
                    else:
                        print("Something went wrong at 4 ROLEASSINGMENT, or invalid input.")
                elif "-h" in str(row):
                    summtimer4 = healtimer
                    Spell4 = "HEAL"
                    if "adc" in str(row):
                        Role4 = "ADC"
                        timer4 = time.time()
                    elif "supp" in str(row):
                        Role4 = "SUPPORT"
                        timer4 = time.time()
                    elif "jg" in str(row):
                        Role4 = "JUNGLE"
                        timer4 = time.time()
                    elif "mid" in str(row):
                        Role4 = "MID"
                        timer4 = time.time()
                    elif "top" in str(row):
                        Role4 = "TOP"
                        timer4 = time.time()
                    else:
                        print("Something went wrong at 1 ROLEASSINGMENT, or invalid input.")
                elif "-t" in str(row):
                    summtimer4 = teleporttimer
                    Spell4 = "TELEPORT"
                    if "adc" in str(row):
                        Role4 = "ADC"
                        timer4 = time.time()
                    elif "supp" in str(row):
                        Role4 = "SUPPORT"
                        timer4 = time.time()
                    elif "jg" in str(row):
                        Role4 = "JUNGLE"
                        timer4 = time.time()
                    elif "mid" in str(row):
                        Role4 = "MID"
                        timer4 = time.time()
                    elif "top" in str(row):
                        Role4 = "TOP"
                        timer4 = time.time()
                    else:
                        print("Something went wrong at 4 ROLEASSINGMENT, or invalid input.")
                elif "-i" in str(row):
                    summtimer4 = ignitetimer
                    Spell4 = "Ignite"
                    if "adc" in str(row):
                        Role4 = "ADC"
                        timer4 = time.time()
                    elif "supp" in str(row):
                        Role4 = "SUPPORT"
                        timer4 = time.time()
                    elif "jg" in str(row):
                        Role4 = "JUNGLE"
                        timer4 = time.time()
                    elif "mid" in str(row):
                        Role4 = "MID"
                        timer4 = time.time()
                    elif "top" in str(row):
                        Role4 = "TOP"
                        timer4 = time.time()
                    else:
                        print("Something went wrong at 4 ROLEASSINGMENT, or invalid input.")
                elif "-c" in str(row):
                    summtimer4 = cleansetimer
                    Spell4 = "CLEANSE"
                    if "adc" in str(row):
                        Role4 = "ADC"
                        timer4 = time.time()
                    elif "supp" in str(row):
                        Role4 = "SUPPORT"
                        timer4 = time.time()
                    elif "jg" in str(row):
                        Role4 = "JUNGLE"
                        timer4 = time.time()
                    elif "mid" in str(row):
                        Role4 = "MID"
                        timer4 = time.time()
                    elif "top" in str(row):
                        Role4 = "TOP"
                        timer4 = time.time()
                    else:
                        print("Something went wrong at 4 ROLEASSINGMENT, or invalid input.")
                else:
                    print("Something went wrong at summtimer4 assignment, or there was invalid input")


    elif not fiveclosed:
        linenumber = {8}
        for i, row in enumerate(open(r'C:\Riot Games\League of Legends\MyNotes.txt', "r")):
            if i in linenumber:
                if "-f" in str(row):
                    summtimer5 = flashtimer
                    Spell5 = "FLASH"
                    if "adc" in str(row):
                        Role5 = "ADC"
                        timer5 = time.time()
                        print("ADC FLASH DOWN")
                        fiveclosed = True
                    elif "supp" in str(row):
                        Role5 = "SUPPORT"
                        timer5 = time.time()
                    elif "jg" in str(row):
                        Role5 = "JUNGLE"
                        timer5 = time.time()
                    elif "mid" in str(row):
                        Role5 = "MID"
                        timer5 = time.time()
                    elif "top" in str(row):
                        Role5 = "TOP"
                        timer5 = time.time()
                    else:
                        print("Something went wrong at 5 ROLEASSINGMENT, or invalid input.")
                elif "-b" in str(row):
                    summtimer5 = barriertimer
                    Spell5 = "BARRIER"
                    if "adc" in str(row):
                        Role5 = "ADC"
                        timer5 = time.time()
                    elif "supp" in str(row):
                        Role5 = "SUPPORT"
                        timer5 = time.time()
                    elif "jg" in str(row):
                        Role5 = "JUNGLE"
                        timer5 = time.time()
                    elif "mid" in str(row):
                        Role5 = "MID"
                        timer5 = time.time()
                    elif "top" in str(row):
                        Role5 = "TOP"
                        timer5 = time.time()
                    else:
                        print("Something went wrong at 5 ROLEASSINGMENT, or invalid input.")
                elif "-h" in str(row):
                    summtimer5 = healtimer
                    Spell5 = "HEAL"
                    if "adc" in str(row):
                        Role5 = "ADC"
                        timer5 = time.time()
                    elif "supp" in str(row):
                        Role5 = "SUPPORT"
                        timer5 = time.time()
                    elif "jg" in str(row):
                        Role5 = "JUNGLE"
                        timer5 = time.time()
                    elif "mid" in str(row):
                        Role5 = "MID"
                        timer5 = time.time()
                    elif "top" in str(row):
                        Role5 = "TOP"
                        timer5 = time.time()
                    else:
                        print("Something went wrong at 5 ROLEASSINGMENT, or invalid input.")
                elif "-t" in str(row):
                    summtimer5 = teleporttimer
                    Spell5 = "TELEPORT"
                    if "adc" in str(row):
                        Role5 = "ADC"
                        timer5 = time.time()
                    elif "supp" in str(row):
                        Role5 = "SUPPORT"
                        timer5 = time.time()
                    elif "jg" in str(row):
                        Role5 = "JUNGLE"
                        timer5 = time.time()
                    elif "mid" in str(row):
                        Role5 = "MID"
                        timer5 = time.time()
                    elif "top" in str(row):
                        Role5 = "TOP"
                        timer5 = time.time()
                    else:
                        print("Something went wrong at 5 ROLEASSINGMENT, or invalid input.")
                elif "-i" in str(row):
                    summtimer5 = ignitetimer
                    Spell5 = "Ignite"
                    if "adc" in str(row):
                        Role5 = "ADC"
                        timer5 = time.time()
                    elif "supp" in str(row):
                        Role5 = "SUPPORT"
                        timer5 = time.time()
                    elif "jg" in str(row):
                        Role5 = "JUNGLE"
                        timer5 = time.time()
                    elif "mid" in str(row):
                        Role5 = "MID"
                        timer5 = time.time()
                    elif "top" in str(row):
                        Role5 = "TOP"
                        timer5 = time.time()
                    else:
                        print("Something went wrong at 5 ROLEASSINGMENT, or invalid input.")
                elif "-c" in str(row):
                    summtimer5 = cleansetimer
                    Spell5 = "CLEANSE"
                    if "adc" in str(row):
                        Role5 = "ADC"
                        timer5 = time.time()
                    elif "supp" in str(row):
                        Role5 = "SUPPORT"
                        timer5 = time.time()
                    elif "jg" in str(row):
                        Role5 = "JUNGLE"
                        timer5 = time.time()
                    elif "mid" in str(row):
                        Role5 = "MID"
                        timer5 = time.time()
                    elif "top" in str(row):
                        Role5 = "TOP"
                        timer5 = time.time()
                    else:
                        print("Something went wrong at 5 ROLEASSINGMENT, or invalid input.")
                else:
                    print("Something went wrong at summtimer5 assignment, or there was invalid input")


    elif not sixclosed:
        linenumber = {9}
        for i, row in enumerate(open(r'C:\Riot Games\League of Legends\MyNotes.txt', "r")):
            if i in linenumber:
                if "-f" in str(row):
                    summtimer6 = flashtimer
                    Spell6 = "FLASH"
                    if "adc" in str(row):
                        Role6 = "ADC"
                        timer6 = time.time()
                        print("ADC FLASH DOWN")
                        sixclosed = True
                    elif "supp" in str(row):
                        Role6 = "SUPPORT"
                        timer6 = time.time()
                    elif "jg" in str(row):
                        Role6 = "JUNGLE"
                        timer6 = time.time()
                    elif "mid" in str(row):
                        Role6 = "MID"
                        timer6 = time.time()
                    elif "top" in str(row):
                        Role6 = "TOP"
                        timer6 = time.time()
                    else:
                        print("Something went wrong at 6 ROLEASSINGMENT, or invalid input.")
                elif "-b" in str(row):
                    summtimer6 = barriertimer
                    Spell6 = "BARRIER"
                    if "adc" in str(row):
                        Role6 = "ADC"
                        timer6 = time.time()
                    elif "supp" in str(row):
                        Role6 = "SUPPORT"
                        timer6 = time.time()
                    elif "jg" in str(row):
                        Role6 = "JUNGLE"
                        timer6 = time.time()
                    elif "mid" in str(row):
                        Role6 = "MID"
                        timer6 = time.time()
                    elif "top" in str(row):
                        Role6 = "TOP"
                        timer6 = time.time()
                    else:
                        print("Something went wrong at 6 ROLEASSINGMENT, or invalid input.")
                elif "-h" in str(row):
                    summtimer6 = healtimer
                    Spell6 = "HEAL"
                    if "adc" in str(row):
                        Role6 = "ADC"
                        timer6 = time.time()
                    elif "supp" in str(row):
                        Role6 = "SUPPORT"
                        timer6 = time.time()
                    elif "jg" in str(row):
                        Role6 = "JUNGLE"
                        timer6 = time.time()
                    elif "mid" in str(row):
                        Role6 = "MID"
                        timer6 = time.time()
                    elif "top" in str(row):
                        Role6 = "TOP"
                        timer6 = time.time()
                    else:
                        print("Something went wrong at 6 ROLEASSINGMENT, or invalid input.")
                elif "-t" in str(row):
                    summtimer6 = teleporttimer
                    Spell6 = "TELEPORT"
                    if "adc" in str(row):
                        Role6 = "ADC"
                        timer6 = time.time()
                    elif "supp" in str(row):
                        Role6 = "SUPPORT"
                        timer6 = time.time()
                    elif "jg" in str(row):
                        Role6 = "JUNGLE"
                        timer6 = time.time()
                    elif "mid" in str(row):
                        Role6 = "MID"
                        timer6 = time.time()
                    elif "top" in str(row):
                        Role6 = "TOP"
                        timer6 = time.time()
                    else:
                        print("Something went wrong at 6 ROLEASSINGMENT, or invalid input.")
                elif "-i" in str(row):
                    summtimer6 = ignitetimer
                    Spell6 = "Ignite"
                    if "adc" in str(row):
                        Role6 = "ADC"
                        timer6 = time.time()
                    elif "supp" in str(row):
                        Role6 = "SUPPORT"
                        timer6 = time.time()
                    elif "jg" in str(row):
                        Role6 = "JUNGLE"
                        timer6 = time.time()
                    elif "mid" in str(row):
                        Role6 = "MID"
                        timer6 = time.time()
                    elif "top" in str(row):
                        Role6 = "TOP"
                        timer6 = time.time()
                    else:
                        print("Something went wrong at 6 ROLEASSINGMENT, or invalid input.")
                elif "-c" in str(row):
                    summtimer6 = cleansetimer
                    Spell6 = "CLEANSE"
                    if "adc" in str(row):
                        Role6 = "ADC"
                        timer6 = time.time()
                    elif "supp" in str(row):
                        Role6 = "SUPPORT"
                        timer6 = time.time()
                    elif "jg" in str(row):
                        Role6 = "JUNGLE"
                        timer6 = time.time()
                    elif "mid" in str(row):
                        Role6 = "MID"
                        timer6 = time.time()
                    elif "top" in str(row):
                        Role6 = "TOP"
                        timer6 = time.time()
                    else:
                        print("Something went wrong at 6 ROLEASSINGMENT, or invalid input.")
                else:
                    print("Something went wrong at summtimer6 assignment, or there was invalid input")


    else:
        print("Either no inputs, or something went wrong.")



