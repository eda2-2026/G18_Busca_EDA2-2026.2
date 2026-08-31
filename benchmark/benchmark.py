import sys
import time
import random
from pathlib import Path

sys.path.insert(0, str(Path(_file_).resolve().parent.parent / "src"))

from busca_binaria import busca_binaria_iterativa  
from baseline import busca_sequencial  

# A lista de tamanhos de arrays que serão testados no benchmark
TAMANHOS = [10*3, 104, 105, 106, 10*7]
REPETICOES = 5  # número de buscas por tamanho, para tirar uma média


def medir_tempo(funcao_busca, arr, alvo, repeticoes=REPETICOES) -> float:
    # Mede o tempo médio de repetições chamadas a funcao_busca
    inicio = time.perf_counter()
    for _ in range(repeticoes):
        funcao_busca(arr, alvo)
    fim = time.perf_counter()
    return (fim - inicio) / repeticoes


def rodar_benchmark():
    resultados_binaria = []
    resultados_sequencial = []

    for n in TAMANHOS:
        arr = sorted(random.sample(range(n * 10), n))
        alvo = arr[-1]

        tempo_binaria = medir_tempo(busca_binaria_iterativa, arr, alvo)
        tempo_sequencial = medir_tempo(busca_sequencial, arr, alvo)

        resultados_binaria.append(tempo_binaria)
        resultados_sequencial.append(tempo_sequencial)

        print(f"n={n:>10} | binaria={tempo_binaria:.8f}s | sequencial={tempo_sequencial:.8f}s")

    return resultados_binaria, resultados_sequencial


def plotar_resultados(resultados_binaria, resultados_sequencial):

    import matplotlib.pyplot as plt

    # Desenha a linha azul (padrão) conectando os pontos de tempo da busca binária
    plt.plot(TAMANHOS, resultados_binaria, label="Busca Binária")

    # Desenha a linha laranja (padrão) conectando os pontos de tempo da busca sequencial
    plt.plot(TAMANHOS, resultados_sequencial, label="Busca Sequencial")

    # Define o texto que aparecerá na base do gráfico (Eixo X)
    plt.xlabel("Tamanho do array (n)")

    # Define o texto que aparecerá na lateral do gráfico (Eixo Y)
    plt.ylabel("Tempo médio (s)")

    # Cria uma caixinha no canto explicando qual cor representa qual busca
    plt.legend()

    # Salva o gráfico gerado em um arquivo de imagem dentro da pasta benchmark
    plt.savefig("benchmark/resultado.png")

    print("Gráfico salvo em benchmark/resultado.png")


if _name_ == "_main_":
    binaria, sequencial = rodar_benchmark()
    plotar_resultados(binaria, sequencial)