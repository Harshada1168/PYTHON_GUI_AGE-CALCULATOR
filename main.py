from tkinter import *
from datetime import *
App=Tk()
App.geometry("300x300")
App.title("Age Calculator")
msg=Label(App, text="Enter your date of birth")
msg.grid(row=1, column=0, columnspan=3)

day=Label(App, text='Day: ')
dayI=Entry(App, width=3)

month=Label(App, text='Month: ')
monthI=Entry(App, width=3)

year=Label(App, text='Year: ')
yearI=Entry(App, width=5)

day.grid(row=2, column=0)
dayI.grid(row=2, column=1)
month.grid(row=2, column=2)
monthI.grid(row=2, column=3)
year.grid(row=2, column=4)
yearI.grid(row=2, column=5)


def findDays():
    date=int(dayI.get())
    mon=int(monthI.get())
    yr=int(yearI.get())
    dob=datetime(day=date, month=mon, year=yr)
    time_now=datetime.now()
    time_dff=time_now-dob
    dys=Label(App, text="You lived: " + str(time_dff.days)+"days!")
    dys.grid(row=6, column=1, columnspan=4)

def findSec():
    date = int(dayI.get())
    mon = int(monthI.get())
    yr = int(yearI.get())
    dob = datetime(day=date, month=mon, year=yr)
    time_now = datetime.now()
    time_dff = time_now - dob
    dys = Label(App, text="You lived: " + str(time_dff.total_seconds())+"seconds!")
    dys.grid(row=8, column=1, columnspan=6)

B=Button(App, text="Total days", command=findDays)
B.grid(row=5, column=0)
B1=Button(App, text="Total seconds", command=findSec)
B1.grid(row=5, column=1)
App.mainloop()