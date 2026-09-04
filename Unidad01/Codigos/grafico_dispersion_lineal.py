mport matplotlib.pyplot as plt
import numpy as np

# --- Configuración general del gráfico ---
plt.figure(
    figsize=(6, 4),   # tamaño de la figura (ancho, alto) en pulgadas
    dpi=120           # resolución del gráfico
)

# --- Gráfico de dispersión ---
plt.scatter(
    x, y,
    marker="o",       # forma
    color='blue',     # color de los puntos
    edgecolor='black',    # borde de los puntos
    alpha=0.8,            # transparencia
    s=30,                 # tamaño de los puntos
    label='Datos originales' # etiqueta para la leyenda
)

# --- Calcular la recta de regresión ---
# Ajustar un polinomio de grado 1 (regresión lineal) a los datos x e y
coeficientes = np.polyfit(x, y, 1)
# Crear una función polinómica a partir de los coeficientes
recta_regresion = np.poly1d(coeficientes)
# Calcular los valores y predichos (y_calculada) usando la recta de regresión
y_calculada = recta_regresion(x)

# --- Gráfico de línea ---
plt.plot(
    x, y_calculada,
    color='black',   # color de la línea
    linewidth=1.0,        # grosor de la línea
    linestyle='-',        # estilo de línea (cambiado de '--' a '-')
    marker='',           # no necesitamos marcador en la línea de regresión
    markersize=0,         # tamaño del marcador
    markerfacecolor='white',
    markeredgecolor='black',
    label='Recta de regresión'
)

# --- Título ---
plt.title(
    'Diagrama de Dispersión con Recta de Regresión',
    fontsize=14,
    fontweight='bold'
)

# --- Etiquetas de los ejes ---
plt.xlabel(
    'Promedio de exámenes cortos',
    fontsize=12
)

plt.ylabel(
    'Promedio final',
    fontsize=12
)
