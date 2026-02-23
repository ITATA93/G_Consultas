# SQLUser.PAC_AdmBookingSystem

**Schema:** SQLUser
**Columnas:** 21
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ADMBS_RowId | bigint | PK |  | NO | - |
| ADMBS_Code | varchar |  |  | NO | Code |
| ADMBS_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| ADMBS_CreatedDate | date |  |  | SI | Created Date |
| ADMBS_CreatedTime | time |  |  | SI | Created Time |
| ADMBS_CreatedUser_DR | bigint |  | FK | SI | Created User |
| ADMBS_Desc | varchar |  |  | NO | Description |
| ADMBS_NationalCode | varchar |  |  | SI | National Code |
| ADMBS_Owner | varchar |  |  | SI | Owner |
| ADMBS_UpdatedDate | date |  |  | SI | Updated Date |
| ADMBS_UpdatedTime | time |  |  | SI | Updated Time |
| ADMBS_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q17Q1 | - |  |  | SI | Date |
| Q17Q2 | - |  |  | SI | Time |
| Q17Q3 | - |  |  | SI | Length of tube from nostril / teeth / gums (cm) |
| Q17Q4 | - |  |  | SI | Tube position checked |
| Q17Q5 | - |  |  | SI | Securement device checked |
| Q17Q6 | - |  |  | SI | Actions performed |
| Q17Q7 | - |  |  | SI | Assessment notes |
| Q17Q8 | - |  |  | SI | Assessment performed by |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*