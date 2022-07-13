#Import tkinter(default downloaded object)
from tkinter import *

#Build window with a default min size, close is stopped using .mainloop()
window = Tk()
window.title("First GUI Program")
window.minsize(width=500, height=500)
window.config(padx=25, pady=80)

#Label
my_label = Label(text="I am a Label", font=("Arial", 24, "bold"))
my_label.config(text="New Text")
my_label.grid(column=0, row=0)
#function called when clicking button, takes input and fstring result
def button_clicked():
    print("I got clicked")
    users_entry = input.get()
    my_label.config(text=f"{users_entry} boi")

#action button
button = Button(text="Click Me!", command=button_clicked)
button.grid(column=1, row=0)

#Entry
input = Entry(width=12 )
input.insert(END, string="Defaulting")
input.grid(column=0, row=1)

#textbox input
text = Text(height=5, width=40)
text.focus()
text.insert(END, "This is some default.")
print(text.get("1.0", END))
text.grid(column=2, row = 1)

# #spin box or num input given range and command takes current value
# def spinbox_used():
#     print(spinbox.get())
# spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_used)
# spinbox.pack()

#Scale bar input used to get input from a range
def scale_used(value):
    print(value)
scale = Scale(from_=0, to=100, command=scale_used)
scale.grid(column=3, row= 0)


# #CheckBox given value and defaulted value
# def checkbox_user():
#     print(checked_state.get())
# checked_state = IntVar()
# checkbox = Checkbutton(text="Is on?", variable=checked_state, command=checkbox_user)
# checked_state.get()
# checkbox.pack()


# #radioButtons
# def radio_user():
#     print(radio_user.get())
#     radio_state = IntVar()
#     radiobutton1 = Radiobutton(text="Option 1", value=1, variable=radio_user)
#     radiobutton2 = Radiobutton(text="Option 2", value=2, variable=radio_user)
#     radiobutton1.pack()
#     radiobutton2.pack()


#Listbox
def list_user(value):
    print(value)
boxy = Listbox(height=3)
fruits = ["Apple", "Pear", "Plum", "Orange", "Watermelon"]
for item in fruits:
    boxy.insert(fruits.index(item), item)
boxy.bind("<<ListboxSelect>>", list_user)
boxy.grid(column=0, row=3)



window.mainloop()