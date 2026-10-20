import pandas as pd

FECHA_INICIO = pd.Timestamp("1997-01-01")
FECHA_FIN_CAL = pd.Timestamp("1997-09-30")


def cargar_transacciones(ruta="data/raw/CDNOW_sample.txt"):
    """Lee CDNOW_sample.txt y une las compras del mismo día (regla 0.1)."""
    df = pd.read_csv(
        ruta, sep=r"\s+", header=None,
        names=["id_master", "id", "fecha", "cds", "monto"],
    )
    df["fecha"] = pd.to_datetime(df["fecha"], format="%Y%m%d")
    df = df.groupby(["id", "fecha"]).agg({"cds": "sum", "monto": "sum"}).reset_index()
    return df


def construir_resumen(df, fecha_fin_cal=FECHA_FIN_CAL):
    """Devuelve x, t_x, T (calibración) y x_star (holdout) por cliente."""
    cal = df[df["fecha"] <= fecha_fin_cal]
    hold = df[df["fecha"] > fecha_fin_cal]

    resumen = cal.groupby("id")["fecha"].agg(primera="min", ultima="max", n="count").reset_index()
    resumen["x"] = resumen["n"] - 1
    resumen["t_x"] = (resumen["ultima"] - resumen["primera"]).dt.days / 7
    resumen["T"] = (fecha_fin_cal - resumen["primera"]).dt.days / 7

    x_star = hold.groupby("id").size().rename("x_star")
    resumen = resumen.merge(x_star, on="id", how="left")
    resumen["x_star"] = resumen["x_star"].fillna(0).astype(int)
    return resumen