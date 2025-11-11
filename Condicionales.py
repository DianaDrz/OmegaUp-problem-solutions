#A. El Reto de Luisa
p1, p2, p3 = map(int, input().split())
suma = p1+p2+p3
if suma>=1000:
    print("SI")
else: 
    print("NO")

#B. Etapas de la vida
L =int(input())
if L <= 3:
    print("BEBE")
elif L <= 14:
    print("NINO")
elif L <= 18:
    print("JOVEN")
elif L <= 65:
    print("ADULTO")    
else:
    print("ADULTO 3RA")     
    
#C. Calculos condicionales
N = int(input())
contador = 0

if N % 2 == 0:
    N = N // 2
    contador += 1
else:
    N = N + 1
    contador += 1

if len(str(N)) >= 3:
    N = N // 100
    contador += 1
elif len(str(N)) == 2:
    N = N // 10
    contador += 1

if N % 3 == 0:
    N = N - 1
    contador += 1

print(N, contador)
#D. Condicionales 2 en 1 (simple)
K,V = map(int,input().split())
if K==1:
    if V <= 19:
        print("Considera buscar otra carrera...")
    elif V <= 39:
        print("Para la próxima échale más ganas")
    elif V <= 59:
        print("Casi aprobabas")
    elif V <= 79:
        print("Al menos no reprobaste")
    elif V <= 99:
        print("Calificación buena")
    elif V == 100:
        print("Calificación perfecta")   
elif K==2:     
    if V <= 19:
        print("Yo le gano B)") 
    elif V <= 39:
        print("Velocidad medio baja")
    elif V <= 59:
        print("No es la gran cosa")
    elif V <= 79:
        print("Rápido")
    elif V <= 99:
        print("Gran velocidad")
    elif V == 100:
        print("Máxima velocidad")

#E. Censista del cielo (versión 1)
T = float(input())
if T >= 33000:
    print("O")
elif 10000 <= T <= 32999:
    print("B")
elif 7500 <= T <= 9999:
    print("A")
elif 6000 <= T <= 7499:
    print("F")
elif 5200 <= T <= 5999:
    print("G")
elif 3700 <= T <= 5199:
    print("K")
elif 2500 <= T <= 3699:
    print("M")

#F. El juego de mamá
p1, p2, p3, p4 = map(int, input().split())
producto=p1*p2*p3*p4
if producto <=250:
    print(producto)
elif producto > 250:
    if p1==10 or p2==10 or p3==10 or p4==10:
        minimo=min(p1,p2,p3,p4)
        producto=producto//minimo
    else:
        maximo=max(p1,p2,p3,p4)
        producto=producto//maximo
    if producto > 250:
        print("pierdes")
    else:
        print(producto)