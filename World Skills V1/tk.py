import tkinter as tk

def get_range(count):
    # изменить текст в метке
    label['text'] = count                     

    if count > 0:
        # Обратный отсчет через каждые 100 мс
        root.after(100, get_range, count-1)

root = tk.Tk()

label = tk.Label(root)
label.place(x=350, y=350)
button = tk.Button(root, text='Click', command=lambda i=100000: get_range(i)).pack()

root.mainloop()