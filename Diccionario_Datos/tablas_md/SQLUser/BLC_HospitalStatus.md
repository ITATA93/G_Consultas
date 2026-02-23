# SQLUser.BLC_HospitalStatus

**Schema:** SQLUser
**Columnas:** 18
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Estados posibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| HOSST_RowId | bigint | PK |  | NO | - |
| HOSST_Class_DR | bigint |  | FK | SI | Des Ref to HOSClass |
| HOSST_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| HOSST_CreatedDate | date |  |  | SI | Created Date |
| HOSST_CreatedTime | time |  |  | SI | Created Time |
| HOSST_CreatedUser_DR | bigint |  | FK | SI | Created User |
| HOSST_DateFrom | date |  |  | NO | Date FRom |
| HOSST_DateTo | date |  |  | SI | Date To |
| HOSST_Hospital_DR | bigint |  | FK | SI | Des Ref Hospital_DR |
| HOSST_Owner | varchar |  |  | SI | Owner |
| HOSST_UpdatedDate | date |  |  | SI | Updated Date |
| HOSST_UpdatedTime | time |  |  | SI | Updated Time |
| HOSST_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q18Q1 | - |  |  | SI | Medicamento |
| Q18Q2 | - |  |  | SI | Dosificación |
| Q18Q3 | - |  |  | SI | Posología |
| Q18Q4 | - |  |  | SI | Función |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*