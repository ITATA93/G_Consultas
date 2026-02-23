# SQLUser.PAC_WardAdm

**Schema:** SQLUser
**Columnas:** 22
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| WADM_ParRef | bigint | PK |  | NO | PAC_Ward Parent Reference |
| Q21Q1 | - |  |  | SI | Maternal position during manoeuvre / action |
| Q21Q2 | - |  |  | SI | Manoeuvre / action order number |
| Q21Q3 | - |  |  | SI | Time stamp |
| Q21Q4 | - |  |  | SI | Manoeuvre / action type |
| Q21Q5 | - |  |  | SI | Other, please specify |
| Q21Q6 | - |  |  | SI | By whom |
| Q21Q7 | - |  |  | SI | Comments |
| QUESParRefDR | - |  |  | SI | Parent Reference |
| WADM_BookedStatus | varchar |  |  | SI | Booked Status |
| WADM_Childsub | double |  |  | NO | Childsub |
| WADM_CreatedDate | date |  |  | SI | Created Date |
| WADM_CreatedTime | time |  |  | SI | Created Time |
| WADM_CreatedUser_DR | bigint |  | FK | SI | Created User |
| WADM_Location_DR | bigint |  | FK | SI | Des Ref Location - Location where the patient was ... |
| WADM_PAADM_DR | bigint |  | FK | SI | Des Ref PAADM |
| WADM_Room_DR | bigint |  | FK | SI | Des Ref Room |
| WADM_RowId | varchar |  |  | NO | - |
| WADM_Trans_DR | varchar |  | FK | SI | Des Ref Trans |
| WADM_UpdatedDate | date |  |  | SI | Updated Date |
| WADM_UpdatedTime | time |  |  | SI | Updated Time |
| WADM_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*