# SQLUser.ORC_ANA_Method_Agent_Alloc

**Schema:** SQLUser
**Columnas:** 14
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Órdenes**. Parámetros de órdenes médicas.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| METAG_RowId | bigint | PK |  | NO | - |
| ChildQ48DR | - |  |  | SI | Child Reference: Special Test 2 ( + or - ) |
| METAG_Agent_DR | bigint |  | FK | SI | Des Ref Agent |
| METAG_CreatedDate | date |  |  | SI | Created Date |
| METAG_CreatedTime | time |  |  | SI | Created Time |
| METAG_CreatedUser_DR | bigint |  | FK | SI | Created User |
| METAG_Method_DR | bigint |  | FK | SI | Des Ref Ana Method |
| METAG_UpdatedDate | date |  |  | SI | Updated Date |
| METAG_UpdatedTime | time |  |  | SI | Updated Time |
| METAG_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q47Q1 | - |  |  | SI | Biceps tendon |
| Q47Q2 | - |  |  | SI | Left |
| Q47Q3 | - |  |  | SI | Right |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*