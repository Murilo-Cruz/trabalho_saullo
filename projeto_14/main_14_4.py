from kivymd.app import MDApp                          # idem a main_0.py
from kivymd.uix.screen import Screen                  # idem a main_0.py
from kivymd.uix.datatables import MDDataTable         # idem a main_1.py
from kivy.metrics import dp                           # idem a main_1.py

class MainApp(MDApp):                               
    def build(self):                                  # idem a main_0.py

        self.title = "Prof. Saulo Santos | main_4.py" # idem a main_0.py       

        self.screen = Screen()                        # idem a main_0.py               

        self.tabela = MDDataTable(                    # idem a main_1.py
            pos_hint = {'center_x':0.5,               # idem a main_3.py
                        'center_y':0.5},
            size_hint=(0.9,0.9),                      # idem a main_3.py
            check = True,                             # inclui um checkbox em cada linha da tabela. Vai servir no futuro para selecionar registros.
            column_data = [                           # idem a main_1.py
                ("ID", dp(20)),
                ("Nome", dp(20)),
                ("Sobrenome", dp(30)),
                ("Email", dp(40)),
                ("Telefone", dp(20))
            ],
            row_data = [                              # idem a main_2.py
                ("1","Saulo", "Santos","saulo@yahoo.com.br","1698134567"),
                ("2","Paulo", "Almeida","paulo@yahoo.com.br","1698789456")
            ]            
        )

        self.theme_cls.theme_style = "Light"          # idem a main_0.py
        self.theme_cls.primary_palette = "Orange"     # Alterei a cor para 'Orange'. Agora você começa a ver onde a paleta atua.

        self.screen.add_widget(self.tabela)           # idem a main_1.py

        return self.screen                            # idem a main_0.py  
    
MainApp().run()                                       # idem a main_0.py


