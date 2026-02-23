# SQLUser.SS_ConversionStatus

**Schema:** SQLUser
**Columnas:** 7
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Estados posibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SSCV_RowId | varchar | PK |  | NO | - |
| SSCV_DateFinished | date |  |  | SI | Date Finished |
| SSCV_DateStart | date |  |  | SI | Date Start |
| SSCV_Error | varchar |  |  | SI | Error |
| SSCV_Routine | varchar |  |  | NO | Routine |
| SSCV_TimeFinished | time |  |  | SI | Time Finished |
| SSCV_TimeStart | time |  |  | SI | Time Start |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*