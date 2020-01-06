import time
import keyboard

#待解決
#鍵盤監測不重複 單次就好

def candycorn4s():
    
    print('i am candy4s runing...')
    while True:
        if keyboard.is_pressed('F2'):
            print('定點完成,返回上層')
            candycorn4s()
            
        elif keyboard.is_pressed('F3'):
            print('run mouse check 4s')
        elif keyboard.is_pressed('F4'):
            candycorn4s()
            print('stop')

candycorn4s()