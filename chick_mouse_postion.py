import time ,sys
import pyautogui as ms #https://pyautogui.readthedocs.io/en/latest/mouse.html
from pynput import keyboard



x, y = int, int
mspoint = int,int
z = int
print(x, y)

def on_press(key):
    if key == keyboard.Key.f12: # 中止
        return False
    elif key == keyboard.Key.f3: # 點擊指定位置
        click_postion()
    elif key == keyboard.Key.f5: # 連點
        ms.click()
    elif key == keyboard.Key.f4: # 連點
        terb_chick()
    elif key == keyboard.Key.f1: # 監測位置 #會BUG進 迴圈出不來
        global x, y
        global mspoint
        x, y = ms.position()
        print('鼠標現在位置','X:' ,x ,'Y:' ,y )
        mspoint = x, y
        print("mspoint", mspoint)
        return x, y, mspoint
    elif key == keyboard.Key.f2: #儲存監測位置
        x, y = ms.position()
        print(x, y)
def terb_chick():
    global x,y

    # exsample:
    # >>> pyautogui.mouseDown(); pyautogui.mouseUp()  # does the same thing as a left-button mouse click
    # >>> pyautogui.mouseDown(button='right')  # press the right button down
    # >>> pyautogui.mouseUp(button='right', x=100, y=200)  # move the mouse to 100, 200, then release the right button up.
    while True:
        ms.mouseDown(button='left',x=x,y=y)
        time.sleep(9)
        ms.mouseUp()
        time.sleep(5)
        


def click_postion():
    z = 0
    while True:
        global x
        global y

        global mspoint
        z += 1
        ms.click(mspoint, clicks=2,button='left', interval=0.1)
        # ms.click(psotion_slot1, clicks=2,button='left', interval=0.1)
        # print('clicked at (400, 400)')
        print(z)
        time.sleep(5)

def main():
    with keyboard.Listener(on_press=on_press) as listener:
        for _ in range(1150000000):
            # print('still running...')
            time.sleep(1)
            if not listener.running:
                break

main()