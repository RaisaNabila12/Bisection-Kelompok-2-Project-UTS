import tkinter as tk
from tkinter import ttk

def create_table(parent, bg_color):
    cols = ('Iterasi', 'a', 'b', 'x_tengah', 'f(x_tengah)', 'Error Mutlak')
    tree = ttk.Treeview(parent, columns=cols, show='headings', height=10)
    for col in cols:
        tree.heading(col, text=col)
        tree.column(col, anchor='center', width=100)

    vsb = ttk.Scrollbar(parent, orient="vertical", command=tree.yview)
    vsb.pack(side='right', fill='y')
    tree.configure(yscrollcommand=vsb.set)
    tree.pack(fill='both', expand=True, pady=10)

    style = ttk.Style()
    style.theme_use("default")
    style.configure("Treeview.Heading", font=('Arial', 9, 'bold'))
    style.configure("Treeview", background="#E1E1E1", foreground="black", rowheight=25)
    style.map('Treeview', background=[('selected', '#549A9F')])

    return tree
