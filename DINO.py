import pyautogui # pip install pyautogui
from PIL import Image, ImageGrab # pip install pillow
# from numpy import asarray
import time

def hit(key):
    pyautogui.keyDown(key)
    return

def isCollide(data):
    
    # Draw the rectangle for cactus  
    for i in range(650, 665):
        for j in range(218, 257):
            if data[i, j] < 100:
                hit("up")
                return 
    # Draw the rectangle for birds        
    #for i in range(610, 625):
     #   for j in range(180, 218 ):
      #      if data[i, j] < 100:
       #         hit("down")
        #        return 
    
    return

if __name__ == "__main__":
    print("Hey.. Dino game about to start in 3 seconds")
    time.sleep(3)
    # hit('up') 

    while True:
        image = ImageGrab.grab().convert('L')  
        data = image.load()
        isCollide(data)
            
        # print(asarray(image))
'''
        # Draw the rectangle for cactus
        for i in range(650, 665):
            for j in range(218, 257):
                data[i, j] = 0
        
        # Draw the rectangle for birds
        
        for i in range(610, 625):
            for j in range(180, 218):
                data[i, j] = 171

        image.show()
        break
'''