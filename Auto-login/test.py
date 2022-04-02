def main():
    # a = 0
    # postion_x = 200
    # postion_y = 992
    # while a < 15 :
    #     postion_xy = postion_x, postion_y
    #     print('第',a ,'次迴圈', postion_xy)
    #     # yahoo_slect_character(postion_xy)
    #     postion_y = postion_y + 100
    #     a = a +1

    postion_x = 200
    postion_y = 992
    position_xy = postion_x, postion_y
    a = 0
    print('外面', a)

    while a < 15 :
        print('第',a ,'次迴圈')
        print('點選角色', position_xy)
        # ms.click(position_xy, clicks=2,button='left', interval=0.1) #點角色格
        postion_x = postion_x + 100
        position_xy = postion_x, postion_y
        print('數值調整', 'xy: ', position_xy, 'x:', postion_x, 'y', postion_y)
        a = a +1


main()