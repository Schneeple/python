from Tkinter import *

# root = Tk()

# root is the object, and Tk is the class

# ...# to create basic tezt in a GUI it is called a Label.
# ...# gonna first put the text on theLabel on the root which is calledf the root.
# ...# next it you will need to assign what theLabel is going to say.

# theLabel = Label(root, text="This is the easiest thing ever")


# ...# Now where do you want to put it ( layout, qhgere you want them on the GUI)
# ...# .pack is the function to use to just pack that object in there, just really put it in there.

# theLabel.pack()


# ...# Whatever you do, you need to put that GUI on the screen a a long lentgh of time.
# ...# mainloop() function will run it infinitely.   :)


# root.mainloop()




# --------------------------------------------------------------------------------------


# root=Tk()
# 
# topFrame = Frame(root)
# topFrame.pack()
# bottomFrame = Frame(root)
# bottomFrame.pack(side=BOTTOM)
# 
# button1=Button(topFrame, text="press here for titties", fg="red")
# button2=Button(topFrame, text="press here for poop", fg="brown")
# button3=Button(topFrame, text="press here for your mom", fg="pink")
# button4=Button(bottomFrame, text="press here for ass", fg="yellow")
# 
# button1.pack(side=LEFT)
# button2.pack(side=LEFT)
# button3.pack(side=LEFT)
# button4.pack(side=BOTTOM)
# 
# 
# root.mainloop()



# --------------------------------------------------------------------------------------
# How to create a username and password prompt

# root=Tk()
#
# label_1 = Label(root, text="Name")
# label_2 = Label(root, text="Password")
#
# entry_1=Entry(root)
# entry_2=Entry(root)
#
# label_1.grid(row=0, sticky= E)
# label_2.grid(row=1)
#
# entry_1.grid(row=0,column=1)
# entry_2.grid(row=1, column=1)
#
# checkbox= Checkbutton(root, text="check if you want to fuck my big boy")
# checkbox.grid(columnspan=2)
#
#
# root.mainloop()



# ---------------------------------------------------------------------------------------------------
# Using a function to make an interactive button in terminal window below.

# root= Tk()
#
# def printName(event):
#     print "Hello you pervert!"
#
# button_1=Button(root,text="Click here for titties")
# button_1.bind("<Button-1>", printName)
# button_1.pack(side=LEFT)
#
#
# root.mainloop()

# ---------------------------------------------------------------------------------------------------
# Using multiple fuctions to provide three different clicking styles with functions
# root=Tk()

# def leftClick(event):
#     print"Left"
#
# def rightClick(event):
#     print "right"
#
# def middleClick(event):
#     print "Middle"
#
# frame= Frame(root, width=300, height= 250)
# frame.bind("<Button-1>", leftClick)
# frame.bind("<Button-2>",middleClick)
# frame.bind("<Button-3>",rightClick)
#
# frame.pack()
# root.mainloop()


# ---------------------------------------------------------------------------------------------------
# Using classes to make GUI

# #
# class ColtonsButtons:
#
#     def __init__(self,master):
#         frame=Frame(master)
#         frame.pack()
#
#         self.printButton = Button(frame, text="Click here for ass", command=self.printMessage)
#         self.printButton.pack(side=LEFT)
#
#         self.quitButton = Button(frame, text="Quit", command=frame.quit)
#         self.quitButton.pack(side=LEFT)
#
#     def printMessage(self):
#         print "Pervert!"
#
# root = Tk()
# objectmade=ColtonsButtons(root)
# root.mainloop()

# ----------------------------------------------------------------------------------------LESSON 9----
# toottips bar, drop down menu, and icon bar




root=Tk()

root.mainloop()

