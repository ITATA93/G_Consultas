# SQLUser.LBDR_Episode

**Schema:** SQLUser
**Columnas:** 152
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Laboratorio DR**. Referencias de laboratorio.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBDRE_ParRef | varchar | PK |  | NO | Parent Reference LBDRRecipient DR |
| LBDRE_AdditionalBloodGroupDescs | varchar |  |  | SI | Patient Additional Blood Groups
Comma-list of Add... |
| LBDRE_Age | varchar |  |  | SI | Age
The Age of the patient at Time of Collection ... |
| LBDRE_AntibodyDescs | varchar |  |  | SI | Patient Antibodies
Comma-list of Antibody Descs ... |
| LBDRE_AuthorisedBy | varchar |  |  | SI | Authorised By
The Username (SSUSR_Name) of latest... |
| LBDRE_AuthorisedDate | varchar |  |  | SI | Authorised Date
The date (last) authorised, in ex... |
| LBDRE_AuthorisedTime | varchar |  |  | SI | Authorised Date
The time (last) authorised, in ex... |
| LBDRE_BloodGroupDesc | varchar |  |  | SI | Patient Blood Group Desc
At the time the episode ... |
| LBDRE_CCC1 | varchar |  |  | SI | CCC1 |
| LBDRE_CCC2 | varchar |  |  | SI | CCC2 |
| LBDRE_CCC3 | varchar |  |  | SI | CCC3 |
| LBDRE_CCC4 | varchar |  |  | SI | CCC4 |
| LBDRE_CCC5 | varchar |  |  | SI | CCC5 |
| LBDRE_CCC6 | varchar |  |  | SI | CCC6 |
| LBDRE_CareProvider | varchar |  |  | SI | Care Provider
The name (CTPCPDesc) of the CarePro... |
| LBDRE_ClinicalConditions | varchar |  |  | SI | Clinical Condition
A string with a comma-list of ... |
| LBDRE_ClinicalDetails | bigint |  |  | SI | Clinical Details |
| LBDRE_CollectionDate | varchar |  |  | SI | The Episode Collection Date
The Episode (Collecti... |
| LBDRE_CollectionTime | varchar |  |  | SI | The Episode Collection Time
The Episode (Collecti... |
| LBDRE_Confidential | varchar |  |  | SI | Confidential
Yes or "", translated |
| LBDRE_ConfidentialText | varchar |  |  | SI | Confidential Text
"CONFIDENTIAL" or "", translate... |
| LBDRE_ContactAccNo | varchar |  |  | SI | Contact Account Number |
| LBDRE_ContactFirstName | varchar |  |  | SI | Owner First Name |
| LBDRE_ContactSurname | varchar |  |  | SI | Contact Surname |
| LBDRE_ContactTitle | varchar |  |  | SI | Contact Title |
| LBDRE_CopyToRecipients | varchar |  |  | SI | Copy To Recipients
A list of recipients for the e... |
| LBDRE_DOB | varchar |  |  | SI | Date of Birth (as known at Time of Collection)
In... |
| LBDRE_EmailAddress | varchar |  |  | SI | Email Address |
| LBDRE_EmployeeNumber | varchar |  |  | SI | Employee Number |
| LBDRE_Episode_DR | bigint |  | FK | SI | The Episode for the Recipient |
| LBDRE_ExternalReferralFrom | varchar |  |  | SI | External Referral From
Desc of Third Party (Reffe... |
| LBDRE_ExternalReferralNumber | varchar |  |  | SI | External Referral Number |
| LBDRE_FacilityDistrict | varchar |  |  | SI | Facility District |
| LBDRE_FacilityName | varchar |  |  | SI | Facility Name |
| LBDRE_FirstName | varchar |  |  | SI | Patient Firstname (as known at Time of Collection) |
| LBDRE_FreeText1 | varchar |  |  | SI | FreeText1 |
| LBDRE_FreeText2 | varchar |  |  | SI | FreeText2 |
| LBDRE_FreeText3 | varchar |  |  | SI | FreeText3 |
| LBDRE_FreeText4 | varchar |  |  | SI | FreeText4 |
| LBDRE_FreeText5 | varchar |  |  | SI | FreeText5 |
| LBDRE_Guarantor | varchar |  |  | SI | Guarantor |
| LBDRE_HomeTelephoneNumber | varchar |  |  | SI | Home Telephone Number |
| LBDRE_Hospital | varchar |  |  | SI | Hospital
The Desc of the Hospital
The Hospital i... |
| LBDRE_LabSite | varchar |  |  | SI | Lab Site
The Desc of the Lab Site Location |
| LBDRE_LanguageID | varchar |  |  | SI | Episode Language
The ID of the language (User.SSL... |
| LBDRE_Latitude | varchar |  |  | SI | Latitude |
| LBDRE_Longitude | varchar |  |  | SI | Longitude |
| LBDRE_MRN | varchar |  |  | SI | MRN (in use at Time of Collection) |
| LBDRE_MobilePhoneNumber | varchar |  |  | SI | Mobile Phone Number |
| LBDRE_NationalID | varchar |  |  | SI | Patient NationalID
National number, e.g. NHS numb... |
| LBDRE_Number | varchar |  |  | SI | Episode Number (for readability) |
| LBDRE_NumberOfCopies | integer |  |  | SI | Number of Copies
The number of copies requested f... |
| LBDRE_OtherHospAdmNo | varchar |  |  | SI | Other Hospital Admission No |
| LBDRE_PassportNumber | varchar |  |  | SI | Passport Number |
| LBDRE_PatientAddress | varchar |  |  | SI | Patient Address  (one line)
  Street(1), City(Des... |
| LBDRE_PatientAddressCity | varchar |  |  | SI | Patient Address  (City) |
| LBDRE_PatientAddressCountry | varchar |  |  | SI | Patient Address  (Country) |
| LBDRE_PatientAddressState | varchar |  |  | SI | Patient Address  (State) |
| LBDRE_PatientAddressStreet | varchar |  |  | SI | Patient Address  (Street) |
| LBDRE_PatientAddressZip | varchar |  |  | SI | Patient Address  (Zip) |
| LBDRE_PatientLocation | varchar |  |  | SI | Patient Location
The Desc of the location of the ... |
| LBDRE_PaymentAgreement | varchar |  |  | SI | Payment Agreement Description |
| LBDRE_Payor | varchar |  |  | SI | Payor |
| LBDRE_PhysicalAddress | varchar |  |  | SI | Physical Address |
| LBDRE_Plan | varchar |  |  | SI | Plan |
| LBDRE_ReceivedDate | varchar |  |  | SI | Received Date
The received date in external (user... |
| LBDRE_ReceivedTime | varchar |  |  | SI | Received Time
The received timee in external (use... |
| LBDRE_ReportStorage_DR | bigint |  | FK | SI | Report Storage |
| LBDRE_RequestDate | varchar |  |  | SI | The Episode Request Date
The date requested, in e... |
| LBDRE_RequestTime | varchar |  |  | SI | The Episode Request Time
The time requested, in e... |
| LBDRE_RequestedBy | varchar |  |  | SI | Requested By
The name (CTPCPDesc) of the CareProv... |
| LBDRE_RequestingLocation | varchar |  |  | SI | Requesting Location |
| LBDRE_RowID | varchar |  |  | NO | - |
| LBDRE_SecondaryReferringDoctor | varchar |  |  | SI | Secondary Referring Doctor |
| LBDRE_SelfGuarantor | varchar |  |  | SI | Self Guarantor |
| LBDRE_Sex | varchar |  |  | SI | Sex (as known at Time of Collection)
Description,... |
| LBDRE_SortKey | varchar |  |  | SI | The Sortkey used to sort Lab-Episodes.
Derived by... |
| LBDRE_Species | varchar |  |  | SI | Species
Description, translated |
| LBDRE_SpeciesBreed | varchar |  |  | SI | Breed |
| LBDRE_SpecimenCodes | varchar |  |  | SI | Specimen Codes
A comma-space list of specimen Cod... |
| LBDRE_Specimens | varchar |  |  | SI | Specimens
A comma-space list of specimen Descs fo... |
| LBDRE_SubjectIdentificationNumber | varchar |  |  | SI | Subject Identification Number |
| LBDRE_SubjectName | varchar |  |  | SI | Subject Name |
| LBDRE_Surname | varchar |  |  | SI | Patient Surname (as known at Time of Collection)
... |
| LBDRE_TestsExcluded | varchar |  |  | SI | Tests Excluded
A list of TestSet codes that are e... |
| LBDRE_TestsExcludedAlt | varchar |  |  | SI | Tests Excluded - Alternate Format |
| LBDRE_TestsRequested | varchar |  |  | SI | Tests Requested
A list of TestSet codes that are ... |
| LBDRE_TestsRequestedAlt | varchar |  |  | SI | Tests Requested - Alternate Format |
| LBDRE_Trust | varchar |  |  | SI | Trust
The Desc of the active Trust
The Trust is ... |
| LBDRE_URN | varchar |  |  | SI | Patient URN |
| Q01 | - |  |  | SI | Torpe o entumecido |
| Q02 | - |  |  | SI | Acalorado |
| Q03 | - |  |  | SI | Con temblor en las piernas |
| Q04 | - |  |  | SI | Incapaz de relajarse |
| Q05 | - |  |  | SI | Con temor a que ocurra lo peor |
| Q06 | - |  |  | SI | Mareado, o que se le va la cabeza |
| Q07 | - |  |  | SI | Con latidos del corazón fuertes y acelerados |
| Q08 | - |  |  | SI | Inestable |
| Q09 | - |  |  | SI | Atemorizado o asustado |
| Q10 | - |  |  | SI | Nervioso |
| Q11 | - |  |  | SI | Con sensación de bloqueo |
| Q12 | - |  |  | SI | Con temblores en las manos |
| Q13 | - |  |  | SI | Inquieto, inseguro |
| Q14 | - |  |  | SI | Con miedo a perder el control |
| Q15 | - |  |  | SI | Con sensación de ahogo |
| Q16 | - |  |  | SI | Con temor a morir |
| Q17 | - |  |  | SI | Con miedo |
| Q18 | - |  |  | SI | Con problemas digestivos |
| Q19 | - |  |  | SI | Con desvanecimientos |
| Q20 | - |  |  | SI | Con rubor facial |
| Q21 | - |  |  | SI | Con sudores, fríos o calientes |
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
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*