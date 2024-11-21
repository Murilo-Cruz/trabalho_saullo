from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.textfield import MDTextField
from kivymd.uix.button import MDRaisedButton
from kivy.metrics import dp


class CalculadoraFinanceira(MDBoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', padding=20, spacing=dp(10), **kwargs)

        self.add_widget(MDLabel(text="Ações em carteira:", halign="center"))
        self.acoes_carteira = MDTextField(hint_text="Número de ações em carteira")
        self.add_widget(self.acoes_carteira)

        self.add_widget(MDLabel(text="Preço médio de compra (R$):", halign="center"))
        self.preco_medio_carteira = MDTextField(hint_text="Preço médio de compra")
        self.add_widget(self.preco_medio_carteira)

        self.add_widget(MDLabel(text="Ações compradas:", halign="center"))
        self.acoes_compradas = MDTextField(hint_text="Número de ações compradas")
        self.add_widget(self.acoes_compradas)

        self.add_widget(MDLabel(text="Preço de compra (R$):", halign="center"))
        self.preco_compra_atual = MDTextField(hint_text="Preço de compra atual")
        self.add_widget(self.preco_compra_atual)

        self.add_widget(MDLabel(text="Preço de venda (R$):", halign="center"))
        self.preco_venda = MDTextField(hint_text="Preço de venda")
        self.add_widget(self.preco_venda)

        self.botao_calcular = MDRaisedButton(text="Calcular", on_release=self.calcular_resultados)
        self.add_widget(self.botao_calcular)

        self.resultado = MDLabel(text="", halign="center", theme_text_color="Secondary")
        self.add_widget(self.resultado)

    def calcular_resultados(self, instance):
        try:
            # Obtendo os dados da interface
            acoes_carteira = int(self.acoes_carteira.text)
            preco_medio_carteira = float(self.preco_medio_carteira.text)
            acoes_compradas = int(self.acoes_compradas.text)
            preco_compra_atual = float(self.preco_compra_atual.text)
            preco_venda = float(self.preco_venda.text)

            # Cálculos
            preco_medio_final = ((acoes_carteira * preco_medio_carteira) + 
                                 (acoes_compradas * preco_compra_atual)) / (acoes_carteira + acoes_compradas)
            lucro = (acoes_carteira + acoes_compradas) * preco_venda - (acoes_carteira * preco_medio_carteira + 
                                                                         acoes_compradas * preco_compra_atual)
            imposto_renda = lucro * 0.15 if lucro > 0 else 0

            # Exibindo resultados
            resultado_texto = (
                f"Preço médio de compra: R${preco_medio_final:.2f}\n"
                f"Lucro obtido: R${lucro:.2f}\n"
                f"Imposto de renda (15%): R${imposto_renda:.2f}"
            )
            self.resultado.text = resultado_texto
        except ValueError:
            self.resultado.text = "Por favor, insira valores válidos."


class MeuApp(MDApp):
    def build(self):
        return CalculadoraFinanceira()


MeuApp().run()
