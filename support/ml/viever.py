import tkinter
from PIL import ImageTk, Image
from os import listdir
import csv

root = tkinter.Tk()
root.title('Learn to code')
# root.geometry('500x500')
# Creating frames
pictures_frame = tkinter.LabelFrame(root, text='Zdjęcie')
pictures_frame.grid(row=0, column=0)
traits_frame = tkinter.LabelFrame(root, text='Cechy')
traits_frame.grid(row=0, column=1, sticky=tkinter.NS)

image_list = [ImageTk.PhotoImage(
    Image.open(f'portraits/{element}').resize(
        (350, 500), resample=Image.ANTIALIAS)) for element in listdir('./portraits')]

image_number = 0
picture_lbl = tkinter.Label(pictures_frame, image=image_list[0])
picture_lbl.grid(row=0, column=0, columnspan=3)
status_lbl = tkinter.Label(root)


def status_bar():
    global status_lbl
    status_lbl.destroy()
    status_lbl = tkinter.Label(
        root,
        text=f'Image {image_number + 1} of {len(image_list)}',
        bd=1, relief=tkinter.SUNKEN,
        anchor=tkinter.E)
    status_lbl.grid(row=3, column=0, columnspan=3, sticky=tkinter.EW, pady=3)


def next():
    global image_number
    global picture_lbl
    if image_number != len(image_list) - 1:
        image_number += 1
        picture_lbl.destroy()
        # picture_lbl.grid_forget()
        picture_lbl = tkinter.Label(pictures_frame, image=image_list[image_number])
        picture_lbl.grid(row=0, column=0, columnspan=3)
    status_bar()


def back():
    global image_number
    global picture_lbl
    if image_number:
        image_number -= 1
        picture_lbl.destroy()
        picture_lbl = tkinter.Label(pictures_frame, image=image_list[image_number])
        picture_lbl.grid(row=0, column=0, columnspan=3)
    status_bar()


status_bar()

button_back = tkinter.Button(pictures_frame, text="<<", command=back)
button_exit = tkinter.Button(pictures_frame, text="EXIT", command=root.quit)
button_next = tkinter.Button(pictures_frame, text=">>", command=next)

button_back.grid(row=1, column=0)
button_exit.grid(row=1, column=1)
button_next.grid(row=1, column=2)

# Traits Frame


def save():
    data_file = open('data.csv', 'a', newline='')
    data_write = csv.writer(data_file)
    data_write.writerow([val.get() for val in traits_ent])
    data_file.close()
    for ent in traits_ent:
        ent.delete(0, tkinter.END)
    next()


def btn_acction(position, value):
    traits_ent[position].delete(0, tkinter.END)
    traits_ent[position].insert(0, value)


# Creating lables in tratis frame
lbl_names_list = ['Wiek:', 'Płeć:', 'WYG:', 'MAJ.:', 'Krzepa']
traits_lbl = [tkinter.Label(traits_frame, text=element) for element in lbl_names_list]
for lbl in enumerate(traits_lbl):
    lbl[1].grid(row=lbl[0], column=0)

# Creating entries in traits frame
traits_ent = [tkinter.Entry(traits_frame) for i in lbl_names_list]
for ent in enumerate(traits_ent):
    ent[1].grid(row=ent[0], column=1)

# Creating level buttons
btn_names_list = [('Młody', 'Dojrzały', 'Stary'),
                  ('Kobieta', 'Mężczyzna'),
                  ('Brzydki/a', 'Przeciętny/a', 'Ładny/a'),
                  ('Biedny/a', 'Kl. Średnia', 'Bogaty/a'),
                  ('Słaba', 'Umiarkowana', 'Silna')
                  ]
for row in enumerate(btn_names_list):
    for name in enumerate(row[1]):
        btn = tkinter.Button(
            traits_frame,
            text=name[1],
            command=lambda row=row, name=name: btn_acction(row[0], name[0]))
        btn.grid(row=row[0], column=name[0]+2, sticky=tkinter.NSEW)

        # Option button_save
button_save = tkinter.Button(traits_frame, text="save", command=save)
button_save.grid(row=5, column=0, columnspan=2, sticky=tkinter.NSEW)

root.mainloop()
