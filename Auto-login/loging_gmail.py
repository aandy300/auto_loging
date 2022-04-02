import time ,sys ,os
import pyautogui as ms # 滑鼠點擊用
from pynput import keyboard 
from pynput.keyboard import Key, Controller

# 180s

# 多線程 測試 
# 需要停止其他線程方法 
# https://medium.com/jeasee%E9%9A%A8%E7%AD%86/python-%E5%A4%9A%E7%B7%9A%E7%A8%8B-eb36272e604b
import threading, time

keyboard = Controller()

global count, first_time_check
first_time_check = 0
count = 1

### 新增的
def two_job():
    print('thread %s is running...' % threading.current_thread().name)
    i =0
    while True:
        i += 1
        print("我是第二個程式：", i)
        time.sleep(0.5)
### 新增的結束

# 讀取
def open_gamebat():
    print('gamebat_loging_star')
    acrobatPath = "C:\\Users\\admin\\Desktop\\game_Gmail.bat" 
    os.startfile(acrobatPath) # 開啟檔案 bat
    print('gamebat_loging_star_wait20s_updata')
    time.sleep(20) # 20s 無更新 讀取置loging Button
    ms.click(660, 670, clicks=1,button='left', interval=0.1) #REMIND ME LATER按鈕
    print('gamebat_loging_star_wait5s_gamestar')
    time.sleep(35) # 等讀取到 角色選取畫面 #等自動登入
    print('gamebat_loging_end')

def gmail_slect_character():
    global wait_sec, count, first_time_check

    postion_solot1 = 767, 1000
    postion_solot2 = 863, 1000
    postion_solot3 = 962, 1000
    postion_solot4 = 1060, 1000
    postion_solot5 = 1160, 1000
    
    print('in 選角色 第:', count, '次')

    if count == 1 :
        p = postion_solot1
    elif count == 2 :
        p = postion_solot2
    elif count == 3 :
        p = postion_solot3
    elif count == 4 :
        p = postion_solot4
    elif count == 5 :
        p = postion_solot5
    
    # 想用bool反轉
    # 但python沒辦法直接 !bool? 解: https://stackoverflow.com/questions/8335029/is-there-a-way-to-negate-a-boolean-returned-to-variable
    if first_time_check == 0 :
        wait_sec = 30
    else :
        wait_sec = 20
      
    print(p)
    # ms.click(767, 988, clicks=2,button='left', interval=0.1)
    ms.click(p, clicks=2,button='left', interval=0.1)
    print('等地圖', p)
    time.sleep(15) # wait map load
    press_f()
    print('換角', p)
    ms.click(11, 13, clicks=1,button='left', interval=0.1)
    time.sleep(2)
    ms.click(950, 579, clicks=1,button='left', interval=0.1)
    time.sleep(2)
    print('back')
    ms.click(966, 595, clicks=1,button='left', interval=0.1)
    time.sleep(2)
    
    first_time_check+=1
    
    # 點F
def press_f():
    ms.click(1307, 748, clicks=2,button='left', interval=0.1)

    # 關遊戲
def closegame():
    ms.click(11, 13, clicks=1,button='left', interval=0.1)
    time.sleep(2)
    ms.click(949, 609, clicks=1,button='left', interval=0.1)
    time.sleep(2)

def main():
    global count

    # 新增的
    t = threading.Thread(target = two_job)
    t.start()
    print('thread %s is running...' % threading.current_thread().name)
    # 新增的 結束
    
    open_gamebat()

    while count < 6 :
        gmail_slect_character()
        count+= 1
    print('迴圈結束')
    print('結束遊戲')
    closegame()

    # 新增的
    t.join()
    print('thread %s is running...' % threading.current_thread().name)
    print("Done.")
    # 新增的結束

main()