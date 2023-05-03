# Projeto 1 - Gerador de dados para testes(app no terminal)

# Importação de bibliotecas
import random
import os


# Criar uma lista de 5 nomes, 5 e-mail, 5 telefones, 5 cidades e 5 estados
nomes = ['Maripilda', 'Leopoldo', 'Ariosvaldo', 'Edileuza', 'Josefina']
emails = ['mari@gmail.com','leo@gmail.com','valdo@gmail.com','leuza@gmail.com','jose@gmail.com']
telefone = ['98809-8978','98874-5874','98475-85740','98874-8528','99987-5823']
cidade = ['Juiz de Fora','Volta Redonda','Fortaleza','Curitiba','Florianopolis']
estado =['MG','RJ','CE','PR','SC']


# Criação das variáveis do programa
selecao_do_usuario = 0
salvar_em_arquivo = 0

# Criando funções para cada ação que será escolhida

def selecao1():
    return random.choice(nomes)
    print('')
    print(100*'-')

def selecao2():
    return random.choice(emails)
    print('')
    print(100*'-')

def selecao3():
    return random.choice(telefone)
    print('')
    print(100*'-')

def selecao4():
    return random.choice(cidade)
    print('')
    print(100*'-')

def selecao5():
    return random.choice(estado)
    print('')
    print(100*'-')

def cria_arquivo(dado):
    with open('dados.txt','a',newline='',encoding='utf-8') as arquivo:
        arquivo.write(dado+os.linesep)



while True:
# Criação o menu inicial
    print('Bem-vindo ao Gerador de Dados de Testes - Para finalizar o programa, digite "parar"')
    print(100*'-')
    print('Escolha uma ou mais opções abaixo a serem geradas aleatóriamente')
    print('[1] - Nome')
    print('[2] - E-mail')
    print('[3] - Telefone')
    print('[4] - Cidade')
    print('[5] - Estado')
    selecao_do_usuario = input('Digite uma(as) opções: ')
    print(100*'-')

    if selecao_do_usuario == 'parar':
        break

    # Criar lógica para salvar os dados em um arquivo de texto
    salvar_em_arquivo = input('Gostaria de salvar os dados em um arquivo de texto? (s/n) ')
    if salvar_em_arquivo == 's':
        print('Arquivo salvo')
    print('')
    print('')
    
    # Criando a lógica para exibir o nome aleatorio
    if selecao_do_usuario == '1':
        nome = selecao1()
        print(nome)
        if salvar_em_arquivo == 's':
            cria_arquivo(nome)
    if selecao_do_usuario == '2':
        email = selecao2()
        print(email)
        if salvar_em_arquivo == 's':
            cria_arquivo(email)
    if selecao_do_usuario == '3':
        telefone = selecao3()
        print(telefone)
        if salvar_em_arquivo == 's':
            cria_arquivo(telefone)
    if selecao_do_usuario == '4':
        cidade = selecao4()
        print(cidade)
        if salvar_em_arquivo == 's':
            cria_arquivo(cidade)
    if selecao_do_usuario == '5':
        estado = selecao5()
        print(estado)
        if salvar_em_arquivo == 's':
            cria_arquivo(estado)
    


print('Encerrando o programa')
print('')














# Criar lógica para parar o programa