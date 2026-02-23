# SQLUser.LBC_Facility

**Schema:** SQLUser
**Columnas:** 48
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Laboratorio**. Parámetros del módulo de laboratorio.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBCFAC_RowID | bigint | PK |  | NO | - |
| LBCFAC_AccountNumber | varchar |  |  | SI | Facility Account Number |
| LBCFAC_Address1 | varchar |  |  | SI | Postal Address |
| LBCFAC_Address2 | varchar |  |  | SI | Address Line 2 |
| LBCFAC_CityCode_DR | bigint |  | FK | SI | City |
| LBCFAC_Code | varchar |  |  | NO | Code |
| LBCFAC_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| LBCFAC_ConfidentalFax | varchar |  |  | SI | Primary Contact Confidental fax |
| LBCFAC_ContactAccNo | varchar |  |  | SI | Primary Contact Account Number |
| LBCFAC_ContactFirstName | varchar |  |  | SI | Primary Contact First Name |
| LBCFAC_ContactSurname | varchar |  |  | SI | Primary Contact Surname |
| LBCFAC_ContactTitle_DR | bigint |  | FK | SI | Primary Contact Title |
| LBCFAC_Country_DR | bigint |  | FK | SI | Country |
| LBCFAC_CountyParish_DR | bigint |  | FK | SI | County/Parish |
| LBCFAC_CreatedDate | date |  |  | SI | Created Date |
| LBCFAC_CreatedTime | time |  |  | SI | Created Time |
| LBCFAC_CreatedUser_DR | bigint |  | FK | SI | Created User |
| LBCFAC_DateFrom | date |  |  | SI | From Date |
| LBCFAC_DateTo | date |  |  | SI | To Date |
| LBCFAC_Desc | varchar |  |  | NO | Description |
| LBCFAC_Email | varchar |  |  | SI | Primary Contact email |
| LBCFAC_FacilityDistrict | varchar |  |  | SI | Facility District |
| LBCFAC_FacilityType_DR | bigint |  | FK | SI | Facility Type |
| LBCFAC_Fax | varchar |  |  | SI | Primary Contact fax |
| LBCFAC_HomePhone | varchar |  |  | SI | Primary Contact Home Phone |
| LBCFAC_Latitude | varchar |  |  | SI | Facility Latitude |
| LBCFAC_Longitude | varchar |  |  | SI | Facility Longitude |
| LBCFAC_MobilePhone | varchar |  |  | SI | Primary Contact mobile phone |
| LBCFAC_Owner | varchar |  |  | SI | Owner |
| LBCFAC_PhysicalAddress | varchar |  |  | SI | Physical Address (may be different from postal add... |
| LBCFAC_PhysicalAddress1 | varchar |  |  | SI | Physical Postal Address |
| LBCFAC_PhysicalAddress2 | varchar |  |  | SI | Physical Address Line 2 |
| LBCFAC_PhysicalCity_DR | bigint |  | FK | SI | Physical City |
| LBCFAC_PhysicalCountry_DR | bigint |  | FK | SI | Physical Country |
| LBCFAC_PhysicalCountyParish_DR | bigint |  | FK | SI | Physical County/Parish |
| LBCFAC_PhysicalLatitude | varchar |  |  | SI | Physical Latitude |
| LBCFAC_PhysicalLongitude | varchar |  |  | SI | Physical Longitude |
| LBCFAC_PhysicalProvince_DR | bigint |  | FK | SI | Physical Province |
| LBCFAC_PhysicalZip_DR | bigint |  | FK | SI | Physical Postal Code |
| LBCFAC_StateCode_DR | bigint |  | FK | SI | State |
| LBCFAC_SubjectType | varchar |  |  | SI | Subject Type Restriction |
| LBCFAC_UpdatedDate | date |  |  | SI | Updated Date |
| LBCFAC_UpdatedTime | time |  |  | SI | Updated Time |
| LBCFAC_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| LBCFAC_UsePhysicalAddress | varchar |  |  | SI | Use Physical Address |
| LBCFAC_Zip_DR | bigint |  | FK | SI | Zip Code |
| Q37Q1 | - |  |  | SI | 01 |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*