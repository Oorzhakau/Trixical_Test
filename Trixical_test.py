from matplotlib import pyplot as plt
from scipy.interpolate import interp1d
import numpy as np
import xlwt

#book = xlwt.Workbook(encoding="utf-8")
#sheet1 = book.add_sheet("Sheet 1")

n = 100 

class LineBuilder:
    def __init__(self, line):
        self.line = line
        self.xs = list(line.get_xdata())
        self.ys = list(line.get_ydata())
        self.cid = line.figure.canvas.mpl_connect('button_press_event', self)
        self.cid1 = line.figure.canvas.mpl_connect('key_press_event', self.press)
        self.book = xlwt.Workbook(encoding="utf-8")
        self.sheet = self.book.add_sheet("Sheet 1") 

    def __call__(self, event):
        print('click', event)
        if event.inaxes!=self.line.axes: return
        self.xs.append(event.xdata)
        self.ys.append(event.ydata)
        self.line.set_data(self.xs, self.ys)
        self.line.figure.canvas.draw()
        
    def press(self, event):
        if event.key == 'x':
            self.xs = list()
            self.ys = list()
            self.line.set_data(self.xs, self.ys)
            self.line.figure.canvas.draw()
        if event.key == 'w':
            f = interp1d(self.xs, self.ys, kind='cubic')
            xnew = np.linspace(self.xs[0], self.xs[-1], num = n)
            ynew = f(xnew)
            self.line.set_data(xnew, ynew)
            self.line.figure.canvas.draw()
            for num in range(len(xnew)):
                row = self.sheet.row(num)
                row.write(0,xnew[num])
                row.write(1,ynew[num])
            self.book.save("test.xls")

fig = plt.figure()
ax = fig.add_subplot(111)
ax.set_title('click to build line segments')

line, = ax.plot([], [])  # empty line
linebuilder = LineBuilder(line)
xl = ax.set_xlabel('Press x to clear canvas\nPress w to interpolate and save data')
plt.xlim(0, 0.16)
plt.ylim(0, 0.6)
plt.xlabel('eps, d.e.')
plt.ylabel('Sigma1 - Sigma3, MPa')
plt.show()