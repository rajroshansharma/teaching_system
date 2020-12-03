from tkinter import *
from gtts import gTTS
import os
def speak_now():
    line_ing = user_input.get()
    language = 'en'
    obj = gTTS(text=line_ing,lang=language,slow=FALSE)
    obj.save("pro.mp3")
    os.system("pro.mp3")


main_root = Tk()
main_root.title("Teaching assistant")
main_root.geometry("1145x552")
Label(text = "Welcome to our Teaching assistant",bg = "green2",font = "arial 29 bold",padx = 610,pady = 50).pack()
Label(text = "Enter your text !",font = "arial 15 bold").pack(pady=5)
# variable for the string input

user_input = StringVar()
user_value = Entry(main_root,textvariable = user_input,bg = "grey19",fg="white",font = "arial 15") # submutting the values

# place concept helps to arrange the elements in the coordinate manner.

user_value.place(x=520,y=200,width=500,height=200)
b2 = Button(bg = "pink",text = "Speak now",padx=5,pady=5,command=speak_now)
b2.place(x=730,y=380)


main_root.mainloop()