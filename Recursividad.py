# #Implemtar la funcion de fibonacci
# #caso base
# # f(0)=0
# # f(1)=1
# #paso recursivo
# #f(n)=f(n-1)+f(n-2)

# def fibonaci(n):
#     if n==0:
#         return 0
#     elif n==1:
#         return 1
#     return (fibonaci(n-1)+fibonaci(n-2))
# fibo=[]
# indices=[]
# for i in range(1,11):
#     indices.append(i)
#     fibo.append(fibonaci(i))
# print (indices)
# print (fibo)

#Problema de la escalera
#caso baseb=10,n=1,n=0

# def escalera(n):
#     if n==0:
#         return 0
#     escalera(n-1)
#     print('*'*n)
# escalera(5)

# def escalera(n):
#     if n==1:
#         return "*\n"
#     return escalera(n-1)+"*"*n+"\n"
#     print('*'*n)
# anse=escalera(5)
# print(anse)
#calcular la suma de los n numeros naturales
#s(n)=1+2+3...+n
#caso base

#paso recursivo

# def suma(n):
#     if n==0:
#         return n
#     return (suma(n-1))+n

# print(suma(10))

#calcular el factorial de un numero n
#f(n)=1*2*3*...*n
def factorial(n):
    if n==0 or n==1:
        return 1
    return (factorial(n-1)*n)
for i in range (1,11):
    print(i, factorial(i))


#Ejercicios 
# #A. El hechizo de la suma
def suma(n):
    if n==0:
        return n
    return (suma(n-1))+n
N=int(input())
print(suma(N))

# B. Factorial hasta el 20
def factorial(n):
    if n==0 or n==1:
        return 1
    return (factorial(n-1)*n)
N=int(input())
print(factorial(N))

# C. La espiral de Apolo
def fibonaci(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    return (fibonaci(n-1)+fibonaci(n-2))
n=int(input())
print (fibonaci(n))

# D. El brillo de Selene
def potencia(a,b):
    if b==0:
        return 1
    elif b==1:
        return a
    return a * potencia(a,b-1)

a,b=map(int,input().split())
print(potencia(a,b))


# E. Cantidad a pagar
def pagar(N):
    if 1 <= N <= 5:
        return 10
    return 2 * pagar(N - 2)

M = int(input())
print(pagar(M))


# F. Mínimo común múltiplo de varios enteros
def mcd(a, b):
    if b == 0:
        return a
    return mcd(b, a % b)

def mcm(a, b):
    return a * b // mcd(a, b)

def mcmCompleto(numeros):
    if len(numeros) == 1:
        return numeros[0]
    return mcm(numeros[0], mcmCompleto(numeros[1:]))


N = int(input())
numeros = list(map(int, input().split()))
print(mcmCompleto(numeros))
