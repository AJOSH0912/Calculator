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

    def on_button_click(self, char):
        if char == 'C':
            self.entry.delete(0, ctk.END)
        elif char == '=':
            try:
                expression = self.entry.get()
                result = self.evaluate_expression(expression)
                self.entry.delete(0, ctk.END)
                self.entry.insert(ctk.END, str(result))
            except Exception as e:
                self.entry.delete(0, ctk.END)
                self.entry.insert(ctk.END, "Error")
        elif char == '√':
            current_text = self.entry.get()
            self.entry.delete(0, ctk.END)
            self.entry.insert(ctk.END, current_text + '√')
        elif char == 'x²':
            current_text = self.entry.get()
            self.entry.delete(0, ctk.END)
            self.entry.insert(ctk.END, current_text + '**2')
        elif char == '!':
            current_text = self.entry.get()
            self.entry.delete(0, ctk.END)
            self.entry.insert(ctk.END, current_text + '!')
        elif char == '^':
            current_text = self.entry.get()
            self.entry.delete(0, ctk.END)
            self.entry.insert(ctk.END, current_text + '**')
        elif char in ['sin⁻¹', 'cos⁻¹', 'tan⁻¹']:
            current_text = self.entry.get()

            self.entry.delete(0, ctk.END)
            self.entry.insert(ctk.END, current_text + char)
        elif char in ['exp', 'log']:
            current_text = self.entry.get()
            self.entry.delete(0, ctk.END)
            self.entry.insert(ctk.END, current_text + char)
        else:
            current_text = self.entry.get()
            self.entry.delete(0, ctk.END)
            self.entry.insert(ctk.END, current_text + char)

    def evaluate_expression(self, expression):
        # Replace trigonometric, sqrt, and other function names with their corresponding math function calls
        expression = expression.lower()
        expression = re.sub(r'sin(\d+)', r'math.sin(math.radians(\1))', expression)
        expression = re.sub(r'cos(\d+)', r'math.cos(math.radians(\1))', expression)
        expression = re.sub(r'tan(\d+)', r'math.tan(math.radians(\1))', expression)
        expression = re.sub(r'√(\d+)', r'math.sqrt(\1)', expression)
        expression = re.sub(r'sin⁻¹(\d+)', r'math.degrees(math.asin(\1))', expression)
        expression = re.sub(r'cos⁻¹(\d+)', r'math.degrees(math.acos(\1))', expression)
        expression = re.sub(r'tan⁻¹(\d+)', r'math.degrees(math.atan(\1))', expression)
        expression = re.sub(r'(\d+)!', r'math.factorial(\1)', expression)
        expression = re.sub(r'exp(\d+)', r'math.exp(\1)', expression)
        expression = re.sub(r'log(\d+)', r'math.log(\1)', expression)
        
        # Evaluate the modified expression
        return eval(expression)

if __name__ == "__main__":
    app = CalculatorApp()
    app.mainloop()
