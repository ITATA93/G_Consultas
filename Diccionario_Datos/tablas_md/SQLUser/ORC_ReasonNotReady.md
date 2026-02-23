# SQLUser.ORC_ReasonNotReady

**Schema:** SQLUser
**Columnas:** 23
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Órdenes**. Parámetros de órdenes médicas.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| REANR_RowId | bigint | PK |  | NO | - |
| ChildQ28DR | - |  |  | SI | Child Reference: Lower Endoscopy Specimens & Inter... |
| Q23Q1 | - |  |  | SI | Intervention |
| Q23Q2 | - |  |  | SI | Location |
| Q23Q3 | - |  |  | SI | Other location |
| Q23Q4 | - |  |  | SI | Number |
| Q23Q5 | - |  |  | SI | Specimen removal and treatment methods |
| Q23Q6 | - |  |  | SI | Other methods |
| Q23Q7 | - |  |  | SI | Retrieved |
| Q23Q8 | - |  |  | SI | Comments |
| QUESParRefDR | - |  |  | SI | Parent Reference |
| REANR_Code | varchar |  |  | NO | Code |
| REANR_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| REANR_CreatedDate | date |  |  | SI | Created Date |
| REANR_CreatedTime | time |  |  | SI | Created Time |
| REANR_CreatedUser_DR | bigint |  | FK | SI | Created User |
| REANR_DateFrom | date |  |  | SI | Date From |
| REANR_DateTo | date |  |  | SI | Date To |
| REANR_Desc | varchar |  |  | NO | Description |
| REANR_Owner | varchar |  |  | SI | Owner |
| REANR_UpdatedDate | date |  |  | SI | Updated Date |
| REANR_UpdatedTime | time |  |  | SI | Updated Time |
| REANR_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*