# Diccionario de Datos

## Fuente del Dataset

- **Nombre:** Loan Approval Classification Data
- **Fuente:** [Kaggle - taweilo](https://www.kaggle.com/datasets/taweilo/loan-approval-classification-data)
- **Tipo de datos:** Sintético para clasificación binaria
- **Tamaño:** ~45.000 registros, 13 variables
- **Variable objetivo:** `loan_status`

---

## Descripción de Variables

| # | Variable | Tipo | Descripción | Valores / Rango |
|---|----------|------|-------------|-----------------|
| 1 | `person_age` | int | Edad del solicitante en años | 18 - 144 |
| 2 | `person_gender` | object | Género del solicitante | male, female |
| 3 | `person_education` | object | Nivel educativo más alto alcanzado | High School, Associate, Bachelor, Master, Doctorate |
| 4 | `person_income` | float | Ingreso anual del solicitante en USD | > 0 |
| 5 | `person_emp_exp` | int | Años de experiencia laboral | 0 - 125 |
| 6 | `person_home_ownership` | object | Tipo de tenencia de vivienda del solicitante | RENT, OWN, MORTGAGE, OTHER |
| 7 | `loan_amnt` | float | Monto total del préstamo solicitado en USD | > 0 |
| 8 | `loan_intent` | object | Propósito declarado del préstamo | PERSONAL, EDUCATION, MEDICAL, VENTURE, HOMEIMPROVEMENT, DEBTCONSOLIDATION |
| 9 | `loan_int_rate` | float | Tasa de interés anual del préstamo en % | 0 - 100 |
| 10 | `loan_percent_income` | float | Proporción del ingreso anual que representa el monto del préstamo | 0.0 - 1.0 |
| 11 | `cb_person_cred_hist_length` | float | Longitud del historial crediticio del solicitante en años | > 0 |
| 12 | `credit_score` | int | Puntaje crediticio del solicitante | 300 - 850 |
| 13 | `previous_loan_defaults_on_file` | object | Indica si el solicitante tiene incumplimientos previos registrados | Yes, No |
| 14 | `loan_status` | int | **Variable objetivo:** indica si el crédito fue aprobado o no | 0 = Rechazado, 1 = Aprobado |

---

## Notas sobre los datos

- El dataset es de naturaleza **sintética**, generado para fines académicos y de práctica en ML.
- No contiene valores nulos en ninguna de sus columnas.
- Las variables categóricas (`person_home_ownership`, `loan_intent`, etc.) requieren **codificación** antes del modelamiento (Label Encoding u One-Hot Encoding).
- Variables como `person_age` y `person_emp_exp` pueden contener **valores atípicos** (outliers) que deben revisarse en la etapa de preprocesamiento.
- La variable `loan_percent_income` es una variable derivada: resulta de dividir `loan_amnt` entre `person_income`.