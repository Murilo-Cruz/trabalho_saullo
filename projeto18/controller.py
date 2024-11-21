from model import Model
from view import View
from datetime import datetime


class Controller:
    def __init__(self):
        self.model = Model("bd_mvc.db")
        self.view = View(self)
        self.refresh_data_table()

    def insert_data(self, nome, salario, datanascimento, telefone):
        self.model.insert_data(nome, salario, datanascimento, telefone)
        self.refresh_data_table()

    def update_data(self, id, nome, salario, datanascimento, telefone):
        self.model.update_data(id, nome, salario, datanascimento, telefone)
        self.refresh_data_table()

    def delete_data(self, id):
        self.model.delete_data(id)
        self.refresh_data_table()

    def refresh_data_table(self):
        data = self.model.get_data()
        self.view.update_data_table(data)





        

    def calcular_idade(self,data_str):
        data_nascimento = datetime.strptime(data_str, "%d/%m/%Y")
        data_atual = datetime.now()
        idade = data_atual.year - data_nascimento.year
        if (data_atual.month, data_atual.day) < (data_nascimento.month, data_nascimento.day):
            idade -= 1        
        return idade
    







   
    def aumentar_salario(self, id, nome, salario, datanascimento, telefone):
        idade = self.calcular_idade(datanascimento) 
        if idade > 20:
            novo_salario = salario * 1.1  # Aumento de 10%
            self.model.aumentar_salario(id, novo_salario)
            self.refresh_data_table()
        else:
            self.show_message("A idade do funcionário deve ser maior que 20 para aumentar o salário.")






