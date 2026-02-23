# SQLUser.PAC_CareType

**Schema:** SQLUser
**Columnas:** 30
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Tipos/categorías disponibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CARETYP_RowId | bigint | PK |  | NO | - |
| CARETYP_AdmSource | varchar |  |  | SI | AdmSource |
| CARETYP_AgeFrom | double |  |  | SI | Age From |
| CARETYP_AgeTo | double |  |  | SI | Age To |
| CARETYP_AgeType | varchar |  |  | SI | Age Type |
| CARETYP_CarerAvail | varchar |  |  | SI | CarerAvail |
| CARETYP_Code | varchar |  |  | SI | Code |
| CARETYP_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| CARETYP_CreatedDate | date |  |  | SI | Created Date |
| CARETYP_CreatedTime | time |  |  | SI | Created Time |
| CARETYP_CreatedUser_DR | bigint |  | FK | SI | Created User |
| CARETYP_DateFrom | date |  |  | SI | Date From |
| CARETYP_DateTo | date |  |  | SI | Date To |
| CARETYP_Default | varchar |  |  | SI | Default |
| CARETYP_Desc | varchar |  |  | SI | Description |
| CARETYP_DischargeType | varchar |  |  | SI | Discharge Type codes |
| CARETYP_FundingSource | varchar |  |  | SI | FundingSource |
| CARETYP_ICDEdit | varchar |  |  | SI | ICD Edit |
| CARETYP_InsType | varchar |  |  | SI | InsType |
| CARETYP_MedicareSuffix | varchar |  |  | SI | MedicareSuffix |
| CARETYP_NationCode | varchar |  |  | SI | National Code |
| CARETYP_Owner | varchar |  |  | SI | Owner |
| CARETYP_UpdatedDate | date |  |  | SI | Updated Date |
| CARETYP_UpdatedTime | time |  |  | SI | Updated Time |
| CARETYP_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| ChildQ14DR | - |  |  | SI | Child Reference: Protein |
| Q13Q1 | - |  |  | SI | Items |
| Q13Q2 | - |  |  | SI | Likes and dislikes |
| Q13Q3 | - |  |  | SI | Comments |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*