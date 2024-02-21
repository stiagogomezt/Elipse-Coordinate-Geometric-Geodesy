import math

def calcular_excentricidad(f):
    e = math.sqrt(2 * f - f ** 2)
    return e

def calcular_rg(a, e, w):
    Rg = a * math.sqrt(1 - e**2) / math.sqrt(1 - e**2 * math.sin(w)**2)
    return Rg

def calcular_coordenadas_rectangulares(Rg, w, lam):
    x = Rg * math.cos(lam) * math.cos(w)
    y = Rg * math.sin(lam) * math.cos(w)
    z = Rg * math.sin(w)
    return x, y, z

# Solicitar al usuario que ingrese los valores
a = float(input("Ingrese el valor del semieje mayor (en metros): "))
f = float(input("Ingrese el valor de aplanamiento f: "))
w_deg = float(input("Ingrese la latitud geocéntrica en grados: "))
lam_deg = float(input("Ingrese la longitud en grados: "))

# Convertir latitud y longitud a radianes
w = math.radians(w_deg)
lam = math.radians(lam_deg)

# Calcular la excentricidad
e = calcular_excentricidad(f)

# Calcular Rg
Rg = calcular_rg(a, e, w)

# Calcular las coordenadas rectangulares
x, y, z = calcular_coordenadas_rectangulares(Rg, w, lam)

# Mostrar resultados
print("Coordenadas Rectangulares:")
print("x:", x)
print("y:", y)
print("z:", z)
