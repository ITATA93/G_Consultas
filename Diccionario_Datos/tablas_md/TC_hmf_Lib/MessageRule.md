# TC_hmf_Lib.MessageRule

**Schema:** TC_hmf_Lib
**Columnas:** 7
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**TrakCare HMF**. Framework de mensajería y procesamiento de Health Messages.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| HMFLIBMSGRUL_ParRef | bigint | PK |  | NO | Message Format Parent Reference |
| HMFLIBMSGRUL_Class | varchar |  |  | SI | Message rule class |
| HMFLIBMSGRUL_Code | varchar |  |  | NO | Message rule code |
| HMFLIBMSGRUL_Desc | varchar |  |  | SI | Message rule description |
| HMFLIBMSGRUL_Enabled | bit |  |  | SI | Enabled flag |
| ID | varchar |  |  | NO | - |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*