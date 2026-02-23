# TC_hmf_Deploy_Interface.CustomHost

**Schema:** TC_hmf_Deploy_Interface
**Columnas:** 7
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**TrakCare HMF**. Framework de mensajería y procesamiento de Health Messages.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| HMFDEPHOST_ParRef | varchar | PK |  | NO | Interface Parent Reference |
| HMFDEPHOST_CustomClassName | varchar |  |  | SI | The generated Gateway Production business host cla... |
| HMFDEPHOST_GeneratedDate | date |  |  | SI | Records last date production was generated  |
| HMFDEPHOST_GeneratedTime | time |  |  | SI | Records last time production was generated  |
| HMFDEPHOST_Type | varchar |  |  | SI | Business Host Class Type |
| ID | varchar |  |  | NO | - |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*