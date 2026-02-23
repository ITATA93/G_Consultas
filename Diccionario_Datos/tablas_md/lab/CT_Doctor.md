# lab.CT_Doctor

**Schema:** lab
**Columnas:** 68
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de configuración**. Tabla de referencia del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CTDR_RowId | varchar | PK |  | NO | - |
| CTDR_ALPHAUPExtraName_1 | varchar |  |  | SI | ALPHAUP ExtraName_1 |
| CTDR_ALPHAUPExtraName_2 | varchar |  |  | SI | ALPHAUP ExtraName_2 |
| CTDR_ALPHAUPExtraName_3 | varchar |  |  | SI | ALPHAUP ExtraName_3 |
| CTDR_ALPHAUPGivenName | varchar |  |  | SI | ALPHAUP Given Name |
| CTDR_ALPHAUPProviderNumber | varchar |  |  | SI | ALPHAUP ProviderNumber |
| CTDR_ALPHAUPSurname | varchar |  |  | NO | ALPHAUP Surname |
| CTDR_ActiveFlag | varchar |  |  | SI | Active Flag |
| CTDR_Address | varchar |  |  | SI | Address |
| CTDR_Address1 | varchar |  |  | SI | Address 1 |
| CTDR_Address2 | varchar |  |  | SI | Address 2 |
| CTDR_Address3_Suburb | varchar |  |  | SI | Suburb |
| CTDR_Address4_State | varchar |  |  | SI | State |
| CTDR_Address5_PostCode | varchar |  |  | SI | PostCode |
| CTDR_AutoAuth | varchar |  |  | SI | Auto Authorise |
| CTDR_Client_DR | varchar |  | FK | SI | Client DR |
| CTDR_Code | varchar |  |  | NO | Code |
| CTDR_Comment | varchar |  |  | SI | Comment |
| CTDR_Company_DR | varchar |  | FK | SI | Des Ref Company |
| CTDR_CopyToOnly | varchar |  |  | SI | Copy To Only |
| CTDR_CourierRun_DR | varchar |  | FK | SI | Courier Run |
| CTDR_Cummulative | varchar |  |  | SI | Cummulative |
| CTDR_DefaultBillingLocation_DR | varchar |  | FK | SI | Default Billing Location DR |
| CTDR_DefaultBillingName_DR | varchar |  | FK | SI | Default Billing Name DR |
| CTDR_DefaultCollCentre_DR | varchar |  | FK | SI | Default Collection Centre DR |
| CTDR_DefaultInitCode_DR | varchar |  | FK | SI | Default Initiation Code DR |
| CTDR_DefaultPaymentCode_DR | varchar |  | FK | SI | Default Payment Code DR |
| CTDR_DischargeSummaryDR | varchar |  | FK | SI | Discharge Summary Doctors Reports |
| CTDR_EDIEnabled | varchar |  |  | SI | EDI Enabled |
| CTDR_EDI_Results | varchar |  |  | SI | EDI Results |
| CTDR_EDI_TypeDemographics | varchar |  |  | SI | EDI Type Demographics |
| CTDR_EDI_TypeResults | varchar |  |  | SI | EDI Type Results |
| CTDR_ExtraName_1 | varchar |  |  | SI | Extra Name 1 |
| CTDR_ExtraName_2 | varchar |  |  | SI | Extra Name 2 |
| CTDR_ExtraName_3 | varchar |  |  | SI | Extra Name 3 |
| CTDR_Fax | varchar |  |  | SI | Fax |
| CTDR_FaxEnabled | varchar |  |  | SI | Fax Enabled |
| CTDR_FaxFF | varchar |  |  | SI | Fax Full Final Only |
| CTDR_GivenName | varchar |  |  | SI | Given Name |
| CTDR_Language_DR | bigint |  | FK | SI | Language DR |
| CTDR_LetterReceiveToDoc | varchar |  |  | SI | Receive Letters to Doctors |
| CTDR_LetterReceiveToPat | varchar |  |  | SI | Receive Letters to Patients |
| CTDR_LicenceNumber1 | varchar |  |  | SI | Licence Number 1 |
| CTDR_LicenceNumber2 | varchar |  |  | SI | Licence Number 2 |
| CTDR_MainLocation | varchar |  |  | SI | Main Location |
| CTDR_MarketingCode_DR | varchar |  | FK | SI | Marketing Code |
| CTDR_NoOfCopies | double |  |  | SI | No Of Copies |
| CTDR_NoOfFaxedCopies | double |  |  | SI | No of Faxed Copies |
| CTDR_Phone1 | varchar |  |  | SI | Phone 1 |
| CTDR_Phone2 | varchar |  |  | SI | Phone 2 |
| CTDR_Phone3SMS | varchar |  |  | SI | Phone 3 SMS |
| CTDR_Phone4 | varchar |  |  | SI | Phone 4 |
| CTDR_Phone5 | varchar |  |  | SI | Phone 5 |
| CTDR_Phone6 | varchar |  |  | SI | Phone 6 |
| CTDR_PrintEnabled | varchar |  |  | SI | Print Enabled |
| CTDR_PrintFormat_DR | varchar |  | FK | SI | Print Format |
| CTDR_PriorityCode_DR | varchar |  | FK | SI | Des Ref Priority Code |
| CTDR_ProviderNumber | varchar |  |  | SI | Provider Number |
| CTDR_ProviderNumberOld | varchar |  |  | SI | Provider Number Old |
| CTDR_ProviderNumberOld_Date | date |  |  | SI | Provider Number Old Date |
| CTDR_RequestPad_DR | varchar |  | FK | SI | Request Pad DR |
| CTDR_SMSEnabled | varchar |  |  | SI | SMS Enabled |
| CTDR_SelfDetermined | varchar |  |  | SI | Self Determined |
| CTDR_Specialty_DR | varchar |  | FK | SI | Specialty DR |
| CTDR_StartDate | date |  |  | SI | Start Date |
| CTDR_Surname | varchar |  |  | SI | Surname |
| CTDR_Title | varchar |  |  | SI | Title |
| CTDR_UserSite_DR | varchar |  | FK | SI | User Site DR |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*