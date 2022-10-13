from tkinter import *

window = Tk()
window.title("My first GUI program")
window.minsize(width = 500, height=300)

def button_clicked():
    print("I got clicked!")
    new_text = input.get()
    my_label.config(text=new_text)

#label
my_label = Label(text="I am a Label", font=("Arial", 24, "bold"))

#my_label.place(x=100, y=0)
#my_label.pack()

#Entry
input = Entry(width=15)
#input.pack()

#button
button = Button(text="Click Here", command=button_clicked)
#button.pack()



window.mainloop()