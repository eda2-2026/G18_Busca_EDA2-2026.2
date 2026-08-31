# G18_Busca_EDA2-2026.2

# T1 - Busca Binária

Trabalho da disciplina Estrutura de Dados 2 (UnB) — tema: Busca.

## Integrantes
- Caio Vilas Boas Miranda — 232001380
- Guilherme Gusmão Nepomuceno — 232021516

## Objetivo

Implementar e analisar a Busca Binária, incluindo variações do algoritmo
clássico, e comparar sua complexidade com a Busca Sequencial.

## Estrutura do repositório

```
G18_Busca_EDA2-2026.2/
├── src/
│   ├── busca_binaria.py     # versões iterativa e recursiva
│   ├── variacoes.py         # lower_bound, upper_bound, busca binária na resposta
│   └── baseline.py          # busca sequencial (apenas para comparação)
├── tests/
│   └── test_busca_binaria.py
|   └── conftest.py
|   └── test_baseline.py
|   └── test_variacoes.py
├── benchmark/
│   └── benchmark.py         # gera dados, mede tempos, plota gráfico
└── README.md
```

## Conteúdo 

1. **Busca Binária clássica** — iterativa e recursiva
   - Complexidade: O(log n) tempo | O(1) espaço (iterativa) / O(log n) espaço (recursiva)
   - Pré-condição: array ordenado
2. **Variações**
   - `lower_bound`: primeira posição onde o valor poderia ser inserido mantendo a ordem
   - `upper_bound`: última posição onde o valor poderia ser inserido mantendo a ordem
   - Busca binária "na resposta": aplicação do princípio da busca binária a um
     espaço de soluções, não a um array literal
3. **Baseline de comparação**
   - Busca sequencial, usada apenas para evidenciar empiricamente o ganho de
     O(log n) sobre O(n)
4. **Benchmark**
   - Tempo de execução para tamanhos de entrada crescentes (10^3 a 10^7)
   - Gráfico tempo × n comparando busca binária e busca sequencial

## Como rodar

**1. Instale a biblioteca para geração de gráficos:**
```bash
pip install matplotlib 
```
**2. Execute a suíte de testes automatizados:**
```bash
python -m pytest tests/
```
**3. Execute o benchmark comparativo:**
```bash
python3 benchmark/benchmark.py
```

## Vídeo de apresentação 

Link do vídeo: 

