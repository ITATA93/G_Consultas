# SQLUser.LBC_AdditionalBloodGroup

**Schema:** SQLUser
**Columnas:** 21
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Laboratorio**. Parámetros del módulo de laboratorio.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBCABG_RowID | bigint | PK |  | NO | - |
| LBCABG_AdditionalBloodGroupSystem_DR | bigint |  | FK | NO | Additional Blood Group System |
| LBCABG_Code | varchar |  |  | NO | Code
The collation is an exception as we need to ... |
| LBCABG_CodeTableTags | varchar |  |  | SI | List of code table tags |
| LBCABG_CreatedDate | date |  |  | SI | Created Date |
| LBCABG_CreatedTime | time |  |  | SI | Created Time |
| LBCABG_CreatedUser_DR | bigint |  | FK | SI | Created User |
| LBCABG_DateFrom | date |  |  | SI | Effective date for the record |
| LBCABG_DateTo | date |  |  | SI | Last day the record is active |
| LBCABG_Desc | varchar |  |  | NO | Description
The collation is an exception as we n... |
| LBCABG_Owner | varchar |  |  | SI | Owner |
| LBCABG_UpdatedDate | date |  |  | SI | Updated Date |
| LBCABG_UpdatedTime | time |  |  | SI | Updated Time |
| LBCABG_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q20Q1 | - |  |  | SI | Child status |
| Q20Q2 | - |  |  | SI | Screening level |
| Q20Q3 | - |  |  | SI | Screening result |
| Q20Q4 | - |  |  | SI | Screen outcome |
| Q20Q5 | - |  |  | SI | Date |
| Q20Q6 | - |  |  | SI | Time |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*