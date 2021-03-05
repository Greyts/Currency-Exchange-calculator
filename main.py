from forex_python.converter import CurrencyRates, CurrencyCodes
import tkinter as tk
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
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):

        self.bottomframe = tk.Frame()
        self.bottomframe.pack(side='bottom')

        self.first_curr = tk.Button(self, padx= 30, pady=30)
        self.second_curr = tk.Button(self, padx= 30, pady=30)

        self.first_curr["text"] = "Choose your first currency"
        self.second_curr["text"] = "Choose your second currency"
        self.first_curr["command"] = self.choose_first
        self.second_curr["command"] = self.choose_second

        self.first_curr.pack( side="left", fill='x', padx=20, pady = 30,expand=1)
        self.second_curr.pack( side="right",fill='x',padx=20, pady = 30,)

        self.quit = tk.Button(self.bottomframe, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.pack( side="bottom", pady=100)

    def create_list_of_currencies(self, side='left'):

        self.scrollbar = tk.Scrollbar()
        self.scrollbar.pack(side=side,padx =10 ,fill='x')

        mylist = tk.Listbox(root, yscrollcommand=self.scrollbar.set)
        for key in currency_keys:
            mylist.insert('end', key)

        mylist.pack(side=side, padx=20, fill='both')
        self.scrollbar.config(command=mylist.yview)

    def choose_first(self):

        self.create_list_of_currencies()

    def choose_second(self):

        self.create_list_of_currencies(side='right')


root = tk.Tk()
app = Application(master=root)
app.master.maxsize(1000,400)
app.master.minsize(1000,400)
app.mainloop()


#mybutton.grid(row=0,column=0)