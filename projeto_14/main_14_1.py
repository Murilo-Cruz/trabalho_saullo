from kivymd.app import MDApp                          # idem a main0.py
from kivymd.uix.screen import Screen                  # idem a main0.py
from kivymd.uix.datatables import MDDataTable         # widget que cria uma tabela para apresentação de dados.
from kivy.metrics import dp                           # Permite espaçar os títulos da tabela

class MainApp(MDApp):                               
    def build(self):                                  # idem a main0.py

        self.title = "Prof. Saulo Santos | main_1.py" # Define um título        

        self.screen = Screen()                        # idem a main0.py               

        self.tabela = MDDataTable(                    # Instanciamos um objeto denominado 'tabela' 
            column_data = [                           # acessei o atributo 'column_data' e montei os títulos da tabela que irá apresentar os futuros registros de nosso banco de dados
                ("ID", dp(20)),
                ("Nome", dp(20)),
                ("Sobrenome", dp(30)),
                ("Email", dp(30)),
                ("Telefone", dp(30))
            ]            
        )

        self.theme_cls.theme_style = "Light"          # idem a main0.py
        self.theme_cls.primary_palette = "BlueGray"   # idem a main0.py

        self.screen.add_widget(self.tabela)           # insere o widget 'tabela' dentro do widget 'screen'. Lembre-se das aulas anteriores. Screen serve como um container para todos os outros widgets

        return self.screen                            # idem a main0.py  
    
MainApp().run()                                       # idem a main0.py