#!/home/bcr/anaconda3/bin/python
# -*- coding: utf-8 -*-

import data
import tkinter as tk


class Application(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        master.title('TODO')
        master.geometry('750x450')

        self.selected_task = 0
        self.last_index = len(file.tasks)

        self.create_widgets()
        self.show_task()

    def create_widgets(self):
        self.tasks_text = tk.StringVar()
        self.tasks_label = tk.Label(self.master, text='New task :', font=('bold', 14), pady=10)
        self.tasks_label.grid(row=0, column=0, sticky=tk.W)
        self.tasks_entry = tk.Entry(self.master, textvariable=self.tasks_text, width=50)
        self.tasks_entry.grid(row=0, column=1, columnspan=10)

        self.tasks_list = tk.Listbox(self.master, height=25, width=100, border=0)
        self.tasks_list.grid(row=2, column=0, columnspan=30, rowspan=6, pady=20, padx=20)

        self.scrollbar = tk.Scrollbar(self.master)
        self.scrollbar.grid(row=2, column=29)
        # Set scrollbar to parts
        self.tasks_list.configure(yscrollcommand=self.scrollbar.set)
        self.scrollbar.configure(command=self.tasks_list.yview)

        # Bind select
        self.tasks_list.bind('<<ListboxSelect>>', self.selected_task)

        # Buttons
        self.add_btn = tk.Button(self.master, text="Add Task", width=12, command=self.add_task)
        self.add_btn.grid(row=1, column=0, pady=10)

        self.complete_btn = tk.Button(self.master, text="Complete Task", width=12, command=self.complete_task)
        self.complete_btn.grid(row=1, column=1)

    def show_task(self):
        for i in file.tasks:
            self.tasks_list.insert(tk.END, ''.join(i))

    def add_task(self):
        new_task = self.tasks_text.get()
        file.add_task(new_task)
        self.tasks_list.insert(tk.END, 'TODO : '+new_task)
        print('add :', new_task)

    def complete_task(self):
        try:
            index = self.tasks_list.curselection()[0]
            self.selected_task = self.tasks_list.get(index)
            print('delete :',self.selected_task)
            file.complete_task(index)
            self.tasks_list.delete(index)
        except IndexError:
            print('no task selected')
            pass


if __name__ == '__main__':
    filePath = './data.txt'
    file = data.Data(path=filePath)

    root = tk.Tk()
    app = Application(root)
    app.mainloop()
