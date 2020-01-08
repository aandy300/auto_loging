import time ,sys
import pyautogui as ms
from pynput import keyboard

x, y = int, int
count = 0

def on_press(key):
    if key == keyboard.Key.f1: # 監測滑鼠位置 並 儲存
        global x, y
        x, y = ms.position()
        print('鼠標現在位置','X:' ,x ,'Y:' ,y )
    elif key == keyboard.Key.f2: # 印出儲存的監測位置
        print(x, y)
    elif key == keyboard.Key.f3: # 點擊指定位置
        click_postion()
    elif key == keyboard.Key.f4: # 連點儲存的位置
        click_savepostion()
    elif key == keyboard.Key.f12: # 中止
        return False

def click_postion():
    while True:
        global x
        x += 1
        ms.click(400, 400, clicks=2,button='left', interval=0.1)
        print('clicked at (400, 400)')
        print(x, '次')
        time.sleep(5)

def click_savepostion():
    while True:
        global x, y, count
        count += 1
        ms.click(x, y, clicks=2,button='left', interval=0.1)
        print('clicked at (',x ,y ,')')
        print('已點擊', count, '次')
        time.sleep(5)

def main():
    with keyboard.Listener(on_press=on_press) as listener:
        for _ in range(50):
            print('still running...')
            time.sleep(1)
            if not listener.running:
                break

main()