# 🧮 Multiplicação de Matrizes

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Algorithms](https://img.shields.io/badge/Algorithms-Data_Structures-orange?style=for-the-badge)

Este projeto foi desenvolvido com o propósito de estudar a **Análise de Algoritmos**, especificamente para demonstrar e observar o comportamento de um algoritmo com complexidade de tempo **Cúbica**, ou $O(n^3)$.

## 🎯 Objetivo Acadêmico

Diferente de implementações que buscam a eficiência máxima (como o uso de bibliotecas otimizadas em C ou o Algoritmo de Strassen), este código implementa a multiplicação de matrizes de forma "ingênua" (naive) para fins de:
- Estudo de **estruturas de repetição aninhadas** (triplo laço).
- Verificação prática do crescimento do tempo de execução em relação ao tamanho da entrada ($n$).
- Demonstração de limites computacionais para algoritmos de alta complexidade.

## 🧠 Análise de Algoritmos (Big O)

A multiplicação de duas matrizes $n \times n$ requer três níveis de iteração:
1. Iteração sobre as linhas da Matriz A ($n$).
2. Iteração sobre as colunas da Matriz B ($n$).
3. Iteração para a soma dos produtos (produto escalar) ($n$).

Isso resulta em uma complexidade de:
$$T(n) = O(n \times n \times n) = O(n^3)$$

## 🚀 Funcionalidades

- **Cálculo de Produto:** Realiza a multiplicação de duas matrizes seguindo as regras da álgebra linear (linhas por colunas).
- **Validação de Dimensões:** Verifica automaticamente se o número de colunas da primeira matriz é igual ao número de linhas da segunda antes de iniciar o cálculo.
- **Entrada Dinâmica:** Permite a definição de matrizes de diferentes tamanhos (M x N).
- **Interface via Console:** Saída formatada no terminal para fácil visualização dos resultados.

## 🛠️ Tecnologias Utilizadas

- **Linguagem:** [Python 3.12.1]
- **Conceitos:** Laços de repetição aninhados, manipulação de listas e algoritmos de complexidade O(n³).

## 📦 Como rodar o projeto

1. **Pré-requisitos:**
   Certifique-se de ter o Python instalado. Você pode verificar digitando `python --version` no seu terminal.

2. **Clonar o repositório:**
   ```bash
   git clone [https://github.com/Pedro-Coquito/Multiplica-o-de-matrizes.git](https://github.com/Pedro-Coquito/Multiplica-o-de-matrizes.git)
   ```

## 🧠 Explicação do Algoritmo
A multiplicação de matrizes é realizada através de um algoritmo de triplo laço (nested loops):

O primeiro laço percorre as linhas da Matriz A.

O segundo laço percorre as colunas da Matriz B.

O terceiro laço realiza a soma dos produtos dos elementos correspondentes.

Este projeto demonstra a compreensão de como estruturas de dados bidimensionais são manipuladas na memória.

## 📝 Licença
Este projeto é voltado para fins acadêmicos e de estudo de algoritmos.

Desenvolvido por Pedro Coquito 🚀
