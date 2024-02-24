#import tkinter
#or
from tkinter import * #this is preventing tkinter. writing
window = Tk() #create window
""" def Hello():
    print('Hello World')


window.title("New Application") #name of application
b1 = Button(window, text= "Click on",state=DISABLED,borderwidth=20) #it cannot visible
b2 = Button(window, text= "Click on",command=Hello,bg='#FFD733',fg='green',borderwidth=8) #it cannot visible #hexadecimal color palette
#b1. pack() #this show the button
#b2.pack()

#direction
#b1.pack(padx=20,pady=30)
#b2.pack(padx=15,pady=10)

#create label
l = Label(window,text="Hello World",bg='yellow',fg='red')
c = Canvas(window,width=300,height=100)
d = Canvas(window,width=300,height=100)
c.pack()
d.pack()
d.create_line(0,30,100,30,fill='red',dash=24)
c.create_line(50,30,50,130,fill='blue',dash=24)
c.coords(1,30,20,30,100) #change coordinate
e = Canvas(window, width=300,height=150)
e.pack()
e.create_rectangle(20,30,100,90,fill='red')
f = Canvas(window, width=300,height=150)
f.pack()
f.create_oval(20,30,100,90,fill='yellow')
g = Canvas(window, width=300,height=150)
g.pack()
g.create_polygon(10,20,30,100,90,50,outline='green')
c.itemconfig(1)
c.delete(1) #or ALL
l.pack()
b1.pack(side=LEFT,padx=5)
e = Canvas(window,width=300,height=150,bg='purple')
e.pack()
img = PhotoImage(file="Pictures/py.png")
e.create_image(100,100,image=img)
#b2.pack(side=RIGHT) """
y = Canvas(window,width=300,height=300)
y.pack(side=RIGHT,padx=150,pady=150)
y.create_text(200,200,text="Hello GUI",font='Algerian')
z = Canvas(window,width=300,height=150)
z.pack()
bitmaps = ["error","gray12","gray25","gray50","gray75","hourglass","info","questhead","question","warning"]
z.create_bitmap(50,50,bitmap = bitmaps[5])
p = Canvas(window,width=300,height=150)
p.pack()
p.create_arc(20,20,200,200,start = 0,extent = 180, fill ='red')
#exist = IntVar()
exist = StringVar()
cb = Checkbutton(window,text='Choice',variable=exist,onvalue='RGB',offvalue='L')
cb.pack()
Label(window,text="C",bg ='red',fg='black',width=10,height=5,border=10).pack(side=LEFT,fill='x')
Label(window,text="A",bg ='green',fg='white',width=10,height=5,border=10).pack(side=LEFT,fill='y')
Label(window,text="R",bg ='blue',fg='purple',width=10,height=5,border=10).pack(side=LEFT,fill='x')
#or
#b2.place(x=100,y=100,width=100,height= 50) #pixel
#window.iconbitmap('Pictures/py.png') #favicon
window.mainloop() #prevent close the window
