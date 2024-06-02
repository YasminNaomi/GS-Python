import time  # Importa a biblioteca time para manipular tempo

# Função para verificar se o código inserido está correto
def verificar_codigo(codigo):
    codigo_correto = "1234"
    return codigo == codigo_correto

# Função para mostrar os prêmios disponíveis e quantos pontos faltam para cada um
def mostrar_premios(pontos):
    # Dicionário com exemplos de prêmios e os pontos necessários para resgatar cada um
    premios = {
        "fone bluetooth": 4000,
        "carregador portátil": 3000,
        "capa de celular": 2000,
        "adesivo": 1000
    }

    print("\nPrêmios disponíveis:")
    for premio, pontos_necessarios in premios.items():
        if pontos >= pontos_necessarios:
            # Mostra se o usuário tem os pontos necessários, e onde resgatar o prêmio
            print(f"Você pode resgatar: {premio} (Pontos necessários: {pontos_necessarios})")
            print(f"Você poderá resgatar o prêmio no site da *nome aleatório*.")
        else:
            # Mostra a contagem de pontos e quantos faltam para resgatar o prêmio
            pontos_faltando = pontos_necessarios - pontos
            print(f"Para {premio} faltam {pontos_faltando} pontos.")