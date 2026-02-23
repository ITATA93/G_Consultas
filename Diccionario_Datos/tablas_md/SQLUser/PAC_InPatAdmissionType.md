# SQLUser.PAC_InPatAdmissionType

**Schema:** SQLUser
**Columnas:** 31
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Tipos/categorías disponibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| IPAT_RowId | bigint | PK |  | NO | - |
| ChildQ23DR | - |  |  | SI | Child Reference: Occupational therapist goals |
| IPAT_AdmReason | varchar |  |  | SI | AdmReason |
| IPAT_AdmSource | varchar |  |  | SI | AdmSource |
| IPAT_Age1From | double |  |  | SI | Age1From |
| IPAT_Age1To | double |  |  | SI | Age1To |
| IPAT_Age1Type | varchar |  |  | SI | Age1 Type |
| IPAT_AgeFrom | double |  |  | SI | Age From |
| IPAT_AgeTo | double |  |  | SI | Age To |
| IPAT_AgeType | varchar |  |  | SI | AgeType |
| IPAT_CategType_DR | bigint |  | FK | SI | Des Ref CategType |
| IPAT_Code | varchar |  |  | SI | Code |
| IPAT_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| IPAT_CreatedDate | date |  |  | SI | Created Date |
| IPAT_CreatedTime | time |  |  | SI | Created Time |
| IPAT_CreatedUser_DR | bigint |  | FK | SI | Created User |
| IPAT_DateFrom | date |  |  | SI | Date From |
| IPAT_DateTo | date |  |  | SI | Date To |
| IPAT_Desc | varchar |  |  | SI | Description |
| IPAT_ICD_Edit | varchar |  |  | SI | ICD Edit |
| IPAT_NationalCode | varchar |  |  | SI | National Code |
| IPAT_Owner | varchar |  |  | SI | Owner |
| IPAT_QualificationStatus | varchar |  |  | SI | Qualification Status codes |
| IPAT_Sex | varchar |  |  | SI | Sex |
| IPAT_UpdatedDate | date |  |  | SI | Updated Date |
| IPAT_UpdatedTime | time |  |  | SI | Updated Time |
| IPAT_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q21Q1 | - |  |  | SI | Goal |
| Q21Q2 | - |  |  | SI | Timing |
| Q21Q3 | - |  |  | SI | Notes |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*