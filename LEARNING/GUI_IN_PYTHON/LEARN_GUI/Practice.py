from tkinter import *

window = Tk() #Create window
window.title("Genetic Algorithm") #Create title

myEntry = Entry(window, width = 40, borderwidth= 2) #Create text box
myEntry.grid(row=0, column=0, columnspan=5, padx=10, pady=10)
myEntry.pack()








myButton = Button(window,text = "Enter String", fg = "blue", bg = "white")

myButton.pack()
window.mainloop()