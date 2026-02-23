# SQLUser.PAC_ReAdmissionToRehab

**Schema:** SQLUser
**Columnas:** 23
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| RTR_RowId | bigint | PK |  | NO | - |
| Q02Q1 | - |  |  | SI | Tourniquet applied |
| Q02Q2 | - |  |  | SI | Body site |
| Q02Q3 | - |  |  | SI | Side |
| Q02Q4 | - |  |  | SI | Pressure (mmHg) |
| Q02Q5 | - |  |  | SI | Inflated time |
| Q02Q6 | - |  |  | SI | Deflated time |
| Q02Q7 | - |  |  | SI | Total tourniquet time |
| Q02Q8 | - |  |  | SI | Body site |
| QUESParRefDR | - |  |  | SI | Parent Reference |
| RTR_Code | varchar |  |  | NO | Code |
| RTR_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| RTR_CreatedDate | date |  |  | SI | Created Date |
| RTR_CreatedTime | time |  |  | SI | Created Time |
| RTR_CreatedUser_DR | bigint |  | FK | SI | Created User |
| RTR_DateFrom | date |  |  | SI | Date From |
| RTR_DateTo | date |  |  | SI | Date To |
| RTR_Desc | varchar |  |  | NO | Description |
| RTR_NationalCode | varchar |  |  | SI | NationalCode |
| RTR_Owner | varchar |  |  | SI | Owner |
| RTR_UpdatedDate | date |  |  | SI | Updated Date |
| RTR_UpdatedTime | time |  |  | SI | Updated Time |
| RTR_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*