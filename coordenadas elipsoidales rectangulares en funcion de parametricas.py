import math

def calcular_excentricidad(a, f):
    e = math.sqrt(2 * f - f ** 2)
    return e

def calcular_semieje_menor(a, e):
    b = a * math.sqrt(1 - e ** 2)
    return b

def calcular_coordenadas_rectangulares(a, b, phi, lam):
    x = a * math.cos(phi) * math.cos(lam)
    y = a * math.cos(phi) * math.sin(lam)
    z = b * math.sin(phi)
    return x, y, z

# Solicitar al usuario que ingrese los valores
a = float(input("Ingrese el valor del semieje mayor (en metros): "))
f = float(input("Ingrese el valor de aplanamiento f: "))
phi_deg = float(input("Ingrese la latitud paramétrica en grados: "))
lam_deg = float(input("Ingrese la longitud en grados: "))

# Convertir latitud y longitud a radianes
phi = math.radians(phi_deg)
lam = math.radians(lam_deg)

# Calcular la excentricidad
e = calcular_excentricidad(a, f)

# Calcular el semieje menor
b = calcular_semieje_menor(a, e)

# Calcular las coordenadas rectangulares
x, y, z = calcular_coordenadas_rectangulares(a, b, phi, lam)

# Mostrar resultados
print("Excentricidad (e):", e)
print("Semieje Menor (b):", b)
print("Coordenadas Rectangulares:")
print("x:", x)
print("y:", y)
print("z:", z)
