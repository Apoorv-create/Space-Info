from tkinter import *
from PIL import ImageTk, Image
from tkinter import ttk

root = Tk()
root.title("Planet Info")
root.geometry("400x400")

Mercury = ImageTk.PhotoImage(Image.open("P:\\Planet Info Python Project\\mercury.jpg"))
Venus = ImageTk.PhotoImage(Image.open("P:\\Planet Info Python Project\\venus.jpg"))
Earth = ImageTk.PhotoImage(Image.open("P:\\Planet Info Python Project\\earth.jpg"))


label_planet = Label(root, text = "Planet : ", bg = "lightblue")
label_planet_name = Label(root, font=("courier", 18, "italic"),bg = "lightblue")
label_planet_image = Label(root, bg = "gold", highlightthickness = 5, borderwidth = 1, relief = SOLID)
label_planet_gravity_radius = Label(root, font=("castellar"), bg = "lightblue")
label_planet_info = Label(root, font=("Sanssarif"), bg = "lightblue")


planets=["mercury", "venus", "earth"]
selectedval = StringVar()
dropdown = ttk.Combobox(root, values = planets, textvariable = selectedval)

def planetinfo():
    planet = selectedval.get()
    
    if planet == "mercury":
        label_planet_name['text'] = "Mercury"
        label_planet_image['image'] = Mercury
        label_planet_gravity_radius['text'] = "Gravity: 3.7 m/s \n Radius: 2,439.7km"
        label_planet_info['text'] = "Mercury is the smallest planet in our solar system and closest to the sun, its just slightly bigger than the earth's moon."
        
    elif planet == "venus":
        label_planet_name['text'] = "Venus"
        label_planet_image['image'] = Venus
        label_planet_gravity_radius['text'] = "Gravity: 8.87 m/s \n Radius: 6,051.8km"
        label_planet_info['text'] = "Venus is the most bright object in our solar system after the sun, it has a thin atmosphere too."
        
    elif planet == "earth":
        label_planet_name['text'] = "Earth"
        label_planet_image['image'] = Earth
        label_planet_gravity_radius['text'] = "Gravity: 9.807 m/s \n Radius: 6,371km"
        label_planet_info['text'] = "The Blue planet, Is where we all reside."
        
    
dropdown.place(relx = 0.5, rely = 0.1, anchor=CENTER)
    
        
    

btn = Button(root, text = "show info!", command=planetinfo)
btn.place(relx = 0.5, rely = 0.18, anchor=CENTER)

label_planet.place(relx = 0.2, rely = 0.1, anchor=CENTER)
label_planet_name.place(relx = 0.5, rely = 0.25, anchor=CENTER)
label_planet_image.place(relx = 0.5, rely = 0.5, anchor=CENTER)
label_planet_gravity_radius.place(relx = 0.5, rely = 0.8, anchor=CENTER)
label_planet_info.place(relx = 0.5, rely = 0.9, anchor=CENTER)

root.mainloop()