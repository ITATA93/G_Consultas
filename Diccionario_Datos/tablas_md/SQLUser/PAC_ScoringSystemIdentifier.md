# SQLUser.PAC_ScoringSystemIdentifier

**Schema:** SQLUser
**Columnas:** 19
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SSI_RowId | bigint | PK |  | NO | - |
| Q26Q1 | - |  |  | SI | Micro goal |
| Q26Q2 | - |  |  | SI | Timing |
| Q26Q3 | - |  |  | SI | Outcome |
| Q26Q4 | - |  |  | SI | Notes |
| QUESParRefDR | - |  |  | SI | Parent Reference |
| SSI_CTLocs | varchar |  |  | SI | Locations |
| SSI_Code | varchar |  |  | NO | Code |
| SSI_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| SSI_CreatedDate | date |  |  | SI | Created Date |
| SSI_CreatedTime | time |  |  | SI | Created Time |
| SSI_CreatedUser_DR | bigint |  | FK | SI | Created User |
| SSI_DateFrom | date |  |  | SI | Date From |
| SSI_DateTo | date |  |  | SI | Date To |
| SSI_Desc | varchar |  |  | NO | Description |
| SSI_Owner | varchar |  |  | SI | Owner |
| SSI_UpdatedDate | date |  |  | SI | Updated Date |
| SSI_UpdatedTime | time |  |  | SI | Updated Time |
| SSI_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*