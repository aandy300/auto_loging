import time ,sys ,os
import pyautogui as ms # 滑鼠點擊用
from pynput import keyboard 
from pynput.keyboard import Key, Controller

keyboard = Controller()

# 7m30s

global x 
global y
x = 0
y = 0

# 讀取
def open_gamebat():
    print('gamebat_loging_star')
    # bat地址
    acrobatPath = "C:\\Users\\admin\\Desktop\\game_Yahoo.bat" 
    # 跑bat
    os.startfile(acrobatPath)
    print('gamebat_loging_star_wait20s_updata')
    time.sleep(20) # 20s 無更新 讀取置loging Button
    ms.click(679, 665, clicks=1,button='left', interval=0.1)
    print('gamebat_loging_star_wait5s_gamestar')
    time.sleep(35) # 等讀取到 角色選取畫面
    print('gamebat_loging_end')

def yahoo_slect_character():
    postion_arrow = 1330, 992
    psotion_slot1 = 1149, 997
    # 1330 992 = >
    # 698 981 = 最右邊後第一個格子
    # 1149, 997 = 倒數第二個格子
    # 1052, 997 = 倒數第三個格子
    # 962, 997 = 倒數第四個格子
    # 862, 997 = 倒數第五個格子
    # 769, 997 = 倒數第六個格子
    # 676, 997 = 倒數第七個格子
    
    ms.click(postion_arrow, clicks=1,button='left', interval=0.1)
    time.sleep(1)
    ms.click(postion_arrow, clicks=1,button='left', interval=0.1)
    time.sleep(1)
    ms.click(psotion_slot1, clicks=2,button='left', interval=0.1)
    time.sleep(16) #等地圖讀取

    #f
    press_f() 

    # 換角開始
    print('換角開始')
    ms.click(11, 13, clicks=1,button='left', interval=0.1)
    time.sleep(2)
    ms.click(950, 579, clicks=1,button='left', interval=0.1)
    time.sleep(2)
    ms.click(966, 595, clicks=1,button='left', interval=0.1)
    time.sleep(2)
    print('換角結束')
    # 換角結束
   
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
    while a < 15 :
        print('第',a ,'次迴圈')
        yahoo_slect_character()
        a = a +1
    print('迴圈結束')
    print('結束遊戲') 
    closegame()

main()