from kivymd.app import MDApp                        # idem a main0.py
from kivymd.uix.screen import Screen                # idem a main0.py
from kivymd.uix.datatables import MDDataTable       # idem a main1.py
from kivy.metrics import dp                         # idem a main1.py

class MainApp(MDApp):                               
    def build(self):                                # idem a main0.py

        self.title = "Prof. Saulo Santos | main_2.py"# idem a main0.py       

        self.screen = Screen()                      # idem a main0.py               

        self.tabela = MDDataTable(                  # idem a main1.py
            column_data = [                         # idem a main1.py
                ("ID", dp(20)),
                ("Nome", dp(20)),
                ("Sobrenome", dp(30)),
                ("Email", dp(40)),
                ("Telefone", dp(20))
            ],
            row_data = [                            # acessei o atributo 'row_data' e simulei a inserção de 2 registros na tabela. No exemplo main_8.py iniciarei o trabalho com BD.
                ("1","Saulo", "Santos","saulo@yahoo.com.br","1698134567"),
                ("2","Paulo", "Almeida","paulo@yahoo.com.br","1698789456")
            ]            
        )

        self.theme_cls.theme_style = "Light"         # idem a main0.py
        self.theme_cls.primary_palette = "BlueGray"  # idem a main0.py

        self.screen.add_widget(self.tabela)          # idem a main1.py

        return self.screen                           # idem a main0.py  
    
MainApp().run()                                      # idem a main0.py

