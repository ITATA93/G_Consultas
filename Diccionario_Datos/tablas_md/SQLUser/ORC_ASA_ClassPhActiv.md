# SQLUser.ORC_ASA_ClassPhActiv

**Schema:** SQLUser
**Columnas:** 18
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Órdenes**. Parámetros de órdenes médicas.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ORASA_RowId | bigint | PK |  | NO | - |
| ChildQ49DR | - |  |  | SI | Child Reference: Special Test 3 ( + or - ) |
| ORASA_Code | varchar |  |  | NO | Code |
| ORASA_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| ORASA_CreatedDate | date |  |  | SI | Created Date |
| ORASA_CreatedTime | time |  |  | SI | Created Time |
| ORASA_CreatedUser_DR | bigint |  | FK | SI | Created User |
| ORASA_DateFrom | date |  |  | SI | Date From |
| ORASA_DateTo | date |  |  | SI | Date To |
| ORASA_Desc | varchar |  |  | NO | Description |
| ORASA_Owner | varchar |  |  | SI | Owner |
| ORASA_UpdatedDate | date |  |  | SI | Updated Date |
| ORASA_UpdatedTime | time |  |  | SI | Updated Time |
| ORASA_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q48Q1 | - |  |  | SI | Rotator cuff |
| Q48Q2 | - |  |  | SI | Left |
| Q48Q3 | - |  |  | SI | Right |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*