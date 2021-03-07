from forex_python.converter import CurrencyRates, CurrencyCodes
import tkinter as tk
from tkinter import *
import requests


URL =  'https://api.ratesapi.io/api/latest'
r = requests.get(url=URL)
keys_data = r.json()
currency_keys = keys_data['rates'].keys()


c = CurrencyRates()
print(c.get_rate('USD', 'PLN'))

codes = CurrencyCodes()

class Application(tk.Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.grid()
        self.master = master
        self.create_widgets()


    def create_widgets(self):

        self.first_clicked = StringVar()
        self.second_clicked = StringVar()

        self.first_curr = OptionMenu(self, self.first_clicked, *currency_keys, command=self.show_full_first)
        self.second_curr = OptionMenu(self, self.second_clicked, *currency_keys, command=self.show_full_second)

        self.first_curr.grid(column = 0, row = 0)
        self.second_curr.grid(column = 2, row = 0)

        self.left_frame = Frame(self)
        self.left_frame.grid(column=0,row=2)
        self.left_name = Label(self.left_frame)
        self.left_name.grid()

        self.right_frame = Frame(self)
        self.right_frame.grid(column=2, row=2)
        self.right_name = Label(self.right_frame)
        self.right_name.grid()

        self.amount = Entry(self)
        self.amount.grid(column=1, row = 2)

        self.count = Button(self, text="Count", command=self.count)
        self.count.grid(column=1,row=3)

    def show_full_first(self, curr):

        self.left_name.configure(text=f'{codes.get_currency_name(curr)} {codes.get_symbol(curr)}')

    def show_full_second(self, curr):

        self.right_name.configure(text=f'{codes.get_currency_name(curr)} {codes.get_symbol(curr)}')

    def count(self):

        rate = c.get_rate(self.first_clicked.get(), self.second_clicked.get())
        amount = float(self.amount.get())
        outcome = Label(root, text=str(rate*amount))
        outcome.grid(column=0, row=4)

        def show_pre_rates(self):

            pass



root = tk.Tk()
app = Application(master=root)
app.master.title("Currency exchange calculator")
# app.master.maxsize(1300,400)
# app.master.minsize(1300,400)
app.mainloop()
