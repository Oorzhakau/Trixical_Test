# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 15:02:30 2019

@author: Ferma301
"""
from tkinter import *

class Application(Frame):
    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid()
        self.creat_widget()
    def creat_widget(self):
        self.lbl1 = Label(self, text = "Введите начальную деформацию после этапа\n реконсолидации и значение желаемого секущего модуля")
        self.lbl1.grid(row = 0, column = 0, columnspan = 2, rowspan = 2, sticky = W)
        
        self.pw_lbl_bh = Label(self, text = "№ скважины - ")
        self.pw_lbl_bh.grid(row = 3, column = 0, sticky = W)
        self.pw_entry_bh = Entry(self)
        self.pw_entry_bh.grid(row = 3, column = 1, sticky = W)
        
        self.pw_lbl_dp = Label(self, text = "Глубина, м - ")
        self.pw_lbl_dp.grid(row = 4, column = 0, sticky = W)
        self.pw_entry_dp = Entry(self)
        self.pw_entry_dp.grid(row = 4, column = 1, sticky = W)
        
        self.pw_lbl1 = Label(self, text = "Eps, д.е. = ")
        self.pw_lbl1.grid(row = 5, column = 0, sticky = W)
        self.pw_entry1 = Entry(self)
        self.pw_entry1.grid(row = 5, column = 1, sticky = W)
        
        self.pw_lbl2 = Label(self, text = "E50, MPa = ")
        self.pw_lbl2.grid(row = 6, column = 0, sticky = W)
        self.pw_entry2 = Entry(self)
        self.pw_entry2.grid(row = 6, column = 1, sticky = W)
        
        self.bttn1 = Button(self, text = "Ok", command = self.graph_pic)
        self.bttn1.grid(row = 8, column = 0)

    def graph_pic(self):
        self.eps1 = float(self.pw_entry1.get())
        self.E50 = float(self.pw_entry2.get())
        print(self.eps1)
        print(self.E50)    


if __name__ == "__main__":
    root = Tk()
    app = Application(root)
    root.mainloop()
    