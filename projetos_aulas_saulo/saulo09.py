import requests
from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.textfield import MDTextField
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.core.window import Window
from kivymd.uix.dialog import MDDialog

class ManipulaJanela:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def ajustar_tamanho_janela(self):
        Window.size = (self.largura, self.altura)

class BuscaCEP(MDBoxLayout):
    def pesquisar(self):
        entrada_dados = self.ids.entrada_dados.text
        saida_dados = self.ids.saida_dados
        
        if entrada_dados.isdigit() and len(entrada_dados) == 8:
            url = f'http://viacep.com.br/ws/{entrada_dados}/json/'
            response = requests.get(url)
            data = response.json()
            
            if 'erro' in data:
                saida_dados.text = 'CEP não encontrado.'
            else:
                endereco = (
                    f"CEP: {data['cep']}\nLogradouro: {data['logradouro']}\n"
                    f"Bairro: {data['bairro']}\nCidade: {data['localidade']}\n"
                    f"Estado: {data['uf']}"
                )
                saida_dados.text = endereco
        else:
            saida_dados.text = 'CEP inválido.'

class MeuApp(MDApp):
    def build(self):
        manipulador = ManipulaJanela(400, 600)
        manipulador.ajustar_tamanho_janela()

        # Criando o layout principal
        layout = MDBoxLayout(orientation='vertical', padding=20, spacing=20)

        # Campo de entrada para o CEP
        self.entrada_dados = MDTextField(
            hint_text="Digite o CEP",
            helper_text="Apenas números (ex: 01001000)",
            helper_text_mode="on_focus",
            max_text_length=8,
            id="entrada_dados"
        )
        layout.add_widget(self.entrada_dados)

        # Botão para pesquisar o CEP
        botao_pesquisar = MDRaisedButton(text="Pesquisar CEP", on_release=self.pesquisar_cep)
        layout.add_widget(botao_pesquisar)

        # Área de saída de dados
        self.saida_dados = MDLabel(
            text="Resultado: ",
            halign="left",
            id="saida_dados"
        )
        layout.add_widget(self.saida_dados)

        return layout

    def pesquisar_cep(self, instance):
        entrada_dados = self.entrada_dados.text
        saida_dados = self.saida_dados

        if entrada_dados.isdigit() and len(entrada_dados) == 8:
            url = f'http://viacep.com.br/ws/{entrada_dados}/json/'
            response = requests.get(url)
            data = response.json()

            if 'erro' in data:
                saida_dados.text = 'CEP não encontrado.'
            else:
                endereco = (
                    f"CEP: {data['cep']}\nLogradouro: {data['logradouro']}\n"
                    f"Bairro: {data['bairro']}\nCidade: {data['localidade']}\n"
                    f"Estado: {data['uf']}"
                )
                saida_dados.text = endereco
        else:
            saida_dados.text = 'CEP inválido.'

MeuApp().run()
