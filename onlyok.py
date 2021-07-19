import sys
import tkinter as tk
sys.argv[1]
window = tk.Tk()
window.title('已收單')
doneCup=str(sys.argv[1])
print(doneCup)
window.geometry('1680x1000+0+0')
lbl_1 = tk.Label(window, text=f'飲料 {doneCup} 正在出杯', bg='yellow', fg='#263238', font=('Arial', 170))
lbl_1.grid(column=0, row=0)
window.attributes('-topmost', 1)
# window.attributes('-topmost', 0)
window.after(20000, lambda: window.destroy()) # Destroy the widget after 30 seconds
window.mainloop()