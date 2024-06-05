import time  # Importa a biblioteca time para manipular tempo

# Função para verificar se o código inserido está correto
def verificar_codigo(codigo):
    codigo_correto = "1234"
    return codigo == codigo_correto

# Função para mostrar os prêmios disponíveis e quantos pontos faltam para cada um
def mostrar_premios(pontos):
    # Dicionário com os prêmios e os pontos necessários para resgatar cada um
    premios = {
        "fone bluetooth": 4000,
        "carregador portátil": 3000,
        "capa de celular": 2000,
        "adesivo": 1000
    }

    print("\nPrêmios disponíveis:")
    for premio, pontos_necessarios in premios.items():
        if pontos >= pontos_necessarios:
            # Se o usuário tem pontos suficientes, mostra o prêmio e onde resgatar
            print(f"Você pode resgatar: {premio} (Pontos necessários: {pontos_necessarios})")
            print(f"Você poderá resgatar o prêmio no site da *nome aleatório*.")
        else:
            # Se o usuário não tem pontos suficientes, mostra quantos pontos faltam
            pontos_faltando = pontos_necessarios - pontos
            print(f"Para {premio} faltam {pontos_faltando} pontos.")

# Função para calcular e exibir o tempo restante para a próxima verificação
def exibir_tempo_restante(tempo_restante):
    horas_restantes = int(tempo_restante // 3600)
    minutos_restantes = int((tempo_restante % 3600) // 60)
    segundos_restantes = int(tempo_restante % 60)
    print(f"Você poderá verificar o código novamente em {horas_restantes}h {minutos_restantes}m {segundos_restantes}s.")

# Função principal do programa
def main():
    pontos = 0  # Inicializa os pontos do usuário
    intervalo_5_horas = 5 * 60 * 60  # Define o intervalo de 5 horas em segundos

    while True:
        codigo = input("Insira o código de 4 dígitos: ")  # Solicita o código ao usuário
        
        if verificar_codigo(codigo):
            pontos += 3  # Adiciona 3 pontos se o código estiver correto
            print(f"Código correto! Você ganhou 3 pontos. Total de pontos: {pontos}")
            mostrar_premios(pontos)  # Mostra os prêmios disponíveis
        else:
            print("Código incorreto, tente novamente.")
        
        # Exibe a contagem regressiva para a próxima verificação
        print("Aguarde 5 horas para inserir o próximo código.")
        for _ in range(intervalo_5_horas):
            time.sleep(1)  # Espera por um segundo
            tempo_restante = intervalo_5_horas - _
            exibir_tempo_restante(tempo_restante)
        
        print()  # Adiciona uma linha em branco para clareza

if __name__ == "__main__":
    main()  # Chama a função principal do programa
