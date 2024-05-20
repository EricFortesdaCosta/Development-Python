import pandas as pd
from tkinter import *
from tkinter import messagebox

class AutomacaoBazar:
    def __init__(self, planilha):
        self.planilha = planilha
        self.colunas = ['Item', 'Descrição', 'Preço', 'Quantidade', 'Categoria', 'Disponível']
        self.df = self.carregar_bazar()

    def carregar_bazar(self):
        try:
            return pd.read_excel(self.planilha)
        except FileNotFoundError:
            return pd.DataFrame(columns=self.colunas)

    def adicionar_item(self, item_info):
        novo_item = pd.DataFrame([item_info], columns=self.colunas)
        self.df = pd.concat([self.df, novo_item], ignore_index=True)
        self.salvar_bazar()

    def visualizar_bazar(self):
        return self.df

    def remover_item(self, nome_item):
        self.df = self.df[self.df['Item'] != nome_item]
        self.salvar_bazar()

    def salvar_bazar(self):
        self.df.to_excel(self.planilha, index=False)

class InterfaceBazar:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestão de Bazar")

        cor_fundo = "#8FB8DE"
        cor_botao = "#2E5D95"

        self.root.configure(bg=cor_fundo)

        self.bazar = AutomacaoBazar("automaçãoBazar.xlsx")

        self.label_item = Label(root, text="Item:", bg=cor_fundo)
        self.entry_item = Entry(root)

        self.label_descricao = Label(root, text="Descrição:", bg=cor_fundo)
        self.entry_descricao = Entry(root)

        self.label_preco = Label(root, text="Preço:", bg=cor_fundo)
        self.entry_preco = Entry(root)

        self.label_quantidade = Label(root, text="Quantidade:", bg=cor_fundo)
        self.entry_quantidade = Entry(root)

        self.label_categoria = Label(root, text="Categoria:", bg=cor_fundo)
        self.entry_categoria = Entry(root)

        self.label_disponivel = Label(root, text="Disponível:", bg=cor_fundo)
        self.entry_disponivel = Entry(root)

        self.btn_adicionar = Button(root, text="Adicionar Item", command=self.adicionar_item, bg=cor_botao, fg="white", relief=FLAT)
        self.btn_remover = Button(root, text="Remover Item", command=self.remover_item, bg=cor_botao, fg="white", relief=FLAT)

        self.label_bazar = Label(root, text="Bazar Atual", bg=cor_fundo, font=("Arial", 12, "bold"))

        self.lista_bazar = Listbox(root, selectmode=SINGLE)
        self.lista_bazar.config(width=80, height=10)

        self.btn_atualizar_bazar = Button(root, text="Atualizar Bazar", command=self.atualizar_bazar, bg=cor_botao, fg="white", relief=FLAT)

        self.label_item.grid(row=0, column=0, padx=10, pady=5, sticky="w")
        self.entry_item.grid(row=0, column=1, padx=10, pady=5)

        self.label_descricao.grid(row=1, column=0, padx=10, pady=5, sticky="w")
        self.entry_descricao.grid(row=1, column=1, padx=10, pady=5)

        self.label_preco.grid(row=2, column=0, padx=10, pady=5, sticky="w")
        self.entry_preco.grid(row=2, column=1, padx=10, pady=5)

        self.label_quantidade.grid(row=3, column=0, padx=10, pady=5, sticky="w")
        self.entry_quantidade.grid(row=3, column=1, padx=10, pady=5)

        self.label_categoria.grid(row=4, column=0, padx=10, pady=5, sticky="w")
        self.entry_categoria.grid(row=4, column=1, padx=10, pady=5)

        self.label_disponivel.grid(row=5, column=0, padx=10, pady=5, sticky="w")
        self.entry_disponivel.grid(row=5, column=1, padx=10, pady=5)

        self.btn_adicionar.grid(row=6, column=0, columnspan=2, pady=10)
        self.btn_remover.grid(row=6, column=1, pady=10)

        self.label_bazar.grid(row=7, column=0, columnspan=2, pady=10)

        self.lista_bazar.grid(row=8, column=0, columnspan=2, padx=10, pady=5)

        self.btn_atualizar_bazar.grid(row=9, column=0, columnspan=2, pady=10)

        self.atualizar_bazar()

    def adicionar_item(self):
        try:
            item_info = {
                'Item': self.entry_item.get(),
                'Descrição': self.entry_descricao.get(),
                'Preço': self.entry_preco.get(),
                'Quantidade': self.entry_quantidade.get(),
                'Categoria': self.entry_categoria.get(),
                'Disponível': self.entry_disponivel.get(),
            }

            self.bazar.adicionar_item(item_info)
            self.atualizar_bazar()
            messagebox.showinfo("Sucesso", "Item adicionado com sucesso!")

            self.entry_item.delete(0, END)
            self.entry_descricao.delete(0, END)
            self.entry_preco.delete(0, END)
            self.entry_quantidade.delete(0, END)
            self.entry_categoria.delete(0, END)
            self.entry_disponivel.delete(0, END)

        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao adicionar item: {str(e)}")

    def atualizar_bazar(self):
        self.lista_bazar.delete(0, END)

        bazar_atual = self.bazar.visualizar_bazar()

        for index, row in bazar_atual.iterrows():
            item_info = f"Item: {row['Item']}, Descrição: {row['Descrição']}, Preço: {row['Preço']}, Quantidade: {row['Quantidade']}, Categoria: {row['Categoria']}, Disponível: {row['Disponível']}"
            self.lista_bazar.insert(END, item_info)

    def remover_item(self):
        try:
            indice_selecionado = self.lista_bazar.curselection()[0]
            nome_item = self.bazar.df.iloc[indice_selecionado]['Item']
            self.bazar.remover_item(nome_item)
            self.atualizar_bazar()
            messagebox.showinfo("Sucesso", "Item removido com sucesso!")

        except IndexError:
            messagebox.showwarning("Aviso", "Por favor, selecione um item para remover.")

if __name__ == "__main__":
    root = Tk()
    app = InterfaceBazar(root)
    root.mainloop()
