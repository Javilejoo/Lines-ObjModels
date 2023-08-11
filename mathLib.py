from math import isclose
import math

def multiplicar_matrices(A, B):
    resultado = [[0 for _ in range(len(B[0]))] for _ in range(len(A))]
    
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                resultado[i][j] += A[i][k] * B[k][j]
    
    return resultado

def multiplicar_matriz_vector(M, v):
    resultado = [0 for _ in range(len(M))]
    
    for i in range(len(M)):
        for j in range(len(v)):
            resultado[i] += M[i][j] * v[j]
    
    return resultado

def barycentricCoords(A, B, C, P):
    
    # Se saca el �rea de los subtri�ngulos y del tri�ngulo
    # mayor usando el Shoelace Theorem, una f�rmula que permite
    # sacar el �rea de un pol�gono de cualquier cantidad de v�rtices.

    areaPCB = abs((P[0]*C[1] + C[0]*B[1] + B[0]*P[1]) - 
                  (P[1]*C[0] + C[1]*B[0] + B[1]*P[0]))

    areaACP = abs((A[0]*C[1] + C[0]*P[1] + P[0]*A[1]) - 
                  (A[1]*C[0] + C[1]*P[0] + P[1]*A[0]))

    areaABP = abs((A[0]*B[1] + B[0]*P[1] + P[0]*A[1]) - 
                  (A[1]*B[0] + B[1]*P[0] + P[1]*A[0]))

    areaABC = abs((A[0]*B[1] + B[0]*C[1] + C[0]*A[1]) - 
                  (A[1]*B[0] + B[1]*C[0] + C[1]*A[0]))

    # Si el �rea del tri�ngulo es 0, retornar nada para
    # prevenir divisi�n por 0.
    if areaABC == 0:
        return None

    # Determinar las coordenadas baric�ntricas dividiendo el 
    # �rea de cada subtri�ngulo por el �rea del tri�ngulo mayor.
    u = areaPCB / areaABC
    v = areaACP / areaABC
    w = areaABP / areaABC

    # Si cada coordenada est� entre 0 a 1 y la suma de las tres
    # es igual a 1, entonces son v�lidas.
    if 0<=u<=1 and 0<=v<=1 and 0<=w<=1 and isclose(u+v+w, 1.0):
        return (u, v, w)
    else:
        return None
    

def matriz_identidad(n):
    return [[1 if i == j else 0 for j in range(n)] for i in range(n)]

def intercambiar_filas(matriz, fila1, fila2):
    matriz[fila1], matriz[fila2] = matriz[fila2], matriz[fila1]

def escalar_fila(matriz, fila, factor):
    for i in range(len(matriz[fila])):
        matriz[fila][i] *= factor

def agregar_fila_escala(matriz, fila_fuente, fila_destino, factor):
    for i in range(len(matriz[fila_fuente])):
        matriz[fila_destino][i] += factor * matriz[fila_fuente][i]

def matriz_inversa(matriz):
    n = len(matriz)
    matriz_aumentada = [fila + matriz_identidad(n)[i] for i, fila in enumerate(matriz)]

    for col in range(n):
        fila_pivote = col
        while matriz_aumentada[fila_pivote][col] == 0:
            fila_pivote += 1
            if fila_pivote == n:
                return None
        intercambiar_filas(matriz_aumentada, col, fila_pivote)
        escalar_fila(matriz_aumentada, col, 1 / matriz_aumentada[col][col])

        for fila in range(n):
            if fila != col:
                factor = -matriz_aumentada[fila][col]
                agregar_fila_escala(matriz_aumentada, col, fila, factor)

    matriz_inversa = [fila[n:] for fila in matriz_aumentada]

    return matriz_inversa

def restar(tupla1, tupla2):
    resultado = []
    for i in range(len(tupla1)):
        resultado.append(tupla1[i] - tupla2[i])
    
    return resultado

def producto_cruz(arr1, arr2):
    producto_cruz = [
        (arr1[1] * arr2[2] - arr1[2] * arr2[1]),
        (arr1[2] * arr2[0] - arr1[0] * arr2[2]),
        (arr1[0] * arr2[1] - arr1[1] * arr2[0])
    ]
    return producto_cruz

def normalizar(lista_param):
    resultado = 0
    for i in range(len(lista_param)):
        resultado += lista_param[i] ** 2
    
    return math.sqrt(resultado)

def division_vector_escalar(vector, escalar):
    resultado = []
    for i in range(len(vector)):
        resultado.append(vector[i] / escalar)
    
    return resultado
