import customtkinter as ctk


class TaxCalculator:
    def __init__(self):
        self.window = ctk.CTk()
        self.window.title('Tax Calculator')
        self.window.geometry('280x280')
        self.window.resizable(False, False)

        self.padding: dict = {'padx': 20, 'pady': 20}

        # Income
        self.income_label = ctk.CTkLabel(self.window, text='Income:')
        self.income_label.grid(row=0, column=0, **self.padding)
        self.income_entry = ctk.CTkEntry(self.window)
        self.income_entry.grid(row=0, column=1, **self.padding)

        # Percent
        self.perc_entry_label = ctk.CTkLabel(self.window, text='Percent:')
        self.perc_entry_label.grid(row=1, column=0, **self.padding)
        self.perc_entry = ctk.CTkEntry(self.window)
        self.perc_entry.grid(row=1, column=1, **self.padding)

        # Result
        self.result_label = ctk.CTkLabel(self.window, text='Tax:')
        self.result_label.grid(row=2, column=0, **self.padding)
        self.result_entry = ctk.CTkEntry(self.window)
        self.result_entry.insert(0, '0')
        self.result_entry.grid(row=2, column=1, **self.padding)

        # self.calculate_button = ctk.CTkButton(self.window, text='Calculate', command=self.calculate_tax)
        # self.calculate_button.grid(row=3, column=1, **self.padding)

        self.calculate_button = ctk.CTkButton(self.window, text='Calculate', command=self.calculate_tax)
        self.calculate_button.grid(row=3, column=1, **self.padding)

    def update_result(self, text):
        self.result_entry.delete(0, ctk.END)
        self.result_entry.insert(0, text)

    def calculate_tax(self):
        try:
            income: float = float(self.income_entry.get())
            rate: float = float(self.perc_entry.get())
            total_tax = float((income * rate) / 100)
            self.update_result(f'$ {total_tax:,.2f}')
        except ValueError:
            self.update_result(f'Invalid Value')

    def run(self):
        self.window.mainloop()


if __name__ == '__main__':
    tk = TaxCalculator()
    tk.run()
