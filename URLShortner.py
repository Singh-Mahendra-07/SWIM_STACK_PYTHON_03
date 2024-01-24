import tkinter as tk
from tkinter import messagebox
import pyshorteners


def shorten_url():
    long_url = entry_long_url.get()

    if not long_url:
        messagebox.showwarning("Error", "Please enter a URL")
        return

    try:
        s = pyshorteners.Shortener()
        short_url = s.tinyurl.short(long_url)
        entry_short_url.delete(0, tk.END)  # Clear the previous value
        entry_short_url.insert(0, short_url)
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")


def clear_textboxes():
    entry_long_url.delete(0, tk.END)
    entry_short_url.delete(0, tk.END)


# main window
root = tk.Tk()
root.title("URL Shortener")

# widgets
label_long_url = tk.Label(root, text="Enter Long URL:")
label_long_url.grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)

entry_long_url = tk.Entry(root, width=40)
entry_long_url.grid(row=0, column=1, padx=10, pady=10)

label_short_url = tk.Label(root, text="Shortened URL:")
label_short_url.grid(row=1, column=0, padx=10, pady=10, sticky=tk.W)

entry_short_url = tk.Entry(root, width=40)
entry_short_url.grid(row=1, column=1, padx=10, pady=10)

button_convert = tk.Button(root, text="Convert", command=shorten_url)
button_convert.grid(row=2, column=0, columnspan=2, pady=10)

button_clear = tk.Button(root, text="Clear", command=clear_textboxes)
button_clear.grid(row=3, column=0, columnspan=2, pady=10)

root.mainloop()