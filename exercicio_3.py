import random  # é necessário importar o módulo para utilização de comandos

cont = 0
int(cont)

listaSorteio = []  # variável que armazena a lista


def cadastro_doadores(nome, valor):     # Função para armazenar o cadastro multiplicado pelo valor doado
    listaSorteio.extend(((nome + ' ') * int(valor // 10)).split())
    return


def sorteia_ganhador():     # Função para realizar o sorteio
    random.shuffle(listaSorteio)  # método utilizado para embaralhar a lista
    print(f'\n LISTA PARA SORTEIO EMBARALHADA: {listaSorteio}')
    return random.choice(listaSorteio)  # método utilizado para realizar o sorteio


while cont >= 0:
    menu = int(input('DESEJA CADASTRAR NOVO DOADOR?  0 - NÃO |    1 - SIM '))   # Opção de cadastro
    sortear = int(input('DESEJA REALIZAR O SORTEIO? 2 - SIM |   3 - NÃO '))     # Opção de sorteio
    cont += 1   # Contador lógico

    if menu == 0:   # Primeira opção do cadastro
        print('\n')

    elif menu == 1: # Segunda opção do cadastro que permite o usuário a informar os dados do doador
        nome = str(input('INFORME O NOME DO DOADOR:   '))       # Variável de entrada do nome do doador
        valor = float(input('QUAL O VALOR DA DOAÇÃO?    '))     # Variável de entrada do valor doado
        if len(nome.strip()) == 0 or valor < 10:                # Se o nome ou o valor não se encaixar na condição é informado o erro
            print('É OBRIGATÓRIO INFORMAR O NOME E O VALOR MÍNIMO DE DOAÇÃO SÃO R$ 10')

    if sortear == 2 and len(listaSorteio) > 0:  # Opção de realizar o sorteio + verificação condicional
        print(f'\nLISTA DOS DOADORES(AS) PARA SORTEIO: {listaSorteio}')     # exibição da lista de doadores
        print(f'\nO(A) SORTEADO(A) É: {sorteia_ganhador()}')                # exibição do ganhador

    elif sortear == 3:      # Opção de não sortear e seguir com as outras opções
        print('\n')
    cadastro_doadores(nome, valor)      # Chamada da função cadastro