# Para rodar esse código você precisa instalar a biblioteca kivymd
# Manual online do kivymd: https://kivymd.readthedocs.io/en/1.1.1/
# Como instalar:
#   1. Abra o terminal do vscode e digite: pip install kivymd
#   2. O kivymd deve rodar em qualquer versão 3.x do python.
# Após instalar o kivymd, execute o código deste arquivo, deverá aparecer uma janela com fundo branco.

from kivymd.app import MDApp                         # Classe principal do kivymd
from kivymd.uix.screen import Screen                 # Classe que instancia objetos screen

class MainApp(MDApp):                                # Criei uma classe MainApp(e herdei a classe MDApp aqui)
    def build(self):                                 # Todos os elementos gráficos (widgets) devem ser definidos aqui dentro desse método build()

        self.title = "Prof. Saulo Santos | main_0.py"# Define um título
        
        self.screen = Screen()                       # Screen() é um widget da biblioteca kivymd instancio um objeto da classe Screen() responsável por alocar dentro dela todos os outros widgets
                                                     # Em projetos anteriores estávamos usando um BoxLayout!

        self.theme_cls.theme_style = "Light"         # Temas possíveis para a aplicação. Troque Light (default) para Dark e execute o código.
        self.theme_cls.primary_palette = "BlueGray"  # Paleta de cor. Existem outras possibilidades. Veja abaixo. 

        return self.screen                           # Retorno do método build. Ele irá retornar o screen. Saiba que todos os widgets serão inseridos dentro deste objeto.
    
MainApp().run()                                      # Executa a aplicação

"""
"Red"
"Pink"
"Purple"
"DeepPurple"
"Indigo"
"Blue"
"LightBlue"
"Cyan"
"Teal"
"Green"
"LightGreen"
"Lime"
"Yellow"
"Amber"
"Orange"
"DeepOrange"
"Brown"
"Gray"
"BlueGray"
"""