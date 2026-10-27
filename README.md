# Proyecto 2: Contando clientes con modelos Buy 'Til You Die

Curso de Business Intelligence. Implementación del modelo **BG/NBD** (Beta-Geométrico / Binomial Negativo) desde cero y su aplicación a dos conjuntos de datos: la muestra de **CDNOW** y **Online Retail**.

## Equipo

| Parte | Contenido | Responsable | Notebook |
|---|---|---|---|
| 0, 1 y 2 | Preparación de datos, derivación de la verosimilitud, simulación, estimación e incertidumbre | Noel | `01_preparacion_datos.ipynb`, `02_modelo_bgnbd.ipynb` |
| 3 | Pronóstico de compras: bottom-up (BG/NBD) y top-down | Ximena | `03_pronostico.ipynb` |
| 4 | ¿Quién sigue vivo? P(vivo), P(compra) y MBG/NBD | Olga | `04_quien_sigue_vivo.ipynb` |
| 5 | Aplicación a Online Retail | Cristina | `parte5_online_retail.ipynb` |
| 6 | Regresión logística vs BG/NBD | Hugo | `parte6_logistica_vs_bgnbd.ipynb` |

## Estructura del repositorio

```
.
├── data/
│   └── raw/
│       ├── CDNOW_sample.txt        # muestra de CDNOW (2,357 clientes)
│       └── Online_Retail.xlsx      # transacciones de Online Retail
├── notebooks/                      # un notebook por parte (ver tabla)
├── src/
│   ├── data_prep.py                # lectura de transacciones y resumen (x, t_x, T)
│   └── bgnbd.py                    # log-verosimilitud del BG/NBD
├── requirements.txt
└── README.md
```

## Cómo reproducir

1. Clonar el repositorio y entrar a la carpeta:

   ```
   git clone https://github.com/xNoksS/bi-proyecto2-btyd
   cd bi-proyecto2-btyd
   ```

2. Crear un entorno virtual e instalar las dependencias (Python 3.10 o superior):

   ```
   python -m venv .venv
   .venv\Scripts\activate          # Windows
   source .venv/bin/activate       # macOS / Linux
   pip install -r requirements.txt
   ```

3. Abrir Jupyter **desde la carpeta `notebooks/`**, porque los notebooks leen los datos con rutas relativas (`../data/raw/...`):

   ```
   cd notebooks
   jupyter notebook
   ```

4. Ejecutar cada notebook con *Kernel → Restart & Run All*. Se pueden correr en cualquier orden; cada uno carga sus propios datos. El orden recomendado para leerlos es el de la numeración.

Los datos originales no se modifican: los notebooks los leen desde `data/raw/`.

## Descripción de cada parte

**Partes 0, 1 y 2 (notebooks 01 y 02).** Se leen las transacciones, se fusionan las compras del mismo cliente en el mismo día y se construye el resumen por cliente (x, t_x, T) en semanas, con calibración del 1 de enero al 30 de septiembre de 1997. Se deriva la verosimilitud del BG/NBD, se programa en escala logarítmica (`src/bgnbd.py`) y se estima por máxima verosimilitud, con lo que se reproduce la log-verosimilitud del artículo original (−9,582.4). Se valida con una simulación de parámetros conocidos y se mide la incertidumbre con bootstrap.

**Parte 3 (notebook 03).** Pronóstico de compras repetidas en las semanas 40 a 78: bottom-up con la esperanza del BG/NBD y alternativas top-down (media histórica, ingenuo, medias móviles y tendencias), comparadas con las compras reales.

**Parte 4 (notebook 04).** Probabilidad de que cada cliente siga vivo, probabilidad de comprar en el periodo de validación, evaluación (ROC, calibración, Brier) y extensión al modelo MBG/NBD.

**Parte 5 (notebook parte5).** Aplicación del BG/NBD a Online Retail con una cohorte de clientes y un periodo de validación.

**Parte 6 (notebook parte6).** Comparación del BG/NBD con una regresión logística usando las mismas variables (x, t_x, T).

## Resultados principales (CDNOW)

| Parámetro | Estimación |
|---|---|
| r | 0.243 |
| α | 4.414 |
| a | 0.793 |
| b | 2.426 |

Log-verosimilitud: −9,582.4. En el periodo de validación, el pronóstico bottom-up del BG/NBD fue de 1,666.65 compras repetidas frente a 1,882 reales (−11.44 %).

## Presentación

Las diapositivas de la presentación final se entregan en PDF junto con este repositorio.
