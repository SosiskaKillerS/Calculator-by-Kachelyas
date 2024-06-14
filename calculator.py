import tkinter as tk
win = tk.Tk()
win.geometry(f"240x260+100+200")
win['bg'] = '#33ffe6'
win.title('Calculator')

calc = tk.Entry(win)
calc.grid(row=0,column=0)

tk.Button(text='1').grid(row=1,column=0)
tk.Button(text='2').grid(row=1,column=0)
tk.Button(text='3').grid(row=1,column=0)
tk.Button(text='4').grid(row=1,column=0)
tk.Button(text='5').grid(row=1,column=0)
tk.Button(text='6').grid(row=1,column=0)
tk.Button(text='7').grid(row=1,column=0)
tk.Button(text='8').grid(row=1,column=0)

win.mainloop()
