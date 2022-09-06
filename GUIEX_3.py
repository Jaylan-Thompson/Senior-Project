import tkinter as tk
from PIL import ImageTk, Image

#first menu option
options1 = { "":"",
            "X-Cubed":"",   #this line options1 variable
            "X5-Cubed":"",
            "X-Squared":"",
            "X-Mod5":"",
            "Mod5":"",
            "X-SquaredMod7":"",
            "X-CubeMod7":"",
            "X Mod7 in Z7":"",
            "X Mod11 in Z11":"",
            "X SquaredMod11 in Z11":"",
            "X CubedMod11 in Z11":"",
           }

#second menu option
options2 = {   #this line contain option 2 variable
# menu name: url of image to show
"Curve_1": "UpGraph1.jpeg",
"Curve_2": "UpGraph4.jpeg",
"Curve_3": "UpGraph6.jpeg",
"Curves_4": "UpGraph13.jpeg", #circle 
"Field_1":"X5cubeGraph.jpeg",
"Field_2":"XcubeMod5Graph.jpeg",
"Field_3":"Xmod5Graph.jpeg",
"Field_4":"XsquareMod5Graph.jpeg",
"Field_5":"Mod5Graphs.jpeg", #fix this one later 
"Field_6": "AVGraph.jpeg",
"Field_7":"XsquareMod7Graph.jpeg",# THIS ONE IS KINDA HARD TO SEE
"Field_8":"XMod7Graph.jpeg",
"Field_9":"XcubeMod7.jpeg",
"Field_10":"AVXMod7Graph.jpeg",
"Field_11":"XMod11Graph.jpeg",
"Field_12":"XsquareMod11Graph.jpeg",
"Field_13":"XcubeMod11Graph.jpeg",
}

#window and window color
app = tk.Tk()
app.configure(bg='black')
# set the app geometry (size of the window)
app.geometry('850x750')
options_dict = {}

# store actual images in the second menu

for menu in options2:
    options_dict[menu] = ImageTk.PhotoImage(Image.open(options2[menu]))

# use varibale to display menu

Button1 = tk.StringVar(app)   #Making variable1 for option1 
Button2=tk.StringVar(app)  #Making variable2 for option 2

Button1.set("")
Button2.set("")

# when the option is changed this function will be called.
def change_image(e):
# Change image here
  image.config(image=options_dict[e])

# create menu options
opt = tk.OptionMenu(app, Button1, *list(options1.keys()))
opt.config(width=100, font=("Arial", 25))
opt.pack()

#create second menu option
opt = tk.OptionMenu(app, Button2, *list(options2.keys()), command=change_image)
opt.config(width=100, font=("Arial", 25))
opt.pack()

# create a label to show image
image = tk.Label(app)
image.pack()

# run the application
app.mainloop()