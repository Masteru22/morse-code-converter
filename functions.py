import time
import winsound
frequency = 1500  

def verify_text(text,my_dict):
    for letters in text:
        if letters not in my_dict and letters !=" ":
            return 1
    return 0

def program(text,my_dict,answer):
    if answer==0:
        for letter in text:
            print(f"{my_dict[letter]}",end="   ",flush=True)
            if letter==" ":
                time.sleep(0.7)
            else:
                for character in my_dict[letter]:
                    if character==".":
                        winsound.Beep(1000, 100)
                    else:
                        winsound.Beep(1000, 300)  
                    time.sleep(0.1) 
                time.sleep(0.3)
    else:
        print("\nINVALID CHARACTER!")
