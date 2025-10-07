import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from function_parser import evaluate_function

class PlotFrame(tk.Frame):
    def _init_(self, master):
        super()._init_(master, bg="#2C1810")
        self.figure = Figure(figsize=(5, 4), dpi=100)
        self.ax = self.figure.add_subplot(111)
        self.canvas = FigureCanvasTkAgg(self.figure, self)
        self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

    def plot_function(self, func_str, a, b, root):
        import numpy as np
        x = np.linspace(a - 1, b + 1, 400)
        y = [evaluate_function(func_str, val) for val in x]
        self.ax.clear()
        self.ax.plot(x, y, color="#D4A373")
        self.ax.axhline(0, color="white", linestyle="--")
        self.ax.axvline(root, color="red", linestyle="--")
        self.ax.set_title("Grafik f(x)", color="white")
        self.ax.set_facecolor("#3B2314")
        self.figure.patch.set_facecolor("#2C1810")
        self.canvas.draw()
