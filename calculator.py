import tkinter as tk


class Calculator:
    def __init__(self, parent):
        # Numbers
        self.mem = 0
        self.pressop = ''
        self.second_flag = False
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
        self.labelr = tk.Label(bg='white', fg='black', width=10, anchor='e')
        self.labelr.config(font=("Courier", 36))
        self.labelr.place(x=10, y=10)

    def initbpress(self):
        def pressb0():
            if (self.pressop == '' or self.second_flag is False) and self.labelr['text'] != '0':
                self.labelr['text'] = self.labelr['text'] + '0'
            else:
                self.labelr['text'] = '0'
                self.second_flag = False

        self.button0['command'] = pressb0

        def pressb1():
            if self.pressop == '' or self.second_flag is False:
                self.labelr['text'] = self.labelr['text'] + '1'
            else:
                self.labelr['text'] = '1'
                self.second_flag = False

        self.button1['command'] = pressb1

        def pressb2():
            if self.pressop == '' or self.second_flag is False:
                self.labelr['text'] = self.labelr['text'] + '2'
            else:
                self.labelr['text'] = '2'
                self.second_flag = False

        self.button2['command'] = pressb2

        def pressb3():
            if self.pressop == '' or self.second_flag is False:
                self.labelr['text'] = self.labelr['text'] + '3'
            else:
                self.labelr['text'] = '3'
                self.second_flag = False

        self.button3['command'] = pressb3

        def pressb4():
            if self.pressop == '' or self.second_flag is False:
                self.labelr['text'] = self.labelr['text'] + '4'
            else:
                self.labelr['text'] = '4'
                self.second_flag = False

        self.button4['command'] = pressb4

        def pressb5():
            if self.pressop == '' or self.second_flag is False:
                self.labelr['text'] = self.labelr['text'] + '5'
            else:
                self.labelr['text'] = '5'
                self.second_flag = False

        self.button5['command'] = pressb5

        def pressb6():
            if self.pressop == '' or self.second_flag is False:
                self.labelr['text'] = self.labelr['text'] + '6'
            else:
                self.labelr['text'] = '6'
                self.second_flag = False

        self.button6['command'] = pressb6

        def pressb7():
            if self.pressop == '' or self.second_flag is False:
                self.labelr['text'] = self.labelr['text'] + '7'
            else:
                self.labelr['text'] = '7'
                self.second_flag = False

        self.button7['command'] = pressb7

        def pressb8():
            if self.pressop == '' or self.second_flag is False:
                self.labelr['text'] = self.labelr['text'] + '8'
            else:
                self.labelr['text'] = '8'
                self.second_flag = False

        self.button8['command'] = pressb8

        def pressb9():
            if self.pressop == '' or self.second_flag is False:
                self.labelr['text'] = self.labelr['text'] + '9'
            else:
                self.labelr['text'] = '9'
                self.second_flag = False

        self.button9['command'] = pressb9

        def pressbdot():
            self.labelr['text'] = self.labelr['text'] + '.'

        self.buttondot['command'] = pressbdot

        def pressbc():
            self.labelr['text'] = ''
            self.mem = 0
            self.pressop = ''
            self.second_flag = False

        self.buttonc['command'] = pressbc

        def pressbsign():
            s = self.labelr['text']
            if s[0] == '-':
                self.labelr['text'] = s[1:]
            else:
                self.labelr['text'] = '-' + s

        self.buttonsign['command'] = pressbsign

        def pressplus():
            self.mem = float(self.labelr['text'])
            self.pressop = '+'
            self.second_flag = True

        self.buttonplus['command'] = pressplus

        def pressminus():
            self.mem = float(self.labelr['text'])
            self.pressop = '-'
            self.second_flag = True

        self.buttonmin['command'] = pressminus

        def pressmul():
            self.mem = float(self.labelr['text'])
            self.pressop = '*'
            self.second_flag = True

        self.buttonmul['command'] = pressmul

        def pressdiv():
            self.mem = float(self.labelr['text'])
            self.pressop = '/'
            self.second_flag = True

        self.buttondiv['command'] = pressdiv

        def pressr():
            if self.pressop == '+':
                self.mem = self.mem + float(self.labelr['text'])
            elif self.pressop == '-':
                self.mem = self.mem - float(self.labelr['text'])
            elif self.pressop == '*':
                self.mem = self.mem * float(self.labelr['text'])
            elif self.pressop == '/' and float(self.labelr['text']) != 0:
                self.mem = self.mem / float(self.labelr['text'])
            if (self.pressop == '/' and float(self.labelr['text']) == 0) or len(str(self.mem // 1)) > 8:
                self.labelr['text'] = ''
            else:
                if self.mem % 1 == 0:
                    self.labelr['text'] = str(int(self.mem))
                elif len(str(self.mem)) <= 8:
                    self.labelr['text'] = str(self.mem)
                else:
                    temp = self.mem % 1
                    temp = int((10 ** (9 - len(str(self.mem // 1))) * temp) // 1)
                    print(str(temp))
                    self.labelr['text'] = str(int(self.mem // 1)) + '.' + str(temp)




            self.pressop = ''
            self.second_flag = False


        self.buttonr['command'] = pressr



root = tk.Tk()
root.geometry('320x350')
calc = Calculator(root)
calc.initbpress()
root.mainloop()
