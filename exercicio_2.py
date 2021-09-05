nome_user = str(input('Informe seu nome: '))        # variável de entra nome
sobrenome = str(input('Informe seu sobrenome: '))   # variável de entra sobrenome
digitos = str(input('Informe dois digitos: '))      # variável de entrada do dígito


# função que vai concatenar as variáveis de entrada com o final do email e apresentar pro usuário quando requerida
def concat(nome_user, sobrenome, digitos):
    print('\nSr (Sra)', nome_user + ' ' + sobrenome, 'seu email é:')
    print(nome_user[0].lower() + sobrenome.lower() + digitos + '@algoritmos.com.br')


concat(nome_user, sobrenome, digitos)              # chamada da função
