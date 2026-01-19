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
        Label(window, font = "Albert Sans 12 bold", bg = "magenta", text = "Conversion Rate:").grid(row=2, column=1, sticky=W)
        Label(window, font = "Albert Sans 12 bold", bg = "magenta", text = "Converted Amount:").grid(row=3, column=1, sticky=W)
        # Object Creation
        self.amount_to_convert = StringVar() # StringVar Object is a Class from tkinter
        # Entry Configuration
        Entry(window, textvariable = self.amount_to_convert, justify = RIGHT).grid(row=1, column=2)
        self.conversion_rate = StringVar()
        Entry(window, textvariable = self.conversion_rate, justify = RIGHT).grid(row=2, column=2)
        self.converted_amount = StringVar()
        # For Converted Amount no user input is needed
        lblConverted_amount = Label(window, font = "Albert Sans 12 bold", bg = "magenta", textvariable = self.converted_amount).grid(row=3, column=2, sticky=E)
        # Button Configuration
        # Button to perform conversion
        btConvertedAmount = Button(window, font = "Albert Sans 12 bold", bg = "White", fg= "Black", command = self.converted_amount).grid(row=4, column=2, sticky=E) #self.converted_amount is a function that will be created later
        # Button to clear all fields
        btClear = Button(window, font = "Albert Sans 12 bold", bg = "White", fg = "Black", command = self.delete_all).grid(row=4, column=6, padx=25, pady=25,sticky=E)
    
        window.mainloop() # Start the GUI event loop

    # Creating the function that will perform the conversion
    def converted_amount(self):
        rate = float(self.conversion_rate.get())
        convertedAmount = amount = float(self.amount_to_convert.get()) * rate
        self.converted_amount.set(format(convertedAmount, '10.2f'))

    # Creating function to clear inputs
    def delete_all(self):
        self.amount_to_convert.set("")
        self.conversion_rate.set("")
        self.converted_amount.set("")

    # Main method to run the application
if __name__ == "__main__":
    CurrencyConverter(Tk())
