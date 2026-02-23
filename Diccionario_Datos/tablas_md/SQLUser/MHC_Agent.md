# SQLUser.MHC_Agent

**Schema:** SQLUser
**Columnas:** 27
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Salud Mental**. Parámetros de psiquiatría.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| MHCAGN_RowId | bigint | PK |  | NO | - |
| MHCAGN_Address1 | varchar |  |  | SI | Address1 |
| MHCAGN_Address2 | varchar |  |  | SI | Address2 |
| MHCAGN_CareProvider_DR | varchar |  | FK | SI | Des Ref CTCareProv |
| MHCAGN_City_DR | bigint |  | FK | SI | Des Ref CTCity |
| MHCAGN_Code | varchar |  |  | NO | Code |
| MHCAGN_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| MHCAGN_Country_DR | bigint |  | FK | SI | Des Ref CTCountry |
| MHCAGN_CreatedDate | date |  |  | SI | Created Date |
| MHCAGN_CreatedTime | time |  |  | SI | Created Time |
| MHCAGN_CreatedUser_DR | bigint |  | FK | SI | Created User |
| MHCAGN_DateFrom | date |  |  | SI | Date From |
| MHCAGN_DateTo | date |  |  | SI | Date To |
| MHCAGN_Desc | varchar |  |  | NO | Description |
| MHCAGN_GeneralPhone | varchar |  |  | SI | GeneralPhone |
| MHCAGN_Hospital_DR | bigint |  | FK | SI | Des Ref CTHospital |
| MHCAGN_OtherPhone | varchar |  |  | SI | OtherPhone |
| MHCAGN_Owner | varchar |  |  | SI | Owner |
| MHCAGN_PostCode_DR | bigint |  | FK | SI | Des Ref CTZip |
| MHCAGN_UpdatedDate | date |  |  | SI | Updated Date |
| MHCAGN_UpdatedTime | time |  |  | SI | Updated Time |
| MHCAGN_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q46Q1 | - |  |  | SI | Pulso |
| Q46Q2 | - |  |  | SI | lateralidad |
| Q46Q3 | - |  |  | SI | Hallagzos |
| Q46Q4 | - |  |  | SI | Comentarios |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*