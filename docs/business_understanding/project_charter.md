# Project Charter - Entendimiento del Negocio

## Nombre del Proyecto

Credit Risk - Predicción de Aprobación de Créditos

## Objetivo del Proyecto

Desarrollar un modelo de clasificación basado en Machine Learning que prediga si un solicitante de crédito será aprobado o rechazado, a partir de sus características financieras y demográficas. Este proyecto es relevante porque permite a las entidades financieras tomar decisiones de crédito más objetivas, reducir el riesgo de incumplimiento y optimizar su proceso de evaluación de clientes.

## Alcance del Proyecto

### Incluye:

- Dataset de Kaggle: [Loan Approval Classification Data](https://www.kaggle.com/datasets/taweilo/loan-approval-classification-data), con 45.000 registros sintéticos y 13 variables sobre solicitantes de crédito.
- Análisis exploratorio de datos (EDA) y preprocesamiento de variables numéricas y categóricas.
- Entrenamiento y evaluación de modelos de clasificación supervisada para predecir la variable `loan_status` (0 = rechazado, 1 = aprobado).
- Criterios de éxito: AUC-ROC superior a 0.85 y F1-score superior a 0.80 en el conjunto de prueba.

### Excluye:

- Datos de clientes reales o información financiera en tiempo real.
- Integración con sistemas bancarios o APIs externas.
- Análisis de variables macroeconómicas externas al dataset.

## Metodología

Se seguirá la metodología **TDSP (Team Data Science Process)**, que contempla las siguientes etapas: entendimiento del negocio, adquisición y exploración de datos, modelamiento, evaluación y despliegue. Para el modelamiento se evaluarán algoritmos de clasificación como Regresión Logística, Random Forest y XGBoost, seleccionando el de mejor desempeño según las métricas definidas.

## Cronograma

| Etapa | Duración Estimada | Fechas |
|-------|------------------|--------|
| Entendimiento del negocio y carga de datos | 1 semanas | del 7 de mayo al 15 de mayo |
| Preprocesamiento y análisis exploratorio | 2 semanas | del 16 de mayo al 30 de Mayo |
| Modelamiento y extracción de características | 1 semanas | del 31 de mayo al 7 de junio |
| Despliegue | 1 semanas | del 8 de junio al 15 de junio |
| Evaluación y entrega final | 1 semana | del 15 de Junio  |

## Equipo del Proyecto

- [Santiago Bejarano Ariza] - Estudiante Ingeniería de Sistemas UNAL
- [Juan Diego Velasquez] - Estudiante Ingeniería de Sistemas UNAL

## Stakeholders

- **Entidades financieras y bancos:** Principal beneficiario del modelo. Esperan una herramienta que reduzca el riesgo crediticio y agilice la evaluación de solicitudes.
- **Solicitantes de crédito:** Se ven impactados indirectamente por las decisiones del modelo; se espera que el sistema sea justo y basado en criterios objetivos.
- **Equipo académico MLDS - Universidad Nacional:** Evalúa el desarrollo del proyecto y espera la aplicación correcta de la metodología y las técnicas de ML vistas en el curso.

## Aprobaciones

- Proyecto desarrollado en el marco del **Programa de Formación Machine Learning and Data Science (MLDS)** - Facultad de Ingeniería, Universidad Nacional de Colombia.
- Fecha de inicio: 1 de mayo de 2026.