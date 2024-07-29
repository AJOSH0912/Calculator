import customtkinter as ctk
import math
import re

# Initialize customtkinter
ctk.set_appearance_mode("dark")  # Modes: system (default), light, dark
ctk.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

class CalculatorApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        self.title("Python Calculator")
        self.geometry("400x600")
        
        # Display screen
        self.entry = ctk.CTkEntry(self, width=300, height=50, font=("Arial", 24))
        self.entry.grid(row=0, column=0, columnspan=4, pady=20)

        # Buttons
        button_texts = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+',
            'sin', 'cos', 'tan', 'C',
            '√', 'x²', 'sin⁻¹', 'cos⁻¹',
            'tan⁻¹', '/'
        ]