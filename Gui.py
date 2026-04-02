import tkinter as tk
from tkinter import messagebox
from datetime import datetime

expenses = []
total = 0

def add_expense():
    global total

    name = entry_name.get()
    amount = entry_amount.get()

    if not name or not amount:
        return

    try:
        amount = int(amount) 
    except:
        return
    date = datetime.now().strftime("%d-%m-%Y %H:%M")
    expenses.append((name, amount, date))
    total += amount
    amount = entry_amount.get()
    try:
        amount = int(amount)
    except:
        return

    update_list()
    update_total()

    entry_name.delete(0, tk.END)
    entry_amount.delete(0, tk.END)

def delete_expense():
    global total

    try:
        selected = listbox.curselection()[0]
        total -= expenses[selected][1]
        expenses.pop(selected)

        update_list()
        update_total()
    except:
        messagebox.showwarning("Select an item to delete!")

def update_list():
    listbox.delete(0, tk.END)
    for exp in expenses:
        listbox.insert(tk.END, f"{exp[0]} | ₹{exp[1]} | {exp[2]}")

def update_total():
    label_total.config(text=f"Total: ₹{total}")

root = tk.Tk()
root.title("Expense Tracker")
root.geometry("400x500")

tk.Label(root, text="Name").pack()
entry_name = tk.Entry(root)
entry_name.pack()

tk.Label(root, text="Amount").pack()
entry_amount = tk.Entry(root)
entry_amount.pack()

tk.Button(root, text="Add Expense", command=add_expense).pack(pady=5)
tk.Button(root, text="Delete Selected", command=delete_expense).pack(pady=5)

listbox = tk.Listbox(root, width=50)
listbox.pack(pady=10)

label_total = tk.Label(root, text="Total: ₹0", font=("Arial", 12))
label_total.pack()

root.mainloop()