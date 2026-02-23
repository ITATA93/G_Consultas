# SQLUser.LB_Subject

**Schema:** SQLUser
**Columnas:** 53
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Laboratorio**. Módulo de laboratorio clínico.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBSUB_RowID | bigint | PK |  | NO | - |
| ChildQ20DR | - |  |  | SI | Child Reference: Plan consensuado |
| LBSUB_Address1 | varchar |  |  | SI | Primary Contact Address |
| LBSUB_Address2 | varchar |  |  | SI | Primary Contact Address Line 2 |
| LBSUB_Age | varchar |  |  | SI | Age External |
| LBSUB_AgeDay | varchar |  |  | SI | Age In Day |
| LBSUB_AgeMth | varchar |  |  | SI | Age In Month |
| LBSUB_AgeYr | varchar |  |  | SI | Age In Year |
| LBSUB_BGTestSetItem_DR | varchar |  | FK | SI | Lab Enterprise Test Set Item from which the blood ... |
| LBSUB_BGUpdateDate | date |  |  | SI | Lab Blood Group Update Date |
| LBSUB_BGUpdateTime | time |  |  | SI | Lab Blood Group Update Time |
| LBSUB_BGUpdateUser_DR | bigint |  | FK | SI | Lab Blood Group Update User |
| LBSUB_BloodGroupStatus | varchar |  |  | SI | Blood Group Status |
| LBSUB_BloodGroup_DR | bigint |  | FK | SI | Blood Group |
| LBSUB_BloodProduct_DR | bigint |  | FK | SI | Blood Product
In use and required for SubjectType... |
| LBSUB_CityCode_DR | bigint |  | FK | SI | City |
| LBSUB_ConfidentalFax | varchar |  |  | SI | Primary Contact confidental fax |
| LBSUB_ContactAccNo | varchar |  |  | SI | Primary Contact Acc No |
| LBSUB_ContactFirstName | varchar |  |  | SI | Primary Contact Name |
| LBSUB_ContactSurname | varchar |  |  | SI | Primary Contact Surname |
| LBSUB_ContactTitle_DR | bigint |  | FK | SI | Primary Contact Title |
| LBSUB_Country_DR | bigint |  | FK | SI | Country |
| LBSUB_County_DR | bigint |  | FK | SI | County/Parish |
| LBSUB_Dob | date |  |  | SI | Date Of Birth |
| LBSUB_Email | varchar |  |  | SI | Primary Contact email |
| LBSUB_EstDOB | varchar |  |  | SI | Flag to indicate estimated DOB |
| LBSUB_EstDOBInFuture | varchar |  |  | SI | Flag to indicate estimated DOB |
| LBSUB_FacilityDistrict | varchar |  |  | SI | [DEPRECATED]Facility District[/DEPRECATED] |
| LBSUB_FacilityName | varchar |  |  | SI | Facility Name |
| LBSUB_Facility_DR | bigint |  | FK | SI | Facility Reference |
| LBSUB_Fax | varchar |  |  | SI | Primary Contact fax |
| LBSUB_HomePhone | varchar |  |  | SI | Primary Contact home phone |
| LBSUB_IdentificationNumber | varchar |  |  | SI | Identification Number (e.g. microchip, ear tag for... |
| LBSUB_Latitude | varchar |  |  | SI | Primary Contact latitude |
| LBSUB_Longitude | varchar |  |  | SI | Primary Contact longitude |
| LBSUB_MobilePhone | varchar |  |  | SI | Primary Contact mobile phone |
| LBSUB_Name | varchar |  |  | SI | Name |
| LBSUB_PhysicalAddress | varchar |  |  | SI | [DEPRECATED]Physical Address (may be different fro... |
| LBSUB_Sex_DR | bigint |  | FK | SI | Sex |
| LBSUB_SpeciesBreed_DR | varchar |  | FK | SI | Breed |
| LBSUB_Species_DR | bigint |  | FK | SI | Species |
| LBSUB_StateCode_DR | bigint |  | FK | SI | State |
| LBSUB_SubjectID | varchar |  |  | NO | - |
| LBSUB_SubjectType_DR | bigint |  | FK | NO | - |
| LBSUB_UseFacilityContact | varchar |  |  | SI | Use Facility Contact |
| LBSUB_Zip_DR | bigint |  | FK | SI | Zip Code |
| Q09Q1 | - |  |  | SI | Acuerdos |
| Q09Q2 | - |  |  | SI | Responsables |
| Q09Q3 | - |  |  | SI | Fecha |
| Q09Q4 | - |  |  | SI | Profesional |
| Q09Q5 | - |  |  | SI | Seguimiento del plan de intervención |
| Q09Q6 | - |  |  | SI | CESFAM |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*