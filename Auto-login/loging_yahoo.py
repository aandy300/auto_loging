import time ,sys ,os
from turtle import position
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
    ms.click(660, 670, clicks=1,button='left', interval=0.1)
    print('gamebat_loging_star_wait5s_gamestar')
    time.sleep(35) # 等讀取到 角色選取畫面
    print('gamebat_loging_end')

# 改成外面傳入位置訊息 在外面 for做增加100橫向軸 來更改位置資訊
def yahoo_slect_character():
    postion_x = 200
    postion_y = 992
    position_xy = postion_x, postion_y
    a = 0
    print('外面', a)

    while a < 15 :
        print('第',a ,'次迴圈')
        print('點選角色', position_xy)
        ms.click(position_xy, clicks=2,button='left', interval=0.1) #點角色格
        ms.click(position_xy, clicks=2,button='left', interval=0.1) #點角色格
        time.sleep(15) #等地圖
        postion_x = postion_x + 100
        position_xy = postion_x, postion_y
        print('數值調整', 'xy: ', position_xy, 'x:', postion_x, 'y', postion_y)
        #f
        press_f() 
        logout()
        a = a +1
    
    # time.sleep(16) #等地圖讀取
    # time.sleep(16) #等地圖讀取


    

def logout():
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
    # open_gamebat()
    yahoo_slect_character()
    print('迴圈結束')
    print('結束遊戲') 
    closegame()

main()