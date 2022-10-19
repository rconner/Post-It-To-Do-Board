import tkinter as tk

root = tk.Tk()



test = tk.Label(root, text="red", bg="red", fg="white")
test.pack(padx=10, pady=20, side=tk.LEFT)
test = tk.Label(root, text="green", bg="green", fg="white")
test.pack(padx=10, pady=20, side=tk.LEFT)
test = tk.Label(root, text="purple", bg="purple", fg="white")
test.pack(padx=10, pady=20, side=tk.LEFT)

test = tk.Label(root, text="red", bg="red", fg="white")
test.pack(padx=10, pady=20, side=tk.RIGHT)
test = tk.Label(root, text="green", bg="green", fg="white")
test.pack(padx=10, pady=20, side=tk.RIGHT)
test = tk.Label(root, text="purple", bg="purple", fg="white")
test.pack(padx=10, pady=20, side=tk.RIGHT)

root.mainloop()