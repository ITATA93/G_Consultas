# SQLUser.PAC_ContReferralTo

**Schema:** SQLUser
**Columnas:** 21
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| REFTO_RowId | bigint | PK |  | NO | - |
| ChildQ96DR | - |  |  | SI | Child Reference: Peripheral IV Assessment |
| Q68Q1 | - |  |  | SI | Status |
| Q68Q2 | - |  |  | SI | Care / Troubleshoot	 |
| Q68Q3 | - |  |  | SI | Site Care	 |
| Q68Q4 | - |  |  | SI | Site Condition	 |
| Q68Q5 | - |  |  | SI | Dressing Condition	 |
| Q68Q6 | - |  |  | SI | Dressing |
| QUESParRefDR | - |  |  | SI | Parent Reference |
| REFTO_Code | varchar |  |  | NO | Code |
| REFTO_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| REFTO_CreatedDate | date |  |  | SI | Created Date |
| REFTO_CreatedTime | time |  |  | SI | Created Time |
| REFTO_CreatedUser_DR | bigint |  | FK | SI | Created User |
| REFTO_DateFrom | date |  |  | SI | Date From |
| REFTO_DateTo | date |  |  | SI | Date To |
| REFTO_Desc | varchar |  |  | NO | Description |
| REFTO_Owner | varchar |  |  | SI | Owner |
| REFTO_UpdatedDate | date |  |  | SI | Updated Date |
| REFTO_UpdatedTime | time |  |  | SI | Updated Time |
| REFTO_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*