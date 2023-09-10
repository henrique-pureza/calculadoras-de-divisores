import tkinter as tk
from   tkinter import ttk, messagebox

def calcular_divisores():
    texto_digitado = get_numero.get()

    if not texto_digitado.isnumeric():
        messagebox.showerror(
            title="Erro",
            message="Você não digitou um número válido. Não é possível haver letras ou números negativos digitados."
        )
    else:
        numero = int(texto_digitado)

        divisores_arr = [str(i) for i in range(1, numero + 1) if numero % i == 0]
        divisores     = ", ".join(divisores_arr)

        messagebox.showinfo(
            title="Resultado",
            message=f"Os divisores de {numero} são: {divisores}."
        )

def limpar_texto():
    get_numero.set("")

# ------------------------------------------------- #

root = tk.Tk()
root.resizable(False, False)
root.title("Calculadora de Divisores Tkinter Procedural")

label_boas_vindas = ttk.Label(
    master=root,
    text="Bem-vindo à versão gráfica da Calculadora de Divisores!"
).grid(
    column=0,
    row=0,
    columnspan=4,
    padx=10,
    pady=5
)

label_digite_numero = ttk.Label(
    master=root,
    text="Digite um número:"
).grid(
    column=0,
    row=1,
    padx=5,
    pady=5
)

get_numero      = tk.StringVar()

textbox_numero  = ttk.Entry(
    master=root,
    width=20,
    textvariable=get_numero
).grid(
    column=1,
    row=1,
    padx=3,
    pady=5
)

botao_calcular = ttk.Button(
    master=root,
    text="Calcular",
    width=8,
    command=calcular_divisores
).grid(
    column=2,
    row=1,
    padx=(3, 2),
    pady=5
)

botao_limpar = ttk.Button(
    master=root,
    text="Limpar",
    width=8,
    command=limpar_texto
).grid(
    column=3,
    row=1,
    padx=(2, 5),
    pady=5
)

root.mainloop()
