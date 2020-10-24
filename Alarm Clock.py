from tkinter import *
import time as dt
root=Tk()
root.title("Alarm Clock")
root.geometry("500x500")
mb = Menubutton(root,text="File",relief= RAISED)
mb = Menubutton(root,text="Tools",relief= RAISED)
mb = Menubutton(root,text="Exit",relief= RAISED)
mb.pack()

menubar = Menu(root)

# mb.grid()
# mb.menu = Menu(mb,tearoff=0)
# mb["menu"] = mb.menu
# filemenu = Menu(menubar,tearoff=0)
# filemenu.add_command(label="New")
Label1=Label(root,text=dt.ctime()).pack()

#root.config(menu=menubar)
root.mainloop()
