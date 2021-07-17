import tkinter
from PIL import Image, ImageTk
import random

# toplevel widget which represents the main window of an application
root = tkinter.Tk()
root.geometry('400x400')
root.title(' Roll the Dice')

# Adding label into the frame
l0 = tkinter.Label(root, text="Welcome")
#pack() is used to place the widget along x and y coordinates
l0.pack()

# images
dice = ['die1.png', 'die2.png', 'die3.png', 'die4.png', 'die5.png', 'die6.png']
# simulating the dice with random numbers between 0 to 6 and generating image
#"PhotoImage()" function returns the image object.But, the problem is PhotoImage class only supports GIF and PGM/PPM formats.
 #The more generalized formats are JPEG/JPG and PNG. To open and display with those formats, we need help of ImageTk and Image classes from PIL(photo imaging Library) package.
image1 = ImageTk.PhotoImage(Image.open(random.choice(dice)))

# construct a label widget for image
label1 = tkinter.Label(root, image=image1)
# packing a widget in the parent widget
#The expand option tells the manager to assign additional space to the widget box
label1.pack(expand=True)

# function activated by button
def rolling_dice():
    image2= ImageTk.PhotoImage(Image.open(random.choice(dice)))
    # update image
    #widget's config method is used to modify its options at any time, instead of passing them all to the object's constructor.
    label1.configure(image=image2)
    # keep a reference
    label1.image = image2


# adding button, and command will use rolling_dice function
button = tkinter.Button(root, text='Roll the Dice', fg='blue', command=rolling_dice)

# pack a widget in the parent widget
button.pack(expand=True)

# call the mainloop of Tk
# keeps window open
root.mainloop()