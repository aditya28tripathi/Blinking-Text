import os
import time

def clear():
    os.system('cls' if os.name=='nt' else 'clear')
    
def blink_text(text,interval=0.5,num_blinks=10):
    for i in range(num_blinks):
        clear()
        print(text)
        time.sleep(interval)
        clear()
        time.sleep(interval)
        
blink_text("Aditya Tripathi" , 0.5,3)
