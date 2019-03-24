# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 15:02:30 2019

@author: Ferma301
"""
from tkinter import *
import Trixical_test
from matplotlib import pyplot as plt
from scipy.interpolate import interp1d
import numpy as np
import xlwt

MAX_eps = 0.16

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
        
        self.pw_lbl4 = Label(self, text = "Sigma3, MPa = ")
        self.pw_lbl4.grid(row = 7, column = 0, sticky = W)
        self.pw_entry4 = Entry(self)
        self.pw_entry4.grid(row = 7, column = 1, sticky = W)
        
        self.pw_lbl3 = Label(self, text = "(Sigma1 - Sigma3)max, MPa = ")
        self.pw_lbl3.grid(row = 8, column = 0, sticky = W)
        self.pw_entry3 = Entry(self)
        self.pw_entry3.grid(row = 8, column = 1, sticky = W)
               
        self.bttn1 = Button(self, text = "Ok", command = self.graph_pic)
        self.bttn1.grid(row = 9, column = 0)

    def graph_pic(self):
        self.bh = self.pw_entry_bh.get()
        self.dp = self.pw_entry_dp.get()
        self.eps1 = float(self.pw_entry1.get())
        self.E50 = float(self.pw_entry2.get())
        self.SSmax = float(self.pw_entry3.get())
        self.S3 = float(self.pw_entry4.get())
        self.eraz = self.SSmax/(2.0*self.E50)+self.eps1
        self.half_SSmax = self.SSmax/2.0

        self.fig = plt.figure()
        self.ax = self.fig.add_subplot(111)
        self.ax.set_title('Click on canvas to paint line\nPress "x" to clear canvas or "w" to interpolate and save data')

        self.line, = self.ax.plot([self.eps1], [0])  # empty line
        self.linebuilder = Trixical_test.LineBuilder(line = self.line, bh = self.bh, depth = self.dp, sigma3 = self.S3)
        self.xl = self.ax.set_xlabel('')
        
        self.ax.scatter([self.eps1, self.eraz], [0, self.half_SSmax], marker = 'o')
        self.ax.hlines(y=self.SSmax, xmin=0, xmax=MAX_eps, linewidth=2, color='r')

        plt.xlim(0, MAX_eps)
        plt.ylim(0, 0.6)
        plt.xlabel('eps, d.e.')
        plt.ylabel('Sigma1 - Sigma3, MPa')
        plt.show()   


if __name__ == "__main__":
    root = Tk()
    app = Application(root)
    root.mainloop()
    