# Corrected code snippet with 'pandas' library import
# Importing pandas library
import pandas as pd
from tkinter import *
from tkinter import messagebox

class InventarioDrones:
    def __init__(self, planilha):
        self.planilha = planilha
        self.colunas = ['Ano Produção', 'Serial', 'estado', 'peso', 'Nome', 'modelo', 'Data aquisição', 'Preço', 'Localização', 'Tempo de Voo', 'Modificação', 'Testado', 'recebido']
        self.df = self.carregar_inventario()

    def carregar_inventario(self):
        try:
            return pd.read_excel(self.planilha)
        except FileNotFoundError:
            return pd.DataFrame(columns=self.colunas)

    def adicionar_drone(self, drone_info):
        novo_drone = pd.DataFrame([drone_info], columns=self.colunas)
        self.df = pd.concat([self.df, novo_drone], ignore_index=True)
        self.salvar_inventario()

    def visualizar_inventario(self):
        return self.df

    def remover_drone(self, nome_drone):
        self.df = self.df[self.df['Nome'].str.lower() != nome_drone.lower()]
        self.salvar_inventario()

    def salvar_inventario(self):
        self.df.to_excel(self.planilha, index=False)

class InterfaceGrafica:
    def __init__(self, root):
        self.root = root
        self.root.title("Inventário de Drones")

        # Configurações de cores
        cor_fundo = "#8FB8DE"
        cor_botao = "#2E5D95"

        self.root.configure(bg=cor_fundo)

        self.inventario = InventarioDrones("PlanilhaDrone.xlsx")

        # Criação e posicionamento dos widgets
        self.label_ano_producao = Label(root, text="Ano de Produção:", bg=cor_fundo)
        self.entry_ano_producao = Entry(root)

        self.label_serial = Label(root, text="Serial do Drone:", bg=cor_fundo)
        self.entry_serial = Entry(root)

        self.label_estado = Label(root, text="Qual o estado do Drone:", bg=cor_fundo)
        self.entry_estado = Entry(root)

        self.label_peso = Label(root, text="Peso do Drone:", bg=cor_fundo)
        self.entry_peso = Entry(root)

        self.label_nome = Label(root, text="Nome do Drone:", bg=cor_fundo)
        self.entry_nome = Entry(root)

        self.label_modelo = Label(root, text="Modelo do Drone:", bg=cor_fundo)
        self.entry_modelo = Entry(root)

        self.label_data_aquisicao = Label(root, text="Data de Aquisição (DD/MM/AAAA):", bg=cor_fundo)
        self.entry_data_aquisicao = Entry(root)

        self.label_preco = Label(root, text="Preço do Drone:", bg=cor_fundo)
        self.entry_preco = Entry(root)

        self.label_localizacao = Label(root, text="Localização do Drone:", bg=cor_fundo)
        self.entry_localizacao = Entry(root)

        self.label_tempo_voo = Label(root, text="Tempo de Voo do Drone:", bg=cor_fundo)
        self.entry_tempo_voo = Entry(root)

        self.label_modificacao = Label(root, text="Modificação no Drone:", bg=cor_fundo)
        self.entry_modificacao = Entry(root)

        self.label_testado = Label(root, text="Testado:", bg=cor_fundo)
        self.entry_testado = Entry(root)

        self.label_recebido = Label(root, text="Quem Recebeu o Drone:", bg=cor_fundo)
        self.entry_recebido = Entry(root)

        self.btn_adicionar = Button(root, text="Adicionar Drone", command=self.adicionar_drone, bg=cor_botao, fg="white", relief=FLAT)
        self.btn_apagar = Button(root, text="Apagar Drone Selecionado", command=self.apagar_drone_selecionado, bg=cor_botao, fg="white", relief=FLAT)

        self.label_inventario = Label(root, text="Inventário Atual", bg=cor_fundo, font=("Arial", 12, "bold"))

        self.lista_inventario = Listbox(root, selectmode=SINGLE)
        self.lista_inventario.config(width=80, height=10)

        self.btn_atualizar_inventario = Button(root, text="Atualizar Inventário", command=self.atualizar_inventario, bg=cor_botao, fg="white", relief=FLAT)

        # Posicionamento dos widgets
        self.label_ano_producao.grid(row=0, column=0, padx=10, pady=5, sticky="w")
        self.entry_ano_producao.grid(row=0, column=1, padx=10, pady=5)

        self.label_serial.grid(row=1, column=0, padx=10, pady=5, sticky="w")
        self.entry_serial.grid(row=1, column=1, padx=10, pady=5)

        self.label_estado.grid(row=2, column=0, padx=10, pady=5, sticky="w")
        self.entry_estado.grid(row=2, column=1, padx=10, pady=5)

        self.label_peso.grid(row=3, column=0, padx=10, pady=5, sticky="w")
        self.entry_peso.grid(row=3, column=1, padx=10, pady=5)

        self.label_nome.grid(row=4, column=0, padx=10, pady=5, sticky="w")
        self.entry_nome.grid(row=4, column=1, padx=10, pady=5)

        self.label_modelo.grid(row=5, column=0, padx=10, pady=5, sticky="w")
        self.entry_modelo.grid(row=5, column=1, padx=10, pady=5)

        self.label_data_aquisicao.grid(row=6, column=0, padx=10, pady=5, sticky="w")
        self.entry_data_aquisicao.grid(row=6, column=1, padx=10, pady=5)

        self.label_preco.grid(row=7, column=0, padx=10, pady=5, sticky="w")
        self.entry_preco.grid(row=7, column=1, padx=10, pady=5)

        self.label_localizacao.grid(row=8, column=0, padx=10, pady=5, sticky="w")
        self.entry_localizacao.grid(row=8, column=1, padx=10, pady=5)

        self.label_tempo_voo.grid(row=9, column=0, padx=10, pady=5, sticky="w")
        self.entry_tempo_voo.grid(row=9, column=1, padx=10, pady=5)

        self.label_modificacao.grid(row=10, column=0, padx=10, pady=5, sticky="w")
        self.entry_modificacao.grid(row=10, column=1, padx=10, pady=5)

        self.label_testado.grid(row=11, column=0, padx=10, pady=5, sticky="w")
        self.entry_testado.grid(row=11, column=1, padx=10, pady=5)

        self.label_recebido.grid(row=12, column=0, padx=10, pady=5, sticky="w")
        self.entry_recebido.grid(row=12, column=1, padx=10, pady=5)

        self.btn_adicionar.grid(row=13, column=0, columnspan=2, pady=10)
        self.btn_apagar.grid(row=13, column=1, pady=10)

        self.label_inventario.grid(row=14, column=0, columnspan=2, pady=10)

        self.lista_inventario.grid(row=15, column=0, columnspan=2, padx=10, pady=5)

        self.btn_atualizar_inventario.grid(row=16, column=0, columnspan=2, pady=10)

        self.atualizar_inventario()

    def adicionar_drone(self):
        try:
            drone_info = {
                'Ano Produção': self.entry_ano_producao.get(),
                'Serial': self.entry_serial.get(),
                'estado': self.entry_estado.get(),
                'peso': self.entry_peso.get(),
                'Nome': self.entry_nome.get(),
                'modelo': self.entry_modelo.get(),
                'Data aquisição': self.entry_data_aquisicao.get(),
                'Preço': self.entry_preco.get(),
                'Localização': self.entry_localizacao.get(),
                'Tempo de Voo': self.entry_tempo_voo.get(),
                'Modificação': self.entry_modificacao.get(),
                'Testado': self.entry_testado.get(),
                'recebido': self.entry_recebido.get(),
            }

            self.inventario.adicionar_drone(drone_info)
            self.atualizar_inventario()
            messagebox.showinfo("Sucesso", "Drone adicionado com sucesso!")

            # Limpar os campos após adicionar o drone
            self.entry_ano_producao.delete(0, END)
            self.entry_serial.delete(0, END)
            self.entry_estado.delete(0, END)
            self.entry_peso.delete(0, END)
            self.entry_nome.delete(0, END)
            self.entry_modelo.delete(0, END)
            self.entry_data_aquisicao.delete(0, END)
            self.entry_preco.delete(0, END)
            self.entry_localizacao.delete(0, END)
            self.entry_tempo_voo.delete(0, END)
            self.entry_modificacao.delete(0, END)
            self.entry_testado.delete(0, END)
            self.entry_recebido.delete(0, END)

        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao adicionar drone: {str(e)}")

    def atualizar_inventario(self):
        self.lista_inventario.delete(0, END)

        inventario_atual = self.inventario.visualizar_inventario()

        for index, row in inventario_atual.iterrows():
            drone_info = f"Nome: {row['Nome']}, Modelo: {row['modelo']}, Preço: {row['Preço']}, Localização: {row['Localização']}, Tempo de Voo: {row['Tempo de Voo']}, Modificação: {row['Modificação']}, Testado: {row['Testado']}, Recebido por: {row['recebido']}"
            self.lista_inventario.insert(END, drone_info)

    def apagar_drone_selecionado(self):
        try:
            # Obter o índice do item selecionado na lista
            indice_selecionado = self.lista_inventario.curselection()[0]

            # Obter o nome do drone com base no índice
            nome_drone = self.inventario.df.iloc[indice_selecionado]['Nome']

            # Chamar a função de remover drone
            self.inventario.remover_drone(nome_drone)

            # Atualizar o inventário após remover o drone
            self.atualizar_inventario()

            messagebox.showinfo("Sucesso", "Drone removido com sucesso!")

        except IndexError:
            messagebox.showwarning("Aviso", "Por favor, selecione um drone para remover.")

if __name__ == "__main__":
    root = Tk()
    app = InterfaceGrafica(root)
    root.mainloop()
