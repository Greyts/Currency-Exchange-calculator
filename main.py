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
        self.label = tk.Label(root)
        self.listbox = tk.Listbox(root)

    def create_widgets(self):

        self.first_curr = tk.Button(self,text='Choose your first currency', padx=100, pady=20)
        self.second_curr = tk.Button(self,text='Choose your second currency', padx=100, pady=20)

        self.symbols = tk.Button(self, text='Symbols', padx=100, pady=20)

        self.first_curr["command"] = self.choose_first
        self.second_curr["command"] = self.choose_second
        self.symbols["command"] = self.show_symbols

        self.first_entry = tk.Entry(width = 50)
        self.second_entry = tk.Entry(width = 50)

        #self.grid_columnconfigure(2, weight=1)

        self.first_curr.grid(row=0, column =0, pady=30, padx=20)
        self.second_curr.grid(row=0, column=1, pady=30, padx=20)
        self.first_entry.grid(row=1, column=0, padx=20)
        self.second_entry.grid(row=1, column=1, padx=20)

        self.symbols.grid(row=4,column=2,padx=20)

        self.quit = tk.Button(text="QUIT", fg="red", command=self.master.destroy)
        self.quit.grid(row = 3, column=0)

    def create_list_of_currencies(self, column='0', event = "<<ListboxSelect>>"):

        self.scrollbar = tk.Scrollbar()
        self.scrollbar.grid(column = column, row = 2)

        mylist = tk.Listbox(yscrollcommand=self.scrollbar.set)
        for key in currency_keys:
            mylist.insert('end', key)

        mylist.grid(column=column, row = 2)
        self.scrollbar.config(command=mylist.yview)

    def callback(self):

        selection = self.widget.curselection()
        if selection:
            index = selection[0]
            data = self.widget.get(index)
            self.label.configure(text=data)
        else:
            self.label.configure(text=' ')

    def choose_first(self):

        first = self.create_list_of_currencies()
        self.listbox.bind("<<ListboxSelect>>", self.callback)
        global first_symbol
        first_symbol = self.label.cget('text')


    def choose_second(self):

        second = self.create_list_of_currencies(column='1')
        self.listbox.bind("<<ListboxSelect>>", self.callback)
        self.label.cget('text')
        global second_symbol
        second_symbol = self.label.cget('text')


    def show_symbols(self):

        print(first_symbol)
        print(second_symbol)

root = tk.Tk()
app = Application(master=root)
app.master.maxsize(1300,400)
app.master.minsize(1300,400)
app.mainloop()




#mybutton.grid(row=0,column=0)
#, padx= 30, pady=30