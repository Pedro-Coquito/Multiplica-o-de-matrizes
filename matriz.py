def matriz_Multiplicacao(A, B):  
    n = len(A)      # Linhas de A
    m = len(A[0])   # Colunas de A
    x = len(B)      # Linhas de B
    y = len(B[0])   # Colunas de B

    if m != x:
        print("Não é possivel realizar a multiplicação")
        return None

    C = [[0 for _ in range(y)] for _ in range(n)]

    for i in range(n):
        for j in range(y):
            soma = 0
            for k in range(m):
                soma += A[i][k] * B[k][j]
            C[i][j] = soma   # <- fora do loop k!!!

    return C 


print("Matriz A: \n")
n = int(input("Número de linhas da Matriz A: "))
m = int(input("Número de Colunas da Matriz A: "))

A = []
print("\nDigite os valores da Matriz A, linha por linha:")
for i in range(n):
    while True:
        linha = list(map(int, input(f"Linha {i+1}: ").split()))
        if len(linha) == m:
            A.append(linha)
            break
        else:
            print("Quantidade incorreta! Digite novamente.")


print("\nMatriz B: \n")
x = int(input("Número de linhas da Matriz B: "))
y = int(input("Número de Colunas da Matriz B: "))

B = []
print("\nDigite os valores da Matriz B, linha por linha:")
for i in range(x):
    while True:
        linha = list(map(int, input(f"Linha {i+1}: ").split()))
        if len(linha) == y:
            B.append(linha)
            break
        else:
            print("Quantidade incorreta! Digite novamente.")


print("\n=== RESULTADO DE A X B ===")
C = matriz_Multiplicacao(A, B)

if C is not None:
    for linha in C:
        print(linha)
