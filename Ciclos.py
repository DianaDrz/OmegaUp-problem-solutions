#A. Entrenando con Tanjiro
N =int(input())
suma=0
for i in range(N):
   suma += 2**i
print(suma)

#B. Zenitzu y su técnica del rayo
N=int(input())
for i in range (1,N+1):
   for j in range(1,i+1):
       print('*',end='')
   print()

#C. Luna Superior
V,R,K=map(int,input().split())
for i in range(K):
   espada=int(input())
   V-=espada
   if V<1:
       break
   V+=R
if V<=0:
   print("VICTORIA >:3")
else:
   print("DERROTA :'(")

#D. Los gritos de Inosuke
N=int(input())
for i in range (1,N+1):
   print("A", end="") 
   for j in range(1,i+1):
       print('H',end='')
   print()

#E. Números prohibidos
N,X=map(int,input().split())
contador=0
suma=0
for i in range(N):
   energia=int(input())
   if energia==X:
       contador+=1
   else:
       suma=suma+energia 
if contador==N:
   print(0)
else:
   N=N-contador
   suma=suma//N
   print(suma)

#F. Tanjiro y las multiplicaciones
A,B=map(int,input().split())
for i in range (A,B+1):
    for j in range (1,11):
        print(i,"x",j,"=",i*j)
    print()

