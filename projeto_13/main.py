from kivymd.app import MDApp
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.label import MDLabel
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.core.window import Window
import random
import openpyxl

# Função para abrir e ler os dados do arquivo Excel. Recebe o caminho do arquivo Excel como parâmetro
def abre_arquivo_excel(path_do_arquivo):
    workbook = openpyxl.load_workbook(path_do_arquivo) # A função usa a biblioteca openpyxl para abrir o arquivo Excel especificado pelo caminho path_do_arquivo
    sheet = workbook.active #  Retorna a aba ativa onde os dados serão extraídos.

    data = [] # Inicializa uma lista vazia chamada data. Essa lista será preenchida com os dados lidos da planilha, onde cada linha da planilha será uma lista dentro desta lista.
    for row in sheet.iter_rows(values_only=True): # Esta função gera as linhas da planilha, retornando apenas os valores das células (ignorando formatação ou fórmulas).
        data.append(row) # Cada linha (representada por uma tupla de valores) é adicionada à lista data.

    return data

# Classe para manipulação da janela
class ManipulaJanela:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def ajustar_tamanho_janela(self):
        Window.size = (self.largura, self.altura)

# Classe principal do app
class MeuApp(MDApp):
    def __init__(self):
        super().__init__()
        self.pessoas = []  # Lista para armazenar os nomes lidos do Excel

    def build(self):
        manipulador = ManipulaJanela(400, 600)
        manipulador.ajustar_tamanho_janela()

        layout = MDBoxLayout(orientation='vertical', padding=20, spacing=20)

        # Carregar os dados do arquivo Excel
        # Os dados lidos do Excel são armazenados no atributo self.data. 
        # Esse atributo será uma lista de tuplas, onde cada tupla representa uma linha da planilha, e cada elemento da tupla é o valor de uma célula.
        # Exemplo:
        # [
        #     (1, 'Ana', 25),
        #     (2, 'João', 30),
        #     (3, 'Pedro', 22)
        # ]

        self.data = abre_arquivo_excel('arquivo_excel.xlsx') 

        # Esta linha usa uma list comprehension para extrair os nomes das pessoas do arquivo Excel, 
        # supondo que os nomes estão na segunda coluna.
        # O atributo self.pessoas é uma lista que armazena apenas os valores da segunda 
        # coluna (row[1]), ou seja, os nomes.
        # row[1]: refere-se ao segundo item de cada tupla em self.data. 
        # Então, para cada linha da planilha, o código está pegando o valor da segunda coluna (nome da pessoa).

        self.pessoas = [row[1] for row in self.data]  # Supondo que os nomes estão na segunda coluna

        # Exibir os dados lidos na interface
        # Esta é uma list comprehension que percorre cada linha de self.data fazendo uma concatenação de cada linha lida separando-as com \n.
        self.resultado = MDLabel(text='\n'.join([f'{row[0]}. {row[1]} ({row[2]})' for row in self.data]), halign="left")
        layout.add_widget(self.resultado)

        # Botão para sortear nome
        botao_sortear = MDRaisedButton(text="Sortear Nome", on_release=self.sortear_nome)
        layout.add_widget(botao_sortear)

        # Rótulo para exibir o nome sorteado
        self.nome_sorteado = MDLabel(text="Nome Sorteado: ", halign="center")
        layout.add_widget(self.nome_sorteado)

        return layout

    def sortear_nome(self, instance):
        if self.pessoas:
            random_name = random.choice(self.pessoas) # Faz uma escolha aleatória dentre os nomes armazenados na lista pessoas
            self.nome_sorteado.text = f'Nome Sorteado: {random_name}'
        else:
            self.nome_sorteado.text = 'Nenhum nome disponível para sorteio.'



MeuApp().run()
