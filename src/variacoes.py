def lower_bound(arr: list[int], alvo: int) -> int:
    inicio = 0
    fim = len(arr)
    
    # O laço continua até que os ponteiros se encontrem no ponto exato
    while inicio < fim:
        meio = (inicio + fim) // 2
        
        # Se o elemento do meio for menor, a primeira ocorrência do alvo está à direita
        if arr[meio] < alvo:
            inicio = meio + 1
        # Se for maior ou igual, a primeira ocorrência está à esquerda ou é o meio mesmo
        else:
            fim = meio
            
    return inicio


def upper_bound(arr: list[int], alvo: int) -> int:
    inicio = 0
    fim = len(arr)
    
    while inicio < fim:
        meio = (inicio + fim) // 2
        
        # Se o elemento do meio for menor ou igualao alvo, o limite superior está mais à direita
        if arr[meio] <= alvo:
            inicio = meio + 1
        # Se for estritamente maior, o limite pode ser o meio ou estar à esquerda
        else:
            fim = meio
            
    return inicio


def busca_binaria_na_resposta(condicao, baixo: int, alto: int) -> int:
    while baixo < alto:
        meio = (baixo + alto) // 2
        
        # Se a condição atende, esse pode ser o menor valor, mas temos que ver se há menores à esquerda
        if condicao(meio):
            alto = meio
        # Se a condição não atende sendo (False), precisamos de um valor maior à direita
        else:
            baixo = meio + 1
            
    return baixo