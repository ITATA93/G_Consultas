# SQLUser.GLC_GLAccountMap

**Schema:** SQLUser
**Columnas:** 33
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Contabilidad General (GL)**. Libro mayor y asientos contables.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| GLMAP_RowId | bigint | PK |  | NO | - |
| ChildQ48DR | - |  |  | SI | Child Reference: Assessment |
| GLMAP_AdjustDiscGLAccount_DR | bigint |  | FK | SI | Adjustment Discount GL Account, Des Ref GLCAcct |
| GLMAP_BillGroup_DR | bigint |  | FK | SI | Des Ref BillGroup |
| GLMAP_BillSub_DR | varchar |  | FK | SI | Des Ref BillSub |
| GLMAP_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| GLMAP_ContrDiscGLAccount_DR | bigint |  | FK | SI | Contract Discount GL Account, Des Ref GLCAcct |
| GLMAP_CostCentreType | varchar |  |  | SI | Cost Centre Type |
| GLMAP_CostCentre_DR | bigint |  | FK | SI | Des Ref GLCCC |
| GLMAP_CreatedDate | date |  |  | SI | Created Date |
| GLMAP_CreatedTime | time |  |  | SI | Created Time |
| GLMAP_CreatedUser_DR | bigint |  | FK | SI | Created User |
| GLMAP_DateFrom | date |  |  | SI | DateFrom |
| GLMAP_DateTo | date |  |  | SI | DateTo |
| GLMAP_DiscretDiscGLAccount_DR | bigint |  | FK | SI | Discretionary Discount GL Account, Des Ref GLCAcct |
| GLMAP_EpisSubtype_DR | bigint |  | FK | SI | Des Ref EpisSubtype |
| GLMAP_EpisodeType | varchar |  |  | SI | Episode Type |
| GLMAP_Hospital_DR | bigint |  | FK | SI | Des Ref Hospital |
| GLMAP_Owner | varchar |  |  | SI | Owner |
| GLMAP_Rank | double |  |  | SI | Rank |
| GLMAP_RecLoc_DR | bigint |  | FK | SI | Des Ref CTLoc |
| GLMAP_RevenueGLAccount_DR | bigint |  | FK | SI | Revenue GL Account, Des Ref GLCAcct |
| GLMAP_UpdatedDate | date |  |  | SI | Updated Date |
| GLMAP_UpdatedTime | time |  |  | SI | Updated Time |
| GLMAP_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q25Q1 | - |  |  | SI | Central intravenous central venous pressure cathet... |
| Q25Q2 | - |  |  | SI | Central intravenous external catheter length |
| Q25Q3 | - |  |  | SI | Central internal catheter length |
| Q25Q4 | - |  |  | SI | Central intravenous mid arm circumference |
| Q25Q5 | - |  |  | SI | Date and time |
| Q25Q6 | - |  |  | SI | Time |
| Q25Q7 | - |  |  | SI | Care provider |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*