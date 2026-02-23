# SQLUser.LBC_InstrumentEventRecord

**Schema:** SQLUser
**Columnas:** 21
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Laboratorio**. Parámetros del módulo de laboratorio.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBCIER_RowID | bigint | PK |  | NO | - |
| LBCIER_Code | varchar |  |  | NO | Instrument Code |
| LBCIER_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| LBCIER_CreatedDate | date |  |  | SI | Created Date |
| LBCIER_CreatedTime | time |  |  | SI | Created Time |
| LBCIER_CreatedUser_DR | bigint |  | FK | SI | Created User |
| LBCIER_DataType | varchar |  |  | NO | Data Type |
| LBCIER_DateFrom | date |  |  | SI | Date From |
| LBCIER_DateTo | date |  |  | SI | Date To |
| LBCIER_Desc | varchar |  |  | NO | Instrument Description |
| LBCIER_Owner | varchar |  |  | SI | Owner |
| LBCIER_UpdatedDate | date |  |  | SI | Updated Date |
| LBCIER_UpdatedTime | time |  |  | SI | Updated Time |
| LBCIER_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q33Q1 | - |  |  | SI | Phone number |
| Q33Q2 | - |  |  | SI | Call attempt number |
| Q33Q3 | - |  |  | SI | Call answered |
| Q33Q4 | - |  |  | SI | Time of attempt |
| Q33Q5 | - |  |  | SI | Responder name |
| Q33Q6 | - |  |  | SI | Relationship |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*