import tkinter as tk
from tkinter import ttk, messagebox
from bisection_logic import bisection_method
from gui_table import ResultTable
from gui_plot import PlotFrame

class BisectionApp:
    def _init_(self, master):
        self.master = master
        self.master.title("Metode Bisection")
        self.master.configure(bg="#2C1810")
        self.create_widgets()

    def create_widgets(self):
        # Frame Input
        frame_input = tk.Frame(self.master, bg="#2C1810", pady=10)
        frame_input.pack(side=tk.TOP, fill=tk.X)

        tk.Label(frame_input, text="Fungsi f(x):", bg="#2C1810", fg="white").grid(row=0, column=0, padx=5, pady=5)
        self.entry_func = tk.Entry(frame_input, width=40)
        self.entry_func.insert(0, "x**3 - 4*x + 1")
        self.entry_func.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(frame_input, text="a:", bg="#2C1810", fg="white").grid(row=1, column=0, padx=5, pady=5)
        self.entry_a = tk.Entry(frame_input)
        self.entry_a.insert(0, "-2")
        self.entry_a.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(frame_input, text="b:", bg="#2C1810", fg="white").grid(row=2, column=0, padx=5, pady=5)
        self.entry_b = tk.Entry(frame_input)
        self.entry_b.insert(0, "3")
        self.entry_b.grid(row=2, column=1, padx=5, pady=5)

        tk.Label(frame_input, text="ε (epsilon):", bg="#2C1810", fg="white").grid(row=3, column=0, padx=5, pady=5)
        self.entry_eps = tk.Entry(frame_input)
        self.entry_eps.insert(0, "0.001")
        self.entry_eps.grid(row=3, column=1, padx=5, pady=5)

        tk.Label(frame_input, text="Iterasi Maks:", bg="#2C1810", fg="white").grid(row=4, column=0, padx=5, pady=5)
        self.entry_iter = tk.Entry(frame_input)
        self.entry_iter.insert(0, "10")
        self.entry_iter.grid(row=4, column=1, padx=5, pady=5)

        tk.Button(frame_input, text="Hitung", command=self.calculate, bg="#B67E4C", fg="white").grid(row=5, column=1, pady=10)

        # Frame Output
        self.frame_output = tk.Frame(self.master, bg="#2C1810")
        self.frame_output.pack(fill=tk.BOTH, expand=True)

        # Table
        self.table = ResultTable(self.frame_output)
        self.table.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Plot
        self.plot = PlotFrame(self.frame_output)
        self.plot.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

    def calculate(self):
        func_str = self.entry_func.get()
        a = float(self.entry_a.get())
        b = float(self.entry_b.get())
        eps = float(self.entry_eps.get())
        max_iter = int(self.entry_iter.get())

        root, msg, results = bisection_method(func_str, a, b, eps, max_iter)

        if msg:
            messagebox.showwarning("Peringatan", msg)
        else:
            messagebox.showinfo("Hasil", f"Akar hampiran ≈ {root:.6f}")

        self.table.update_table(results)
        self.plot.plot_function(func_str, a, b, root)
