import pandas as pd
from tkinter import *
from tkinter import messagebox

class EstoqueAlimentos:
    def __init__(self, planilha):
        self.planilha = planilha
        self.colunas = ['Nome', 'Quantidade', 'Categoria', 'Data de Validade', 'Fornecedor', 'Preço Unitário']
        self.df = self.carregar_estoque()

    def carregar_estoque(self):
        try:
            return pd.read_excel(self.planilha)
        except FileNotFoundError:
            return pd.DataFrame(columns=self.colunas)

    def adicionar_alimento(self, alimento_info):
        novo_alimento = pd.DataFrame([alimento_info], columns=self.colunas)
        self.df = pd.concat([self.df, novo_alimento], ignore_index=True)
        self.salvar_estoque()

    def visualizar_estoque(self):
        return self.df

    def remover_alimento(self, nome_alimento):
        self.df = self.df[self.df['Nome'] != nome_alimento]
        self.salvar_estoque()

    def salvar_estoque(self):
        self.df.to_excel(self.planilha, index=False)

class InterfaceRestaurante:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestão de Estoque de Alimentos")

        cor_fundo = "#8FB8DE"
        cor_botao = "#2E5D95"

        self.root.configure(bg=cor_fundo)

        self.estoque = EstoqueAlimentos("estoqueAlimentos.xlsx")

        self.label_nome = Label(root, text="Nome:", bg=cor_fundo)
        self.entry_nome = Entry(root)

        self.label_quantidade = Label(root, text="Quantidade:", bg=cor_fundo)
        self.entry_quantidade = Entry(root)

        self.label_categoria = Label(root, text="Categoria:", bg=cor_fundo)
        self.entry_categoria = Entry(root)

        self.label_validade = Label(root, text="Data de Validade (DD/MM/AAAA):", bg=cor_fundo)
        self.entry_validade = Entry(root)

        self.label_fornecedor = Label(root, text="Fornecedor:", bg=cor_fundo)
        self.entry_fornecedor = Entry(root)

        self.label_preco = Label(root, text="Preço Unitário:", bg=cor_fundo)
        self.entry_preco = Entry(root)

        self.btn_adicionar = Button(root, text="Adicionar Alimento", command=self.adicionar_alimento, bg=cor_botao, fg="white", relief=FLAT)
        self.btn_remover = Button(root, text="Remover Alimento", command=self.remover_alimento, bg=cor_botao, fg="white", relief=FLAT)

        self.label_estoque = Label(root, text="Estoque Atual", bg=cor_fundo, font=("Arial", 12, "bold"))

        self.lista_estoque = Listbox(root, selectmode=SINGLE)
        self.lista_estoque.config(width=80, height=10)

        self.btn_atualizar_estoque = Button(root, text="Atualizar Estoque", command=self.atualizar_estoque, bg=cor_botao, fg="white", relief=FLAT)

        self.label_nome.grid(row=0, column=0, padx=10, pady=5, sticky="w")
        self.entry_nome.grid(row=0, column=1, padx=10, pady=5)

        self.label_quantidade.grid(row=1, column=0, padx=10, pady=5, sticky="w")
        self.entry_quantidade.grid(row=1, column=1, padx=10, pady=5)

        self.label_categoria.grid(row=2, column=0, padx=10, pady=5, sticky="w")
        self.entry_categoria.grid(row=2, column=1, padx=10, pady=5)

        self.label_validade.grid(row=3, column=0, padx=10, pady=5, sticky="w")
        self.entry_validade.grid(row=3, column=1, padx=10, pady=5)

        self.label_fornecedor.grid(row=4, column=0, padx=10, pady=5, sticky="w")
        self.entry_fornecedor.grid(row=4, column=1, padx=10, pady=5)

        self.label_preco.grid(row=5, column=0, padx=10, pady=5, sticky="w")
        self.entry_preco.grid(row=5, column=1, padx=10, pady=5)

        self.btn_adicionar.grid(row=6, column=0, columnspan=2, pady=10)
        self.btn_remover.grid(row=6, column=1, pady=10)

        self.label_estoque.grid(row=7, column=0, columnspan=2, pady=10)

        self.lista_estoque.grid(row=8, column=0, columnspan=2, padx=10, pady=5)

        self.btn_atualizar_estoque.grid(row=9, column=0, columnspan=2, pady=10)

        self.atualizar_estoque()

    def adicionar_alimento(self):
        try:
            alimento_info = {
                'Nome': self.entry_nome.get(),
                'Quantidade': self.entry_quantidade.get(),
                'Categoria': self.entry_categoria.get(),
                'Data de Validade': self.entry_validade.get(),
                'Fornecedor': self.entry_fornecedor.get(),
                'Preço Unitário': self.entry_preco.get(),
            }

            self.estoque.adicionar_alimento(alimento_info)
            self.atualizar_estoque()
            messagebox.showinfo("Sucesso", "Alimento adicionado com sucesso!")

            self.entry_nome.delete(0, END)
            self.entry_quantidade.delete(0, END)
            self.entry_categoria.delete(0, END)
            self.entry_validade.delete(0, END)
            self.entry_fornecedor.delete(0, END)
            self.entry_preco.delete(0, END)

        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao adicionar alimento: {str(e)}")

    def atualizar_estoque(self):
        self.lista_estoque.delete(0, END)

        estoque_atual = self.estoque.visualizar_estoque()

        for index, row in estoque_atual.iterrows():
            alimento_info = f"Nome: {row['Nome']}, Quantidade: {row['Quantidade']}, Categoria: {row['Categoria']}, Data de Validade: {row['Data de Validade']}, Fornecedor: {row['Fornecedor']}, Preço Unitário: {row['Preço Unitário']}"
            self.lista_estoque.insert(END, alimento_info)

    def remover_alimento(self):
        try:
            indice_selecionado = self.lista_estoque.curselection()[0]
            nome_alimento = self.estoque.df.iloc[indice_selecionado]['Nome']
            self.estoque.remover_alimento(nome_alimento)
            self.atualizar_estoque()
            messagebox.showinfo("Sucesso", "Alimento removido com sucesso!")

        except IndexError:
            messagebox.showwarning("Aviso", "Por favor, selecione um alimento para remover.")

if __name__ == "__main__":
    root = Tk()
    app = InterfaceRestaurante(root)
    root.mainloop()
