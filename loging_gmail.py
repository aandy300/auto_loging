import time ,sys ,os
import pyautogui as ms # 滑鼠點擊用
from pynput import keyboard 
from pynput.keyboard import Key, Controller

keyboard = Controller()

global x 
global y
x = 0
y = 0

# 讀取
def open_gamebat():
    print('gamebat_loging_star')
    acrobatPath = "C:\\Users\\admin\\Desktop\\game_Gmail.bat" 
    os.startfile(acrobatPath)
    print('gamebat_loging_star_wait20s_updata')
    time.sleep(20) # 20s 無更新 讀取置loging Button
    ms.click(679, 665, clicks=1,button='left', interval=0.1)
    print('gamebat_loging_star_wait5s_gamestar')
    time.sleep(35) # 等讀取到 角色選取畫面
    print('gamebat_loging_end')

def gmail_slect_character():
    global x
    global y
    postion_solot0 = 767, 988
    postion_solot1 = 863, 988
    postion_solot2 = 962, 988
    postion_solot3 = 1060, 988
    postion_solot4 = 1160, 988
    
    print(x, '上')

    if x == 0 :
        p = postion_solot0
    elif x == 1 :
        p = postion_solot1
    elif x == 2 :
        p = postion_solot2
    elif x == 3 :
        p = postion_solot3
    elif x == 4 :
        p = postion_solot4
    
    if y == 0 :
        wait_sec = 30
    else :
        wait_sec = 20
      
    print(p)
    # ms.click(767, 988, clicks=2,button='left', interval=0.1)
    ms.click(p, clicks=2,button='left', interval=0.1)
    print('等地圖', p)
    time.sleep(wait_sec) # wait map load
    press_f()
    print('換角', p)
    ms.click(11, 13, clicks=1,button='left', interval=0.1)
    time.sleep(2)
    ms.click(950, 579, clicks=1,button='left', interval=0.1)
    time.sleep(2)
    print('back')
    ms.click(966, 595, clicks=1,button='left', interval=0.1)
    time.sleep(2)
    
    x = x + 1
    y = y + 1
    print(x, '下')
    
def press_f():
    ms.click(1307, 748, clicks=2,button='left', interval=0.1)

def closegame():
    ms.click(11, 13, clicks=1,button='left', interval=0.1)
    time.sleep(2)
    ms.click(949, 609, clicks=1,button='left', interval=0.1)
    time.sleep(2)

def main():
    open_gamebat()
    a = 0
    while a < 4 :
        gmail_slect_character()
        a = a +1
    print('迴圈結束')
    print('結束遊戲')
    closegame()

main()