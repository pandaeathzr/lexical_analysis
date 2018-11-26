import tkinter  as tk
import cifafenxi

window = tk.Tk()
window.title('my window')
window.geometry('800x300')

e = tk.Entry(window,width = 300,show = None)
e.pack()


def insert_point():
    var = e.get()
    cifafenxi.lexical_analysis(var)
    t1.insert('insert',var)



b1 = tk.Button(window,text= '词法分析',width = 40,height = 4,command = insert_point)
b1.pack()

t1 = tk.Text(window,height = 10,width = 50)
t1.place(x=40,y=110)

t2 = tk.Text(window,height = 10,width = 50)
t2.place(x=410,y=110)

window.mainloop()
