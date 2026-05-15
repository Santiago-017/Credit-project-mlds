# =============================================================
# Proyecto: Credit Risk - Predicción de Aprobación de Créditos
# Fase 1: Carga y exploración inicial de datos
# Dataset: Loan Approval Classification Data (Kaggle - taweilo)
# =============================================================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

# ── Configuración general ────────────────────────────────────
sns.set_theme(style="whitegrid")
plt.rcParams["figure.figsize"] = (10, 5)

# ── 1. CARGA DE DATOS ────────────────────────────────────────
# Ajusta la ruta si guardaste el CSV en otra carpeta
DATA_PATH = os.path.join("data", "raw", "loan_data.csv")

df = pd.read_csv(DATA_PATH)

print("=" * 55)
print(" CARGA DE DATOS EXITOSA")
print("=" * 55)


# ── 2. INFORMACIÓN GENERAL ───────────────────────────────────
print(f"\nDimensiones del dataset: {df.shape[0]} filas x {df.shape[1]} columnas")

print("\nTipos de datos por columna:")
print(df.dtypes)


# ── 3. VALORES NULOS ─────────────────────────────────────────
print("\n" + "=" * 55)
print(" VALORES NULOS")
print("=" * 55)
nulos = df.isnull().sum()
print(nulos[nulos >= 0].to_string())
print(f"\nTotal de valores nulos: {df.isnull().sum().sum()}")


# ── 4. REGISTROS DUPLICADOS ──────────────────────────────────
duplicados = df.duplicated().sum()
print(f"\nRegistros duplicados: {duplicados}")


# ── 5. PRIMERAS FILAS ────────────────────────────────────────
print("\n" + "=" * 55)
print(" PRIMERAS 5 FILAS")
print("=" * 55)
print(df.head().to_string())


# ── 6. ESTADÍSTICAS DESCRIPTIVAS ─────────────────────────────
print("\n" + "=" * 55)
print(" ESTADÍSTICAS DESCRIPTIVAS - VARIABLES NUMÉRICAS")
print("=" * 55)
print(df.describe().round(2).to_string())


# ── 7. DISTRIBUCIÓN DE LA VARIABLE OBJETIVO ──────────────────
print("\n" + "=" * 55)
print(" VARIABLE OBJETIVO: loan_status")
print("=" * 55)
conteo = df["loan_status"].value_counts()
proporcion = df["loan_status"].value_counts(normalize=True) * 100
resumen = pd.DataFrame({"Cantidad": conteo, "Porcentaje (%)": proporcion.round(2)})
resumen.index = ["Rechazado (0)", "Aprobado (1)"]
print(resumen.to_string())

fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# Gráfico de barras
axes[0].bar(
    ["Rechazado (0)", "Aprobado (1)"],
    conteo.values,
    color=["#E74C3C", "#2ECC71"],
    edgecolor="white",
    width=0.5
)
axes[0].set_title("Distribución de loan_status", fontsize=13, fontweight="bold")
axes[0].set_ylabel("Cantidad de registros")
for i, v in enumerate(conteo.values):
    axes[0].text(i, v + 200, str(v), ha="center", fontweight="bold")

# Gráfico de torta
axes[1].pie(
    conteo.values,
    labels=["Rechazado (0)", "Aprobado (1)"],
    autopct="%1.1f%%",
    colors=["#E74C3C", "#2ECC71"],
    startangle=90
)
axes[1].set_title("Proporción de loan_status", fontsize=13, fontweight="bold")

plt.tight_layout()
plt.savefig(os.path.join("docs", "figures", "distribucion_loan_status.png"),
            dpi=150, bbox_inches="tight")
plt.show()
print("\nGráfico guardado en docs/figures/distribucion_loan_status.png")


# ── 8. DISTRIBUCIÓN DE VARIABLES NUMÉRICAS ───────────────────
vars_numericas = df.select_dtypes(include=[np.number]).columns.tolist()
vars_numericas = [v for v in vars_numericas if v != "loan_status"]

fig, axes = plt.subplots(3, 3, figsize=(16, 12))
axes = axes.flatten()

for i, col in enumerate(vars_numericas):
    if i >= len(axes):
        break
    axes[i].hist(df[col], bins=40, color="#3498DB", edgecolor="white", alpha=0.85)
    axes[i].set_title(col, fontsize=11, fontweight="bold")
    axes[i].set_xlabel("Valor")
    axes[i].set_ylabel("Frecuencia")

# Ocultar subplots vacíos
for j in range(len(vars_numericas), len(axes)):
    axes[j].set_visible(False)

plt.suptitle("Distribución de Variables Numéricas", fontsize=14, fontweight="bold", y=1.01)
plt.tight_layout()
plt.savefig(os.path.join("docs", "figures", "distribucion_numericas.png"),
            dpi=150, bbox_inches="tight")
plt.show()
print("Gráfico guardado en docs/figures/distribucion_numericas.png")


# ── 9. DISTRIBUCIÓN DE VARIABLES CATEGÓRICAS ─────────────────
vars_categoricas = df.select_dtypes(include=["object"]).columns.tolist()

fig, axes = plt.subplots(2, 3, figsize=(16, 9))
axes = axes.flatten()

for i, col in enumerate(vars_categoricas):
    if i >= len(axes):
        break
    conteo_cat = df[col].value_counts()
    axes[i].bar(conteo_cat.index, conteo_cat.values,
                color="#9B59B6", edgecolor="white", alpha=0.85)
    axes[i].set_title(col, fontsize=11, fontweight="bold")
    axes[i].set_ylabel("Frecuencia")
    axes[i].tick_params(axis="x", rotation=30)

for j in range(len(vars_categoricas), len(axes)):
    axes[j].set_visible(False)

plt.suptitle("Distribución de Variables Categóricas", fontsize=14, fontweight="bold", y=1.01)
plt.tight_layout()
plt.savefig(os.path.join("docs", "figures", "distribucion_categoricas.png"),
            dpi=150, bbox_inches="tight")
plt.show()
print("Gráfico guardado en docs/figures/distribucion_categoricas.png")


# ── 10. MATRIZ DE CORRELACIÓN ─────────────────────────────────
plt.figure(figsize=(11, 8))
corr = df[vars_numericas + ["loan_status"]].corr()
mask = np.triu(np.ones_like(corr, dtype=bool))
sns.heatmap(corr, mask=mask, annot=True, fmt=".2f",
            cmap="coolwarm", center=0,
            linewidths=0.5, cbar_kws={"shrink": 0.8})
plt.title("Matriz de Correlación - Variables Numéricas", fontsize=13, fontweight="bold")
plt.tight_layout()
plt.savefig(os.path.join("docs", "figures", "matriz_correlacion.png"),
            dpi=150, bbox_inches="tight")
plt.show()
print("Gráfico guardado en docs/figures/matriz_correlacion.png")


print("\n" + "=" * 55)
print(" CARGA Y EXPLORACIÓN INICIAL COMPLETADA")
print("=" * 55)