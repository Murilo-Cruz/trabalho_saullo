from kivymd.uix.screen import Screen                        # idem a main_0.py
from kivymd.uix.datatables import MDDataTable               # idem a main_1.py
from kivy.metrics import dp                                 # idem a main_1.py
from kivymd.uix.textfield import MDTextField                # idem a main_8.py
from kivymd.uix.boxlayout import MDBoxLayout                # idem a main_8.py
from kivymd.uix.button import MDRaisedButton                # importei a biblioteca que me permite instanciar widgets textfield
from kivymd.uix.label import MDLabel
from kivymd.uix.dialog import MDDialog
from datetime import datetime

class View:
    def __init__(self, controller):
        self.controller = controller

        self.title = "Prof. Saulo Santos | Projeto 14 - MVC.py"       # idem a main_0.py       

        self.screen = Screen()                              # idem a main_0.py               

        self.tabela = MDDataTable(                          # idem a main_1.py
            # background_color_header="#65275d",
            # background_color_cell="#451938",
            # background_color_selected_cell="#e4514f",
            pos_hint = {'center_x':0.5,                     # idem a main_3.py
                        'center_y':0.65},                   # idem a main_8.py 
            size_hint=(0.9,0.6),                            # idem a main_6.py
            check = True,                                   # idem a main_6.py
            use_pagination = True,                          # idem a main_6.py
            rows_num = 6,                                   # idem a main_6.py 
            pagination_menu_height = '120dp',                # idem a main_6.py
            column_data = [                                 # idem a main_1.py
                ("ID", dp(20)),
                ("Nome", dp(20)),
                ("Salário", dp(30)),
                ("Data Nasc.", dp(40)),
                ("Telefone", dp(20))
            ],
            row_data = []                                   # Retirei todos os registros             
        )


        self.tabela.bind(on_check_press = self.checked)     # idem a main_5.py
        self.tabela.bind(on_row_press=self.on_row_press)
                                                            # idem a main_5.py     

        self.textfield_codigo = MDLabel(
            text="ID",
            theme_text_color="Hint",
            size_hint_x=None,
            width=60,
            # readonly = True,
            # mode = "rectangle", 
            # max_text_length=0, 
            size_hint_y ="0.1"        
        )                                                  

        self.textfield_nome = MDTextField(
            hint_text="Nome",
            #helper_text="Nome",
            max_text_length=20,
            width=150,
        )

        self.textfield_salario = MDTextField(
            hint_text="Salário",
            #helper_text="Salário",
            max_text_length=15,
            size_hint_x=None,
            width=150,
            input_filter="float",
        )
        
        self.textfield_datanascimento = MDTextField(
            hint_text="Data Nascimento",
            helper_text="dd/mm/aaaa",
            max_text_length=10,
            width=150,
        )

        self.textfield_telefone = MDTextField(
            hint_text="Telefone",
            helper_text="99999999999",
            max_text_length=13,
            width=150,
            input_filter="int",
        )

        data = self.controller.model.get_data()  # Obtenha os dados do banco de dados
        self.update_data_table(data)        

        self.boxLayout1 = MDBoxLayout(spacing="20dp",padding="50dp",pos_hint = {'center_x': 0.5,'center_y':0.65})    # idem a main_8.py
        self.boxLayout1.add_widget(self.textfield_codigo)   # idem a main_8.py
        self.boxLayout1.add_widget(self.textfield_nome)     # idem a main_8.py
        self.boxLayout1.add_widget(self.textfield_salario)# idem a main_8.py
        self.boxLayout1.add_widget(self.textfield_datanascimento)    # idem a main_8.py    
        self.boxLayout1.add_widget(self.textfield_telefone) # idem a main_8.py


        adicionar_button = MDRaisedButton(text="Adicionar") # Assim como foi feito com o textfield, estou adicionando 3 buttons
        atualizar_button = MDRaisedButton(text="Atualizar") # Um para incluir, outro para eliminar e outro para alterar registros
        eliminar_button = MDRaisedButton(text="Eliminar")
        aumentar_button = MDRaisedButton(text="Aumentar Salário")

        self.boxLayout2 = MDBoxLayout(spacing="20dp", padding="50dp")   # Estou criando um segundo BoxLayout para 'jogar' os botões dentro dele     
        self.boxLayout2.add_widget(adicionar_button)        # adicionando botão ao BoxLayout2
        self.boxLayout2.add_widget(atualizar_button)        # adicionando botão ao BoxLayout2
        self.boxLayout2.add_widget(eliminar_button)         # adicionando botão ao BoxLayout2
        self.boxLayout2.add_widget(aumentar_button)         # adicionando botão ao BoxLayout2

        self.screen.add_widget(self.tabela)                 # idem a main_1.py
        self.screen.add_widget(self.boxLayout1)             # idem a main_8.py
        self.screen.add_widget(self.boxLayout2)             # Estou adicionando o BoxLayout2 dentro do screen

        self.dados_selecionados_linha = None                #  Criei uma variável para armazenar os dados da linha selecionada
        
        # self.refresh_data_table()

        adicionar_button.bind(on_release=self.add_data)
        eliminar_button.bind(on_release=self.delete_data)
        atualizar_button.bind(on_release=self.update_data)
        aumentar_button.bind(on_release=self.aumentar_salario)

    def get_root_widget(self):
        return self.screen
    
    
    

    def checked(self, tabela, linha):
        self.dados_selecionados_linha = linha             # usada para eliminar e atualizar registros
        self.textfield_codigo.text = "ID: "+linha[0]
        self.textfield_nome.text = linha[1]
        self.textfield_salario.text = linha[2]
        self.textfield_datanascimento.text = linha[3]
        self.textfield_telefone.text = linha[4]


    def on_row_press(self,a, linha):
            if linha.ids.check.state == "down":
                linha.change_check_state_no_notify("down")            
            else:
                linha.change_check_state_no_notify("normal") 
                self.textfield_codigo.text = "ID: "
                self.textfield_nome.text = ""
                self.textfield_salario.text = ""
                self.textfield_datanascimento.text = ""
                self.textfield_telefone.text = "" 

    def is_valid_salary(self, salario): #verifica se o valor de entrada no campo de salário é um número válido
        try:
            # Tenta converter o salário para um número float
            salario_float = float(salario)
            return salario_float >= 0  # Verifica se o salário é maior ou igual a zero
        except ValueError:
            return False
        

    def add_data(self, instance):
        nome = self.textfield_nome.text
        salario = self.textfield_salario.text
        datanascimento = self.textfield_datanascimento.text
        telefone = self.textfield_telefone.text

        # Validação do campo salário
        if not self.is_valid_salary(salario):
            self.show_message("O salário deve ser um número válido.")
            return
        
        # Validar e formatar a data de nascimento
        try:
            # Converte a data de nascimento de string para datetime
            data_formatada = datetime.strptime(datanascimento, "%d/%m/%Y")  # ou outro formato conforme necessário
            # Formata a data no formato desejado, por exemplo, YYYY-MM-DD
            datanascimento = data_formatada.strftime("%d/%m/%Y")
        except ValueError:
            self.show_message("A data de nascimento deve estar no formato DD/MM/AAAA.")
            return

        if nome and salario and datanascimento and telefone:
            # Converter o salário para float, já que passou na validação
            salario = float(salario)
            self.controller.insert_data(nome, salario, datanascimento, telefone)

            # Recarregar os dados e limpar os campos
            data = self.controller.model.get_data()
            self.update_data_table(data)
            self.clear_text_fields()
        else:
            self.show_message("Preencha todos os campos")


    def delete_data(self, instance):
        if self.dados_selecionados_linha:
            id = int(self.dados_selecionados_linha[0])
            self.controller.delete_data(id)

            # Após a eliminação, recarregue os dados na tabela
            data = self.controller.model.get_data()
            self.update_data_table(data)

            self.clear_text_fields()
        else:
            self.show_message("Selecione um registro para excluir")

        self.uncheck_all_rows()

    def update_data(self, instance):
        if self.dados_selecionados_linha:
            id = int(self.dados_selecionados_linha[0])
            nome = self.textfield_nome.text
            salario = self.textfield_salario.text
            datanascimento = self.textfield_datanascimento.text
            telefone = self.textfield_telefone.text

            # Validação do campo salário
            if not self.is_valid_salary(salario):
                self.show_message("O salário deve ser um número válido.")
                return

            if nome and salario and datanascimento and telefone:
                salario = float(salario)  # Conversão após validação
                self.controller.update_data(id, nome, salario, datanascimento, telefone)

                # Recarregar dados e limpar campos
                data = self.controller.model.get_data()
                self.update_data_table(data)
                self.clear_text_fields()
            else:
                self.show_message("Preencha todos os campos")
        else:
            self.show_message("Selecione um registro para atualizar")


    def show_message(self, message):
        dialog = MDDialog(
            title="Mensagem",
            text=message,
            buttons=[
                MDRaisedButton(
                    text="OK",
                    on_release=lambda x: dialog.dismiss()
                )
            ]
        )
        dialog.open()

    def clear_text_fields(self):
        self.textfield_nome.text = ""
        self.textfield_salario.text = ""
        self.textfield_datanascimento.text = ""
        self.textfield_telefone.text = ""
        self.textfield_codigo.text = "ID: "
        self.dados_selecionados_linha = None 

    def update_data_table(self, data):
        # Atualizar os dados da tabela
        self.tabela.row_data = data

        # Limpar a seleção
        self.textfield_codigo.text = "ID: "
        self.textfield_nome.text = ""
        self.textfield_salario.text = ""
        self.textfield_datanascimento.text = ""
        self.textfield_telefone.text = ""
        self.dados_selecionados_linha = None   

    def aumentar_salario(self, instance):
        if self.dados_selecionados_linha:
            id = int(self.dados_selecionados_linha[0])
            nome = self.textfield_nome.text
            salario = float(self.textfield_salario.text)
            datanascimento = self.textfield_datanascimento.text
            telefone = self.textfield_telefone.text

            self.controller.aumentar_salario(id, nome, salario, datanascimento, telefone)

            # Após a eliminação, recarregue os dados na tabela
            data = self.controller.model.get_data()
            self.update_data_table(data)

            self.clear_text_fields()

        else:
            self.show_message("Selecione um registro para aumentar o salário")   