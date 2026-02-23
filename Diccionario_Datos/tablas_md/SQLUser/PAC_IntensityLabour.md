# SQLUser.PAC_IntensityLabour

**Schema:** SQLUser
**Columnas:** 13
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| INLAB_RowId | bigint | PK |  | NO | - |
| INLAB_Code | varchar |  |  | NO | Code |
| INLAB_CreatedDate | date |  |  | SI | Created Date |
| INLAB_CreatedTime | time |  |  | SI | Created Time |
| INLAB_CreatedUser_DR | bigint |  | FK | SI | Created User |
| INLAB_Desc | varchar |  |  | NO | Description |
| INLAB_UpdatedDate | date |  |  | SI | Updated Date |
| INLAB_UpdatedTime | time |  |  | SI | Updated Time |
| INLAB_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q12Q1 | - |  |  | SI | Relation |
| Q12Q2 | - |  |  | SI | Breast cancer (Age) |
| Q12Q3 | - |  |  | SI | Ovarian cancer (Age) |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*