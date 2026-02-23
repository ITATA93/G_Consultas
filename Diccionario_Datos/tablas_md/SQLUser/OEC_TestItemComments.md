# SQLUser.OEC_TestItemComments

**Schema:** SQLUser
**Columnas:** 21
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Items/líneas de detalle.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| TICOM_RowId | bigint | PK |  | NO | - |
| ChildQ13DR | - |  |  | SI | Child Reference: Stoma Care |
| Q11Q1 | - |  |  | SI | Date |
| Q11Q2 | - |  |  | SI | Appearance |
| Q11Q3 | - |  |  | SI | Skin peristomal |
| Q11Q4 | - |  |  | SI | Excretion |
| Q11Q5 | - |  |  | SI | Pain |
| Q11Q6 | - |  |  | SI | Pain Score |
| Q11Q7 | - |  |  | SI | Note |
| Q11Q8 | - |  |  | SI | Time |
| QUESParRefDR | - |  |  | SI | Parent Reference |
| TICOM_Code | varchar |  |  | NO | Code |
| TICOM_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| TICOM_CreatedDate | date |  |  | SI | Created Date |
| TICOM_CreatedTime | time |  |  | SI | Created Time |
| TICOM_CreatedUser_DR | bigint |  | FK | SI | Created User |
| TICOM_Desc | varchar |  |  | NO | Description |
| TICOM_Owner | varchar |  |  | SI | Owner |
| TICOM_UpdatedDate | date |  |  | SI | Updated Date |
| TICOM_UpdatedTime | time |  |  | SI | Updated Time |
| TICOM_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*