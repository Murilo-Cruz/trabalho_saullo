from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.datatables import MDDataTable
from kivy.metrics import dp
from kivymd.uix.textfield import MDTextField
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.label import MDLabel       

class MainApp(MDApp):

    def __init__(self, **kwargs):

        super().__init__(**kwargs)

        self.row_data_global = [
            ("CDB","Diária","1","Mensal"),
            ("CDB","180 dias","1.8","Mensal"),
            ("LCI","Diária","1","Mensal"),
            ("LCI","200 dias","1.5","Mensal"),
            ("Poupança","Diária","0.5","Mensal"),
            ("MXRF11","Diária","1","Mensal")
        ]

        self.taxa_global = 0

    def build(self):


        self.title = "Organizador de investimentos"
        self.screen = Screen()

        self.tabela = MDDataTable(

            pos_hint = {'center_x':0.5,'center_y':0.5},

            size_hint=(0.95,0.57), 

            column_data = [
                ("Nome do Investimento", dp(50)),
                ("Liquidez", dp(30)),
                ("Rendimento(%)", dp(30)),
                ("Retorno do Rendimento", dp(30))
            ],

            row_data = self.row_data_global,

            check = True,
            use_pagination = True,
            rows_num = 4,
            pagination_menu_height = '120dp',
            elevation = 8.5,          

        )

        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Red"
        self.tabela.bind(on_check_press = self.checked)

        self.textfield_valor = MDTextField(                
            hint_text = "Valor que será investido(R$)",                             
            helper_text = "Insira o valor",                  
            max_text_length = 100,                              
            size_hint_x = None,                               
            width = 195                                       
        )

        self.textfield_tempo = MDTextField(                
            hint_text = "Tempo em que quer deixar o dinheiro investido(meses)",                             
            helper_text = "Insira o tempo(meses)",                  
            max_text_length = 100,                              
            size_hint_x = None,                               
            width = 382                                       
        )

        self.boxLayout = MDBoxLayout(spacing="20dp", padding="50dp", pos_hint = {'center_x': 0.47,'center_y':0.53})    
        self.boxLayout.add_widget(self.textfield_valor)
        self.boxLayout.add_widget(self.textfield_tempo)

        self.boxLayout1 = MDBoxLayout(spacing="20dp", padding="50dp", pos_hint = {'center_x': 0.47,'center_y':0.45})
        verificar_button = MDRaisedButton(text="Verificar o resultado", on_release = self.pegar_valores)  
        self.boxLayout1.add_widget(verificar_button)

        self.resultado = MDLabel(text="Resultado: ", halign="right", pos_hint = {'center_x': 0.28,'center_y':0.06}, font_style = "H6")                                                     

        self.screen.add_widget(self.tabela)
        self.screen.add_widget(self.boxLayout)
        self.screen.add_widget(self.boxLayout1)
        self.screen.add_widget(self.resultado)
    
        return self.screen
    
    def checked(self, tabela, linha):                      
        print('tabela: ',tabela, ' linha: ',linha)
        taxa = float(linha[2])
        self.taxa_global = taxa

    def pegar_valores(self, instance):
        try:
            value = float(self.textfield_valor.text)
            temp = int(self.textfield_tempo.text)
            taxa = self.taxa_global

            if taxa > 0:

                montante = value * (1 + taxa)**(temp/10)
                montante = round(montante, 2)
                self.resultado.text = f"O resultado é de: {montante} !"

            else:

                self.resultado.text = f"Seleciona uma das opçoes acima!"
        
        except ValueError:

            self.resultado.text = "Por favor, insira números válidos."

mainApp = MainApp()
mainApp.run()           