# SQLUser.PAC_RefDoctor

**Schema:** SQLUser
**Columnas:** 91
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| REFD_RowId | bigint | PK |  | NO | - |
| Q12Q1 | - |  |  | SI | Date |
| Q12Q10 | - |  |  | SI | Other Type |
| Q12Q2 | - |  |  | SI | Time |
| Q12Q3 | - |  |  | SI | Type |
| Q12Q4 | - |  |  | SI | Situation / Trigger |
| Q12Q5 | - |  |  | SI | What happened? |
| Q12Q6 | - |  |  | SI | What did you do? |
| Q12Q7 | - |  |  | SI | Behavioural outcome |
| Q12Q8 | - |  |  | SI | Notes |
| Q12Q9 | - |  |  | SI | Staff |
| QUESParRefDR | - |  |  | SI | Parent Reference |
| REFD_Account | varchar |  |  | SI | Account |
| REFD_Address | varchar |  |  | SI | Indirizo |
| REFD_Address2 | varchar |  |  | SI | Indirizo2 |
| REFD_Agency_DR | bigint |  | FK | SI | Des Ref Agency |
| REFD_Bank_DR | bigint |  | FK | SI | Des Ref Bank |
| REFD_BillGrp_DR | bigint |  | FK | SI | Des Ref BillGrp |
| REFD_BusPhone | varchar |  |  | SI | Bus Phone |
| REFD_CITY2_DR | bigint |  | FK | SI | Des Ref CITY2 |
| REFD_CITY_DR | bigint |  | FK | SI | Des Ref CITY |
| REFD_CTZIP2_DR | bigint |  | FK | SI | Des Ref CTZIP2 |
| REFD_CTZIP_DR | bigint |  | FK | SI | Des Ref CTZIP |
| REFD_CheckRefrerralLimit | double |  |  | SI | Check Refrerral Limit |
| REFD_Code | varchar |  |  | NO | Code |
| REFD_CodeTranslated | varchar |  |  | SI | Code Translated |
| REFD_ConfidentialFax | varchar |  |  | SI | Confidential Fax |
| REFD_CourierCopies | numeric |  |  | SI | Deprecated
The default number of copies of Lab Do... |
| REFD_Courier_DR | bigint |  | FK | SI | Deprecated
Courier |
| REFD_CreatedDate | date |  |  | SI | Created Date |
| REFD_CreatedTime | time |  |  | SI | Created Time |
| REFD_CreatedUser_DR | bigint |  | FK | SI | Created User |
| REFD_CumulativeEpisodes | integer |  |  | SI | Deprecated
Cumulatives Maximum Number of Episodes... |
| REFD_CumulativeOrder | varchar |  |  | SI | Deprecated
Doctors Reports Cumulative Order
The ... |
| REFD_CumulativePreference | varchar |  |  | SI | Deprecated
Doctors Reports Cumulative Preference... |
| REFD_CurrentNumberOfPatients | double |  |  | SI | CurrentNumberOfPatients |
| REFD_Date | date |  |  | SI | Data nascita |
| REFD_DateActiveFrom | date |  |  | NO | Date Active From |
| REFD_DateActiveTo | date |  |  | SI | Date Active To |
| REFD_Desc | varchar |  |  | NO | Description |
| REFD_DescTranslated | varchar |  |  | SI | Desc Translated |
| REFD_DoctorsReportsDeliverySort | varchar |  |  | SI | Deprecated
Doctors Reports Delivery Sort
The sor... |
| REFD_DoctorsReportsType | varchar |  |  | SI | Deprecated
Report Type
The ReportType to use for... |
| REFD_Email | varchar |  |  | SI | Email |
| REFD_Email2 | varchar |  |  | SI | Email2 |
| REFD_ExternalInterfaceQueue_DR | bigint |  | FK | SI | Deprecated
External Interface Queue |
| REFD_Fax | varchar |  |  | SI | Fax |
| REFD_FiscalCode1 | varchar |  |  | SI | Fiscal Code1 |
| REFD_FiscalCode2 | varchar |  |  | SI | Fiscal Code2 |
| REFD_Forename | varchar |  |  | SI | Forename |
| REFD_GraduationDate | date |  |  | SI | Graduation Date |
| REFD_GraduationPlace_DR | bigint |  | FK | SI | Des Ref City |
| REFD_Group | varchar |  |  | SI | Gruppo |
| REFD_HCA_DR | bigint |  | FK | SI | Des Ref HCA |
| REFD_HCR_DR | bigint |  | FK | SI | Des Ref HCR |
| REFD_Language_DR | bigint |  | FK | SI | Deprecated
Doctors Reports Language
The language... |
| REFD_MailingInfo | varchar |  |  | SI | Attivato |
| REFD_ManualPrint | varchar |  |  | SI | Deprecated
Manual Print
Flag to show if Doctors ... |
| REFD_MastersDate | date |  |  | SI | Masters Date |
| REFD_MastersPlace_DR | bigint |  | FK | SI | Des Ref City |
| REFD_MaximumReferralLimit | double |  |  | SI | Numero mutuati |
| REFD_MedicalCode | varchar |  |  | SI | Medical Code |
| REFD_MiddleName | varchar |  |  | SI | Middle Name |
| REFD_MobilePhone | varchar |  |  | SI | Mobile Phone |
| REFD_OrgChangeDate | date |  |  | SI | Org Change Date |
| REFD_Pager | varchar |  |  | SI | Pager |
| REFD_Phone | varchar |  |  | SI | Telefono |
| REFD_PreferredContact | varchar |  |  | SI | Preferred Contact |
| REFD_Province2_DR | bigint |  | FK | SI | Des REf Province2 |
| REFD_Province_DR | bigint |  | FK | SI | Des REf Province |
| REFD_QualificationDate | date |  |  | SI | Qualification Date |
| REFD_QualificationPlace_DR | bigint |  | FK | SI | Des Ref City |
| REFD_QuickPrint | varchar |  |  | SI | Deprecated
The default Quick-Print flag for Docto... |
| REFD_ReasonForNonConsent | varchar |  |  | SI | Reason For Non Consent |
| REFD_ReasonToFinishContract | varchar |  |  | SI | Reason To Finish Contract |
| REFD_RegNumber1 | varchar |  |  | SI | Reg Number1 |
| REFD_RegNumber2 | varchar |  |  | SI | Reg Number2 |
| REFD_RegistrDate | date |  |  | SI | Registration Date |
| REFD_ReportMode | varchar |  |  | SI | Deprecated
Report Mode |
| REFD_Specialist | varchar |  |  | SI | Specialist Flag |
| REFD_Specialty_DR | bigint |  | FK | SI | Des Ref Specialty |
| REFD_Text1 | varchar |  |  | SI | Text1 |
| REFD_Text2 | varchar |  |  | SI | Text2 |
| REFD_Title | varchar |  |  | SI | Titolo |
| REFD_Title_DR | bigint |  | FK | SI | Des Ref Title |
| REFD_Type | varchar |  |  | SI | Type |
| REFD_USSL | varchar |  |  | SI | USSL |
| REFD_UpdatedDate | date |  |  | SI | Updated Date |
| REFD_UpdatedTime | time |  |  | SI | Updated Time |
| REFD_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| REFD_ZipCode | varchar |  |  | SI | ZipCode |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*