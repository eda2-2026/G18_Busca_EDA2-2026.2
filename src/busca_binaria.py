def busca_binaria_iterativa(arr: list[int], alvo: int) -> int:
    # Define o índice inicial apontando para o primeiro elemento da lista
    inicio = 0
    # Define o índice final apontando para o último elemento da lista
    fim = len(arr) - 1

    while inicio <= fim:
        # Encontra o índice central do intervalo usando divisão inteira
        meio = (inicio + fim) // 2

        if arr[meio] == alvo:
            return meio
        elif arr[meio] < alvo:
            inicio = meio + 1
        else:
            fim = meio - 1

    return -1

def busca_binaria_recursiva(arr: list[int], alvo: int, inicio: int = 0, fim: int | None = None) -> int:
    if fim is None:
        fim = len(arr) - 1

    # Condição de parada: se as posições se cruzam, significa que o alvo não existe
    if inicio > fim:
        return -1

    # Calcula o ponto central do intervalo atual com divisão inteira
    meio = (inicio + fim) // 2

    if arr[meio] == alvo:
        return meio
    elif arr[meio] < alvo:
        return busca_binaria_recursiva(arr, alvo, meio + 1, fim)
    else:
        return busca_binaria_recursiva(arr, alvo, inicio, meio - 1)

if __name__ == "__main__":
    exemplo = [1, 3, 5, 7, 9, 11, 13]
    # Imprime no terminal o resultado da busca iterativa (deve imprimir 3)
    print(busca_binaria_iterativa(exemplo, 7))
    # Imprime no terminal o resultado da busca recursiva (deve imprimir 3)
    print(busca_binaria_recursiva(exemplo, 7))