import tkinter as tk


class Calculator:
    def __init__(self, parent):
        self.parent = parent
        self.initUI(self.parent)
        pass

    def initUI(self, parent):
        # Numbers
        bsize = 50
        b_interval = 10
        for i in range(1, 10):
            exec('self.button' + str(i) + '= tk.Button(parent, activebackground=\'white\')')
            exec('self.button' + str(i) + '[\'text\'] =' + str(i))
            if i > 6:
                row = 1
            elif i > 3:
                row = 2
            else:
                row = 3
            if i % 3 == 1:
                col = 1
            elif i % 3 == 2:
                col = 2
            else:
                col = 3
            exec('self.button' + str(i) + '.place(x=b_interval*col+bsize*(col-1),'
                                          ' y=300-(b_interval*row)-bsize*(row), '
                                          'height=bsize, width=bsize)')
        self.button0 = tk.Button(parent, activebackground='white')
        self.button0['text'] = '0'
        self.button0.place(x=b_interval * 2 + bsize, y=300 - b_interval / 2, height=bsize, width=bsize)
        self.buttondot = tk.Button(parent, activebackground='white')
        self.buttondot['text'] = '.'
        self.buttondot.place(x=b_interval, y=300 - b_interval / 2, height=bsize, width=bsize)
        self.buttonsign = tk.Button(parent, activebackground='white')
        self.buttonsign['text'] = '+/-'
        self.buttonsign.place(x=b_interval * 3 + 2 * bsize, y=300 - b_interval / 2, height=bsize, width=bsize)

        # Operations
        self.buttonplus = tk.Button(parent, activebackground='white')
        self.buttonplus['text'] = '+'
        self.buttonplus.place(x=bsize * 3 + b_interval * 5, y=300 - bsize * 3 - b_interval * 3,
                              height=bsize, width=bsize)
        self.buttonmin = tk.Button(parent, activebackground='white')
        self.buttonmin['text'] = '-'
        self.buttonmin.place(x=bsize * 4 + b_interval * 6, y=300 - bsize * 3 - b_interval * 3,
                             height=bsize, width=bsize)
        self.buttonmul = tk.Button(parent, activebackground='white')
        self.buttonmul['text'] = '*'
        self.buttonmul.place(x=bsize * 3 + b_interval * 5, y=300 - bsize * 2 - b_interval * 2,
                             height=bsize, width=bsize)
        self.buttondiv = tk.Button(parent, activebackground='white')
        self.buttondiv['text'] = '/'
        self.buttondiv.place(x=bsize * 4 + b_interval * 6, y=300 - bsize * 2 - b_interval * 2,
                             height=bsize, width=bsize)

        self.buttonc = tk.Button(parent, activebackground='white')
        self.buttonc['text'] = 'C'
        self.buttonc.place(x=bsize * 3 + b_interval * 5, y=300 - bsize - b_interval,
                           height=bsize, width=bsize)
        self.buttonr = tk.Button(parent, activebackground='white')
        self.buttonr['text'] = '='
        self.buttonr.place(x=bsize * 4 + b_interval * 6, y=300 - bsize - b_interval,
                           height=bsize, width=bsize)
        # Label
        self.labelr = tk.Label(bg='white', fg='black', width=10, height=1)
        self.labelr.config(font=("Courier", 36))
        self.labelr.place(x=10, y=10)


root = tk.Tk()
root.geometry('320x350')
calc = Calculator(root)
root.mainloop()
