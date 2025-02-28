from tkinter import *
pro1 = Tk()
pro2 = Tk()

pro1.title('1')
pro2.title('window2')
################################
## to make topic window >>
pro1.lift(pro1) # topic window is behind

## to minimize window >>    choose one of the following:
# pro2.iconify()            # window2 is minimized 
# pro2.lower()              # window2 is minimized 
# pro2.state('iconic')      # window2 is minimized 
# pro2.state('withdrawn')   # window2 is hidden 
pro2.state('normal') 
################################
pro1.mainloop()
# pro2.mainloop()