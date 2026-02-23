# lab.CT_Hospital

**Schema:** lab
**Columnas:** 55
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de Hospital**. Configuración del establecimiento.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CTHOS_RowId | varchar | PK |  | NO | - |
| CTHOS_ActiveFlag | varchar |  |  | SI | Active Flag |
| CTHOS_Address | varchar |  |  | SI | Address |
| CTHOS_Address1 | varchar |  |  | SI | Address 1 |
| CTHOS_Address2 | varchar |  |  | SI | Address 2 |
| CTHOS_Address3_Suburb | varchar |  |  | SI | Suburb |
| CTHOS_Address4_State_DR | varchar |  | FK | SI | State |
| CTHOS_Address5_PostCode | varchar |  |  | SI | PostCode |
| CTHOS_Client_DR | varchar |  | FK | SI | Client DR |
| CTHOS_Code | varchar |  |  | NO | Code |
| CTHOS_Comments | varchar |  |  | SI | Comments |
| CTHOS_Contact | varchar |  |  | SI | Contact |
| CTHOS_CourierRun_DR | varchar |  | FK | SI | Des Ref CourierRun |
| CTHOS_Cumulative | varchar |  |  | SI | Cumulative |
| CTHOS_DefaultAccountNumber_DR | varchar |  | FK | SI | Default Account Number DR |
| CTHOS_DefaultPaymentCode_DR | varchar |  | FK | SI | Default Payment Code DR |
| CTHOS_DischargeSummaryDR | varchar |  | FK | SI | Discharge Summary Doctors Reports |
| CTHOS_DisplaySequence | numeric |  |  | SI | Display Sequence |
| CTHOS_EDIEnabled | varchar |  |  | SI | EDI Enabled |
| CTHOS_EDI_Results | varchar |  |  | SI | EDI Results |
| CTHOS_EDI_TypeDemographics | varchar |  |  | SI | EDI Type Demographics |
| CTHOS_EDI_TypeResults | varchar |  |  | SI | EDI Type Results |
| CTHOS_Fax | varchar |  |  | SI | Fax |
| CTHOS_FaxEnabled | varchar |  |  | SI | Fax Enabled |
| CTHOS_FaxFF | varchar |  |  | SI | Fax Full Final Only |
| CTHOS_FloppyFormat | varchar |  |  | SI | Floppy Format |
| CTHOS_InterimWardReportTime | numeric |  |  | SI | Interim Ward Report Time Slot |
| CTHOS_Language_DR | bigint |  | FK | SI | Language DR |
| CTHOS_Latitude | varchar |  |  | SI | Latitude |
| CTHOS_LocationType | varchar |  |  | SI | Location Type |
| CTHOS_Longitude | varchar |  |  | SI | Longitude |
| CTHOS_Name | varchar |  |  | SI | Description |
| CTHOS_NoOfCopies | numeric |  |  | SI | No Of Copies |
| CTHOS_NoOfFaxedCopies | numeric |  |  | SI | No Of Faxed Copies |
| CTHOS_PMIHospitalCode | varchar |  |  | SI | PMI Hospital Code |
| CTHOS_Phone1 | varchar |  |  | SI | Phone 1 |
| CTHOS_Phone2 | varchar |  |  | SI | Phone 2 |
| CTHOS_Phone3SMS | varchar |  |  | SI | Phone 3 SMS |
| CTHOS_Phone4 | varchar |  |  | SI | Phone 4 |
| CTHOS_Phone5 | varchar |  |  | SI | Phone 5 |
| CTHOS_Phone6 | varchar |  |  | SI | Phone 6 |
| CTHOS_PrintEnabled | varchar |  |  | SI | Print Enabled |
| CTHOS_PrintFormat_DR | varchar |  | FK | SI | Print Format |
| CTHOS_ProviderNumber | varchar |  |  | SI | Provider Number |
| CTHOS_ReferenceNumber | varchar |  |  | SI | Reference Number |
| CTHOS_SMSEnabled | varchar |  |  | SI | SMS Enabled |
| CTHOS_Specialty_DR | varchar |  | FK | SI | Specialty DR |
| CTHOS_StructuredCode | varchar |  |  | SI | Structured code |
| CTHOS_StructuredCodeLength | double |  |  | SI | Structured code length |
| CTHOS_StructuredCodeLevel | varchar |  |  | SI | Structured code level |
| CTHOS_StructuredDescription | varchar |  |  | SI | Structured Description |
| CTHOS_UserBasedPrinting | varchar |  |  | SI | User Based Printing |
| CTHOS_UserSite_DR | varchar |  | FK | SI | User Site DR |
| CTHOS_WebEnquiry_DR | varchar |  | FK | SI | Web Enquiry |
| CTHOS_email | varchar |  |  | SI | Email |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*