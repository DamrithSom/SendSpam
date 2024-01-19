from tkinter import * 
import pyautogui as auto
from tkinter import messagebox
import time
def help():
    messagebox.showinfo("about me",
                        "copyright 2023\nCreate By <Damrith 2023>")
def limit10(): # function for send spam loop 10 
    for a in range(10):
        show = auto.write(inputValue.get())
        textInfor.insert(0.0, str(inputValue.get()))
        auto.press("enter")
def limit25(): # function for send spam loop 25
    for b in range(25):
        auto.write(inputValue.get())
        textInfor.insert(0.0, str(inputValue.get()))
        auto.press("enter")
def limit50(): # function for send spam loop 50
    for c in range(50):
        auto.write(inputValue.get())
        textInfor.insert(0.0, str(inputValue.get()))
        auto.press("enter")
def limit100(): # function for send spam loop 10
    for d in range(100):
        auto.write(inputValue.get())
        textInfor.insert(0.0, str(inputValue.get()))
        auto.press("enter")
def sendSMS(): #function for send SMS 
    selected_option = var.get() # creareVariable selected_option
    if selected_option == 1:
        time.sleep(3)
        limit10()
    elif selected_option ==2:
        time.sleep(3)
        limit25()
    elif selected_option ==3:
        time.sleep(3)
        limit50()
    elif selected_option ==4:
        time.sleep(3)
        limit100()
#def Clear():  #funtion clear input and text add 
 #   inputValue.delete("1.0","end")
windowns = Tk()
var = IntVar()
windowns.geometry("400x400") # size form windows 400x400
windowns.resizable(0,0)
windowns.title("Send SMS Boom") # set title name "send sms boom"
windowns.configure(bg="lightslategrey") # set background color "lightslategrey"
# lable for show text "welcom to send sms spamming"
textFile = Label(windowns, text="Welcome to Send SMS Spamming!",
                 fg="red",
                 bg="lightslategrey",
                 font=(5),).pack()
showHelp = Button(windowns, text="?", bg="lightslategrey",command=help)
showHelp.place(x=350, y=0)
# createLabel for show text "Type Message"
textType = Label(windowns, text="Type Message: ", 
                 bg="lightslategrey",
                 fg="navy",font=(1))
textType.place(x=5, y=50)
inputValue = Entry(windowns, width=31, 
                   fg="green",bd=3)
inputValue.place(x=130, y=50,)
textLimit = Label(windowns, text="Limit: ", 
                 bg="lightslategrey",
                 fg="navy",font=(1))
textLimit.place(x=5, y=95)
radioButton10 = Radiobutton(windowns, text="Limit 10", 
                          variable=var,value=1,
                          bg="lightslategrey",
                          fg="gold",font=(1))
radioButton10.place(x=130, y=95)
radioButton25 = Radiobutton(windowns, text="Limit 25", 
                          variable=var,value=2,
                          bg="lightslategrey",
                          fg="gold",font=(1))
radioButton25.place(x=225, y=95)
radioButton50 = Radiobutton(windowns, text="Limit 50", 
                          variable=var,value=3,
                          bg="lightslategrey",
                          fg="gold",font=(1))
radioButton50.place(x=130, y=120)
radioButton100 = Radiobutton(windowns, text="Limit 100", 
                         variable=var, value=4,
                          bg="lightslategrey",
                          fg="gold",font=(1))
radioButton100.place(x=225, y=120)
buttonClear = Button(windowns, text="Clear", 
                     fg="white",
                     bg="red",font=('arial'),width=5,
                     command=lambda:textInfor.delete("1.0", "end"))
buttonClear.place(x=130, y=160)
buttonSend = Button(windowns, text="Send", 
                     fg="white",
                     bg="green",font=('arial'),width=5,
                     command=sendSMS)
buttonSend.place(x=250, y=160)
textInfor = Text(windowns,width=35, height=10, fg="green")
textInfor.place(x=105,y=225)
windowns.mainloop()