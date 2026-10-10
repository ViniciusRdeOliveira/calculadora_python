import tkinter as tk

window = tk.Tk()

window.geometry("500x400")
window.title("Calculadora Simples")

# Frame principal
frame = tk.Frame(window)
frame.pack(fill="both", expand=True)

# Frame centralizado
content_frame = tk.Frame(frame)
content_frame.place(relx=0.5, rely=0.5, anchor="center")

# Labels
num1 = tk.Label(content_frame, text="Digite o primeiro número")
num1.grid(row=0, column=0, padx=5, pady=10)

num2 = tk.Label(content_frame, text="Digite o segundo número")
num2.grid(row=0, column=2, padx=5, pady=10)

resultado = tk.Label(content_frame, text="Resultado: ")
resultado.grid(row=3, column=0, columnspan=4, pady=10)

# Entradas
num1_inp = tk.Entry(content_frame)
num1_inp.grid(row=1, column=0, padx=5, pady=5)

num2_inp = tk.Entry(content_frame)
num2_inp.grid(row=1, column=2, padx=5, pady=5)


# Função para realizar as operações
def clickResultado(operacao):
    try:
        n1 = float(num1_inp.get().replace(",", ".")) #tratamento para transformar input em decimal e utilização de . ou , 
        n2 = float(num2_inp.get().replace(",", "."))

        if operacao == "somar":
            res = n1 + n2

        elif operacao == "subtrair":
            res = n1 - n2

        elif operacao == "multiplicar":
            res = n1 * n2

        elif operacao == "dividir":
            if n2 == 0:
                resultado.config(text="Não é possível dividir por zero!")
                return
            res = n1 / n2

        resultado.config(text=f"Resultado: {res:g}")

    except ValueError:
        resultado.config(text="Digite dois números válidos!")


# Botões
button_sum = tk.Button(
    content_frame,
    text="Somar",
    command=lambda: clickResultado("somar")
)
button_sum.grid(row=2, column=0, padx=5, pady=5)

button_sub = tk.Button(
    content_frame,
    text="Subtrair",
    command=lambda: clickResultado("subtrair")
)
button_sub.grid(row=2, column=1, padx=5, pady=5)

button_multi = tk.Button(
    content_frame,
    text="Multiplicar",
    command=lambda: clickResultado("multiplicar")
)
button_multi.grid(row=2, column=2, padx=5, pady=5)

button_div = tk.Button(
    content_frame,
    text="Dividir",
    command=lambda: clickResultado("dividir")
)
button_div.grid(row=2, column=3, padx=5, pady=5)

window.mainloop()
