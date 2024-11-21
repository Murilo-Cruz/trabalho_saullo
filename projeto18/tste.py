from datetime import datetime

def calcular_idade(data_str):
    print(data_str)
    # Converte a string da data para um objeto datetime
    data_nascimento = datetime.strptime(data_str, "%d/%m/%Y")
    # Obtém a data atual
    data_atual = datetime.now()
    # Calcula a diferença em anos
    idade = data_atual.year - data_nascimento.year
    
    # Verifica se o aniversário já ocorreu este ano
    if (data_atual.month, data_atual.day) < (data_nascimento.month, data_nascimento.day):
        idade -= 1
    
    return idade

# Exemplo de uso
data_input = "19/01/2000"
idade = calcular_idade(data_input)
print(f"A quantidade de anos entre {data_input} e hoje é: {idade} anos.")
