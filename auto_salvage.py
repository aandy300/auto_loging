import time ,sys
import pyautogui as ms
from pynput import keyboard

mspoint = int,int # 監測回報用
tool_point = int,int # 拆解器1位置
tool2_point = int,int # 拆解器2位置
sl_item_postion = int, int #要拆的位置
first_time = True #第一次 -開關
z = int

def on_press(key):
    global first_time
    if key == keyboard.Key.f1: # 中止
        report_postion()
    elif key == keyboard.Key.f2: #分解器位置
        sl_tool()
    elif key == keyboard.Key.f3: #要拆的位置
        chick_salvage_item_postion()
    elif key == keyboard.Key.f4: #執行拆解
        salvage()
    elif key == keyboard.Key.f5: #執行拆解
        print(sl_item_postion)
    elif key == keyboard.Key.f12: # 監測位置 #會BUG進 迴圈出不來
        return False


#回傳目前位置 F1
def report_postion():
    global mspoint

    mspoint = ms.position()
    print("鼠標現在位置:", mspoint, "已儲存至 mspoint")
    return mspoint

#拆解 F4
def salvage():
    global first_time
    global sl_item_postion
    # 判定是否第一次 第一次拆解,單點十個道具
    if first_time == True:
        first_time = False
        print("第一次拆解,單點十個道具")
        #先跑一次確定是否可以執行
        for _ in range(1):
                try:
                    for i in range(10):
                        i += 1
                        if sl_item_postion == False :
                            print("str")
                        ms.click(sl_item_postion, clicks=2,button='left', interval=0.2)
                        print("第一次拆解,單點十個道具,第", i,"次")
                except:
                    first_time = True
                    print('未設定位置,使用F3定位要拆的道具位置')
                break
    print("拆解結束")

#要拆解的位置 F3
def chick_salvage_item_postion():
    global sl_item_postion
    sl_item_postion = ms.position()
    print("要拆解的", sl_item_postion)
    return sl_item_postion

#拆解器位置
def sl_tool():
    
    #追加數值用容器
    x,y = ms.position()
    #分解器1位置
    tool_point = ms.position()
    #分解器2位置
    tool2_point = ms.position(x=x+50,y=y+0)
    # XY +50+50 = 藍綠分解位置
    
    
    
    print("拆解器a位置",tool_point, "拆解器b位置", tool2_point,)
    return tool_point, tool2_point

#擠頻道
def channel_try():
    x = int
    x +=1
    print(x)
    ms.click(80,231, clicks=1,button='right', interval=0.1)
    time.sleep(1)
    ms.click(159,307, clicks=1,button='left', interval=0.1)
    time.sleep(1)
    ms.click(1089,581, clicks=1,button='left', interval=0.1)
    time.sleep(1)


    

def click_postion():
    z = 0
    while True:
        global mspoint

        z += 1
        ms.click(mspoint, clicks=2,button='left', interval=0.1)
        # ms.click(psotion_slot1, clicks=2,button='left', interval=0.1)
        # print('clicked at (400, 400)')
        print(z)
        time.sleep(5)


def main():

    with keyboard.Listener(on_press=on_press) as listener:
        for _ in range(50000):
            # print('still running...')
            time.sleep(1)
            if not listener.running:
                print('離開監聽_break')
                break
    print("程式結束")

main()