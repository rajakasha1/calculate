
import tkinter as tk
from tkinter import ttk

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Calculator")
        
        # Create entry fields
        self.num1 = ttk.Entry(root)
        self.num2 = ttk.Entry(root)
        
        # Create labels
        ttk.Label(root, text="First Number:").grid(row=0, column=0, padx=5, pady=5)
        self.num1.grid(row=0, column=1, padx=5, pady=5)
        
        ttk.Label(root, text="Second Number:").grid(row=1, column=0, padx=5, pady=5)
        self.num2.grid(row=1, column=1, padx=5, pady=5)
        
        # Create buttons
        ttk.Button(root, text="Add", command=self.add).grid(row=2, column=0, padx=5, pady=5)
        ttk.Button(root, text="Multiply", command=self.multiply).grid(row=2, column=1, padx=5, pady=5)
        
        # Result label
        self.result_var = tk.StringVar()
        ttk.Label(root, textvariable=self.result_var).grid(row=3, column=0, columnspan=2, pady=10)

    def add(self):
        try:
            num1 = float(self.num1.get())
            num2 = float(self.num2.get())
            result = num1 + num2
            self.result_var.set(f"Result: {result}")
        except ValueError:
            self.result_var.set("Please enter valid numbers")

    def multiply(self):
        try:
            num1 = float(self.num1.get())
            num2 = float(self.num2.get())
            result = num1 * num2
            self.result_var.set(f"Result: {result}")
        except ValueError:
            self.result_var.set("Please enter valid numbers")

if __name__ == "__main__":
    root = tk.Tk()
    app = Calculator(root)
    root.mainloop()
