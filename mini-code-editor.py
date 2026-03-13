import tkinter as tk
from tkinter import filedialog

def new_file():
    text_area.delete(1.0, tk.END)

def open_file():
    file = filedialog.askopenfile(mode="r")
    if file:
        content = file.read()
        text_area.delete(1.0, tk.END)
        text_area.insert(tk.END, content)

def save_file():
    file = filedialog.asksaveasfile(mode="w", defaultextension=".txt")
    if file:
        content = text_area.get(1.0, tk.END)
        file.write(content)
        file.close()

root = tk.Tk()
root.title("Mini Code Editor")

menu = tk.Menu(root)
root.config(menu=menu)

file_menu = tk.Menu(menu)
menu.add_cascade(label="File", menu=file_menu)

file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)

text_area = tk.Text(root, wrap="word")
text_area.pack(expand=True, fill="both")

root.mainloop()