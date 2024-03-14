import tkinter as tk

# Function to update display when a button is clicked
def button_click(symbol):
    current = display_var.get()
    if current == '0' or current == 'Error':
        display_var.set(symbol)
    else:
        display_var.set(current + symbol)

# Function to clear the display
def clear_display():
    display_var.set('0')

# Function to evaluate the expression in the display
def calculate():
    try:
        result = eval(display_var.get())
        display_var.set(str(result))
    except Exception as e:
        display_var.set("Error")

# Create the main window
root = tk.Tk()
root.title("Colorful Calculator")
root.configure(bg='#F0F0F0')

# Create a variable to hold the display value
display_var = tk.StringVar()
display_var.set("0")

# Create the display
display = tk.Entry(root, textvariable=display_var, justify="right", font=("Arial", 20), bg='#FFFFFF')
display.grid(row=0, column=0, columnspan=4, sticky="nsew", padx=10, pady=10)

# Create buttons
button_symbols = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('%', 4, 2), ('+', 4, 3)
]

for symbol, row, col in button_symbols:
    btn = tk.Button(root, text=symbol, width=5, height=2, command=lambda sym=symbol: button_click(sym), bg='#FFD700', fg='#000000')
    btn.grid(row=row, column=col, sticky="nsew", padx=5, pady=5)

# Clear button
clear_btn = tk.Button(root, text="C", width=5, height=2, command=clear_display, bg='#FF6347', fg='#FFFFFF')
clear_btn.grid(row=5, column=0, sticky="nsew", padx=5, pady=5, columnspan=2)

# Equals button
equals_btn = tk.Button(root, text="=", width=5, height=2, command=calculate, bg='#008000', fg='#FFFFFF')
equals_btn.grid(row=5, column=2, sticky="nsew", padx=5, pady=5, columnspan=2)

# Make all rows and columns expandable
for i in range(6):
    root.grid_rowconfigure(i, weight=1)
for i in range(4):
    root.grid_columnconfigure(i, weight=1)

# Run the main event loop
root.mainloop()
