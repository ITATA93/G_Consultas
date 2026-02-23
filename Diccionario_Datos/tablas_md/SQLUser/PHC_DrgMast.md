# SQLUser.PHC_DrgMast

**Schema:** SQLUser
**Columnas:** 33
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Farmacia Clínica**. Validación farmacéutica.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| PHCD_RowId | bigint | PK |  | NO | - |
| PHCD_Code | varchar |  |  | NO | Drug Code |
| PHCD_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| PHCD_CodeTranslated | varchar |  |  | SI | - |
| PHCD_CreatedDate | date |  |  | SI | Created Date |
| PHCD_CreatedTime | time |  |  | SI | Created Time |
| PHCD_CreatedUser_DR | bigint |  | FK | SI | Created User |
| PHCD_Generic_DR | bigint |  | FK | SI | Des Ref Generic |
| PHCD_LabelName1 | varchar |  |  | SI | Drug Label Name (Local) |
| PHCD_LabelName2 | varchar |  |  | SI | Drug Label Name (Foreign) |
| PHCD_LocalName | varchar |  |  | SI | LocalName  |
| PHCD_Logo | varchar |  |  | SI | Logo - MIMS info |
| PHCD_MIMSNo | double |  |  | SI | Product No (To uniquely identify MIMS record) |
| PHCD_MinSubCat_DR | varchar |  | FK | SI | Des Ref to MinSubCat |
| PHCD_Name | varchar |  |  | SI | Drug Name (field CN in MIMS) |
| PHCD_NameTranslated | varchar |  |  | SI | - |
| PHCD_NotUseFlag | varchar |  |  | SI | Not use Flag (also indicate if ready to use) |
| PHCD_OfficialCode | varchar |  |  | SI | Official Code |
| PHCD_Owner | varchar |  |  | SI | Owner |
| PHCD_PHCPO_DR | bigint |  | FK | SI | Des Ref to PHCPO (Poison Code) |
| PHCD_PHCSC_DR | varchar |  | FK | SI | Des Ref to PHC_SubCat (Pham Index Sub Cat) |
| PHCD_PHDIS_DR | bigint |  | FK | SI | Des Ref to PHDIS (Distributor) |
| PHCD_PHMNF_DR | bigint |  | FK | SI | Des Ref to PHMNF |
| PHCD_PregnancyCategory_DR | bigint |  | FK | SI | Des Ref PACPregnancyCategory |
| PHCD_ProductName | varchar |  |  | SI | Full name of the product |
| PHCD_Stat | varchar |  |  | SI | Stat - MIMS |
| PHCD_Type_DR | bigint |  | FK | SI | Product Type (HealthShare) |
| PHCD_UpdateDate | date |  |  | SI | Update Date |
| PHCD_UpdateTime | time |  |  | SI | Update Time |
| PHCD_UpdateUser | bigint |  |  | SI | Update User |
| PHCD_UpdatedDate | date |  |  | SI | Updated Date |
| PHCD_UpdatedTime | time |  |  | SI | Updated Time |
| PHCD_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*