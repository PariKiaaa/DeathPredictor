#libraries
from tkinter import *
from tkinter import ttk
from random import randint
from datetime import datetime

#make a window
YEAR = []
win = Tk()
win.geometry("500x500")
win.title("پیشگوی مرگ")
win.iconbitmap("local-idiot-dies-understandable-death-1.ico")
win.resizable(0,0)

#calculate the jalali year
def gregorian_to_jalali(gy, gm, gd):
 g_d_m = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]
 if (gm > 2):
  gy2 = gy + 1
 else:
  gy2 = gy
 days = 355666 + (365 * gy) + ((gy2 + 3) // 4) - ((gy2 + 99) // 100) + ((gy2 + 399) // 400) + gd + g_d_m[gm - 1]
 jy = -1595 + (33 * (days // 12053))
 days %= 12053
 jy += 4 * (days // 1461)
 days %= 1461
 if (days > 365):
  jy += (days - 1) // 365
  days = (days - 1) % 365
 if (days < 186):
  jm = 1 + (days // 31)
  jd = 1 + (days % 31)
 else:
  jm = 7 + ((days - 186) // 30)
  jd = 1 + ((days - 186) % 30)
 return [jy, jm, jd]

#show the result
def check():
    BirthYear = YEAR[-1]
    for widget in win.winfo_children():
        widget.destroy()
    year = gregorian_to_jalali(datetime.now().year,datetime.now().month,datetime.now().day)[0]
    # print(int(BirthYear.get()))
    try:
        DeathAge = randint(year-int(BirthYear.get()),100)
        if DeathAge>0:
            Label(win, text="شما تنها تا {} سالگی زنده می مانید".format(DeathAge),bg='black',fg= 'red', font=("B Jalal", 20, "bold")).place(relx=.5, rely=.5,anchor= CENTER)
            win.configure(background='black')
        else:
            Label(win, text="اطلاعات وارد شده نادرست است",bg='orange',fg= 'red', font=("B Jalal", 20, "bold")).place(relx=.5, rely=.5,anchor= CENTER)
            Undo=Button(win,text="برگشت",width=5,font=("B Jalal", 10, "bold"),command=main).place(x=210,y=350)

            win.configure(background='orange')
    except Exception as e:
            print(e)
            Label(win, text="اطلاعات وارد شده نادرست است",bg='orange',fg= 'red', font=("B Jalal", 20, "bold")).place(relx=.5, rely=.5,anchor= CENTER)
            win.configure(background='orange')
            Undo=Button(win,text="برگشت",width=5,font=("B Jalal", 10, "bold"),command=play).place(x=210,y=350)

#restart the profram
def play():

    #clear the window
    for widget in win.winfo_children():
        widget.destroy()

    EnterNameText=Label(win, text=":نام خود را وارد کنید",bg='#643c61',fg= 'white',font=("B Jalal", 20 ,"bold")).place(x=290,y=10)
    win.configure(background='#643c61')

    Name=StringVar()
    EnterName= Entry(win, width= 15, textvariable=Name, justify='right',font=('B Traffic', 13)).place(x=350,y=60)
    
    ChooseGenderText=Label(win, text=":جنسیت خود را وارد کنید",bg='#643c61',fg= 'white', font=("B Jalal", 20, "bold")).place(x=245,y=110)
    Gender = StringVar()
    EnterGender = ttk.Combobox(win,width=10,values=("خانم","آقا"),justify='right',font=('B Traffic', 13),textvariable=Gender).place(x=375,y=160)
    # EnterGender = ttk.Combobox(win,width=5,values=("مذکر","مونث"),justify='right',font=('B Traffic', 13),textvariable=Gender).place(x=420,y=160)
    
    ChooseTheYearOfBirthText=Label(win, text=":سال تولد خود را وارد کنید",bg='#643c61',fg= 'white', font=("B Jalal", 20, "bold")).place(x=235,y=210)
    BirthYear=StringVar()
    YEAR.append(BirthYear)
    ChooseTheYearOfBirth = Entry(win, width= 15, textvariable=BirthYear, justify='right',font=('B Traffic', 13)).place(x=350,y=260)
    
    Confirm=Button(win,text="تایید",width=5,font=("B Jalal", 20, "bold"),command=check).place(x=210,y=350)
    Label(win, text="PariKia",bg='#643c61',fg= 'red', font=("Copperplate Gothic Bold", 15)).pack(anchor = "s", side = "left")
    win.mainloop()

play()
