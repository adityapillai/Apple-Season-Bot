import ImageGrab 
import os
import time
import win32api, win32con


''' Bot only works when x_pad and y_pad are pixel values of top left corner with RGB (204,204,204)'''
x_pad=464
y_pad=183


x_left=22
x_right=497

def screenGrab():
    box = (x_pad+1,y_pad+1,511+x_pad,540)
    im = ImageGrab.grab(box)
    #im.save(os.getcwd() + '\\full_snap__' + str(int(time.time())) +
#'.png', 'PNG')
    return im


def customGrab(box):
    im = ImageGrab.grab((box[0]+x_pad,box[1]+y_pad,box[2]+x_pad,box[3]+y_pad))
    return im
   
       
def main():
    start()
    time.sleep(0.5)
    while(True):
        mousePos((find(),474))
        
                
def find():
    x=search2(350)
    while(x==-1):
        x=search2(350)
    return x
        
                       

def leftClick():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

def mousePos(cord):
    win32api.SetCursorPos((x_pad + cord[0], y_pad + cord[1]))
     

def start():
    mousePos((264,474))
    leftClick()


# searches for an apple at specifed row
def search2(y):
    box=(x_left,y,x_right,y+35)
    im=customGrab(box)
    for i in range(0,box[2]-box[0],10):
        pix=im.getpixel((i,0))
        p2=im.getpixel((i,34))
        if  pix[1]!=255:
            return i+x_left
        elif  p2[1]!=255:
            return i+x_left
    return -1



if __name__ == '__main__':
    pass
    
