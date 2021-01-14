from tkinter import * 
from tkinter import ttk 
import sqlite3 
from PIL import ImageTk,Image
#Creates a window of a particular size
root = Tk()
root.title("Find a gas station near you")
root.geometry('800x650')

#Dropdown Box

def selected(event):
    MyLabel = Label(root, text=clicked.get()).pack()


#East Toronto Gas Station Locations


    if clicked.get() == 'East Toronto' : 
       myLabel = Label(root, text="Ultramar, 1121 Broadview Avenue, M4K 2S4, Open 24 Hours").pack()
   
    if clicked.get() == 'East Toronto' :
    	myLabel = Label(root, text="Tonka Gas Bar, 854 Pape Avenue, M4K 3T8, Open 6 a.m - 12 a.m").pack()

    if clicked.get() == 'East Toronto' :
    	myLabel = Label(root, text="Shell, 521 O'Connor Drive, M4J 2W6, Open 24 Hours").pack()

    if clicked.get() == 'East Toronto' :
    	myLabel = Label(root, text="HUSKY, 30 Larid Drive, M4G 3S8, Open 6 a.m - 12 p.m").pack()
   
    if clicked.get() == 'East Toronto' :
        myLabel = Label(root, text="GLOBAL, 381 Sammon Avenue, M4J 2X8, Open 6:30 a.m - 6:30 p.m").pack()

    if clicked.get() == 'East Toronto' :
        myLabel = Label(root,text="Sun Gas Services, 1200 Queen Street East, M4M 1L7, Open 24 Hours").pack()

#West Toronto Gas Stations
    if clicked.get() == 'West Toronto' :
    	myLabel = Label(root, text="Dundas Gas Bar, 1715 Dundas Street West, M6K 1V4, Open 6 a.m - 10 p.m").pack()

    if clicked.get() == 'West Toronto' :
    	myLabel = Label(root, text="1750 Bloor Street West, M6P 1B3, Open 24 Hours").pack()

    if clicked.get() == 'West Toronto' :
    	myLabel = Label(root, text="KEELE STREET GAS & WASH, 537 Keele Street, M6N 3E4, Open 24 Hours").pack()

    if clicked.get() == 'West Toronto' :
    	myLabel = Label(root, text="Lambert Oil, 2145 Dundas Street West, M6R 1X1, Open 24 Hours").pack()

#North Toronto Gas Stations

    if clicked.get() == 'North Toronto' :
    	myLabel = Label(root, text="ESSO CRIClE K, 381 Mount Pleasent Road, M4S 2L5, Open 6 a.m - 12 a.m").pack()

    if clicked.get() == 'North Toronto' :
    	myLabel = Label(root, text="Petro-Canada, 1021 Avenue Road, M5P 2K9, Open 24 hours").pack()

    if clicked.get() == 'North Toronto' :
    	myLabel = Label(root, text="Shell, 2075 Bathurst Street, M6A 1Z9, Open 24 Hours").pack()

    if clicked.get() == 'North Toronto' :
    	myLabel = Label(root, text="453 Wilson Avenue, M3H 1T9, Open 6 a.m - 10 p.m").pack()

#Downtown Toronto Gas Stations

    if clicked.get() == 'Downtown Toronto' :
    	myLabel = Label(root, text="7-Eleven, 873 Queen Street West, M6J 1G4, Open 24 Hours").pack()

    if clicked.get() == 'Downtown Toronto' :
    	myLabel = Label(root, text="CORKTOWN ESSO, 176 Front Street East,  M5A 1E6, Open 6 a.m - 1 a.m ").pack()

    if clicked.get() == 'Downtown Toronto' :
    	myLabel = Label(root, text="Canadian Tire Gas+, 835 Young Street, M4W 2H2, Open 24 Hours").pack()

    if clicked.get() == 'Downtown Toronto' :
    	myLabel = Label(root, text="Circle K, 1110 Bathurst Street, M5R 3H2, Open 24 Hours").pack()










    #else:
    	#MyLabel = Label(root, text="This is the end of the list for your chosen area").pack()






	


options = [
         "East Toronto",
         "West Toronto",
         "North Toronto",
         "Downtown Toronto",
]   

clicked = StringVar()
clicked.set("East Toronto")

drop = OptionMenu(root, clicked, *options, command=selected)
drop.pack()

#New Window
def open():
  global my_img
  top = Toplevel()
  my_img = ImageTk.PhotoImage(Image.open("6ix.jpg"))
  my_label = Label(top, image=my_img).pack()
  btn2 = Button (top, text="close window", command=top.destroy).pack()

btn = Button(root, text="Open Overall Toronto Map", command=open).pack()

#Downtown Toronto New Window
def open():
    global my_img1
    top = Toplevel()
    my_img1 = ImageTk.PhotoImage(Image.open("dt.jpeg"))
    my_label = Label(top, image=my_img1).pack()
    btn3 = Button (top, text="close window", command=top.destroy).pack()

btn2 = Button(root, text="Open Downtown Toronto Map", command=open).pack()

#East York Map
def open():
    global my_img1
    top = Toplevel()
    my_img1 = ImageTk.PhotoImage(Image.open("eastyork.gif"))
    my_label = Label(top, image=my_img1).pack()
    btn5 = Button (top, text="close window", command=top.destroy).pack()

btn4 = Button(root, text="Open East York Map", command=open).pack()






  






#MyButton = Button(root, text="select from list", command=selected)
#MyButton.pack()

root.mainloop()

