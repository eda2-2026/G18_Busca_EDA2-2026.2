from variacoes import lower_bound, upper_bound, busca_binaria_na_resposta

def test_lower_bound_elemento_repetido():
    arr = [1, 2, 2, 2, 4, 5]
    assert lower_bound(arr, 2) == 1

def test_lower_bound_elemento_ausente():
    arr = [1, 2, 2, 2, 4, 5]
    assert lower_bound(arr, 3) == 4

def test_upper_bound_elemento_repetido():
    arr = [1, 2, 2, 2, 4, 5]
    assert upper_bound(arr, 2) == 4

def test_upper_bound_elemento_ausente():
    arr = [1, 2, 2, 2, 4, 5]
    assert upper_bound(arr, 3) == 4

def test_busca_binaria_na_resposta_condicao_simples():
    condicao = lambda x: x >= 5
    assert busca_binaria_na_resposta(condicao, 1, 10) == 5