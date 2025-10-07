import tkinter as tk
from tkinter import ttk

class ResultTable(tk.Frame):
    def _init_(self, master):
        super()._init_(master, bg="#2C1810")
        self.tree = ttk.Treeview(self, columns=("i", "a", "b", "c", "fa", "fb", "fc"), show="headings")
        self.tree.pack(fill=tk.BOTH, expand=True)

        for col in self.tree["columns"]:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=100, anchor="center")

    def update_table(self, results):
        for row in self.tree.get_children():
            self.tree.delete(row)
        for r in results:
            self.tree.insert("", "end", values=[round(x, 6) if isinstance(x, float) else x for x in r])
