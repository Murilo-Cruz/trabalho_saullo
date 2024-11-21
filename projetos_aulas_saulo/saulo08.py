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

        # Quatro campos para as notas
        self.nota1 = MDTextField(hint_text="Digite a primeira nota", input_filter="float")
        self.nota2 = MDTextField(hint_text="Digite a segunda nota", input_filter="float")
        self.nota3 = MDTextField(hint_text="Digite a terceira nota", input_filter="float")
        self.nota4 = MDTextField(hint_text="Digite a quarta nota", input_filter="float")

        # Campo para a quantidade de aulas assistidas
        self.aulas_assistidas = MDTextField(hint_text="Aulas assistidas", input_filter="int")

        # Botão para calcular o resultado
        botao_calcular = MDRaisedButton(text="Calcular Resultado", on_release=self.calcular_resultado)

        # Rótulo para mostrar o resultado
        self.resultado = MDLabel(text="Resultado: ", halign="center")

        # Adicionando os widgets ao layout
        layout.add_widget(self.nota1)
        layout.add_widget(self.nota2)
        layout.add_widget(self.nota3)
        layout.add_widget(self.nota4)
        layout.add_widget(self.aulas_assistidas)
        layout.add_widget(botao_calcular)
        layout.add_widget(self.resultado)

        return layout

    def calcular_resultado(self, instance):
        try:
            # Pegando os valores digitados
            notas = [
                float(self.nota1.text),
                float(self.nota2.text),
                float(self.nota3.text),
                float(self.nota4.text)
            ]
            aulas_assistidas = int(self.aulas_assistidas.text)

            # Calculando a média das notas
            media = sum(notas) / len(notas)

            # Calculando a frequência
            total_aulas = 100
            frequencia = (aulas_assistidas / total_aulas) * 100

            # Determinando o resultado
            if frequencia < 75:
                resultado_final = f"Reprovado por falta! Média: {media:.2f}, Frequência: {frequencia:.2f}%"
            elif media < 3.0:
                resultado_final = f"Reprovado por nota! Média: {media:.2f}, Frequência: {frequencia:.2f}%"
            elif 75 <= frequencia and 3.0 <= media < 7.0:
                resultado_final = "Recuperação"
            elif frequencia >= 75 and media >= 7.0:
                resultado_final = "Aprovado"

            self.resultado.text = f"Resultado: {resultado_final}"
        except ValueError:
            self.resultado.text = "Por favor, insira valores válidos."


MeuApp().run()
