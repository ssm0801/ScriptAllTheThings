import tkinter as tk
from tkinter import filedialog
from tkinter.filedialog import asksaveasfile
from tkinter.colorchooser import askcolor
import pywhatkit
import os

#WINDOW
w = tk.Tk()
w.title(60*" "+ "Text to Handwriting")
w.config(bg="Grey")
w.geometry("800x700")

#FONTS
font30t = ("Courier New",25,"bold")
font30h = ("Freestyle Script",40)
font15 = ("Courier New",15,"bold")
font10 = ("Comic Sans MS",10,"bold")

#variables used
color=[] #color of the handwriting
folder="" #folder where the handwriting image would be saved 

#HEADING
l01 = tk.Label(w, text="Type anything and",background="Black",foreground="White",font=font30t)
l01.pack(fill="x")  
l02 = tk.Label(w, text="Convert it into Handwriting",background="Black",foreground="White",font=font30h)
l02.pack(fill="x")  
                
#user gives input
l1 = tk.Label(w, text="Type your text here",background="Grey",font=font15)
l1.pack(pady=20)
tb1 = tk.Text(w,relief="groove",bd=3,height=10,width=50)
tb1.pack()

#give name to generated handwriting
l2 = tk.Label(w, text="Give the handwriting a cool name",background="Grey",font=font15)
l2.pack(pady=20)
e1 = tk.Entry(w,relief="groove",bd=3,width=50)
e1.pack()  

#COLOR PICKER AND FOLDER SELECTOR

def choose_color_and_save(): 
    color = askcolor(title="Tkinter Color Chooser") 
    color0 = [int(i) for i in color[0]] #store the rgb format of color
    
    folder = filedialog.askdirectory(initialdir=os.path.normpath("C://"), title="Choose folder")
    folder = folder.split("/")
    folder = "//".join(folder)
    location = folder + "/" + e1.get() + ".png" #path and name of file to be saved
    
    content = tb1.get("1.0","end")#the text given as input
    
    pywhatkit.text_to_handwriting(content,location,color0) #generate and save handwriting
    
    l3.config(text="!!!File Saved Successfully ... Check it out!!!")

# BUTTON TO CHOOSE COLOR AND SAVE FILE    
b2=tk.Button(w,text="Choose Handwriting Color and Save File",background="Orange",foreground="Black",font=font10,command=choose_color_and_save)
b2.pack(padx=10,pady=10)

l3 = tk.Label(w, text=" ",background="Grey",font=font15,foreground="Blue")
l3.pack(pady=20)
				
#MAINLOOP
w.mainloop()
