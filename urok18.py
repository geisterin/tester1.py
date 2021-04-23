from tkinter import *

root = Tk()
root.title('This is sample program written in Python')
root.geometry('600x200')

text_label = Label(root, text='Hello world')
text_label2 = Label(root, text='Привет мир')

text_label.pack()
text_label2.pack()
root.mainloop()
