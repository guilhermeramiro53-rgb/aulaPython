import pandas as pd
import os

caminho_excel = "Banco\Base_BANCO_TABAJARA.xlsx"

# Carregar ou criar o DataFrame
if os.path.exists("Banco\Base_BANCO_TABAJARA.xlsx"):
    df = pd.read_excel("Banco\Base_BANCO_TABAJARA.xlsx",dtype={'CPF':str})
else:
    df = pd.DataFrame(columns=["numero_conta", "nome", "CPF", "Tipo_conta"])
def gerar_numero_conta(df):
    if df.empty or "numero_conta" not in df.columns:
        return 1

    ultimo_numero = df["numero_conta"].max()

    if ultimo_numero >= 100:
        print("⚠️ Limite de contas atingido (máximo 100).")
        return None

    return ultimo_numero + 1

# Menu
print("================================================")
print("        BEM - VINDO AO BANCO TABAJARA")
print("================================================\n")
print("1 > Criar conta")
print("2 > Acessar conta")

opcao = int(input("R: "))

if opcao == 1:
    nome = input("Digite seu nome: ")
    cpf = input("Digite seu CPF: ")
    tipo_conta = input("Digite tipo de conta (Corrente/Poupança): ")

    # GERA NÚMERO AUTOMÁTICO
    novo_numero = gerar_numero_conta(df)

    # - numero_conta = Ser á gerada de forma sequencial começando do 0 até 100

    if df.empty:
        numero_conta = 0
    else:
        df["numero_conta"] = df["numero_conta"].astype(int)
        numero_conta = df["numero_conta"].max() + 1

    # - agencia = será gerado de forma sequencial começando do 400 até 700

    if df.empty:
        agencia = 400
    else:
        df["Agencia"] = df["Agencia"].astype(int)
        agencia = df["Agencia"].max() + 1

    # - extrato_bancario = valor inicial terá que começar em 0

    extrato_bancario = 0


            # Criação do dicionário com os dados
    novo_cliente = {
        "numero_conta": numero_conta,
        "nome": nome,
        "CPF": cpf,
        "Tipo_conta": tipo_conta,
        "Agencia": agencia,
        "Extrato": extrato_bancario
        
    }

            # Adiciona ao DataFrame (usando [novo_cliente] para converter em lista de um item)
    df = pd.concat([df, pd.DataFrame([novo_cliente])], ignore_index=True)

            # Salva no Excel
    df.to_excel("Banco\Base_BANCO_TABAJARA.xlsx", index=False)
    print(f"\n✅ Conta criada com sucesso! Seu número é: {novo_numero}")


elif opcao == 2:
    busca_cpf = str(input("Digite o CPF:")).strip()
    numero_conta = int(input("Digite o numero da conta:"))

    conta = df[
        (df["CPF"].astype(str).str.strip() == busca_cpf) &
        (df["numero_conta"].astype(int) == numero_conta)
    ]

    if conta.empty:
        print("Conta não encontrada. CPF invalido.")
    else:
        nome_cliente = conta.iloc[0]["nome"]
        agencia_cliente = conta.iloc[0]["Agencia"]
        tipo_cliente = conta.iloc[0]["Tipo_conta"]
        extrato_cliente = conta.iloc[0]["Extrato"]

        print(f"Bem-vindo(a) BANCO TABAJARA, {nome_cliente}")
        print(f"  Conta N :{numero_conta}")
        print(f"  Agencia :{agencia_cliente}")
        print(f"  Tipo    :{tipo_cliente}")
        print(f"  Saldo   :R${extrato_cliente}")