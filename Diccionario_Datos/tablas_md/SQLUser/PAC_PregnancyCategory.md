# SQLUser.PAC_PregnancyCategory

**Schema:** SQLUser
**Columnas:** 20
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| PREGCAT_RowId | bigint | PK |  | NO | - |
| PREGCAT_Code | varchar |  |  | NO | Code |
| PREGCAT_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| PREGCAT_CreatedDate | date |  |  | SI | Created Date |
| PREGCAT_CreatedTime | time |  |  | SI | Created Time |
| PREGCAT_CreatedUser_DR | bigint |  | FK | SI | Created User |
| PREGCAT_DateFrom | date |  |  | SI | Date From |
| PREGCAT_DateTo | date |  |  | SI | Date To |
| PREGCAT_Desc | varchar |  |  | NO | Description |
| PREGCAT_LongDescription | varchar |  |  | SI | LongDescription |
| PREGCAT_Owner | varchar |  |  | SI | Owner |
| PREGCAT_UpdatedDate | date |  |  | SI | Updated Date |
| PREGCAT_UpdatedTime | time |  |  | SI | Updated Time |
| PREGCAT_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| PREGCAT_Warning | varchar |  |  | SI | Warning |
| Q05Q1 | - |  |  | SI | Are swabs, sharps and instruments correct? |
| Q05Q2 | - |  |  | SI | Theatre scrub practitioner |
| Q05Q3 | - |  |  | SI | Theatre circulator |
| Q05Q4 | - |  |  | SI | Time |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*