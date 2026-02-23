# SQLUser.PAC_RetroplacentalClot

**Schema:** SQLUser
**Columnas:** 25
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| PLACCLOT_RowId | bigint | PK |  | NO | - |
| PLACCLOT_Active | varchar |  |  | SI | Active |
| PLACCLOT_Code | varchar |  |  | NO | Code |
| PLACCLOT_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| PLACCLOT_CreatedDate | date |  |  | SI | Created Date |
| PLACCLOT_CreatedTime | time |  |  | SI | Created Time |
| PLACCLOT_CreatedUser_DR | bigint |  | FK | SI | Created User |
| PLACCLOT_DateFrom | date |  |  | SI | Date From |
| PLACCLOT_DateTo | date |  |  | SI | DateTo |
| PLACCLOT_Desc | varchar |  |  | NO | Description |
| PLACCLOT_NationalCode | varchar |  |  | SI | National code |
| PLACCLOT_Owner | varchar |  |  | SI | Owner |
| PLACCLOT_UpdatedDate | date |  |  | SI | Updated Date |
| PLACCLOT_UpdatedTime | time |  |  | SI | Updated Time |
| PLACCLOT_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q03Q1 | - |  |  | SI | Date |
| Q03Q2 | - |  |  | SI | Time |
| Q03Q3 | - |  |  | SI | Issue identified |
| Q03Q4 | - |  |  | SI | Identified by |
| Q03Q5 | - |  |  | SI | Proposed action |
| Q03Q6 | - |  |  | SI | Person responsible |
| Q03Q7 | - |  |  | SI | Date of action |
| Q03Q8 | - |  |  | SI | Result of action |
| Q03Q9 | - |  |  | SI | Contact number |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*