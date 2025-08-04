import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
import re

def plot_function():
    expression = equation_var.get()
    x_min = x_min_slider.get()
    x_max = x_max_slider.get()

    expression = re.sub(r'\bsin\b', 'np.sin', expression)
    expression = re.sub(r'\bcos\b', 'np.cos', expression)
    expression = re.sub(r'\btan\b', 'np.tan', expression)
    expression = re.sub(r'\barcsin\b', 'np.arcsin', expression)
    expression = re.sub(r'\barccos\b', 'np.arccos', expression)
    expression = re.sub(r'\barctan\b', 'np.arctan', expression)
    expression = re.sub(r'\bsinh\b', 'np.sinh', expression)
    expression = re.sub(r'\bcosh\b', 'np.cosh', expression)
    expression = re.sub(r'\btanh\b', 'np.tanh', expression)
    expression = re.sub(r'\barcsinh\b', 'np.arcsinh', expression)
    expression = re.sub(r'\barccosh\b', 'np.arccosh', expression)
    expression = re.sub(r'\barctanh\b', 'np.arctanh', expression)
    expression = re.sub(r'\bpi\b', 'np.pi', expression)
    expression = re.sub(r'\be\b', 'np.e', expression)

    x = np.linspace(x_min, x_max, 400)

    try:
        y = eval(expression, {"np": np, "x": x})
    except Exception as e:
        output_label.config(text=f"Invalid expression. Error: {str(e)}")
        return

    ax.clear()
    ax.plot(x, y)
    ax.set_title(f"Graph of {equation_var.get()}")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.grid(True)
    canvas.draw()

root = tk.Tk()
root.title("Function Plotter")
root.configure(bg='black')

plot_frame = tk.Frame(root, bg='black')
plot_frame.pack(padx=10, pady=10)

x_min_slider = tk.Scale(plot_frame, from_=-100, to=0, orient=tk.HORIZONTAL, label="Min Range", bg='white', fg='black', length=300)
x_min_slider.pack()

x_max_slider = tk.Scale(plot_frame, from_=0, to=100, orient=tk.HORIZONTAL, label="Max Range", bg='white', fg='black', length=300)
x_max_slider.pack()

equation_var = tk.StringVar()
equation_entry = tk.Entry(root, textvariable=equation_var, bg='white', fg='black')
equation_entry.pack(padx=10, pady=5)
equation_label = tk.Label(root, text="Enter a function (use 'x' as the variable and trig functions without 'np.'):", fg='white', bg='black')
equation_label.pack(padx=10, pady=5)

plot_button = tk.Button(root, text="Plot", command=plot_function, bg='white', fg='black')
plot_button.pack(padx=10, pady=5)

fig, ax = plt.subplots()
canvas = FigureCanvasTkAgg(fig, master=root)
canvas_widget = canvas.get_tk_widget()
canvas_widget.pack()

output_label = tk.Label(root, text="", fg="red", bg='black')
output_label.pack()

root.mainloop()
