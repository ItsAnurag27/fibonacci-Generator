import tkinter as tk

def calculate_fibonacci():
  try:
    num = int(entry.get())
    if num < 0:
      result_label.config(text="Please enter a integer")
      return
    fib_series = [0, 1]
    for i in range(2, num + 1):
      fib_series.append(fib_series[i - 1] + fib_series[i - 2])
    result_label.config(text=f"Fibonacci Series: {fib_series}")
  except ValueError:
    result_label.config(text="Invalid . Please enter a number")

root = tk.Tk()
root.title("Fibonacci  Generator")

entry = tk.Entry(root)
entry.pack()

calculate_button = tk.Button(root, text="Generate", command=calculate_fibonacci)
calculate_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()

