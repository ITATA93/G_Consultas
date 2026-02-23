# SQLUser.ORC_AirwayCircuit

**Schema:** SQLUser
**Columnas:** 18
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Órdenes**. Parámetros de órdenes médicas.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| AIRCIR_RowId | bigint | PK |  | NO | - |
| AIRCIR_Code | varchar |  |  | NO | Code |
| AIRCIR_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| AIRCIR_CreatedDate | date |  |  | SI | Created Date |
| AIRCIR_CreatedTime | time |  |  | SI | Created Time |
| AIRCIR_CreatedUser_DR | bigint |  | FK | SI | Created User |
| AIRCIR_DateFrom | date |  |  | SI | Date From |
| AIRCIR_DateTo | date |  |  | SI | Date To |
| AIRCIR_Desc | varchar |  |  | NO | Description |
| AIRCIR_Owner | varchar |  |  | SI | Owner |
| AIRCIR_UpdatedDate | date |  |  | SI | Updated Date |
| AIRCIR_UpdatedTime | time |  |  | SI | Updated Time |
| AIRCIR_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| ChildQ52DR | - |  |  | SI | Child Reference: Special Test 6 (+ or - ) |
| Q51Q1 | - |  |  | SI | Thoracic outlet syndrome |
| Q51Q2 | - |  |  | SI | Left |
| Q51Q3 | - |  |  | SI | Right |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*