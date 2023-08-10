import time

#Variáveis
teatro = 0
linhas = 0
colunas = 0
preco_ingresso = 0
cadeiras = []
vendido = 0
reservas = 0
nao_recebido = 0
ingressos_total = 0

print('\nBem vindo(a) ao gerenciador de poltronas')

while True:
    print("\n****** MENU PRINCIPAL *********\n")
    print("[1] - Iniciar o teatro")
    print("[2] - Reservar lugar")
    print("[3] - Comprar lugar")
    print("[4] - Liberar lugar")
    print("[5] - Listar poltronas")
    print("[6] - Encerrar o espetáculo")
    print("[7] - Reiniciar o espetáculo\n")
    valor = int(input("Digite uma opção:  "))

    if valor == 1:

        if teatro == 0:

            teatro = 1

            #coleta de dados

            #Linhas
            linhas = int(input("Informe a quantidade de linhas (max. 300): "))
            #verificação
            while linhas > 300:
                print ("Quantidade informada maior que o permitido")
                linhas = int(input("Informe a quantidade de linhas (max. 300): "))


            #Colunas
            colunas = int(input("Informe a quantidade de linhas (max. 300): "))
            #verificação
            while colunas > 300:
                print ("Quantidade informada maior que o permitido")
                colunas = int(input("Informe a quantidade de linhas (max. 300): "))

            #coletando valor do ingresso
            preco = float(input('Qual o valor do ingresso R$ '))
            cadeiras = [['Livre' for _ in range(colunas)] for _ in range(linhas)]
            time.sleep(1)
            print(f"\nTeatro iniciado com {linhas} linhas e {colunas} colunas.")
            time.sleep(1)


        else:
            print ("Teatro já inciciado...")
            time.sleep(1)
    
    elif valor == 2:
        linha = int(input("Informe a linha: "))
        coluna = int(input("Informe a coluna: "))

        if linha > linhas or coluna > colunas:
            print("\nLugar não encontrado!")
            time.sleep(1)
        else:
            linha -= 1
            coluna -= 1
            if cadeiras[linha][coluna] == 'Livre':
                cadeiras[linha][coluna] = 'Reservado'
                reservas += 1
                nao_recebido += preco_ingresso * 0.3
                print("Lugar reservado com sucesso!")
                time.sleep(1)
            else:
                print("\nLugar já está reservado ou vendido.")
                time.sleep(1)

    elif valor == 3:
        linha = int(input("Informe a linha: "))
        coluna = int(input("Informe a coluna: "))
        if linha > linhas or coluna > colunas:
            print("\nLugar não encontrado!")
            time.sleep(1)
        else:
            linha -= 1
            coluna -= 1
            if cadeiras[linha][coluna] == 'Livre':
                cadeiras[linha][coluna] = 'Vendido'
                vendido += 1
                print("Lugar comprado com sucesso!")
                time.sleep(1)
            elif cadeiras[linha][coluna] == 'Reservado':
                cadeiras[linha][coluna] = 'Vendido'
                reservas -= 1
                vendido += 1
                nao_recebido += preco_ingresso * 0.7
                print("Lugar comprado com sucesso (reserva)!")
                time.sleep(1)
            else:
                print("Lugar já está vendido.")
                time.sleep(1)

    elif valor == 4:
        linha = int(input("Informe a linha: "))
        coluna = int(input("Informe a coluna: "))
        if linha > linhas or coluna > colunas:
            print("\nLugar não encontrado!")
            time.sleep(1)
        else:
            linha -= 1
            coluna -= 1
            if cadeiras[linha][coluna] == 'Vendido':
                cadeiras[linha][coluna] = 'Livre'
                vendido -= 1
            elif cadeiras[linha][coluna] == 'Reservado':
                cadeiras[linha][coluna] = 'Livre'
                reservas -= 1
                nao_recebido -= preco_ingresso * 0.3
            else:
                print("Lugar já está livre.")

    elif valor == 5:
        livre = 0
        reservado = 0
        vendido = 0
        for linha in cadeiras:
            for lugar in linha:
                if lugar == 'Livre':
                    livre += 1
                elif lugar == 'Reservado':
                    reservado += 1
                else:
                    vendido += 1
        print(f"Total Geral de Cadeiras: {linhas * colunas}")
        print(f"Total de Cadeiras Vazias: {livre}")
        print(f"Total de Cadeiras Reservadas: {reservado}")
        print(f"Total de Cadeiras Vendidas: {vendido}")
        print(f"Total do Espetáculo em R$: {vendido * preco_ingresso:.2f}")
        print(f"Total não recebido em R$: {preco_ingresso:.2f}")
        print(f"Total em reservas R$: {reservas * preco_ingresso * 0.3:.2f}")
        print("Total em Reservas Liberadas R$: 0.00")
