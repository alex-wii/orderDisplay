import tkinter as tk


window = tk.Tk()
window.title('已經完成')
window.geometry('500x100+1000+0')
lbl_1 = tk.Label(window, text='Hello World', bg='yellow', fg='#263238', font=('Arial', 12))
lbl_1.grid(column=0, row=0)
window.mainloop()