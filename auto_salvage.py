# 處理err handle 
# except Exception,err:
#https://dotblogs.com.tw/caubekimo/2018/09/17/145733
# try:
#   print("test")
# except Exception as e:
#   print(e)
    ##進階版
#   error_class = e.__class__.__name__ #取得錯誤類型
#   detail = e.args[0] #取得詳細內容
#   cl, exc, tb = sys.exc_info() #取得Call Stack
#   lastCallStack = traceback.extract_tb(tb)[-1] #取得Call Stack的最後一筆資料
#   fileName = lastCallStack[0] #取得發生的檔案名稱
#   lineNum = lastCallStack[1] #取得發生的行號
#   funcName = lastCallStack[2] #取得發生的函數名稱
#   errMsg = "File \"{}\", line {}, in {}: [{}] {}".format(fileName, lineNum, funcName, error_class, detail)
#   print(errMsg)
#http://tw.gitbook.net/python/python_exceptions.html
#https://www.runoob.com/python/python-exceptions.html

#2020.06.04 藍綠OK 需要追加個位數拆解與其他拆解全部 "位置"  黃色未處理 迴圈3次約拆2*0個
#2020-10-18 追加拆物品s複數 拉移動
# 待增加 
# 特定次數發動黃拆 
# 最後拉全部物品堆疊
# log回報整理
import time ,sys
import pyautogui as ms
from pynput import keyboard

import sys
import traceback
import test

mspoint = int,int # 監測回報用
tool_point = int,int # 拆解器1位置
tool_point_gb = int, int # 拆解器1位置gb
tool2_point = int,int # 拆解器2位置
tool2_point_gb = int, int # 拆解器2位置gb
sl_item_postion = int, int #要拆的位置
sl_item_postion_useall = int, int #要拆的位置 useall
option_postion = int, int # 齒輪位置
option_postion_deposit = int, int # 齒輪選項
wait_sl_item_postion = [] # 等待要拆解的物品位置
salvage_count = int # 拆解次數計數
first_time = True # 第一次 -開關
chick_ok = False #偵錯用
z = int

# F2分解器位置 > F3要拆的道具位置s > F4齒輪位置 > F5 開始
# 主要控制區
def on_press(key):
    global first_time, tool_point, tool_point_gb, tool2_point, tool2_point_gb
    if key == keyboard.Key.f1: # 回報位置
        report_postion()
    elif key == keyboard.Key.f2: #分解器位置
        chick_salvage_tool_postion()
    elif key == keyboard.Key.f3: #等待要拆的物品位置s
        add_wait_salvage_item_postion()
    elif key == keyboard.Key.f4: #齒輪的位置
        chick_option_postion()
    elif key == keyboard.Key.f5: #拆解
        #拆
        salvage()
    elif key == keyboard.Key.f7: #test
        print("123")
        salvage_all_click()
        
    elif key == keyboard.Key.f12: # 中止
        return False

#F1 回傳目前位置 
def report_postion():
    global mspoint

    mspoint = ms.position()
    print("鼠標現在位置:", mspoint, "已儲存至 mspoint")
    # return mspoint

#F2 拆解器位置  定位分解器1 帶入 藍綠分解位置 與分解器2...+要拆的物品位置 用 +50
def chick_salvage_tool_postion():
    global tool_point, tool_point_gb, tool2_point, tool2_point_gb, sl_item_postion, sl_item_postion_useall
    #追加數值用容器
    x,y = ms.position()
    #分解器1位置
    tool_point = ms.position()
    tool_point_gb = ms.position(x=x+50,y=y+50)
    #分解器2位置
    tool2_point = ms.position(x=x+50,y=y+0)
    tool2_point_gb = ms.position(x=x+100,y=y+50)
    #要拆的物品位置
    sl_item_postion = ms.position(x=x+100,y=y+0)
    sl_item_postion_useall = ms.position(x=x+102,y=y+75)
    # XY +50+50 = 藍綠分解位置 +100 = 要拆的物品位置
    print("拆解器a位置",tool_point, "拆解器a_gb", tool_point_gb)
    print("拆解器b位置",tool2_point, "拆解器b_gb", tool2_point_gb)
    print("要拆解的位置:", sl_item_postion, "要拆解的useall位置:", sl_item_postion_useall)
    return tool_point, tool_point_gb, tool2_point, tool2_point_gb

#F3 等待要拆的物品位置s 複數
def add_wait_salvage_item_postion():
    global wait_sl_item_postion, mspoint
    mspoint = ms.position()
    wait_sl_item_postion.append(mspoint)
    print("等待要拆的物品數量", len(wait_sl_item_postion))
    print("最後加入的一筆座標: ", wait_sl_item_postion[len(wait_sl_item_postion) -1])
    # return sl_item_postion

# F4 齒輪的位置
def chick_option_postion():
    global option_postion, option_postion_deposit
    x,y = ms.position()
    option_postion = ms.position()
    option_postion_deposit = ms.position(x=x+0,y=y+20)
    print("齒輪的位置", option_postion_deposit)

#F5 拆解 
# 先拉進來 > 拆個4次 > 黃拆 > 回傳 > 在拉 
# 記數  如果 F3 等待0 注意錯誤
# 拆解動作 整合 
def salvage():
    global wait_sl_item_postion, salvage_count
    # 防呆
    try_all_postion()

    salvage_count = len(wait_sl_item_postion)

    if (salvage_count > 0):
        salvage_count -= 1
        for postion in wait_sl_item_postion:
            pull_item(postion)
            print("pull_item: ", salvage_count)
            test_frist_tiem() # 開拆10個 待解決 只要跑一次就好
            salvage_all_bg()
            for _ in range(3):
                open_all_item()
                item_to_bank()
                time.sleep(1)
                take_all()
                time.sleep(2)
                salvage_all_bg()
                time.sleep(1)
                take_all()
                time.sleep(2)


# 功能性以下

#防呆偵錯
def try_all_postion():
    global tool_point, tool_point_gb, tool2_point, tool2_point_gb, sl_item_postion, option_postion, chick_ok
    print("防呆偵錯ing...")
    for _ in range(1):
        try:
            ms.click(tool_point, clicks=1,button='left', interval=0.1)
            ms.click(tool_point_gb, clicks=1,button='left', interval=0.1)
            ms.click(tool2_point, clicks=1,button='left', interval=0.1)
            ms.click(tool2_point_gb, clicks=1,button='left', interval=0.1)
            ms.click(sl_item_postion, clicks=1,button='left', interval=0.1)
            ms.click(option_postion, clicks=1,button='left', interval=0.1)
            len(wait_sl_item_postion) < 0
            chick_ok = True
            print("要使用的位置皆已儲存,可以執行分解")
        except Exception as e:
            print(e)
            print("有尚未定位的位置_請在確認!!")
            print("tool_point位置:", tool_point, "tool_point位置_gb:", tool_point_gb, "tool2_point位置:", tool2_point, "tool2_point_gb位置:", tool2_point_gb, "sl_item_postion:", sl_item_postion, "option_postion:", option_postion)
        break

#測 是否第一次 如第一次拆10個
def test_frist_tiem():
    global first_time
    if first_time == True:
        print("第一次拆解")
        first_time = False

        for i in range(10):
            i += 1
            if len(wait_sl_item_postion) == 0 :
                print("沒有設定要拆的物品, 使用F3加入要拆的物品")
            ms.click(wait_sl_item_postion[0], clicks=2,button='left', interval=0.2)
            
        print("第一次拆解,單點十個道具結束")

#拆解 藍綠
def salvage_all_bg():
    global  tool_point, tool_point_gb, tool2_point, tool2_point_gb, sl_item_postion
    #點
    ms.click(tool_point, clicks=1,button='right', interval=0.2)
    time.sleep(2)
    #拆
    ms.click(tool_point_gb, clicks=1,button='left', interval=0.2)
    salvage_all_click()
    print("salvage_all_bg()_end")

#開所有道具
def open_all_item():
    global sl_item_postion, sl_item_postion_useall
    ms.click(sl_item_postion, clicks=1,button='right', interval=0.2)
    time.sleep(1)
    ms.click(sl_item_postion_useall, clicks=1,button='left', interval=0.2)
    time.sleep(5)

#回傳
def item_to_bank():
    global option_postion, option_postion_deposit
    #點
    ms.click(option_postion, clicks=1,button='left', interval=0.2)
    #傳
    ms.click(option_postion_deposit, clicks=1,button='left', interval=0.2)
    print("item_to_bank()_end")

#拆所有 全部座標
def salvage_all_click():
    sl10 = 896, 642
    sl40 = 895, 742
    sl6 = 897, 629
    sl29 = 895, 711
    sl20 = 894, 667
    x = [sl10, sl40, sl6, sl29, sl20]
    for i in x:
        ms.click(i, clicks=1,button='left', interval=0.2)
    time.sleep(3)

#拿溢出
def take_all():
    take_all_ps = 1055, 611
    ms.click(take_all_ps, clicks=1,button='left', interval=0.1)
    print("take_all()")
#移動道具位置 至 拆解位置
def pull_item(postion):
    ms.mouseDown(postion ,button='left')
    ms.moveTo(sl_item_postion)
    time.sleep(1.2)
    ms.mouseUp()
    print(postion)
    print("pull_item")

def main():
    with keyboard.Listener(on_press=on_press) as listener:
        for _ in range(5000000):
            # print('still running...')
            time.sleep(1)
            if not listener.running:
                print('離開監聽_break')
                break
    print("程式結束")

main()