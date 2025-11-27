#A. Las Órbitas Planetarias
N=int(input())
K=int(input())
P=map(int,input().split())

bandera=1
for i in P:
    if N%i!=0:
        bandera=0
        break
if bandera:
    print("SI")
else:
    print("NO")

#B. La Fortaleza de los Primos
N=int(input())
divisores=[]
for i in range(1, 1 +int(N ** 0.5)):
    if N%i==0:
        divisores.append(i)
        if i!=N/1:
            divisores.append(int(N/i))

print("Aprobado" if len(divisores)<=2 else "Rechazado")

#C. La Criba del Hechicero Eratóstenes
n=int(input())
criba=[0]*(n+1)
criba[1]=1
primos=[]

for i in range(2,n+1):
    if criba[i]==0:
        primos.append(i)
        for j in range(i,n+1,i):
            criba[j]=1
print(len(primos))

N = int(input())
if N < 2:
    print(0)
else:
    criba = [True] * (N + 1)
    criba[0] = criba[1] = False
    for i in range(2, int(N ** 0.5) + 1):
        if criba[i]:
            for j in range(i * i, N + 1, i):
                criba[j] = False
    print(sum(criba))


#D. Divisibilidad por 3
n=int(input())
if n%3==0:
    print("Si")
else:
    print("No")
#E. Sincronización de Semáforos
N,M=map(int,input().split())
tiempos=list(map(int,input().split()))
contador =0
for i in tiempos:
    if M%i==0 or i%M==0:
        contador+=1
print (contador)

#F. El Club de Números Primos
L, R = map(int, input().split())
contador = 0
criba = [True] * (R + 1)
criba[0] = criba[1] = False
for i in range(2, int(R ** 0.5) + 1):
    if criba[i]:
        for j in range(i * i, R + 1, i):
            criba[j] = False

for x in range(L, R + 1):
    if criba[x]:
        suma = 0
        n = x
        while n > 0:
            suma += n % 10
            n //= 10
        if criba[suma]:
            contador += 1
print(contador)