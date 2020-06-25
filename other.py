 
# 擠頻道
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

# 連點糖果用
def click_postion_for_candy():
    z = 0
    while True:
        global mspoint

        z += 1
        ms.click(mspoint, clicks=2,button='left', interval=0.1)
        # ms.click(psotion_slot1, clicks=2,button='left', interval=0.1)
        # print('clicked at (400, 400)')
        print(z)
        time.sleep(5)
