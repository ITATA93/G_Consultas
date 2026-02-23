# SQLUser.ARC_DepType

**Schema:** SQLUser
**Columnas:** 21
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Arquetipo de configuración**. Definición base del sistema. Tipos/categorías disponibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ARCDT_RowId | bigint | PK |  | NO | - |
| ARCDT_Code | varchar |  |  | NO | Deposit Type |
| ARCDT_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| ARCDT_CreatedDate | date |  |  | SI | Created Date |
| ARCDT_CreatedTime | time |  |  | SI | Created Time |
| ARCDT_CreatedUser_DR | bigint |  | FK | SI | Created User |
| ARCDT_DateFrom | date |  |  | NO | Date From |
| ARCDT_DateTo | date |  |  | SI | Date To |
| ARCDT_DefDepositAmt | double |  |  | SI | DefDepositAmt |
| ARCDT_Desc | varchar |  |  | NO | Description |
| ARCDT_Owner | varchar |  |  | SI | Owner |
| ARCDT_UpdatedDate | date |  |  | SI | Updated Date |
| ARCDT_UpdatedTime | time |  |  | SI | Updated Time |
| ARCDT_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| ChildQ46DR | - |  |  | SI | Child Reference: Pulsos |
| Q45Q1 | - |  |  | SI | Hallazgos |
| Q45Q2 | - |  |  | SI | Ext. Superior |
| Q45Q3 | - |  |  | SI | Ext. Inferior |
| Q45Q4 | - |  |  | SI | Topografía |
| Q45Q5 | - |  |  | SI | Comentario |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*