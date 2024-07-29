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
        self.geometry("500x700")
        
        # Display screen
        self.entry = ctk.CTkEntry(self, width=400, height=50, font=("Arial", 24))
        self.entry.grid(row=0, column=0, columnspan=5, pady=20)

        # Buttons
        button_texts = [
            '7', '8', '9', '/', 'C',
            '4', '5', '6', '*', '√',
            '1', '2', '3', '-', 'x²',
            '0', '.', '=', '+', '^',
            'sin', 'cos', 'tan', '!',
            'sin⁻¹', 'cos⁻¹', 'tan⁻¹', '/',
            'exp', 'log'
        ]
                # Buttons
        button_texts = [
            '7', '8', '9', '/', 'C',
            '4', '5', '6', '*', '√',
            '1', '2', '3', '-', 'x²',
            '0', '.', '=', '+', '^',
            'sin', 'cos', 'tan', '!',
            'sin⁻¹', 'cos⁻¹', 'tan⁻¹', '/',
            'exp', 'log'
        ]

        row, col = 1, 0
        for text in button_texts:
            button = ctk.CTkButton(self, text=text, width=80, height=80, font=("Arial", 18),
            command=lambda t=text: self.on_button_click(t))
            button.grid(row=row, column=col, padx=5, pady=5)
            col += 1
            if col > 4:
                col = 0
                row += 1
