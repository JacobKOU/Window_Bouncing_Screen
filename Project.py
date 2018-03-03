import tkinter
from tkinter import *
#import ImageTk

main_window = tkinter.Tk() #makes the main window

frame_num = int(0)


#width and height of window
window_width = 100
window_height = 100
#This gets the screen width and height
screen_width = int(main_window.winfo_screenwidth())
screen_height = int(main_window.winfo_screenheight())

#Directs where the window moves
right_move = True
left_move = False
up_move = True
down_move = False

#this is where the window is on the screen
window_place_y = (int(screen_height / 3))
window_place_x = (int(0))

#this puts the window in the specific place
main_window.geometry("%dx%d%+d%+d" % (window_width, window_height, 0, (int(screen_height / 3))))   

def moving():
    #These are the moving variables
    mov_right = 10
    mov_up = 10
    while (1 == 1): #while the program is running

        #makes variables global
        global window_width
        global window_height
        global screen_height
        global screen_width
        global right_move
        global left_move
        global up_move
        global down_move
        global window_place_y
        global window_place_x
        global frame_num
        
        #decides if the window goes up or down
        if (window_place_y >= (screen_height - 100)):
            up_move = False
            down_move = True
        elif (window_place_y <= 0):
            window_place_y = 1
            up_move = True
            down_move = False


        #decides if the window goes right or left
        if (window_place_x >= (screen_width - 50)):
            right_move = False
            left_move = True
        elif (window_place_x <= 0):
            window_place_x = 0
            right_move = True
            left_move = False

        #makes the window go up or down
        if (up_move == True):
            window_place_y = (window_place_y + mov_up)
        elif (down_move == True):
            window_place_y = (window_place_y - mov_up)

        #makes the window go left or right
        if (right_move == True):
            window_place_x = (window_place_x + mov_right)
        elif (left_move == True):
            window_place_x = (window_place_x - mov_right)

        
        #makes the window move
        main_window.geometry("%dx%d%+d%+d" % (window_width, window_height, window_place_x, window_place_y))
#        print("Up:", up_move, ";Down:", down_move, ";Right:", right_move, ";Left:", left_move) #this outputs where the intended window is going
        #the commented out print function is only for developing and curious people
        
        #updates the window
        main_window.update_idletasks()
        main_window.update()
    

moving()
    





