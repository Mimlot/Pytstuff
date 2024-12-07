import tkinter as tk

root = tk.Tk()
root.title("yappign")
root.geometry("1280x720")

def show():
    global count
    count +=1
    lb_1 =tk.Label(root,text=f"so lan click {count}").grid(row=2, column=1)
    
 
count = 0
btn_1 = tk.Button(root, text="click me", command=show).grid(row=0) 

root.mainloop()