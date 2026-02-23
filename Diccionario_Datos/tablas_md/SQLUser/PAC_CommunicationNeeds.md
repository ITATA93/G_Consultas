# SQLUser.PAC_CommunicationNeeds

**Schema:** SQLUser
**Columnas:** 18
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| COMMNEEDS_RowId | bigint | PK |  | NO | - |
| COMMNEEDS_Code | varchar |  |  | NO | Code |
| COMMNEEDS_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| COMMNEEDS_CreatedDate | date |  |  | SI | Created Date |
| COMMNEEDS_CreatedTime | time |  |  | SI | Created Time |
| COMMNEEDS_CreatedUser_DR | bigint |  | FK | SI | Created User |
| COMMNEEDS_DateFrom | date |  |  | SI | Date From |
| COMMNEEDS_DateTo | date |  |  | SI | Date To |
| COMMNEEDS_Desc | varchar |  |  | NO | Description |
| COMMNEEDS_Owner | varchar |  |  | SI | Owner |
| COMMNEEDS_UpdatedDate | date |  |  | SI | Updated Date |
| COMMNEEDS_UpdatedTime | time |  |  | SI | Updated Time |
| COMMNEEDS_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| ChildQ08DR | - |  |  | SI | Child Reference: Basal insulin infusion rate |
| Q11Q1 | - |  |  | SI | Time from |
| Q11Q2 | - |  |  | SI | Time to |
| Q11Q3 | - |  |  | SI | Blood glucose concentration target (mmol/L) |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*