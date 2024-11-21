from kivymd.app import MDApp                                # idem a main_0.py
from kivymd.uix.screen import Screen                        # idem a main_0.py
from kivymd.uix.datatables import MDDataTable               # idem a main_1.py
from kivy.metrics import dp                                 # idem a main_1.py

class MainApp(MDApp):                               
    def build(self):                                        # idem a main_0.py

        self.title = "Prof. Saulo Santos | main_6.py"       # idem a main_0.py       

        self.screen = Screen()                              # idem a main_0.py               

        self.tabela = MDDataTable(                          # idem a main_1.py
            pos_hint = {'center_x':0.5,                     # idem a main_3.py
                        'center_y':0.5},
            size_hint=(0.9,0.6),                            # Alterei o valor 0.9 para 0.6 no eixo Y. Quero reduzir o tamanho da minha tabela para dar espaço para futuros widgets
            check = True,                                   # idem a main_4.py
            use_pagination = True,                          # A propriedade use_pagination tem valor default = False, quando True habilita a paginação.
            rows_num = 3,                                   # Defini que quero apresentar apenas 3 registros por página  
            pagination_menu_height = '120dp',               # Defini a altura da janela de paginação em 120dp. Faça um teste: altere para 60dp
            column_data = [                                 # idem a main_1.py
                ("ID", dp(20)),
                ("Nome", dp(20)),
                ("Sobrenome", dp(30)),
                ("Email", dp(40)),
                ("Telefone", dp(20))
            ],
            row_data = [                                    # Inclui mais 6 registros para simular a paginação
                ("1","Saulo", "Santos","saulo@yahoo.com.br","1698134567"),
                ("2","Paulo", "Almeida","paulo@yahoo.com.br","1698789456"),
                ("3","Saulo", "Santos","saulo@yahoo.com.br","1698134567"),
                ("4","Paulo", "Almeida","paulo@yahoo.com.br","1698789456"),
                ("5","Saulo", "Santos","saulo@yahoo.com.br","1698134567"),
                ("6","Paulo", "Almeida","paulo@yahoo.com.br","1698789456"),
                ("7","Saulo", "Santos","saulo@yahoo.com.br","1698134567"),
                ("8","Paulo", "Almeida","paulo@yahoo.com.br","1698789456")
            ]            
        )

        self.tabela.bind(on_check_press = self.checked)     # idem a main_5.py
                                                            # idem a main_5.py     

        self.theme_cls.theme_style = "Light"                # idem a main_0.py
        self.theme_cls.primary_palette = "Orange"           # idem a main_4.py

        self.screen.add_widget(self.tabela)                 # idem a main_1.py

        return self.screen                                  # idem a main_0.py


    def checked(self, tabela, linha):                       # idem a main_5.py 
        print('tabela: ',tabela, ' linha: ',linha)          # idem a main_5.py
                                                            # idem a main_5.py

    
MainApp().run()                                             # idem a main_0.py