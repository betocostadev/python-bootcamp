# Desafio
# Uma empresa de telecomunicações deseja criar uma solução algorítmica que ajude aos seus clientes a
# escolherem o plano de internet ideal com base em seu consumo mensal de dados.
# Para a resolução, você pode solicitar ao usuário que insira o seu consumo, sendo este um valor 'float'.
# Crie uma função chamada recomendar_plano para receber o consumo médio mensal de dados informado pelo cliente,
# além de utilizar estruturas condicionais para fazer a verificação e retornar o plano adequado.

# Planos Oferecidos:

# - Plano Essencial Fibra - 50Mbps: Recomendado para um consumo médio de até 10 GB.
# - Plano Prata Fibra - 100Mbps: Recomendado para um consumo médio acima de 10 GB até 20 GB.
# - Plano Premium Fibra - 300Mbps: Recomendado para um consumo médio acima de 20 GB.

# Entrada
# Como entrada solicite o consumo médio mensal de dados em GB (float).

# Saída
# Retorne o plano ideal para o cliente de acordo com o consumo informado na entrada.

# Exemplos
# A tabela abaixo apresenta exemplos com alguns dados de entrada e suas respectivas saídas esperadas.
# Certifique-se de testar seu programa com esses exemplos e com outros casos possíveis.

# Entrada	Saída
# 10

# Plano Essencial Fibra - 50Mbps

# 19

# Plano Prata Fibra - 100Mbps
# 21

# Plano Premium Fibra - 300Mbps

# TODO: Crie uma Função: recomendar_plano para receber o consumo médio mensal:


# TODO: Crie uma Estrutura Condicional para verifica o consumo médio mensal
# TODO: Retorne o plano de internet adequado:


def recomendar_plano():
    INVALID = "O valor inserido é inválido, use um valor acima de 0"
    ESSENTIAL = "Plano Essencial Fibra - 50Mbps"
    SILVER = "Plano Prata Fibra - 100Mbps"
    PREMIUM = "Plano Premium Fibra - 300Mbps"

    # Solicita ao usuário que insira o consumo médio mensal de dados:
    # consumo = float(input("Por favor, informe qual é o seu consumo médio em GB (Exemplo: 10, 20, 30, 50):"))
    consumo = input("Por favor, informe qual é o seu consumo médio em GB (Exemplo: 10, 20, 30, 50):")
    # Chama a função recomendar_plano com o consumo inserido e imprime o plano recomendado:

    if not isinstance(consumo, float):
        print(INVALID)
        return recomendar_plano()

    elif (consumo < 0):
        return INVALID
    elif (consumo > 20):
        return PREMIUM
    elif (consumo > 10):
        return SILVER
    else:
        return ESSENTIAL


print(recomendar_plano())
