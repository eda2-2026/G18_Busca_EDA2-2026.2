from baseline import busca_sequencial

def test_busca_sequencial_encontra_elemento():
    arr = [1, 3, 5, 7, 9, 11, 13]
    assert busca_sequencial(arr, 7) == 3

def test_busca_sequencial_elemento_ausente():
    arr = [1, 3, 5, 7, 9, 11, 13]
    assert busca_sequencial(arr, 4) == -1

def test_busca_sequencial_array_desordenado():
    arr = [9, 1, 13, 5, 7, 11, 3]
    assert busca_sequencial(arr, 5) == 3