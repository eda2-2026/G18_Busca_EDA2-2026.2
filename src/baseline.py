def busca_sequencial(arr: list[int], alvo: int) -> int:
    for i, valor in enumerate(arr):
        if valor == alvo:
            return i
    return -1