import pandas as pd
from tkinter import *
from tkinter import messagebox
import os

class InventarioProdutos:
    def __init__(self, planilha):
        self.planilha = planilha
        self.colunas = ['Serial', 'Estado', 'Data de Recebimento', 'Preço', 'Localização de Entrega', 'Entregue']
        self.df = self.carregar_inventario()

    def carregar_inventario(self):
        try:
            return pd.read_excel(self.planilha)
        except FileNotFoundError:
            return pd.DataFrame(columns=self.colunas)

    def adicionar_produto(self, produto_info):
        novo_produto = pd.DataFrame([produto_info], columns=self.colunas)
        self.df = pd.concat([self.df, novo_produto], ignore_index=True)
        self.salvar_inventario()

    def visualizar_inventario(self):
        return self.df

    def remover_produto(self, serial):
        self.df = self.df[self.df['Serial'] != serial]
        self.salvar_inventario()

    def salvar_inventario(self):
        self.df.to_excel(self.planilha, index=False)

class InterfaceGrafica:
    def __init__(self, root):
        self.root = root
        self.root.title("Inventário de Produtos")

        # Configurações de cores
        cor_fundo = "#8FB8DE"
        cor_botao = "#2E5D95"

        self.root.configure(bg=cor_fundo)

        self.inventario = InventarioProdutos("PlanilhaProdutos.xlsx")

        # Criação e posicionamento dos widgets
        self.label_serial = Label(root, text="Serial:", bg=cor_fundo)
        self.entry_serial = Entry(root)

        self.label_estado = Label(root, text="Estado:", bg=cor_fundo)
        self.entry_estado = Entry(root)

        self.label_data_recebimento = Label(root, text="Data de Recebimento (DD/MM/AAAA):", bg=cor_fundo)
        self.entry_data_recebimento = Entry(root)

        self.label_preco = Label(root, text="Preço:", bg=cor_fundo)
        self.entry_preco = Entry(root)

        self.label_localizacao = Label(root, text="Localização de Entrega:", bg=cor_fundo)
        self.entry_localizacao = Entry(root)

        self.label_entregue = Label(root, text="Entregue (Sim/Não):", bg=cor_fundo)
        self.entry_entregue = Entry(root)

        self.btn_adicionar = Button(root, text="Adicionar Produto", command=self.adicionar_produto, bg=cor_botao, fg="white", relief=FLAT)
        self.btn_apagar = Button(root, text="Remover Produto", command=self.remover_produto, bg=cor_botao, fg="white", relief=FLAT)

        self.label_inventario = Label(root, text="Inventário Atual", bg=cor_fundo, font=("Arial", 12, "bold"))

        self.lista_inventario = Listbox(root, selectmode=SINGLE)
        self.lista_inventario.config(width=80, height=10)

        self.btn_atualizar_inventario = Button(root, text="Atualizar Inventário", command=self.atualizar_inventario, bg=cor_botao, fg="white", relief=FLAT)

        # Posicionamento dos widgets
        self.label_serial.grid(row=0, column=0, padx=10, pady=5, sticky="w")
        self.entry_serial.grid(row=0, column=1, padx=10, pady=5)

        self.label_estado.grid(row=1, column=0, padx=10, pady=5, sticky="w")
        self.entry_estado.grid(row=1, column=1, padx=10, pady=5)

        self.label_data_recebimento.grid(row=2, column=0, padx=10, pady=5, sticky="w")
        self.entry_data_recebimento.grid(row=2, column=1, padx=10, pady=5)

        self.label_preco.grid(row=3, column=0, padx=10, pady=5, sticky="w")
        self.entry_preco.grid(row=3, column=1, padx=10, pady=5)

        self.label_localizacao.grid(row=4, column=0, padx=10, pady=5, sticky="w")
        self.entry_localizacao.grid(row=4, column=1, padx=10, pady=5)

        self.label_entregue.grid(row=5, column=0, padx=10, pady=5, sticky="w")
        self.entry_entregue.grid(row=5, column=1, padx=10, pady=5)

        self.btn_adicionar.grid(row=6, column=0, columnspan=2, pady=10)
        self.btn_apagar.grid(row=6, column=1, pady=10)

        self.label_inventario.grid(row=7, column=0, columnspan=2, pady=10)

        self.lista_inventario.grid(row=8, column=0, columnspan=2, padx=10, pady=5)

        self.btn_atualizar_inventario.grid(row=9, column=0, columnspan=2, pady=10)

        self.atualizar_inventario()

    def adicionar_produto(self):
        try:
            produto_info = {
                'Serial': self.entry_serial.get(),
                'Estado': self.entry_estado.get(),
                'Data de Recebimento': self.entry_data_recebimento.get(),
                'Preço': self.entry_preco.get(),
                'Localização de Entrega': self.entry_localizacao.get(),
                'Entregue': self.entry_entregue.get(),
            }

            self.inventario.adicionar_produto(produto_info)
            self.atualizar_inventario()
            messagebox.showinfo("Sucesso", "Produto adicionado com sucesso!")

            # Limpar os campos após adicionar o produto
            self.entry_serial.delete(0, END)
            self.entry_estado.delete(0, END)
            self.entry_data_recebimento.delete(0, END)
            self.entry_preco.delete(0, END)
            self.entry_localizacao.delete(0, END)
            self.entry_entregue.delete(0, END)

        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao adicionar produto: {str(e)}")

    def atualizar_inventario(self):
        self.lista_inventario.delete(0, END)

        inventario_atual = self.inventario.visualizar_inventario()

        for index, row in inventario_atual.iterrows():
            produto_info = f"Serial: {row['Serial']}, Estado: {row['Estado']}, Data de Recebimento: {row['Data de Recebimento']}, Preço: {row['Preço']}, Localização de Entrega: {row['Localização de Entrega']}, Entregue: {row['Entregue']}"
            self.lista_inventario.insert(END, produto_info)

    def remover_produto(self):
        try:
            # Obter o índice do item selecionado na lista
            indice_selecionado = self.lista_inventario.curselection()[0]

            # Obter o serial do produto com base no índice
            serial_produto = self.inventario.df.iloc[indice_selecionado]['Serial']

            # Chamar a função de remover produto
            self.inventario.remover_produto(serial_produto)

            # Atualizar o inventário após remover o produto
            self.atualizar_inventario()

            messagebox.showinfo("Sucesso", "Produto removido com sucesso!")

        except IndexError:
            messagebox.showwarning("Aviso", "Por favor, selecione um produto para remover.")

if __name__ == "__main__":
    root = Tk()
    app = InterfaceGrafica(root)
    root.mainloop()
