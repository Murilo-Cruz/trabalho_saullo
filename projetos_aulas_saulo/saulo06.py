from kivymd.app import MDApp
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.label import MDLabel
from kivymd.uix.textfield import MDTextField
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.core.window import Window


class ManipulaJanela:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def ajustar_tamanho_janela(self):
        # Definindo as dimensões da janela
        Window.size = (self.largura, self.altura)


class MeuApp(MDApp):
    def build(self):
        manipulador = ManipulaJanela(400, 600)
        manipulador.ajustar_tamanho_janela()

        layout = MDBoxLayout(orientation='vertical', padding=20, spacing=20)

        # Três campos para os três lados do triângulo
        self.lado1 = MDTextField(hint_text="Digite o primeiro lado", input_filter="int")
        self.lado2 = MDTextField(hint_text="Digite o segundo lado", input_filter="int")
        self.lado3 = MDTextField(hint_text="Digite o terceiro lado", input_filter="int")

        # Botão para verificar se forma triângulo
        botao_verificar = MDRaisedButton(text="Verificar Triângulo", on_release=self.verificar_triangulo)

        # Rótulo para mostrar o resultado
        self.resultado = MDLabel(text="Resultado: ", halign="center")

        # Adicionando os widgets ao layout
        layout.add_widget(self.lado1)
        layout.add_widget(self.lado2)
        layout.add_widget(self.lado3)
        layout.add_widget(botao_verificar)
        layout.add_widget(self.resultado)

        return layout

    def verificar_triangulo(self, instance):
        try:
            # Pegando os valores digitados
            a = int(self.lado1.text)
            b = int(self.lado2.text)
            c = int(self.lado3.text)

            # Verificando a condição de existência do triângulo
            if a + b > c and a + c > b and b + c > a:
                tipo_triangulo = self.identificar_tipo_triangulo(a, b, c)
                self.resultado.text = f"Os números formam um triângulo: {tipo_triangulo}!"
            else:
                self.resultado.text = "Os números NÃO formam um triângulo!"
        except ValueError:
            self.resultado.text = "Por favor, insira números válidos."

    def identificar_tipo_triangulo(self, a, b, c):
        if a == b == c:
            return "Equilátero"
        elif a == b or a == c or b == c:
            return "Isósceles"
        else:
            return "Escaleno"


MeuApp().run()
