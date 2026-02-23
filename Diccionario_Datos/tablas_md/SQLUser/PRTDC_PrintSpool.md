# SQLUser.PRTDC_PrintSpool

**Schema:** SQLUser
**Columnas:** 11
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Impresión/Reportes**. Generación de documentos.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| PRTDC_RowId | bigint | PK |  | NO | - |
| PRTDC_Description | varchar |  |  | SI | Description |
| PRTDC_Images | varchar |  |  | SI | Page Layout Image List |
| PRTDC_Parameter | varchar |  |  | SI | Parameter |
| PRTDC_PrintedDate | date |  |  | SI | Printed Date |
| PRTDC_PrintedTime | time |  |  | SI | Printed Time |
| PRTDC_RequestedDate | date |  |  | SI | Requested Date |
| PRTDC_RequestedTime | time |  |  | SI | Requested Time |
| PRTDC_Status | varchar |  |  | SI | Print Status |
| PRTDC_UserLocation_DR | bigint |  | FK | SI | User Location |
| PRTDC_User_DR | bigint |  | FK | SI | User Requested |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*