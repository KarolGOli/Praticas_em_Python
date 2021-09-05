# variável de contagem iniciada em zero
cont = 0
int(cont)

# condicional para manter o cadastro sendo requerido
while cont >= 0:
    # opção de escolha
    escolha = int(input('DESEJA INFORMAR OS DADOS DO ALUNO? -> 0 - NÃO | 1 - SIM | 2 - SAIR : \n'))
    cont += 1           # acresce 1 enquanto for atendida a condicional

    if escolha == 0:    # condição escolha "NÃO" para cadastro
        print('\n')

    elif escolha == 1:  # condição escolha "SIM" para cadastro
        nome_aluno = str(input('Digite o nome do aluno: '))     # variável de entrada nome_aluno
        nota_final = float(input('Informe a nota final: '))     # variável de entrada nota_final

        # linhas 12, 14, 16, 18, 20 e 22 são condições para informar a situação em que a nota se enquadra
        if 0.0 <= nota_final <= 2.9:
            print('A aluna', nome_aluno, 'tirou nota', nota_final, 'e se enquadra no conceito E. \n')
        elif 3.0 <= nota_final <= 4.9:
            print('A aluna', nome_aluno, 'tirou nota', nota_final, 'e se enquadra no conceito D. \n')
        elif 5.0 <= nota_final <= 6.9:
            print('A aluna', nome_aluno, 'tirou nota', nota_final, 'e se enquadra no conceito C. \n')
        elif 7.0 <= nota_final <= 8.9:
            print('A aluna', nome_aluno, 'tirou nota', nota_final, 'e se enquadra no conceito B. \n')
        elif 9.0 <= nota_final <= 10:
            print('A aluna', nome_aluno, 'tirou nota', nota_final, 'e se enquadra no conceito A. \n')
        elif nota_final < 0 or nota_final > 10:     # não aceita valores maiores que 10 ou menores que 0
            print('NOTA INCORRETA! \n')

    elif escolha == 2:                              # opção que finaliza o programa
        print('FINALIZANDO...')
        break