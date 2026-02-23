# SQLUser.PAC_ContactType

**Schema:** SQLUser
**Columnas:** 35
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Tipos/categorías disponibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CONTTP_RowId | bigint | PK |  | NO | - |
| CONTTP_Code | varchar |  |  | SI | Code |
| CONTTP_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| CONTTP_CodeTranslated | varchar |  |  | SI | Code Translated (Computed) |
| CONTTP_ContRole | varchar |  |  | SI | ContRole |
| CONTTP_CreatedDate | date |  |  | SI | Created Date |
| CONTTP_CreatedTime | time |  |  | SI | Created Time |
| CONTTP_CreatedUser_DR | bigint |  | FK | SI | Created User |
| CONTTP_Date_From | varchar |  |  | SI | CONTTP Date From |
| CONTTP_Date_To | varchar |  |  | SI | CONTTP Date To |
| CONTTP_DefFemaleReciprocal_DR | bigint |  | FK | SI | Default Female Reciprocal Contact Type |
| CONTTP_DefFemaleRelationship_DR | bigint |  | FK | SI | Default Female Relationship |
| CONTTP_DefMaleReciprocal_DR | bigint |  | FK | SI | Default Male Reciprocal Contact Type |
| CONTTP_DefMaleRelationship_DR | bigint |  | FK | SI | Default Male Relationship |
| CONTTP_Desc | varchar |  |  | SI | Description |
| CONTTP_DescTranslated | varchar |  |  | SI | Description Translated (Computed) |
| CONTTP_DisplayOrder | varchar |  |  | SI | Display Order |
| CONTTP_FamilyRelship | bigint |  |  | SI | Family Relationship |
| CONTTP_FundingArrange | varchar |  |  | SI | FundingArrange |
| CONTTP_NotOngoing | varchar |  |  | SI | Not Ongoing |
| CONTTP_Owner | varchar |  |  | SI | Owner |
| CONTTP_Priority | double |  |  | SI | Priority |
| CONTTP_UpdatedDate | date |  |  | SI | Updated Date |
| CONTTP_UpdatedTime | time |  |  | SI | Updated Time |
| CONTTP_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q58Q1 | - |  |  | SI | Time |
| Q58Q2 | - |  |  | SI | Instrument |
| Q58Q3 | - |  |  | SI | Type / Size |
| Q58Q4 | - |  |  | SI | Action |
| Q58Q5 | - |  |  | SI | Timing |
| Q58Q6 | - |  |  | SI | Traction strength |
| Q58Q7 | - |  |  | SI | By whom |
| Q58Q8 | - |  |  | SI | Notes |
| Q58Q9 | - |  |  | SI | Outcome |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*