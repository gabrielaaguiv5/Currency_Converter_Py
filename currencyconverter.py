from tkinter import *

class CurrencyConverter:
    def __init__(self, root):
        window = Tk()
       # GUI Setup
        window.title("Currency Converter")
        window.configure(bg="magenta")
        window.geometry("400x200")
        # Labels and Entries
        Label(window, font = "Albert Sans 12 bold", bg = "magenta", text = "Amount to Convert:").grid(row=1, column=1, sticky=W)
        
