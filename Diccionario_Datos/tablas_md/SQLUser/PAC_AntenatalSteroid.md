# SQLUser.PAC_AntenatalSteroid

**Schema:** SQLUser
**Columnas:** 17
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ANTST_RowId | bigint | PK |  | NO | - |
| ANTST_Code | varchar |  |  | NO | Code |
| ANTST_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| ANTST_CreatedDate | date |  |  | SI | Created Date |
| ANTST_CreatedTime | time |  |  | SI | Created Time |
| ANTST_CreatedUser_DR | bigint |  | FK | SI | Created User |
| ANTST_DateFrom | date |  |  | SI | Date From |
| ANTST_DateTo | date |  |  | SI | Date To |
| ANTST_Desc | varchar |  |  | NO | Description |
| ANTST_Owner | varchar |  |  | SI | Owner |
| ANTST_UpdatedDate | date |  |  | SI | Updated Date |
| ANTST_UpdatedTime | time |  |  | SI | Updated Time |
| ANTST_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q111Q1 | - |  |  | SI | Recommended |
| Q111Q2 | - |  |  | SI | Others recommended |
| Q111Q3 | - |  |  | SI | Quantity per week |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*