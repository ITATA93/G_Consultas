# SQLUser.ORC_ReasonOTNotAvail

**Schema:** SQLUser
**Columnas:** 23
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Órdenes**. Parámetros de órdenes médicas.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| RNAV_RowId | bigint | PK |  | NO | - |
| ChildQ29DR | - |  |  | SI | Child Reference: Bronchoscopy Sampling |
| Q28Q1 | - |  |  | SI | Intervention |
| Q28Q2 | - |  |  | SI | Location |
| Q28Q3 | - |  |  | SI | Other location |
| Q28Q4 | - |  |  | SI | Number |
| Q28Q5 | - |  |  | SI | Specimen removal and treatment methods |
| Q28Q6 | - |  |  | SI | Other methods |
| Q28Q7 | - |  |  | SI | Retrieved |
| Q28Q8 | - |  |  | SI | Comments |
| QUESParRefDR | - |  |  | SI | Parent Reference |
| RNAV_Code | varchar |  |  | NO | Code |
| RNAV_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| RNAV_CreatedDate | date |  |  | SI | Created Date |
| RNAV_CreatedTime | time |  |  | SI | Created Time |
| RNAV_CreatedUser_DR | bigint |  | FK | SI | Created User |
| RNAV_DateFrom | date |  |  | SI | Date From |
| RNAV_DateTo | date |  |  | SI | Date To |
| RNAV_Desc | varchar |  |  | NO | Description |
| RNAV_Owner | varchar |  |  | SI | Owner |
| RNAV_UpdatedDate | date |  |  | SI | Updated Date |
| RNAV_UpdatedTime | time |  |  | SI | Updated Time |
| RNAV_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*