from kivymd.app import MDApp
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.label import MDLabel
from kivymd.uix.textfield import MDTextField
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.core.window import Window
from kivymd.uix.dialog import MDDialog
from kivymd.uix.selectioncontrol import MDCheckbox
from kivy.uix.gridlayout import GridLayout

class ManipulaJanela:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def ajustar_tamanho_janela(self):
        # Definindo as dimensões da janela
        Window.size = (self.largura, self.altura)

class MeuApp(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.pessoas = []

    def build(self):
        manipulador = ManipulaJanela(400, 600)
        manipulador.ajustar_tamanho_janela()

        layout = MDBoxLayout(orientation='vertical', padding=20, spacing=20)

        # Campo para o nome da pessoa
        self.nome_input = MDTextField(hint_text="Nome")
        layout.add_widget(self.nome_input)

        # Campo para a idade
        self.idade_input = MDTextField(hint_text="Idade", input_filter="int")
        layout.add_widget(self.idade_input)

        # Layout para opções de sexo (usando MDCheckbox como "Radio Button")
        layout_sexo = MDBoxLayout(orientation='vertical', padding=10, spacing=10)
        layout_sexo.add_widget(MDLabel(text="Sexo:", halign="left"))

        # Grid para dispor os botões de seleção em uma linha
        sexo_grid = GridLayout(cols=2, size_hint=(None, None), width=400)

        # Checkbox para masculino
        self.masc_checkbox = MDCheckbox(group='sexo', active=True)
        sexo_grid.add_widget(self.masc_checkbox)
        sexo_grid.add_widget(MDLabel(text="Masculino"))

        # Checkbox para feminino
        self.fem_checkbox = MDCheckbox(group='sexo')
        sexo_grid.add_widget(self.fem_checkbox)
        sexo_grid.add_widget(MDLabel(text="Feminino"))

        layout_sexo.add_widget(sexo_grid)
        layout.add_widget(layout_sexo)

        # Botão para adicionar pessoa
        botao_incluir = MDRaisedButton(text="Incluir Pessoa", on_release=self.incluir_pessoa)
        layout.add_widget(botao_incluir)

        # Botão para listar pessoas
        botao_listar = MDRaisedButton(text="Listar Pessoas", on_release=self.listar_pessoas)
        layout.add_widget(botao_listar)

        # Rótulo para exibir o resultado
        self.resultado = MDLabel(text="Resultado: ", halign="center")
        layout.add_widget(self.resultado)

        return layout

    def incluir_pessoa(self, instance):
        nome = self.nome_input.text
        idade = self.idade_input.text

        # Validações simples
        if not nome or not idade:
            self.show_dialog("Erro", "Por favor, preencha todos os campos.")
            return

        # Definindo o sexo com base no checkbox selecionado
        sexo = "Masculino" if self.masc_checkbox.active else "Feminino"

        # Adicionando a pessoa ao dicionário
        self.pessoas.append({
            'nome': nome,
            'idade': idade,
            'sexo': sexo
        })

        # Limpa os campos
        self.nome_input.text = ""
        self.idade_input.text = ""
        self.masc_checkbox.active = True  # Resetar para masculino

        # Exibir uma mensagem de confirmação
        self.show_dialog("Sucesso", f"{nome} foi adicionado!")

    def listar_pessoas(self, instance):
        if not self.pessoas:
            self.show_dialog("Lista Vazia", "Nenhuma pessoa foi adicionada.")
            return

        resultado_texto = "Pessoas:\n"
        for pessoa in self.pessoas:
            resultado_texto += f"{pessoa['nome']} - Idade: {pessoa['idade']} - Sexo: {pessoa['sexo']}\n"

        self.resultado.text = resultado_texto

    def show_dialog(self, title, text):
        dialog = MDDialog(title=title, text=text, size_hint=(0.8, 1), buttons=[MDRaisedButton(text="OK", on_release=lambda x: dialog.dismiss())])
        dialog.open()

MeuApp().run()
