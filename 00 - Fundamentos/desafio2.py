INITIAL_MESSAGE = """
Digite o numero da opção que deseja:
1 - Deposito
2 - Saque
3 - Extrato
4 - Criar Usuario
5 - Criar Conta
6 - Listar Contas
7 - Sair
"""
LIMITE_SAQUE = 500.00
LIMITE_SAQUES_DIARIOS = 3
USER_1 = {
        "Nome": "Joao da Silva",
        "Data de Nascimento": "10/10/2000",
        "CPF": "123",
        "Endereco": f"Rua Primeira, 1 - Bairro - Cidade/ESTADO"
        }
ACCOUNT_1 = {
        "Agencia": "0001",
        "Numero da Conta": 1,
        "Usuario": "123",
        "Extrato": [{"Deposito": "200,00"}, {"Deposito": "500,00"}, {"Saque": "100,00"}],
        "Saldo": 600.0,
        "Numero de Saques": 0
        }
USERS = [USER_1]
ACCOUNTS = [ACCOUNT_1]

def cpf_input():
    CPF = str(input("Digite seu CPF: \n")).replace('.', "")
    return CPF

def login():
    CPF = cpf_input()
    Numero = int(input("Informe o numero da conta: \n"))
    return {"CPF": CPF, "Numero": Numero}

def find_account(usr):
    for acc in ACCOUNTS:
        if acc["Usuario"] == usr["CPF"] and acc["Numero da Conta"] == usr["Numero"]:
            return acc
    return False

def saque(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    valor_convertido = float(valor.replace('.', ","))
    if (valor_convertido > limite):
        print("Valor maior que o limite por saque!")
        return False
    if numero_saques >= limite_saques:
        print("Maximo de saques diários atingido")
        return False
    if valor_convertido >= saldo:
        print("Saldo Insuficiente")
        return False
    saldo -= valor_convertido 
    extrato.append({"Saque": valor_convertido})
    return {"Saldo": saldo, "Extrato": extrato, "Numero de Saques": numero_saques + 1}

def deposito(saldo, valor, extrato, /):
    valor_convertido = float(valor.replace('.', ","))
    saldo += valor_convertido
    extrato.append({"Depósito": valor_convertido})
    return {"Saldo": saldo, "Extrato": extrato}

def extrato(saldo,/,*,extrato):
    print(f"Histórico da conta: {extrato}")
    print(f"Saldo: {saldo}")
    return saldo, extrato

def criar_usuaro():
    CPF = cpf_input()
    for usr in USERS:
        if (usr["CPF"] == CPF):
            print("CPF ja Cadastrado")
            return False
    user = {
        "Nome": input("Digite Seu Nome: \n"),
        "Data de Nascimento": input("Digite sua data de nascmineto no mormato DD/MM/AAAA: \n"),
        "CPF": CPF,
        "Endereco": f"{input("Digite o nome de sua rua: \n")}, {input("Digite o numero da sua residencia: \n")} - {input("Digite o seu bairro: \n")} - {input("Digite o nome de sua cidade: \n")}/{input("Digite a sigla de seu estado: \n")}"
        }
    return user

def criar_conta():
    account = {
        "Agencia": "0001",
        "Numero da Conta": 1 if len(ACCOUNTS) == 0 else ACCOUNTS[-1]["Numero da Conta"] + 1,
        "Usuario": cpf_input(),
        "Extrato": [],
        "Saldo": 0.0,
        "Numero de Saques": 0
    }
    for usr in USERS:
        if usr["CPF"] == account["Usuaro"]:
            return account
    print("CPF não cadastrado.")
    return  False

def listar_contas():
    CPF = cpf_input()
    user_accounts = []
    for acc in ACCOUNTS:
        if acc["Usuario"] == CPF:
            user_accounts.append({"Numero da Conta": acc["Numero da Conta"], "Saldo": acc["Saldo"]})
    return user_accounts

sair = False
while (not sair):
    print(INITIAL_MESSAGE)
    option = int(input())
    match option:
        
        # Deposito
        case 1:
            usr = login()
            acc = find_account(usr)
            r = deposito(acc["Saldo"], input("Valor a depositar: \n"), acc["Extrato"])
            if (r):
                acc.update(r)
                print(acc)
        # Saque
        case 2:
            usr = login()
            acc = find_account(usr)
            r = saque(saldo=acc["Saldo"], valor=input("Quanto deseja sacar?: \n"), extrato=acc["Extrato"],limite=LIMITE_SAQUE, numero_saques=acc["Numero de Saques"], limite_saques=LIMITE_SAQUES_DIARIOS)
            if (r):
                acc.update(r)
                print(acc)
       
        # Extrato
        case 3:
            usr = login()
            acc = find_account(usr)
            extrato(acc["Saldo"], extrato=acc["Extrato"])
        
        # Criar Usuario
        case 4:
            new_user = criar_usuaro()
            if (new_user):
                USERS.append(new_user)
                print("Usuario cadastrado com sucesso!")
        
        # Criar Conta
        case 5:
            new_account = criar_conta()
            if (new_account):
                ACCOUNTS.append(new_account)
                print(f"Conta criada com sucesso! Numero da Conta: {new_account["Numero"]}") 
        
        # Listar contas
        case 6:
            contas = listar_contas()
            print("Nenhma conta vinculada a este CPF") if len(contas) == 0  else print(contas)
        # Sair     
        case 7:
            print("Obrigado por usar nosso programa.")
            sair = True
        case _:
            print("\nOpção invalida")