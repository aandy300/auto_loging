import time ,sys
import pyautogui as ms
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
        for _ in range(1150):
            # print('still running...')
            time.sleep(1)
            if not listener.running:
                break

main()