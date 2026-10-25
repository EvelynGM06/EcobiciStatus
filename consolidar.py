"""Junta todas las fotos en un solo DataFrame / CSV (para analisis)."""
import glob, pandas as pd
fotos = sorted(glob.glob("data/status/*/*.csv.gz"))
df = pd.concat((pd.read_csv(f, dtype={"station_id": str}) for f in fotos), ignore_index=True)
df["ts_local"] = pd.to_datetime(df["ts_local"])
print(len(fotos), "fotos;", df.station_id.nunique(), "estaciones;", df.ts_local.min(), "->", df.ts_local.max())
df.to_csv("status_consolidado.csv.gz", index=False)
