# =============================================================
# VENTAS-5: Script de análisis de ventas
# Proyecto: TP Analisis de Ventas - UTN TUP
# Autor: P2 - Braian Martinez
# Descripción: Análisis estadístico del dataset de ventas 2024
# =============================================================

import pandas as pd
import matplotlib.pyplot as plt

# Importamos el dataset directamente desde la URL publica del repositorio.
# Usamos una URL en lugar de ruta local para garantizar que el script
# funcione correctamente en Google Colab sin depender de archivos locales.
url = "https://gist.githubusercontent.com/khanusama20/ee33c2869dd5cf3cebdf020be1ca43f6/raw/cbcbbb2651dd0b631d7bd194bc51b2fbb105d108/sales_sample_2024.csv"
df = pd.read_csv(url)
df.head()

# Verificamos que el dataset se cargo correctamente revisando
# la estructura de columnas y tipos de datos antes de operar sobre el.
df.info()
print("Columnas disponibles:", df.columns.tolist())

# Calculamos las metricas basicas de negocio: total y promedio de ventas.
# Esto nos da una vision general del desempeno comercial del periodo analizado.
total_ventas = df["sales_amount"].sum()
promedio_ventas = df["sales_amount"].mean()
print("Total ventas:", total_ventas)
print("Promedio ventas:", promedio_ventas)

# Identificamos los valores extremos del dataset.
# Conocer la venta maxima y minima nos permite detectar dias atipicos
# que podrian indicar promociones, errores de carga o picos de demanda.
max_venta = df["sales_amount"].max()
min_venta = df["sales_amount"].min()
print("Venta maxima:", max_venta)
print("Venta minima:", min_venta)

# Agrupamos las ventas por fecha para analizar el comportamiento diario.
# Este agrupamiento nos permite ver como evolucionaron las ventas a lo largo del tiempo.
ventas_por_dia = df.groupby("sales_date")["sales_amount"].sum()
print(ventas_por_dia)

# Generamos el grafico de evolucion de ventas diarias.
# La visualizacion facilita identificar tendencias y patrones que los
# numeros solos no muestran de forma clara.
plt.figure(figsize=(10,5))
plt.plot(ventas_por_dia.index, ventas_por_dia.values)
plt.title("Evolucion de ventas por dia")
plt.xlabel("Fecha")
plt.ylabel("Ventas")
plt.xticks(rotation=45)
plt.grid(True)
plt.savefig("resultados/grafico_ventas.png", bbox_inches="tight")
plt.show()
print("Grafico guardado en /resultados ✓")
