opçao = cont = 0
fila = []


while opçao <= 3:
    print('-=' * 15)
    print(''' [ 1 ] inserir\n [ 2 ] retirar\n [ 3 ] mostrar fila\n [ 4 ] sair''')
    print('-=' * 15)

    opçao = int(input('Escolha sua opção !! '))

    if opçao == 1:
        num = fila.append(input('Digite um valor para adicionar na fila '))
        cont = cont + 1

        if cont == 7:
            print('***' * 10)
            print(' \nSua fila esta cheia !!! \n')
            print('***' * 10)

    if opçao == 2:

        if cont > 0:
            del fila[0]
            print('Excluido com sucesso !')

        else:
            print('Sua fila ainda esta vazia !!! \nEscolha a opção 1 para adicionar um valor na fila !!!')

        print(fila)

    if opçao == 3:
        print(fila)

        if cont == 0:
            print('Fila esta vazia !!\n')

    if opçao == 4:
        print('Tchau. Ate a proxima !!')