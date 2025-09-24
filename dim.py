import numpy as np
import matplotlib.pyplot as plt
from math import exp, sin, cos

# Parâmetros
gamaAgua = 10  # kN/m³
gamaConcreto = 25  # kN/m³
poisson = 1 / 6
Ec = 3.45 * 10**7  # kN/m²
Ea = 2.1 * 10**8  # kN/m²
h = 0.15  # m
d = 6.65  # m
r = d / 2  # m
beta = ((3 * (1 - poisson**2))**(1 / 4)) / ((r * h)**0.5)
D = (Ec * h**3) / (12 * (1 - poisson**2))

# Valor específico
y = 4

# Função w(y)
def w(y):
    return -(np.exp(-beta * y)) / 126478.53 * (
        9.35 * (np.cos(beta * y) - np.sin(beta * y)) - 20.16 * np.cos(beta * y)
    )

# Função w2(y) -> segunda derivada
def w2(y):
    return -(np.exp(-beta * y)) / 18468.28 * (
        9.35 * (np.cos(beta * y) + np.sin(beta * y)) - 20.16 * np.sin(beta * y)
    )

# Função w3(y) -> terceira derivada
def w3(y):
    return (np.exp(-beta * y)) / 9980.36 * (
        18.69 * np.sin(beta * y) + 20.16 * (np.cos(beta * y) - np.sin(beta * y))
    )

# Funções de esforços
def N(y):
    return (Ec * h / r) * w(y)

def M(y):
    return -D * w2(y)

def Mt(y):
    return poisson * M(y)

def V(y):
    return D * w3(y)

# Valores em y = 4
w_y4, N_y4, M_y4, Mt_y4, V_y4 = w(y), N(y), M(y), Mt(y), V(y)

print(f"w(4)  = {w_y4:.5f}")
print(f"N(4)  = {N_y4:.2f} kN")
print(f"M(4)  = {M_y4:.2f} kNm")
print(f"Mt(4) = {Mt_y4:.2f} kNm")
print(f"V(4)  = {V_y4:.2f} kN")

# Intervalo de profundidade
y_vals = np.linspace(0, 4, 500)
N_vals, M_vals, Mt_vals, V_vals = N(y_vals), M(y_vals), Mt(y_vals), V(y_vals)

# Gráficos (y cresce de baixo para cima, sem inversão)
plt.figure(figsize=(12, 10))

plt.subplot(2, 2, 1)
plt.plot(N_vals, y_vals, label="N(y)")
plt.axhline(y=4, color='r', linestyle='--')
plt.scatter([N_y4], [y], color='red')
plt.title("Esforço normal N(y)")
plt.xlabel("N (kN)")
plt.ylabel("Profundidade y (m)")
plt.grid(True)

plt.subplot(2, 2, 2)
plt.plot(M_vals, y_vals, label="M(y)", color="g")
plt.axhline(y=4, color='r', linestyle='--')
plt.scatter([M_y4], [y], color='red')
plt.title("Momento fletor M(y)")
plt.xlabel("M (kNm)")
plt.ylabel("Profundidade y (m)")
plt.grid(True)

plt.subplot(2, 2, 3)
plt.plot(Mt_vals, y_vals, label="Mt(y)", color="orange")
plt.axhline(y=4, color='r', linestyle='--')
plt.scatter([Mt_y4], [y], color='red')
plt.title("Momento torçor Mt(y)")
plt.xlabel("Mt (kNm)")
plt.ylabel("Profundidade y (m)")
plt.grid(True)

plt.subplot(2, 2, 4)
plt.plot(V_vals, y_vals, label="V(y)", color="purple")
plt.axhline(y=4, color='r', linestyle='--')
plt.scatter([V_y4], [y], color='red')
plt.title("Esforço cortante V(y)")
plt.xlabel("V (kN)")
plt.ylabel("Profundidade y (m)")
plt.grid(True)

plt.tight_layout()
plt.savefig("graficos_esforcos_base_zero.png")
plt.show()

print("Gráficos salvos como 'graficos_esforcos.png'")


