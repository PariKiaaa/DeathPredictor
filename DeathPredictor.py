# Libraries
import tkinter as tk
from tkinter import ttk
from random import randint
from datetime import datetime

class DeathPredictorApp:
    def __init__(self):
        # List to store the entered birth years
        self.YEAR = []
        
        # Initialize the main window
        self.win = tk.Tk()
        self.win.geometry("500x500")
        self.win.title("پیشگوی مرگ")
        self.win.iconbitmap("death.ico")
        self.win.resizable(0, 0)
        
        # Start the main application by calling the play method
        self.play()

    def gregorian_to_jalali(self, gy, gm, gd):
        # Function to convert Gregorian date to Jalali (Persian) date
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

    def calculate_remaining_years(self, birth_year):
        # Function to calculate remaining years until the predicted death age
        current_year = datetime.now().year
        jalali_birth_year = self.gregorian_to_jalali(current_year, datetime.now().month, datetime.now().day)[0]
        remaining_years = jalali_birth_year - int(birth_year)
        return remaining_years if remaining_years > 0 else 0

    def check(self):
        # Function to check the predicted death age based on the user's input
        BirthYear = self.YEAR[-1]  # Get the last entered birth year from the list
        for widget in self.win.winfo_children():
            widget.destroy()  # Clear the window to show the result
        year = self.gregorian_to_jalali(datetime.now().year, datetime.now().month, datetime.now().day)[0]  # Get the current year
        try:
            DeathAge = randint(year - int(BirthYear.get()), 100)  # Generate a random death age based on the user's birth year
            if DeathAge > 0:
                # If the predicted death age is positive, display the result
                tk.Label(self.win, text=f"شما تنها تا {DeathAge} سالگی زنده می‌مانید", bg='black', fg='red',
                         font=("B Jalal", 20, "bold")).place(relx=.5, rely=.5, anchor=tk.CENTER)
                self.win.configure(background='black')
            else:
                # If the predicted death age is non-positive (i.e., incorrect input), show an error message
                tk.Label(self.win, text="اطلاعات وارد شده نادرست است", bg='orange', fg='red',
                         font=("B Jalal", 20, "bold")).place(relx=.5, rely=.5, anchor=tk.CENTER)
                tk.Button(self.win, text="برگشت", width=5, font=("B Jalal", 10, "bold"), command=self.play).place(x=210, y=350)
                self.win.configure(background='orange')
        except Exception as e:
            # Handle any exceptions that may occur during the calculation
            print(e)
            tk.Label(self.win, text="اطلاعات وارد شده نادرست است", bg='orange', fg='red',
                     font=("B Jalal", 20, "bold")).place(relx=.5, rely=.5, anchor=tk.CENTER)
            tk.Button(self.win, text="برگشت", width=5, font=("B Jalal", 10, "bold"), command=self.play).place(x=210, y=350)
            self.win.configure(background='orange')

    def play(self):
        # Function to display the main user interface for entering the data
        for widget in self.win.winfo_children():
            widget.destroy()  # Clear the window

        tk.Label(self.win, text=":نام خود را وارد کنید", bg='#643c61', fg='white', font=("B Jalal", 20, "bold")).place(x=290, y=10)
        self.win.configure(background='#643c61')

        Name = tk.StringVar()
        tk.Entry(self.win, width=15, textvariable=Name, justify='right', font=('B Traffic', 13)).place(x=350, y=60)

        tk.Label(self.win, text=":جنسیت خود را وارد کنید", bg='#643c61', fg='white', font=("B Jalal", 20, "bold")).place(
            x=245, y=110)
        Gender = tk.StringVar()
        ttk.Combobox(self.win, width=10, values=("خانم", "آقا"), justify='right', font=('B Traffic', 13),
                     textvariable=Gender).place(x=375, y=160)

        tk.Label(self.win, text=":سال تولد خود را وارد کنید", bg='#643c61', fg='white', font=("B Jalal", 20, "bold")).place(
            x=235, y=210)
        BirthYear = tk.StringVar()
        self.YEAR.append(BirthYear)  # Add the variable to the list for later access
        tk.Entry(self.win, width=15, textvariable=BirthYear, justify='right', font=('B Traffic', 13)).place(x=350, y=260)

        tk.Button(self.win, text="تایید", width=5, font=("B Jalal", 20, "bold"), command=self.check).place(x=210, y=350)
        tk.Label(self.win, text="PariKia", bg='#643c61', fg='red', font=("Copperplate Gothic Bold", 15)).pack(anchor="s",
                                                                                                             side="left")
        self.win.mainloop()

if __name__ == "__main__":
    # Create an instance of the DeathPredictorApp class and start the application
    app = DeathPredictorApp()
