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
r = 6.65  # m
d = r / 2  # m
beta = ((3 * (1 - poisson**2))**(1 / 4)) / ((r * h)**0.5)
D = (Ec * h**3) / (12 * (1 - poisson**2))

# Valor específico
y = 4

# Função w(y)
def w(y):
    return -(np.exp(-beta * y)) / 126478.53 * (
        9.35 * (np.cos(beta * y) - np.sin(beta * y)) - 20.16 * np.cos(beta * y)
    )

# Função N(y)
def N(y):
    return (Ec * h / r) * w(y)

# Cálculo específico em y = 4
w_y4 = w(y)
N_y4 = N(y)
print(f"w(4) = {w_y4:.5f}")
print(f"N(4) = {N_y4:.2f} kN")

# Intervalo de y de 0 a 4 m
y_vals = np.linspace(0, 4, 500)
N_vals = N(y_vals)

# Gráfico
plt.figure(figsize=(10, 5))
plt.plot(y_vals, N_vals, label="Esforço normal N(y)")
plt.axvline(x=4, color='r', linestyle='--', label="y = 4 m")
plt.scatter([4], [N_y4], color='red')
plt.xlabel("y (m)")
plt.ylabel("N (kN)")
plt.title("Distribuição do Esforço Normal N(y) até y = 4 m")
plt.grid(True)
plt.legend()

# Salva como imagem
plt.savefig("grafico_N_ate_4m.png")
print("Gráfico salvo como 'grafico_N_ate_4m.png'")

