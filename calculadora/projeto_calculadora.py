import tkinter as tk
from tkinter import messagebox


def adicao():
    try:
        resultado = float(entry1.get()) + float(entry2.get())
        if(resultado.is_integer()):
            label_resultado.config(text=f"Resultado: {int(resultado)}")
        else:
            label_resultado.config(text=f"Resultado: {resultado}")
    except:
        messagebox.showerror("Erro", "Digite números válidos")

def subtracao():
    try:
        resultado = float(entry1.get()) - float(entry2.get())
        if(resultado.is_integer()):
            label_resultado.config(text=f"Resultado: {int(resultado)}")
        else:
            label_resultado.config(text=f"Resultado: {resultado}")
    except:
        messagebox.showerror("Erro", "Digite números válidos")

def multiplicacao():
    try:
        resultado = float(entry1.get()) * float(entry2.get())
        if(resultado.is_integer()):
            label_resultado.config(text=f"Resultado: {int(resultado)}")
        else:
            label_resultado.config(text=f"Resultado: {resultado}")
    except:
        messagebox.showerror("Erro", "Digite números válidos")

def divisao():
    try:
        num2 = float(entry2.get())
        if num2 == 0:
            messagebox.showerror("Erro", "Divisão por zero")
        else:
            resultado = float(entry1.get()) / num2
            if(resultado.is_integer()):
                label_resultado.config(text=f"Resultado: {int(resultado)}")
            else:
                label_resultado.config(text=f"Resultado: {resultado}")
    except:
        messagebox.showerror("Erro", "Digite números válidos")

janela = tk.Tk()
janela.title("Calculadora")
janela.geometry("300x250")

entry1 = tk.Entry(janela)
entry1.pack(pady=7)

entry2 = tk.Entry(janela)
entry2.pack(pady=7)

tk.Button(janela, text="Somar", command=adicao).pack(pady=2)
tk.Button(janela, text="Subtrair", command=subtracao).pack(pady=2)
tk.Button(janela, text="Multiplicar", command=multiplicacao).pack(pady=2)
tk.Button(janela, text="Dividir", command=divisao).pack(pady=2)


label_resultado = tk.Label(janela, text="Resultado:")
label_resultado.pack(pady=10)

janela.mainloop()