INITIAL_MESSAGE = """
Digite o numero da opção que deseja:
1 - Deposito
2 - Saque
3 - Extrato
4 - sair
"""
history = []
funds = 0.0
saques = 0
LIMITE_SAQUE = 500.00
LIMITE_SAQUES_DIARIOS = 3

def deposito():
    print("Digite o valor do depósito: ")
    value = float(input())
    if (value < 0): 
        print("Valor Invalido")
        return -1
    global funds
    funds += value
    history.append(f"Depósito: {value}")
    print(f"Saldo: {funds} ")
    return

def saque():
    global funds, saques
    print("Digite o valor do saque: ")
    value = float(input())
    if (value > LIMITE_SAQUE): 
        print("Valor acima do limite por saque")
        return -1
    if(funds < value):
        print("Saldo insuicinte")
        return -1
    if (saques >= LIMITE_SAQUES_DIARIOS):
        print("Limites de saques atingido")
        return
    funds -= value
    history.append(f"Saque: {value}")
    saques += 1
    print(f"Saldo: {funds} ")
    return
def extrato():
    print(f"Extrato {history}")
    print(f"Saldo: {funds} ")
    return

sair = False
while (not sair):
    print(INITIAL_MESSAGE)
    option = int(input())
    result = 0
    match option:
        case 1:
            deposito()
        case 2:
            saque()
        case 3:
            extrato()
        case 4:
            print("Obrigado por usar nosso programa.")
            sair = True
        case _:
            print("\nOpção invalida")