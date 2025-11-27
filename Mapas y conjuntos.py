#A. Coleccionando pokemones
N=int(input())
pokemones= set()
for i in range(N):
    nombre=input()
    pokemones.add(nombre)
print(len(pokemones))

#B. El torneo del profesor Oak
T=int(input())
todos=set()
ini=True
for i in range (T):
    N=int(input())
    pokemones=set(input().split())
    print(len(pokemones))
    if ini:
        todos= pokemones
        ini=False
    else:
        todos=todos & pokemones
if len(todos) > 0:
    print(*sorted(todos))
else: 
    print('Ninguno')   

#C. Un verdadero maestro pokemon
N=int(input())
map={}
cantidad ={}
lst =[]
st=set()
for i in range (N):
    nombre, nivel=input().split()
    nivel=int(nivel)
    if nombre in st:
        map [nombre]=map [nombre]+nivel
        cantidad [nombre]=cantidad [nombre]+1
    else:
        st.add(nombre)
        lst.append(nombre)
        map[nombre]=nivel
        cantidad[nombre]=1
for pokemon in lst:
    print(f'{pokemon}: {map[pokemon]//cantidad[pokemon]}')

#D. Atraparlos Ya!
R=int(input())
todos=set()
for i in range (R):
    N=int(input())
    pokemones=set(input().split())
    print(len(pokemones))
    if len(todos)==0:
        todos= pokemones
    else:
        todos=todos - pokemones
if len(todos) > 0:
    print(*sorted(todos))
else: 
    print('Ninguno')   

#E. Pokédex incompleta
N=int(input())
distintos=set()
repetidos=[]
for i in range (N):
    nombre=input()
    distintos.add(nombre)
M=int(input())
for i in range (M):
    nombre=input()
    repetidos.append(nombre)
repetidosset=set(repetidos)
capturados = set(distintos-repetidosset)
if len(capturados) > 0:
    print(*sorted(capturados), sep='\n')
else: 
    print('¡Pokédex completa!')   

#F. Liga Pokémon
N=int(input())
contador={}
for i in range(N):
    entrenador1, resultado, entrenador2=input().split()
    if entrenador1 not in contador:
        contador[entrenador1] = 0
    if entrenador2 not in contador:
        contador[entrenador2] = 0
    #print(contador)   
    if resultado == "victoria":
        contador[entrenador1] += 3
    elif resultado == "empate":
        contador[entrenador1] += 1
        contador[entrenador2] += 1
    elif resultado == "derrota":
        contador[entrenador2] += 3
puntajes = sorted(contador.items(), key=lambda x: (-x[1], x[0]))
for nombre, puntaje in puntajes:
    print(nombre, puntaje)