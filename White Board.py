# import module
from tkinter import *
from tkinter.colorchooser import askcolor
from tkinter import ttk
import tkinter as tk
from tkinter import filedialog
import os

root=Tk()

# title
root.title("WHITE BOARD")

# geometry
root.geometry("1050x570+150+150")

# background
root.config(bg="#f2f3f5")

# resizable
root.resizable(False,False)

# ======================================================================================== #

''' 
This code defines a function called locate_xy that takes a parameter work. 
It updates the values of two global variables 
current_x and current_y with the values of work.x and work.y respectively.
'''

current_x = 0
current_y = 0
color="black"

def locate_xy(work):
    global current_x,current_y
    
    current_x = work.x
    current_y = work.y

# ======================================================================================== #

''' 
This code defines a function called addline that draws a line on a canvas. 
The line starts at the current position (current_x, current_y) 
and ends at the position (work.x, work.y). 
The line has a width specified 
by get_current_value(), a color specified by color, and a rounded cap. 
After drawing the line, the current position is updated to (work.x, work.y).
'''

def addline(work):
    global current_x,current_y
    Canvas.create_line((current_x,current_y,work.x,work.y),width=get_current_value(),
                    fill = color,capstyle=ROUND,smooth=True)
    current_x,current_y = work.x,work.y


# ======================================================================================== #

'''
This code defines a function called show_color that takes a parameter new_color. 
It updates the value of the global variable color with the value of new_color.
'''

def show_color(new_color):
    global color
    color=new_color
    

# ======================================================================================== #


'''
This code defines a function called new_canvas that clears a canvas and then displays a pallet.
'''

def new_canvas ():
    Canvas.delete('all')
    display_pallet()
    


# ======================================================================================== #

'''
This code defines a function called insertimage that opens a file dialog to select an image file. 
It then creates a PhotoImage object from the selected file and displays it on a canvas. 
Finally, it binds a callback function to the right mouse button motion event.
'''

def insertimage():
    global filename
    global f_img
        
    filename=filedialog.askopenfilename(initialdir=os.getcwd(),title='Select image file')
    filetype=(("PNG file","*.png"),("All file","new.txt"))
    
    f_img=tk.PhotoImage(file=filename)
    my_img=Canvas.create_image(180,50,image=f_img)
    root.bind("<B3-Motion>",my_callback)

# ======================================================================================== #

'''
This code defines a callback function called my_callback that takes an event parameter. 
Inside the function, it creates a global variable f_img and assigns it a tk.
PhotoImage object with the file parameter set to the value of filename. 
Then, it moves an image on a canvas using the create_image method of the Canvas class, 
passing the current x and y coordinates of the event and the f_img object as the image parameter.
'''

def my_callback(event):
    global f_img   
    f_img=tk.PhotoImage(file=filename)
    
    # move the image using right cursor
    my_img=Canvas.create_image(event.x,event.y,image=f_img)


# ======================================================================================== #


# icon
image_icon = PhotoImage(file="logo.png")
root.iconphoto(False,image_icon)

# sidebar
color_box = PhotoImage(file="color section.png")
Label(root,image=color_box,bg="#f2f3f5").place(x=10, y=20)

# side bar button
eraser=PhotoImage(file="eraser.png")
Button(root,image=eraser,bg="#f2f3f5",command=new_canvas).place(x=30,y=400)

importimage=PhotoImage(file="addimage.png")
Button(root,image=importimage,bg="white",command=insertimage).place(x=30,y=450)

# sidebar color
colors=Canvas(root,bg="#fff",width=37,height=300,bd=0)
colors.place(x=30,y=60)

# ======================================================================================== #

'''
This code defines a function display_pallet() that creates a set of colored rectangles on a canvas. 
Each rectangle represents a color, and when clicked, 
it calls the show_color() function with the corresponding color as an argument. 
The colors used are black, yellow, green, blue, red, orange, purple, cyan, and brown.
'''

def display_pallet():
    id =colors.create_rectangle((10,10,30,30),fill='black')
    colors.tag_bind(id,'<Button-1>',lambda x: show_color('black'))
    
    id =colors.create_rectangle((10,40,30,60),fill='yellow')
    colors.tag_bind(id,'<Button-1>',lambda x: show_color('yellow'))
    
    id =colors.create_rectangle((10,70,30,90),fill='green')
    colors.tag_bind(id,'<Button-1>',lambda x: show_color('green'))
    
    id =colors.create_rectangle((10,100,30,120),fill='blue')
    colors.tag_bind(id,'<Button-1>',lambda x: show_color('blue'))
    
    id =colors.create_rectangle((10,130,30,150),fill='red')
    colors.tag_bind(id,'<Button-1>',lambda x: show_color('red'))
    
    id =colors.create_rectangle((10,160,30,180),fill='orange')
    colors.tag_bind(id,'<Button-1>',lambda x: show_color('orange'))
    
    id =colors.create_rectangle((10,190,30,210),fill='purple')
    colors.tag_bind(id,'<Button-1>',lambda x: show_color('purple'))
    
    id =colors.create_rectangle((10,220,30,240),fill='cyan')
    colors.tag_bind(id,'<Button-1>',lambda x: show_color('cyan'))
    
    id =colors.create_rectangle((10,250,30,270),fill='brown')
    colors.tag_bind(id,'<Button-1>',lambda x: show_color('brown'))
    
display_pallet()

# ======================================================================================== #

'''
This code defines a function called get_current_value that returns the value 
of current_value formatted as a float with two decimal places.
'''

# slider scale
current_value = tk.DoubleVar()

def get_current_value():
    return'{: .2f}'.format(current_value.get())

# ======================================================================================== #

'''
This code defines a function called slider_changed that is triggered when a slider is changed. 
It updates the text of a label widget called value_label with the current value of the slider.
'''

def slider_changed(event):
    value_label.configure(text=get_current_value())

slider = ttk.Scale(root, from_=0,to=100,orient="horizontal",command=slider_changed,variable=current_value)
slider.place(x=30,y=530)

value_label=ttk.Label(root,text=get_current_value())
value_label.place(x=27,y=550)

slider =ttk.Scale

# ======================================================================================== #

# main screen
Canvas = Canvas(root,width=930,height=500,background="white",cursor="hand2")
Canvas.place(x=100,y=10)

Canvas.bind('<Button-1>',locate_xy)
Canvas.bind('<B1-Motion>',addline)



root.mainloop()
