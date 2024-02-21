import math

def calcular_gran_normal(a, f, phi):
    e_squared = 2 * f - f ** 2
    N = a / math.sqrt(1 - e_squared * math.sin(phi) ** 2)
    return N

def calcular_coordenadas_rectangulares(N, phi, lam):
    x = N * math.cos(phi) * math.cos(lam)
    y = N * math.cos(phi) * math.sin(lam)
    z = (N * (1 - e_squared)) * math.sin(phi)
    return x, y, z

# Solicitar al usuario que ingrese los valores
a = float(input("Ingrese el valor del semieje mayor (en metros): "))
f = float(input("Ingrese el valor de aplanamiento f: "))
phi_deg = float(input("Ingrese la latitud en grados: "))
lam_deg = float(input("Ingrese la longitud en grados: "))

# Convertir latitud y longitud a radianes
phi = math.radians(phi_deg)
lam = math.radians(lam_deg)

# Calcular la gran normal
N = calcular_gran_normal(a, f, phi)

# Calcular las coordenadas rectangulares
e_squared = 2 * f - f ** 2
x, y, z = calcular_coordenadas_rectangulares(N, phi, lam)

# Mostrar resultados
print("Gran Normal (N):", N)
print("Coordenadas Rectangulares:")
print("x:", x)
print("y:", y)
print("z:", z)
