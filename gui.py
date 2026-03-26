import tkinter as tk
from tkinter import messagebox
from tracker import calculate_portfolio

portfolio = {}

def add_stock():
    symbol = stock_entry.get().upper()

    try:
        qty = int(quantity_entry.get())
    except ValueError:
        messagebox.showerror("Error", "Invalid quantity!")
        return

    portfolio[symbol] = portfolio.get(symbol, 0) + qty
    messagebox.showinfo("Success", f"{symbol} added!")

    stock_entry.delete(0, tk.END)
    quantity_entry.delete(0, tk.END)


def calculate():
    total, result = calculate_portfolio(portfolio)

    output = ""
    for stock, data in result.items():
        if isinstance(data, dict):
            output += f"{stock}: {data['value']}\n"
        else:
            output += f"{stock}: Not Found\n"

    output += f"\nTotal: {total}"
    result_label.config(text=output)


# UI Setup
root = tk.Tk()
root.title("Stock Tracker GUI")
root.geometry("350x400")

tk.Label(root, text="Stock Symbol").pack()
stock_entry = tk.Entry(root)
stock_entry.pack()

tk.Label(root, text="Quantity").pack()
quantity_entry = tk.Entry(root)
quantity_entry.pack()

tk.Button(root, text="Add Stock", command=add_stock).pack(pady=5)
tk.Button(root, text="Calculate", command=calculate).pack(pady=5)

result_label = tk.Label(root, text="", justify="left")
result_label.pack()

root.mainloop()