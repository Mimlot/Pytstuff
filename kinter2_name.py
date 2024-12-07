import tkinter as tk
def display_name():
    name = e1.get()
    lb1 = tk.Label(root, text=name).grid(row=1, column = 2)
    
root = tk.Tk()
root.geometry("1280x720")


    
e1= tk.Entry(root)
e1.grid(row=0)
btn=tk.Button(root,text="display name",command=display_name).grid(row=1)

root.mainloop()