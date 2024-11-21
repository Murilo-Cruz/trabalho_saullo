import sqlite3
from kivymd.app import MDApp                                
from kivymd.uix.screen import Screen                        
from kivymd.uix.datatables import MDDataTable               
from kivy.metrics import dp                                 
from kivymd.uix.textfield import MDTextField                
from kivymd.uix.boxlayout import MDBoxLayout                
from kivymd.uix.button import MDRaisedButton                


class BancoDadosAgenda:
    def __init__(self, nome_banco_dados):        

        self.conn = sqlite3.connect(nome_banco_dados)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute('''
                            CREATE TABLE IF NOT EXISTS banco_dados (
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                nome TEXT,
                                sobrenome TEXT,
                                email TEXT,
                                telefone TEXT
                            )
                            ''')
        self.conn.commit()

    def insert_data(self, nome, sobrenome, email, telefone):
        self.cursor.execute('''
            INSERT INTO banco_dados (nome, sobrenome, email, telefone)
            VALUES (?, ?, ?, ?)
        ''', (nome, sobrenome, email, telefone))
        self.conn.commit()

    def update_data(self, id, nome, sobrenome, email, telefone):
        self.cursor.execute('''
            UPDATE banco_dados
            SET nome=?, sobrenome=?, email=?, telefone=?
            WHERE id=?
        ''', (nome, sobrenome, email, telefone, id))
        self.conn.commit()  

    def delete_data(self, id):
        self.cursor.execute('''
            DELETE FROM banco_dados WHERE id=?
        ''', (id,))
        self.conn.commit()           

    def get_data(self):
        self.cursor.execute("SELECT * FROM banco_dados")
        return self.cursor.fetchall()

class MeuApp(MDApp):
    def build(self):                                        # idem a main_0.py

        self.title = "Prof. Saulo Santos | projeto_13.py"   # idem a main_0.py       

        self.screen = Screen()                              # idem a main_0.py               

        self.tabela = MDDataTable(                          # idem a main_1.py
            pos_hint = {'center_x':0.5,                     # idem a main_3.py
                        'center_y':0.65},                   # idem a main_8.py 
            size_hint=(0.9,0.6),                            # idem a main_6.py
            check = True,                                   # idem a main_6.py
            use_pagination = True,                          # idem a main_6.py
            rows_num = 3,                                   # idem a main_6.py 
            pagination_menu_height = '60dp',                # idem a main_6.py
            column_data = [                                 # idem a main_1.py
                ("ID", dp(20)),
                ("Nome", dp(20)),
                ("Sobrenome", dp(30)),
                ("Email", dp(40)),
                ("Telefone", dp(20))
            ],
            row_data = []                                   # Retirei todos os registros             
        )

        self.tabela.bind(on_check_press = self.checked)     # o método bind está conectando o evento on_check_press da tabela 
                                                            # (a um evento que é disparado quando uma checkbox em uma linha da tabela é 
                                                            # pressionada) à função self.checked. Isso significa que, sempre que o usuário
                                                            #  pressionar uma checkbox na tabela, a função self.checked será chamada 
                                                            # automaticamente para processar essa ação.
                                                                 

        self.theme_cls.theme_style = "Light"                # idem a main_0.py
        self.theme_cls.primary_palette = "Orange"           # idem a main_4.py

        self.textfield_codigo = MDTextField(                # idem a main_7.py
            hint_text="Código",                             
            helper_text="Insira o código",                  
            max_text_length=3,                              
            size_hint_x=None,                                
            width=60,                                      
        )                                                   

        self.textfield_nome = MDTextField(
            hint_text="Nome",
            helper_text="Insira o nome",
            max_text_length=50,
        )

        self.textfield_sobrenome = MDTextField(
            hint_text="Sobrenome",
            helper_text="Insira o sobrenome",
            max_text_length=5,
            size_hint_x=None,
            width=200,
        )
        
        self.textfield_email = MDTextField(
            hint_text="Email",
            helper_text="Insira o email",
            max_text_length=50,
        )

        self.textfield_telefone = MDTextField(
            hint_text="Telefone",
            helper_text="Insira o telefone",
            max_text_length=50,
        )

        self.boxLayout1 = MDBoxLayout(spacing="20dp",padding="50dp",pos_hint = {'center_x': 0.5,'center_y':0.65})    # idem a main_8.py
        self.boxLayout1.add_widget(self.textfield_codigo)   # idem a main_8.py
        self.boxLayout1.add_widget(self.textfield_nome)     # idem a main_8.py
        self.boxLayout1.add_widget(self.textfield_sobrenome)# idem a main_8.py
        self.boxLayout1.add_widget(self.textfield_email)    # idem a main_8.py    
        self.boxLayout1.add_widget(self.textfield_telefone) # idem a main_8.py


        adicionar_button = MDRaisedButton(text="Adicionar") # Assim como foi feito com o textfield, estou adicionando 3 buttons
        atualizar_button = MDRaisedButton(text="Adicionar") # Um para incluir, outro para eliminar e outro para alterar registros
        eliminar_button = MDRaisedButton(text="Eliminar")

        self.boxLayout2 = MDBoxLayout(spacing="20dp", padding="50dp")   # Estou criando um segundo BoxLayout para 'jogar' os botões dentro dele     
        self.boxLayout2.add_widget(adicionar_button)        # adicionando botão ao BoxLayout2
        self.boxLayout2.add_widget(atualizar_button)        # adicionando botão ao BoxLayout2
        self.boxLayout2.add_widget(eliminar_button)         # adicionando botão ao BoxLayout2

        self.screen.add_widget(self.tabela)                 # idem a main_1.py
        self.screen.add_widget(self.boxLayout1)             # idem a main_8.py
        self.screen.add_widget(self.boxLayout2)             # Estou adicionando o BoxLayout2 dentro do screen

        self.dados_selecionados_linha = None                #  Criei uma variável para armazenar os dados da linha selecionada
        
        self.database = BancoDadosAgenda('number_data.db')  # Instancio objeto que cria o Banco de Dados
        self.refresh_data_table()

        adicionar_button.bind(on_release=self.add_data)     
        eliminar_button.bind(on_release=self.delete_data)
        atualizar_button.bind(on_release=self.update_data)

        return self.screen                                  # idem a main_0.py    

    def refresh_data_table(self):
        data = self.database.get_data()
        self.tabela.row_data = data

    # Esse metodo transfere o conteudo da linha clicada no MDDataTable para os textfield
    def checked(self, tabela, linha): 
        self.dados_selecionados_linha = linha
        self.textfield_nome.text = linha[1]
        self.textfield_sobrenome.text = linha[2]
        self.textfield_email.text = linha[3]
        self.textfield_telefone.text = linha[4]


    def add_data(self, instance):
        nome = self.textfield_nome.text
        sobrenome = self.textfield_sobrenome.text
        email = self.textfield_email.text
        telefone = self.textfield_telefone.text

        if nome and sobrenome and email and telefone:
            self.database.insert_data(nome, sobrenome, email, telefone)
            self.refresh_data_table()
            self.clear_text_fields()
        else:
            print("Preencha todos os campos.")

    def delete_data(self, instance):
        if self.dados_selecionados_linha is not None:
            id = self.dados_selecionados_linha[0]  # Obtém o ID da linha selecionada
            self.database.delete_data(id)  # Chama o método para excluir o registro
            self.refresh_data_table()  # Atualiza a tabela após a exclusão
            self.clear_text_fields()  # Limpa os campos de entrada
        else:
            print("Selecione uma linha na tabela para excluir o registro.")


    def update_data(self, instance):
        nome = self.textfield_nome.text
        sobrenome = self.textfield_sobrenome.text
        email = self.textfield_email.text
        telefone = self.textfield_telefone.text

        print(nome)
        print(self.dados_selecionados_linha)

        # Adicione uma verificação para garantir que um item esteja selecionado na tabela
        if self.dados_selecionados_linha is not None:
            
            id = self.dados_selecionados_linha[0]  # Pega o ID da linha selecionada
            print("id=",id)
            print("nome=",nome)
            print("sobrenome=",sobrenome)
            print("email=",email)
            print("telefone=",telefone)
            if nome and sobrenome and email and telefone:
                self.database.update_data(id, nome, sobrenome, email, telefone)  # Chama o método de atualização
                self.refresh_data_table()
                self.clear_text_fields()
            else:
                print("Preencha todos os campos e selecione uma linha na tabela.")
        else:
            print("Selecione uma linha na tabela para atualizar os dados.")


    def clear_text_fields(self):
        self.textfield_nome.text = ""
        self.textfield_sobrenome.text = ""
        self.textfield_email.text = ""
        self.textfield_telefone.text = ""

MeuApp().run()





