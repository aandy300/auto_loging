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
    # acrobatPath = "C:\\Users\\admin\\Desktop\\game_Yahoo.bat" 
    acrobatPath = "C:\\Users\\admin\\Desktop\\game_Yahoo_nocopy.bat"     
    # 跑bat
    os.startfile(acrobatPath)
    print('gamebat_loging_star_wait20s_updata')
    time.sleep(20) # 20s 無更新 讀取置loging Button
    ms.click(660, 670, clicks=1,button='left', interval=0.1)
    print('gamebat_loging_star_wait5s_gamestar')
    time.sleep(35) # 等讀取到 角色選取畫面
    print('gamebat_loging_end')

# 改成使用 x軸 +100 處理選角色
def yahoo_slect_character():
    postion_x = 200 #開始的位置 設置初始值
    postion_y = 992 #開始的位置 設置初始值
    position_xy = postion_x, postion_y
    count = 0

    while count < 17 :
        print('第',count ,'次迴圈')
        print('點選角色', position_xy)
        ms.click(position_xy, clicks=2,button='left', interval=0.1) #點角色格
        ms.click(position_xy, clicks=2,button='left', interval=0.1) #點角色格
        print('等地圖', position_xy)
        time.sleep(16) #等地圖
        postion_x = postion_x + 95
        position_xy = postion_x, postion_y
        print('數值調整+轉存', 'xy: ', position_xy, 'x:', postion_x, 'y', postion_y)
        press_f() #f
        logout() #登出換角
        count =count +1

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
    print('press f')
    ms.click(1307, 748, clicks=2,button='left', interval=0.1)

def closegame():
    ms.click(11, 13, clicks=1,button='left', interval=0.1)
    time.sleep(2)
    ms.click(949, 609, clicks=1,button='left', interval=0.1)
    time.sleep(2)

def main():
    open_gamebat()
    yahoo_slect_character()
    print('迴圈結束')
    print('結束遊戲') 
    closegame()

main()