# G18_Busca_EDA2-2026.2

# T1 - Busca Binária

Trabalho da disciplina Estrutura de Dados 2 (UnB) — tema: Busca.

## Integrantes
- Caio Vilas Boas Miranda — 232001380
- Guilherme Gusmão Nepomuceno — 232021516

## Objetivo

Implementar e analisar a Busca Binária, incluindo variações do algoritmo
clássico, e comparar sua complexidade com a Busca Sequencial.

## Conteúdo 

1. **Busca Binária clássica** — iterativa e recursiva
   - Complexidade: O(log n) tempo | O(1) espaço (iterativa) / O(log n) espaço (recursiva)
   - Pré-condição: array ordenado
2. **Variações**
   - `lower_bound`: primeira posição onde o valor poderia ser inserido mantendo a ordem
   - `upper_bound`: última posição onde o valor poderia ser inserido mantendo a ordem
   - Busca binária "na resposta": aplicação do princípio da busca binária a um
     espaço de soluções, não a um array literal

## Como rodar

```bash
python -m pytest tests/
```
