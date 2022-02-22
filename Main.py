from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Planet Info")
root.geometry("400x400")


#image2 =Image.open('C:\\Users\\adminp\\Desktop\\titlepage\\front.gif')
#image1 = ImageTk.PhotoImage(image2)
#w = image1.width()
#h = image1.height()

#bg = PhotoImage(file = "C:\\space.jpg")
#root.configure(background = bg)

#canv = Canvas(root, width=80, height=80, bg='white')
#canv.grid(row=2, column=3)

#img = PhotoImage(file="C:\\\space.jpg")
#canv.create_image(20,20, anchor=NW, image=img)

label_planet = Label(root, text = "Planet : ", bg = "darkblue")
label_planet_name = Label(root, font=("courier", 18, "italic"),bg = "darkblue")
label_planet_image = Label(root, bg = "gold", highlightthickness = 5, borderwidth = 1, relief = SOLID)
label_planet_gravity_radius = Label(root, font=("castellar"), bg = "darkblue")
label_planet_info = Label(root, font=("Sanssarif"), bg = "darkblue")

def planetinfo():
    pass

btn = Button(root, text = "show info!", command=planetinfo)
btn.place(relx = 0.5, rely = 0.18, anchor=CENTER)

label_planet.place(relx = 0.2, rely = 0.1, anchor=CENTER)
label_planet_name.place(relx = 0.5, rely = 0.25, anchor=CENTER)
label_planet_image.place(relx = 0.5, rely = 0.5, anchor=CENTER)
label_planet_gravity_radius.place(relx = 0.5, rely = 0.8, anchor=CENTER)
label_planet_info.place(relx = 0.5, rely = 0.9, anchor=CENTER)

root.mainloop()