#pip install speedtest-cli
from tkinter import *
import speedtest

def speedcheck():
    sp = speedtest.Speedtest()
    sp.get_servers()
    down = str( round(sp.download()/(10**6),3))+" Mb/S"
    up = str( round(sp.upload()/(10**6),3))+" Mb/S"
    lab_down.config(text=down)
    lab_up.config(text=up)


sp = Tk()

sp.title("Internet Speed")
sp.geometry("500x650")
sp.config(bg = "skyblue")

lab = Label(sp,text = "Internet Speed Test ",font =("Time New Roman",30,"bold"),bg= "skyblue",fg="black")
lab.place(x=55,y=40,height=50,width=380)

lab = Label(sp,text = "Download Speed ",font =("Time New Roman",30,"bold"),fg="black")
lab.place(x=55,y=130,height=50,width=380)

lab_down = Label(sp,text = "00",font =("Time New Roman",30,"bold"),fg="black")
lab_down.place(x=55,y=200,height=50,width=380)

lab = Label(sp,text = "Upload Speed ",font =("Time New Roman",30,"bold"),fg="black")
lab.place(x=55,y=290,height=50,width=380)

lab_up = Label(sp,text = "00",font =("Time New Roman",30,"bold"),fg="black")
lab_up.place(x=55,y=360,height=50,width=380)

button = Button(sp,text= "check speed",font =("Time New Roman",30,"bold"),relief=RAISED,command=speedcheck)
button.place(x=55,y=460,height=50,width=380)

sp.mainloop()