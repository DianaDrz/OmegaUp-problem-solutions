#A. La mochila de Finn
N,M=map(int,input().split())
mazmorra=[]
for i in range(N):
    fila=list(input().strip())
    fila.reverse()
    mazmorra.append(fila)

for i in range(N):
    for j in range(M):
        print(mazmorra[i][j],end="")
    print()

#B. La Botella Mágica
pinguinos=["Gunter", "Kissy", "Waddles", "Chilly", "Gunter2", "Pep", "Snowball"]

nombre,K=input().split()
K=int(K)
iterador = 0
n=len(pinguinos)
for i in range(n):
    if pinguinos[i]==nombre:
        iterador=i
x=K%n
print(pinguinos[(iterador+x)%n])

#C. Mazmorras de Ooo
N,M=map(int,input().split())
mazmorra=[]
for i in range(N):
    fila=list(map(int,input().split()))
    mazmorra.append(fila)
F,C=map(int,input().split())
t=0
e=0
for i in range(N):
    for j in range(M):
        if mazmorra[i][j]==1:
            e+=1
        if mazmorra[i][j]==2:
            t+=1
print(e,t)
if mazmorra[F][C]==0:
    print("La sala está vacía...")
if mazmorra[F][C]==1:
    print("¡Finn se enfrenta a un enemigo!")
if mazmorra[F][C]==2:
    print("¡Jake encontró un tesoro!")

#D. La canción de BMO
N=int(input())
notas=["do", "re", "mi", "fa", "sol", "la", "si"]
for i in range (N):
    print(notas[i],end=" ")

#E. Come Along With Me
personajes=input().split()
orden=input()
if orden=="normal":
    personajes.sort()
    print(*personajes)
if orden=="inverso":
    personajes.sort(reverse=True)
    print(*personajes)

#F. Mapa Mágico
N,M=map(int,input().split())
mazmorra=[]
for i in range(N):
    fila=list(input().strip())
    fila.reverse()
    mazmorra.append(fila)

for i in range(N):
    for j in range(M):
        print(mazmorra[i][j],end="")
    print()