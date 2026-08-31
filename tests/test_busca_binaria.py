import sys
from pathlib import Path
from busca_binaria import busca_binaria_iterativa, busca_binaria_recursiva  


def test_busca_binaria_iterativa_encontra_elemento():
    arr = [1, 3, 5, 7, 9, 11, 13]
    assert busca_binaria_iterativa(arr, 7) == 3


def test_busca_binaria_iterativa_elemento_ausente():
    arr = [1, 3, 5, 7, 9, 11, 13]
    assert busca_binaria_iterativa(arr, 4) == -1


def test_busca_binaria_recursiva_encontra_elemento():
    arr = [1, 3, 5, 7, 9, 11, 13]
    assert busca_binaria_recursiva(arr, 7) == 3


def test_busca_binaria_recursiva_elemento_ausente():
    arr = [1, 3, 5, 7, 9, 11, 13]
    assert busca_binaria_recursiva(arr, 4) == -1


def test_busca_binaria_array_vazio():
    assert busca_binaria_iterativa([], 1) == -1


def test_busca_binaria_um_elemento():
    assert busca_binaria_iterativa([5], 5) == 0
    assert busca_binaria_iterativa([5], 3) == -1


