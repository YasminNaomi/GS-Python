# Importa a biblioteca random
import random

# Função para simular a leitura dos sensores
def ler_sensores():
    temperatura = round(random.uniform(15, 35), 2) # Temperatura em graus celsius
    ph = round(random.uniform(6, 9), 2) # Nível de PH
    nivel_agua = round(random.uniform(0, 100), 2) # Nível de qualidade da água
    return (temperatura, ph, nivel_agua)

# Função para analisar os dados coletados
def analisar_dados(temperatura, ph, nivel_agua):
    alertas = []
    if temperatura > 30:
        alertas.append('Alerta: Temperatura alta: ')
    if ph < 7:
        alertas.append('Alerta: Água com pH baixo: ')
    if nivel_agua < 20:
        alertas.append('Alerta: Nível de água baixo!')
    return alertas

# Função principal
def main():
    # Simula 10 ciclos de leituras
    for ciclo in range(10):
        print(f'\nCiclo {ciclo + 1}:')
        temperatura, ph, nivel_agua = ler_sensores()
        print(f'Temperatura: {temperatura} graus celsius')
        print(f'ph: {ph}')
        print(f'Nível da Água: {nivel_agua} %')
        
        
        alertas = analisar_dados(temperatura, ph, nivel_agua)
        if alertas:
            for alerta in alertas:
                print(alerta)
            else:
                print('Todas as leituras estão normais.')
                
# Executa a função principal         
if __name__ == '__main__':
    main()
