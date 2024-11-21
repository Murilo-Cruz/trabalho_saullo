from kivymd.app import MDApp                                # idem a main_0.py
from kivymd.uix.screen import Screen                        # idem a main_0.py
from kivymd.uix.datatables import MDDataTable               # idem a main_1.py
from kivy.metrics import dp                                 # idem a main_1.py

class MainApp(MDApp):                               
    def build(self):                                        # idem a main_0.py

        self.title = "Prof. Saulo Santos | main_5.py"       # idem a main_0.py       

        self.screen = Screen()                              # idem a main_0.py               

        self.tabela = MDDataTable(                          # idem a main_1.py
            pos_hint = {'center_x':0.5,                     # idem a main_3.py
                        'center_y':0.5},
            size_hint=(0.9,0.9),                            # idem a main_3.py
            check = True,                                   # idem a main_4.py
            column_data = [                                 # idem a main_1.py
                ("ID", dp(20)),
                ("Nome", dp(20)),
                ("Sobrenome", dp(30)),
                ("Email", dp(40)),
                ("Telefone", dp(20))
            ],
            row_data = [                                    # idem a main_2.py
                ("1","Saulo", "Santos","saulo@yahoo.com.br","1698134567"),
                ("2","Paulo", "Almeida","paulo@yahoo.com.br","1698789456")
            ]            
        )

        self.tabela.bind(on_check_press = self.checked)     # Acionei o método bind que tratará do evento de click do mouse sobre uma linha da tabela. 
                                                            # Ao clicar no tabela, o método 'checked' que vou programar será chamado.      

        self.theme_cls.theme_style = "Light"                # idem a main_0.py
        self.theme_cls.primary_palette = "Orange"           # idem a main_4.py

        self.screen.add_widget(self.tabela)                 # idem a main_1.py

        return self.screen                                  # idem a main_0.py


    def checked(self, tabela, linha):                       # Estou criando o método checked. Por default, esse método possui esses tres parâmetros: self, tabela, linha 
        print('tabela: ',tabela, ' linha: ',linha)          # Como ainda não tenho uma tabela de BD nesse projeto, vou apenas imprimir os parâmetros no console. Verifique a impressão.
                                                            # No caso da tabela, ele irá imprimir o endereço de memória alocado ao objeto tabela. 

    
MainApp().run()                                             # idem a main_0.py
