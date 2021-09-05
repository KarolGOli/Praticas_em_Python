from operator import itemgetter
lista = []
cont = 0
int(cont)


def cadastro_produto(produto_para_cadastrar: dict):     # função que adiciona o objeto produto à lista
    lista.append(produto_para_cadastrar)                # o método append faz com que o produto seja adicionado na lista
    return


while cont >= 0:    # condição para manter em execução o 'menu' escolhas e valores a serem informados
    cadastro = int(input('\nCADASTRAR NOVO PRODUTO? (0 - Não     1 - Sim) '))
    cont += 1

    if cadastro == 1:
        new_product = {}        # dicionário para armazenar os produtos, enquanto rodar ele vai ser atualizado com um novo produto armazenado
        new_product['codigo'] = int(input('INFORME O CÓDIGO DO PRODUTO: '))

        if new_product['codigo'] == 0:      # condição para verificar se o valor inserido é válido
            print('CÓDIGO 0, encerra o cadastro de produtos.')
            break
        new_product['atual'] = int(input('INFORME O ESTOQUE ATUAL: '))
        new_product['minimo'] = int(input('INFORME O ESTOQUE MÍNIMO: '))

        if new_product['atual'] < new_product['minimo']:    # condição para informar a situação do estoque
            print('ESTOQUE ATUAL ABAIXO D0 MÍNIMO INDICADO!')
        cadastro_produto(new_product)       # chamada da função de cadastro

    elif cadastro == 0:
        print('\nENCERRANDO CADASTRO DE PRODUTOS...')
        break

visualizar = int(input('\nAPRESENTAR TABELA DE PRODUTOS? (2 - Visualizar | 3 - Cancelar) '))

if visualizar == 2 and len(lista) > 0:      # se o usuário quiser visualizar a tabela e ela estiver preenchida ele à apresenta
        print('TABELA DE PRODUTOS - ORDEM CRESCENTE:')
        print("CÓDIGO".center(10), end='')      # métodos utilizados para centralização e estruturação da tabela
        print("EST. ATUAL".center(15), end='')
        print("EST. MÍNIMO".center(18))

        # linha de comando responsável por ordenar a lista de forma crescente, usando como referência o item código
        for produto in sorted(lista, key=itemgetter('codigo')):
            print(str(produto['codigo']).center(10), end='')
            print(str(produto['atual']).center(15), end='')
            print(str(produto['minimo']).center(18))

elif visualizar == 3:
    print('FINALIZANDO...')