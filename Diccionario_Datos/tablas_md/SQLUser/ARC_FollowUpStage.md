# SQLUser.ARC_FollowUpStage

**Schema:** SQLUser
**Columnas:** 22
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Arquetipo de configuración**. Definición base del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| FOLUPST_RowId | bigint | PK |  | NO | - |
| ChildQ05DR | - |  |  | SI | Child Reference: Hemangiomas y Mancha Mongólica Al... |
| FOLUPST_BillProgrStat_DR | bigint |  | FK | SI | Des Ref ARCBillProgressStatus  |
| FOLUPST_Code | varchar |  |  | NO | Code |
| FOLUPST_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| FOLUPST_CreatedDate | date |  |  | SI | Created Date |
| FOLUPST_CreatedTime | time |  |  | SI | Created Time |
| FOLUPST_CreatedUser_DR | bigint |  | FK | SI | Created User |
| FOLUPST_DateFrom | date |  |  | SI | Date From |
| FOLUPST_DateTo | date |  |  | SI | Date To |
| FOLUPST_Desc | varchar |  |  | NO | Description |
| FOLUPST_Owner | varchar |  |  | SI | Owner |
| FOLUPST_ReportText | varchar |  |  | SI | Report Text |
| FOLUPST_Report_DR | bigint |  | FK | SI | Des Ref websys.Report  |
| FOLUPST_UpdatedDate | date |  |  | SI | Updated Date |
| FOLUPST_UpdatedTime | time |  |  | SI | Updated Time |
| FOLUPST_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q70Q1 | - |  |  | SI | Lesión |
| Q70Q2 | - |  |  | SI | Segmento |
| Q70Q3 | - |  |  | SI | Lateralidad |
| Q70Q4 | - |  |  | SI | Comentarios |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*