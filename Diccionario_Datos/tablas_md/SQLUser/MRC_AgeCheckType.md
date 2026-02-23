# SQLUser.MRC_AgeCheckType

**Schema:** SQLUser
**Columnas:** 21
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Tipos/categorías disponibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| AGECHK_RowId | bigint | PK |  | NO | - |
| AGECHK_Code | varchar |  |  | NO | Code |
| AGECHK_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| AGECHK_CreatedDate | date |  |  | SI | Created Date |
| AGECHK_CreatedTime | time |  |  | SI | Created Time |
| AGECHK_CreatedUser_DR | bigint |  | FK | SI | Created User |
| AGECHK_DateFrom | date |  |  | SI | Date From |
| AGECHK_DateTo | date |  |  | SI | Date To |
| AGECHK_Desc | varchar |  |  | NO | Description |
| AGECHK_Owner | varchar |  |  | SI | Owner |
| AGECHK_UpdatedDate | date |  |  | SI | Updated Date |
| AGECHK_UpdatedTime | time |  |  | SI | Updated Time |
| AGECHK_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| ChildQ108DR | - |  |  | SI | Child Reference: Extremidades |
| Q99Q1 | - |  |  | SI | Palpación |
| Q99Q2 | - |  |  | SI | Percusión |
| Q99Q3 | - |  |  | SI | Auscultación |
| Q99Q4 | - |  |  | SI | Localización |
| Q99Q5 | - |  |  | SI | Lateralidad |
| Q99Q6 | - |  |  | SI | Comentarios |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*