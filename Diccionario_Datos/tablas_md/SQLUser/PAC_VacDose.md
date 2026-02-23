# SQLUser.PAC_VacDose

**Schema:** SQLUser
**Columnas:** 27
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| PACVD_RowID | bigint | PK |  | NO | - |
| ChildQ40DR | - |  |  | SI | Child Reference: Secondary cannula site check |
| PACVD_Code | varchar |  |  | SI | Code |
| PACVD_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| PACVD_CreatedDate | date |  |  | SI | Created Date |
| PACVD_CreatedTime | time |  |  | SI | Created Time |
| PACVD_CreatedUser_DR | bigint |  | FK | SI | Created User |
| PACVD_DateFrom | date |  |  | SI | Date From |
| PACVD_DateTo | date |  |  | SI | Date To |
| PACVD_Desc | varchar |  |  | SI | Description |
| PACVD_OnceOnly | bit |  |  | SI | Determines whether the system should validate that... |
| PACVD_Owner | varchar |  |  | SI | Owner |
| PACVD_PCCI_DR | bigint |  | FK | SI | Parent Preventative Care Item |
| PACVD_RestrictionDose_DR | bigint |  | FK | SI | Restriction fields: vaccination dose |
| PACVD_RestrictionNumber | integer |  |  | SI | Restriction fields: number |
| PACVD_RestrictionUnit | varchar |  |  | SI | Restriction fields: unit of time |
| PACVD_UpdatedDate | date |  |  | SI | Updated Date |
| PACVD_UpdatedTime | time |  |  | SI | Updated Time |
| PACVD_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q20Q1 | - |  |  | SI | Date |
| Q20Q2 | - |  |  | SI | Time |
| Q20Q3 | - |  |  | SI | Condition of site |
| Q20Q4 | - |  |  | SI | Cannula left in situ |
| Q20Q5 | - |  |  | SI | Condition of cannula |
| Q20Q6 | - |  |  | SI | Site check notes |
| Q20Q7 | - |  |  | SI | Checked by |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*