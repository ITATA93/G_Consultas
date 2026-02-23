# lab.HOS_HospitalPatients

**Schema:** lab
**Columnas:** 54
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Hospital**. Configuración del establecimiento.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| HOSP_ParRef | varchar | PK |  | NO | HOS_HospitalDataBase Parent Reference |
| HOSP_ALPHAUPDebtorNumber | varchar |  |  | SI | ALPHAUP DebtorNumber |
| HOSP_ALPHAUPGivenName | varchar |  |  | SI | ALPHAUP GivenName |
| HOSP_ALPHAUPSurname | varchar |  |  | SI | ALPHAUP Surname |
| HOSP_Address1 | varchar |  |  | SI | Address_1 |
| HOSP_Address2 | varchar |  |  | SI | Address_2 |
| HOSP_Address3_Suburb | varchar |  |  | SI | Suburb |
| HOSP_Address4_State | varchar |  |  | SI | State_DR |
| HOSP_Address5_PostCode | varchar |  |  | SI | Post Code |
| HOSP_AdmissionDate | date |  |  | SI | Admission Date |
| HOSP_AdmissionTime | time |  |  | SI | Admission Time |
| HOSP_AdmissionType | varchar |  |  | SI | Admission Type |
| HOSP_Class | varchar |  |  | SI | Patient Class |
| HOSP_DOB | date |  |  | SI | Date of Birth |
| HOSP_DeathDate | date |  |  | SI | Date of death |
| HOSP_DeathTime | time |  |  | SI | Time of death |
| HOSP_DebtorNumber | varchar |  |  | NO | Hospital Debtor Number |
| HOSP_DoctorAdmitting_DR | varchar |  | FK | SI | Admitting Doctor |
| HOSP_DoctorConsulting_DR | varchar |  | FK | SI | Consulting Doctor |
| HOSP_DoctorReferring_DR | varchar |  | FK | SI | Referring Doctor |
| HOSP_Ethnicity_DR | varchar |  | FK | SI | Ethnicity DR |
| HOSP_ExtraInfo | varchar |  |  | SI | Extra Info |
| HOSP_ExtraName_1 | varchar |  |  | SI | Extra Name - 1 |
| HOSP_ExtraName_2 | varchar |  |  | SI | Extra Name - 2 |
| HOSP_ExtraName_3 | varchar |  |  | SI | Extra Name - 3 |
| HOSP_GivenName | varchar |  |  | SI | Given Name |
| HOSP_Hospital_DR | varchar |  | FK | SI | Hospital DR |
| HOSP_IdentifierType | varchar |  |  | SI | Identifier Type |
| HOSP_LabTrakMRN | varchar |  |  | SI | LabTrak MRN |
| HOSP_ListOfSpecimens | varchar |  |  | SI | List Of Specimens |
| HOSP_ListOfTests | varchar |  |  | SI | List Of Tests |
| HOSP_Location_DR | varchar |  | FK | SI | Patient Location |
| HOSP_NHSNumberStatus | varchar |  |  | SI | NHS Number Status |
| HOSP_OperationDate | date |  |  | SI | Operation Date |
| HOSP_PatientSite_DR | varchar |  | FK | SI | Patient Site DR |
| HOSP_PaymentCode_DR | varchar |  | FK | SI | Payment Code DR |
| HOSP_PhoneHome | varchar |  |  | SI | Home Phone |
| HOSP_PhoneWork | varchar |  |  | SI | Phone Work |
| HOSP_RowID | varchar |  |  | NO | - |
| HOSP_Service | varchar |  |  | SI | Hospital Service |
| HOSP_Sex_DR | varchar |  | FK | SI | Sex |
| HOSP_SourceSystem | varchar |  |  | SI | Source System  |
| HOSP_SpecialInterest_DR | varchar |  | FK | SI | Special Interest DR |
| HOSP_Surname | varchar |  |  | SI | Surname |
| HOSP_Title_DR | varchar |  | FK | SI | Title |
| HOSP_TransDate | date |  |  | SI | Transaction Date |
| HOSP_TransTime | time |  |  | SI | Transaction Time |
| HOSP_Visit | varchar |  |  | NO | Hospital Visit Number |
| HOSP_pc_FundNumber | varchar |  |  | SI | Health Fund Number |
| HOSP_pc_FundTable | varchar |  |  | SI | Health Fund Table |
| HOSP_pc_Medicare | varchar |  |  | SI | Medicare number |
| HOSP_pc_MedicareRef | varchar |  |  | SI | Medicare Ref |
| HOSP_pc_Pensioner | varchar |  |  | SI | Pensioner |
| HOSP_pc_VA | varchar |  |  | SI | Veterans Affairs |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*