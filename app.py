# Projeto 1 - Gerador de dados para testes(app no terminal)

# Importação de bibliotecas

import random




# Criar uma lista de 5 nomes, 5 e-mail, 5 telefones, 5 cidades e 5 estados
nomes = ['Maripilda', 'Leopoldo', 'Ariosvaldo', 'Edileuza', 'Josefina']
emails = ['mari@gmail.com','leo@gmail.com','valdo@gmail.com','leuza@gmail.com','jose@gmail.com']
telefone = ['98809-8978','98874-5874','98475-85740','98874-8528','99987-5823']
cidade = ['Juiz de Fora','Volta Redonda','Fortaleza','Curitiba','Florianopolis']
estado =['MG','RJ','CE','PR','SC']


# Criação das variáveis do programa


# Criando funções para cada ação que será escolhida

def selecao1():
    nome_aleatorio = random.choice(nomes)
    return nome_aleatorio

def selecao2():
    email_aleatorio = random.choice(emails)

def selecao3():
    telefone_aleatorio = random.choice(telefone)

def selecao4():
   cidade_aleatoria =  random.choice(cidade)

def selecao5():
    estado_aleatorio = random.choice(estado)





# Criação o menu inicial
print('Bem-vindo ao Gerador de Dados de Testes - Para finalizar o programa, digite "parar"')
print(30*'-')
print('Escolhe uma ou mais opções abaixo a serem geradas aleatóriamente')
print('[1] - Nome')
print('[2] - E-mail')
print('[3] - Telefone')
print('[4] - Cidade')
print('[5] - Estado')
selecoes_do_usuario = input('Digite uma(as) opções: ')


# Criando a lógica para exibir o nome aleatorio





# Criar lógica para salvar os dados em um arquivo de texto






# Criar lógica para parar o programa