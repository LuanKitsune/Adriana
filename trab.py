from tkinter import *
import tkinter as tk
import sqlite3
from tkinter.scrolledtext import ScrolledText
from tkinter import messagebox

# Cria uma conexão com o banco de dados
conexao = sqlite3.connect("cad_prod.db")

# Cria uma tabela para armazenar os dados da folha de pagamento
cursor = conexao.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS Produtos ("
               "id INTEGER PRIMARY KEY AUTOINCREMENT, "
               "nome TEXT, "
               "valor INTEGER, "
               "loja TEXT, "
               "marca TEXT)"
               )
conexao.commit()

janela = tk.Tk()
janela.title("Cadastro de Produto")
janela.geometry("300x300")
menu = tk.Menu(janela)
janela.config(menu=menu)

nome = tk.StringVar()
loja = tk.StringVar()
marca = tk.StringVar()
valor = tk.StringVar()


def verifica():
    nome_produto = entry_nome.get()
    if nome_produto == "":
        messagebox.showerror("Erro", "Por favor, preencha todos os campos.")
    else:
        messagebox.showinfo("Sucesso", "Informações enviadas com sucesso.")


scrolledText = ScrolledText(janela, width=50, height=10)

# Crie um menu dropdown Arquivo
Arqmenu = tk.Menu(menu, tearoff=False)
menu.add_cascade(label="Arquivo", menu=Arqmenu)

# Adicione opções no Arquivo
Arqmenu.add_command(label="Novo")
Arqmenu.add_command(label="Abrir")
Arqmenu.add_separator()
Arqmenu.add_command(label="Sair", command=janela.quit)

label_nome = Label(janela, text="Nome do Produto:", fg='purple', font=('Times'))
label_nome.grid(row=0, column=0)
entry_nome = Entry(janela, textvariable=nome)
entry_nome.grid(row=0, column=1)

label_valor = Label(janela, text="Horas Extras:", fg='purple', font=('Times'))
label_valor.grid(row=1, column=0)
entry_valor = Entry(janela, textvariable=valor)
entry_valor.grid(row=1, column=1)

label_marca = Label(janela, text="INSS (%):", fg='purple', font=('Times'))
label_marca.grid(row=2, column=0)
entry_marca = Entry(janela, textvariable=marca)
entry_marca.grid(row=2, column=1)

label_loja = Label(janela, text="IRPF (%):", fg='purple', font=('Times'))
label_loja.grid(row=3, column=0)
entry_loja = Entry(janela, textvariable=loja)
entry_loja.grid(row=3, column=1)


def salvar_produto():
    nome_produto = entry_nome.get()
    valor_produto = entry_valor.get()
    marca_produto = entry_marca.get()
    loja_produto = entry_loja.get()

    if nome_produto == "":
        messagebox.showerror("Erro", "Por favor, preencha todos os campos.")
    else:
        cursor.execute("INSERT INTO Produtos (nome, valor, loja, marca) VALUES (?, ?, ?, ?)",
                       (nome_produto, valor_produto, loja_produto, marca_produto))
        conexao.commit()
        messagebox.showinfo("Sucesso", "Informações enviadas com sucesso.")


buttonSubmit = Button(janela, text="Calcular e Salvar", fg='purple', font=('Times'),
command=salvar_produto)
buttonSubmit.grid(row=4, column=0)

janela.mainloop()