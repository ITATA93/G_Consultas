# SQLUser.LB_Episode

**Schema:** SQLUser
**Columnas:** 225
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Laboratorio**. Módulo de laboratorio clínico.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBEP_RowID | bigint | PK |  | NO | - |
| LBEP_AccountClass_DR | bigint |  | FK | SI | Account Class |
| LBEP_Address1 | varchar |  |  | SI | Primary Contact Address |
| LBEP_Address2 | varchar |  |  | SI | Primary Contact Address 2 |
| LBEP_Age | double |  |  | SI | Age
The Age of the patient at Time of Collection ... |
| LBEP_Altitude_DR | bigint |  | FK | SI | Altitude |
| LBEP_AuthorisedBy_DR | bigint |  | FK | SI | Authorised By |
| LBEP_AuthorisedDate | date |  |  | SI | Authorised Date |
| LBEP_AuthorisedTime | time |  |  | SI | Authorised Date |
| LBEP_AuxInsType_DR | bigint |  | FK | SI | Plan |
| LBEP_BPBloodGroup_DR | bigint |  | FK | SI | Blood Group |
| LBEP_BPBloodProduct_DR | bigint |  | FK | SI | Product Code |
| LBEP_BPDonationDate | date |  |  | SI | Donation Date |
| LBEP_BPDonationTime | time |  |  | SI | Donation Time |
| LBEP_BPExpiryDate | date |  |  | SI | Expiry Date |
| LBEP_BPExpiryTime | time |  |  | SI | Expiry Time |
| LBEP_BPUnitNumber | varchar |  |  | SI | Unit / Donation Number |
| LBEP_BillTariff_DR | varchar |  | FK | SI | Billing Schedule Triff |
| LBEP_BillText1 | varchar |  |  | SI | BillText1 |
| LBEP_BillText2 | varchar |  |  | SI | BillText2 |
| LBEP_CancellationDate | date |  |  | SI | Cancellation Date  |
| LBEP_CancellationTime | time |  |  | SI | Cancellation Time |
| LBEP_CareProv_DR | varchar |  | FK | SI | Care Provider
CareProvider who placed the Order |
| LBEP_CityCode_DR | bigint |  | FK | SI | City |
| LBEP_Clinic_DR | bigint |  | FK | SI | Referring Doctor Clinic |
| LBEP_ClinicalConditions | varchar |  |  | SI | Clinical Condition
A list of any clinical conditi... |
| LBEP_ClinicalDetailsText | varchar |  |  | SI | Clinical Details Text |
| LBEP_ClinicalDetails_DR | bigint |  | FK | SI | Clinical Details 
HTMLRichText |
| LBEP_CollectionDate | date |  |  | SI | Collection Date of the episode
This will always b... |
| LBEP_CollectionTime | time |  |  | SI | Collection Time of the episode
If this is missing... |
| LBEP_ConfidentalFax | varchar |  |  | SI | Primary Contact Confidental Fax |
| LBEP_Confidential | varchar |  |  | SI | Confidential |
| LBEP_ContactAccNo | varchar |  |  | SI | Primary Contact Acc No |
| LBEP_ContactFirstName | varchar |  |  | SI | Primary Contact First Name |
| LBEP_ContactSurname | varchar |  |  | SI | Primary Contact Surname |
| LBEP_ContactTitle_DR | bigint |  | FK | SI | Primary Contact Title |
| LBEP_Country_DR | bigint |  | FK | SI | Country |
| LBEP_County_DR | bigint |  | FK | SI | County/Parish |
| LBEP_DOB | date |  |  | SI | Date of Birth (as known at Time of Collection) |
| LBEP_DVACardType_DR | bigint |  | FK | SI | DVA Card Type
From PAPMICardTypeDR User.PAPatMas |
| LBEP_DVAExpiryDate | date |  |  | SI | DVA Expiry Date
From PAPERDVAExpiryDate User.PAPe... |
| LBEP_DVANumber | varchar |  |  | SI | DVA Number
From PAPMIDVAnumber User.PAPatMas |
| LBEP_DefenceApprovalNumber | varchar |  |  | SI | Defence Approval Number |
| LBEP_Departments | varchar |  |  | SI | Test set departments of this Episode |
| LBEP_Email | varchar |  |  | SI | Primary Contact email |
| LBEP_EntryDate | date |  |  | SI | Entry Date
Date that the LBEpisode record was cre... |
| LBEP_EntryTime | time |  |  | SI | Entry Time
Time that the LBEpisode record was cre... |
| LBEP_EpisodeDate | date |  |  | SI | Calculated Episode Date (either Collection, Receiv... |
| LBEP_EpisodeGroup_DR | bigint |  | FK | SI | Episode Group |
| LBEP_EpisodeTime | time |  |  | SI | Calculated Episode Time (either Collection, Receiv... |
| LBEP_EstDOB | varchar |  |  | SI | - |
| LBEP_EthnicityList | varchar |  |  | SI | - |
| LBEP_ExpectedDeliveryDate | date |  |  | SI | Expected Delivery Date |
| LBEP_ExternalReferralFrom_DR | bigint |  | FK | SI | External Referral From |
| LBEP_ExternalReferralNumber | varchar |  |  | SI | External Referral Number |
| LBEP_FacilityDistrict | varchar |  |  | SI | [DEPRECATED]Facility District[/DEPRECATED] |
| LBEP_FacilityName | varchar |  |  | SI | Facility Name |
| LBEP_Facility_DR | bigint |  | FK | SI | Facility reference |
| LBEP_Fasting | varchar |  |  | SI | Fasting
Flag to indicate if the patient is fastin... |
| LBEP_Fax | varchar |  |  | SI | Primary Contact fax |
| LBEP_FirstName | varchar |  |  | SI | Patient Firstname (as known at Time of Collection) |
| LBEP_Guarantor_DR | varchar |  | FK | SI | Des Ref to PANok |
| LBEP_HealthFundNumber | varchar |  |  | SI | Health Fund Number
From PAPMIHealthFundNo User.PA... |
| LBEP_HealthFundUPI | varchar |  |  | SI | Health Fund UPI
From PAPMIPatientFundUPI User.PAP... |
| LBEP_HoldRemoveBy_DR | bigint |  | FK | SI | User who On Hold removed |
| LBEP_HoldRemoveDate | date |  |  | SI | Date of On Hold removed |
| LBEP_HoldRemoveTime | time |  |  | SI | Time of On Hold removed |
| LBEP_HoldSetBy_DR | bigint |  | FK | SI | User who On Hold set |
| LBEP_HoldSetDate | date |  |  | SI | Date of On Hold set |
| LBEP_HoldSetTime | time |  |  | SI | Time of On Hold set |
| LBEP_HomePhone | varchar |  |  | SI | Primary Contact home phone |
| LBEP_IndigStat_DR | bigint |  | FK | SI | Ethnicity |
| LBEP_InformedFinancialConsent | varchar |  |  | SI | Informed Financial Consent  |
| LBEP_InpatientBilling | varchar |  |  | SI | Inpatient Billing Flag
TODO: to be set or calcula... |
| LBEP_InsType_DR | bigint |  | FK | SI | Payor |
| LBEP_LabSite_DR | bigint |  | FK | SI | Lab Site
The default Received location (LabSite) ... |
| LBEP_Language_DR | bigint |  | FK | SI | Doctors Reports Language
The language in which th... |
| LBEP_Latitude | varchar |  |  | SI | Primary Contact latitude |
| LBEP_LocalFirstName | varchar |  |  | SI | Patient Local Firstname (as known at Time of Colle... |
| LBEP_LocalOtherName | varchar |  |  | SI | Patient Local Other Name (as known at Time of Coll... |
| LBEP_LocalOtherName2 | varchar |  |  | SI | Patient Local Other Name 2 (as known at Time of Co... |
| LBEP_LocalSurname | varchar |  |  | SI | Patient Local Surname (as known at Time of Collect... |
| LBEP_Longitude | varchar |  |  | SI | Primary Contact longitude |
| LBEP_MRN | varchar |  |  | SI | MRN (in use at Time of Collection) |
| LBEP_MedicareCode | varchar |  |  | SI | Medicare Reference Number 
From PAPMIMedicareCode... |
| LBEP_MedicareExpDate | date |  |  | SI | Medicare Expiry Date
From PAPMIMedicareExpDate Us... |
| LBEP_MedicareNumber | varchar |  |  | SI | Medicare Number
From PAPMIMedicare |
| LBEP_MedicareSuffix_DR | bigint |  | FK | SI | Medicare Number Suffix 
From PAPMIMedicareSuffixD... |
| LBEP_MobilePhone | varchar |  |  | SI | Primary Contact mobile phone |
| LBEP_Number | varchar |  |  | NO | Lab Episode Number  |
| LBEP_OnHold | varchar |  |  | SI | Episode On Hold From Episode Action |
| LBEP_OrderDate | date |  |  | SI | Episode Order Start Date |
| LBEP_OrderTime | time |  |  | SI | Episode Order Start Time |
| LBEP_OtherHospAdmNo | varchar |  |  | SI | Other Hospital Episode Number |
| LBEP_OtherName | varchar |  |  | SI | Patient Other Name (as known at Time of Collection... |
| LBEP_OtherName2 | varchar |  |  | SI | Patient Other Name2  (as known at Time of Collecti... |
| LBEP_OverrideClinicalConditionReason_DR | bigint |  | FK | SI | Clinical Condition Override reason |
| LBEP_PAAdm_DR | bigint |  | FK | SI | Admission
PAAdm (Admission Episode) (User.PAAdm) ... |
| LBEP_PAPERID | varchar |  |  | SI | National ID
NHS Number in UK |
| LBEP_PAPerson_DR | bigint |  | FK | SI | Patient
PAPerson (Patient) (User.PAPerson) Associ... |
| LBEP_PatType_DR | bigint |  | FK | SI | Patient Type |
| LBEP_PatientLocation_DR | bigint |  | FK | SI | Patient Location
The location of the patient at c... |
| LBEP_PatientType | varchar |  |  | SI | [DEPRECATED]The patient type for the lab episode[/... |
| LBEP_PaymentAgreement_DR | bigint |  | FK | SI | Payment Agreement |
| LBEP_PensionNumber | varchar |  |  | SI | Pension Number 
From PAPERGovernCardNo User.PAPer... |
| LBEP_PhysicalAddress | varchar |  |  | SI | [DEPRECATED]Physical Address (may be different fro... |
| LBEP_Pregnant | varchar |  |  | SI | Pregnant
Flag if the patient is known to be Pregn... |
| LBEP_PregnantNumberOfWeeks | double |  |  | SI | Number Of Weeks Pregnant<br>
If the patient is kn... |
| LBEP_Priority_DR | bigint |  | FK | SI | Priority of Episode |
| LBEP_RapidRequest | varchar |  |  | SI | Rapid Request
Y: Lab Episode is from Rapid Reques... |
| LBEP_ReasonForTesting | varchar |  |  | SI | Reason for testing |
| LBEP_ReceivedDate | date |  |  | SI | Received Date |
| LBEP_ReceivedTime | time |  |  | SI | Received Time |
| LBEP_ReferringDoctor_DR | bigint |  | FK | SI | Referring Doctor |
| LBEP_RequestDate | date |  |  | SI | Request Date |
| LBEP_RequestTime | time |  |  | SI | Request Time |
| LBEP_RequestedByType | varchar |  |  | SI | Requested By Type |
| LBEP_RequestingLocation_DR | bigint |  | FK | SI | Subject Requesting Location
The location of the s... |
| LBEP_SecondaryReferringDoctor_DR | bigint |  | FK | SI | Secondary Referring Doctor (used Environmental) |
| LBEP_SelfGuarantor | varchar |  |  | SI | Self Guarantor |
| LBEP_Sex_DR | bigint |  | FK | SI | Sex (as known at Time of Collection) |
| LBEP_SpecialHandling_DR | bigint |  | FK | SI | Special Handling Instructions |
| LBEP_SpeciesBreed_DR | varchar |  | FK | SI | Breed |
| LBEP_Species_DR | bigint |  | FK | SI | Species |
| LBEP_StateCode_DR | bigint |  | FK | SI | State |
| LBEP_Status | varchar |  |  | SI | Status |
| LBEP_StatusBilling | varchar |  |  | SI | Billing Status
TODO: to be set or calculated |
| LBEP_StatusPrinting | varchar |  |  | SI | Printing Status |
| LBEP_SubjectID | varchar |  |  | SI | Subject ID |
| LBEP_SubjectIdentificationNumber | varchar |  |  | SI | Identification Number (e.g. microchip, ear tag for... |
| LBEP_SubjectName | varchar |  |  | SI | Subject Name / Description |
| LBEP_SubjectType_DR | bigint |  | FK | SI | Subject Type |
| LBEP_Subject_DR | bigint |  | FK | SI | Subject 
Replaces the LBEP_PAAdm_DR and LBEP_PAPe... |
| LBEP_Surname | varchar |  |  | SI | Patient Surname (as known at Time of Collection) |
| LBEP_Title_DR | bigint |  | FK | SI | Patient Title (as known at Time of Collection) |
| LBEP_TrafficAccidentCommissionClaimNumber | varchar |  |  | SI | Traffic Accident Commission Claim Number |
| LBEP_UseFacilityContact | varchar |  |  | SI | Use Facility Contact |
| LBEP_User_DR | bigint |  | FK | SI | User Id
User who created the record |
| LBEP_WorkCoverClaimNumber | varchar |  |  | SI | Work Cover Claim Number |
| LBEP_Zip_DR | bigint |  | FK | SI | Zip Code |
| Q01 | - |  |  | SI | Información General de Epilepsia |
| Q02 | - |  |  | SI | ¿Que es la Epilepsia? |
| Q03 | - |  |  | SI | Causas Probables |
| Q04 | - |  |  | SI | Explicación de procedimientos investigativos |
| Q05 | - |  |  | SI | Clasificación de la crisis |
| Q06 | - |  |  | SI | Síndrome |
| Q07 | - |  |  | SI | Epidemiología |
| Q08 | - |  |  | SI | Pronóstico |
| Q09 | - |  |  | SI | Genética |
| Q10 | - |  |  | SI | Muerte súbita en epilepsia |
| Q11 | - |  |  | SI | Drogas antiepilépticas |
| Q12 | - |  |  | SI | Elección de la droga |
| Q13 | - |  |  | SI | Eficacia |
| Q14 | - |  |  | SI | Efectos colaterales |
| Q15 | - |  |  | SI | Adherencia |
| Q16 | - |  |  | SI | Interacción con las drogas |
| Q17 | - |  |  | SI | Factores Gatillantes de Crisis |
| Q18 | - |  |  | SI | Falta de Sueño |
| Q19 | - |  |  | SI | Alcohol |
| Q20 | - |  |  | SI | Stress |
| Q21 | - |  |  | SI | Fotosensibilidad |
| Q22 | - |  |  | SI | Primeros Auxilios |
| Q23 | - |  |  | SI | Guía General |
| Q24 | - |  |  | SI | Status Epiléptico |
| Q25 | - |  |  | SI | Mujer con Epilepsia |
| Q26 | - |  |  | SI | Contracepción |
| Q27 | - |  |  | SI | Pre Concepción |
| Q28 | - |  |  | SI | Embarazo y lactancia |
| Q29 | - |  |  | SI | Menopausia |
| Q30 | - |  |  | SI | Estilos de Vida |
| Q31 | - |  |  | SI | Conducción de vehículos |
| Q32 | - |  |  | SI | Empleo |
| Q33 | - |  |  | SI | Educación (por ej. Guías para profesores) |
| Q34 | - |  |  | SI | Seguridad en casa |
| Q35 | - |  |  | SI | Descanso |
| Q36 | - |  |  | SI | Vida social |
| Q37 | - |  |  | SI | Posibles Consecuencias Psicosociales |
| Q38 | - |  |  | SI | Estigma |
| Q39 | - |  |  | SI | Pérdida de la memoria |
| Q40 | - |  |  | SI | Depresión |
| Q41 | - |  |  | SI | Ansiedad |
| Q42 | - |  |  | SI | Autoestima |
| Q43 | - |  |  | SI | Dificultades sexuales |
| Q44 | - |  |  | SI | Organización y Apoyo |
| Q45 | - |  |  | SI | Direcciones y números de teléfono de organizacione... |
| QUESAnaDR | - |  |  | SI | Anaesthesia |
| QUESAnaOperationDR | - |  |  | SI | Operation |
| QUESConsultDR | - |  |  | SI | Consult |
| QUESCopiedComments | - |  |  | SI | Copied Comments |
| QUESCopiedDate | - |  |  | SI | Copied Date |
| QUESCopiedEpDR | - |  |  | SI | Copied Episode |
| QUESCopiedSourceDR | - |  |  | SI | Copied Source DR |
| QUESCopiedTime | - |  |  | SI | Copied Time |
| QUESCopiedUserDR | - |  |  | SI | Copied User |
| QUESCreateDate | - |  |  | SI | Creation Date |
| QUESCreateTime | - |  |  | SI | Creation Time |
| QUESCreateUserDR | - |  |  | SI | Creation User |
| QUESDate | - |  |  | SI | Last Update Date |
| QUESErrorReasonDR | - |  |  | SI | Error Reason |
| QUESFHResidentDR | - |  |  | SI | Resident |
| QUESMRClinicalPathWaysDR | - |  |  | SI | Clinical Pathway |
| QUESNRCarePlanIssuesDR | - |  |  | SI | Nurse Care Plan Issues |
| QUESOEOrdExecDR | - |  |  | SI | Order Execution |
| QUESORPreanaestheticConsultDR | - |  |  | SI | Preanaesthetic Consultation |
| QUESObsEntryDR | - |  |  | SI | Observation Entry |
| QUESOperRoomDR | - |  |  | SI | Operating Room |
| QUESPAAdmDR | - |  |  | SI | Admission |
| QUESPAAdverseEventDR | - |  |  | SI | Adverse Event |
| QUESPAPatMasDR | - |  |  | SI | Patient |
| QUESPAPregnancyDR | - |  |  | SI | Pregnancy |
| QUESPAWaitingListDR | - |  |  | SI | Waiting List |
| QUESPathwayItemDR | - |  |  | SI | Pathway Item |
| QUESPrePostExamOEOrdItemDR | - |  |  | SI | Pre/Post Exam OrdItem |
| QUESRBAppointmentDR | - |  |  | SI | Appointments |
| QUESRBApptOutcomeDR | - |  |  | SI | Appointment Outcome |
| QUESRBApptSlotDR | - |  |  | SI | Appointment Slot |
| QUESReasonForCorrectionDR | - |  |  | SI | Reason for Correction |
| QUESSSUserDefWindowDR | - |  |  | SI | Questionnaire |
| QUESScore | - |  |  | SI | Score |
| QUESSecondUserDR | - |  |  | SI | Second Signature |
| QUESStatusDR | - |  |  | SI | Status |
| QUESTextResultDR | - |  |  | SI | Text Result |
| QUESTime | - |  |  | SI | Last Update Time |
| QUESTransactionDR | - |  |  | SI | Transaction |
| QUESUserDR | - |  |  | SI | Last Update User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*