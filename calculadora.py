import tkinter as tk

window = tk.Tk()

window.geometry("400x200")
window.title("Calculadora Simples")

frame = tk.Frame(window)

frame.pack(padx=10, pady=10, fill='x', expand=True)

# Labels
num1 = tk.Label(frame, text="Digite o primeiro número")
num1.grid(row=0, column=0, padx=5, pady=5)

num2 = tk.Label(frame, text="Digite o segundo número")
num2.grid(row=0, column=1, padx=5, pady=5)

# Entradas
num1_inp = tk.Entry(frame)
num1_inp.grid(row=1, column=0, padx=5, pady=5)

num2_inp = tk.Entry(frame)
num2_inp.grid(row=1, column=1, padx=5, pady=5)

# Botões
button_sum = tk.Button(frame, text="Somar")
button_sum.grid(row=2, column=0, padx=5, pady=10)

button_sub = tk.Button(frame, text="Subtrair")
button_sub.grid(row=2, column=1, padx=5, pady=10)

button_multi = tk.Button(frame, text="Multiplicar")
button_multi.grid(row=3, column=0, padx=5, pady=10)

button_div = tk.Button(frame, text="Dividir")
button_div.grid(row=3, column=1, padx=5, pady=10)

window.mainloop()