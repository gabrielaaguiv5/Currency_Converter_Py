from tkinter import *

class CurrencyConverter:
    def __init__(self, root):
        window = root
       # GUI Setup
        window.title("Currency Converter")
        window.configure(bg="pink")
        window.geometry("400x200")
        frame = Frame(root, bg="magenta")
        frame.pack(padx=20, pady=20)
        # Labels and Entries
        Label(frame, font = ("Albert Sans", 12, "bold"), bg = "magenta", text = "Amount to Convert:").grid(row=0, column=0, sticky=W, pady=5)
        Label(frame, font = ("Albert Sans", 12, "bold"), bg = "magenta", text = "Conversion Rate:").grid(row=1, column=0, sticky=W, pady=5)
        Label(frame, font = ("Albert Sans", 12, "bold"), bg = "magenta", text = "Converted Amount:").grid(row=2, column=0, sticky=W, pady=5)
        # Object Creation
        self.amount_to_convert = StringVar() # StringVar Object is a Class from tkinter
        # Entry Configuration
        Entry(frame, textvariable = self.amount_to_convert, justify = RIGHT, width=15).grid(row=0, column=1)
        self.conversion_rate = StringVar()
        Entry(frame, textvariable = self.conversion_rate, justify = RIGHT, width=15).grid(row=1, column=1)
        self.converted_amount = StringVar()
        # For Converted Amount no user input is needed
        lblConverted_amount = Label(frame, font = ("Albert Sans", 12, "bold"), bg = "magenta", textvariable = self.converted_amount).grid(row=2, column=1, sticky=E)
        # Button Configuration
        # Button to perform conversion
        btConvertedAmount = Button(frame, text = "Convert", font = ("Albert Sans", 12, "bold"), bg = "White", fg= "Black", command = self.converted_amount).grid(row=3, column=0, pady=15, sticky=E) #self.converted_amount is a function that will be created later
        # Button to clear all fields
        btClear = Button(frame, text = "Clear", font = ("Albert Sans", 12, "bold"), bg = "White", fg = "Black", command = self.delete_all).grid(row=3, column=1, padx=25, pady=15,sticky=E)

    # Creating the function that will perform the conversion
    def converted_amount_function(self):
        try:
            rate = float(self.conversion_rate.get())
            convertedAmount = float(self.amount_to_convert.get()) * rate
            self.converted_amount.set(format(convertedAmount, '10.2f'))
        except ValueError:
            self.converted_amount.set("Invalid input")  

    # Creating function to clear inputs
    def delete_all(self):
        self.amount_to_convert.set("")
        self.conversion_rate.set("")
        self.converted_amount.set("")

    # Main method to run the application
if __name__ == "__main__":
    root = Tk()
    CurrencyConverter(root)
    root.mainloop()

