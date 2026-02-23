# SQLUser.PA_AdmInsuranceContacts

**Schema:** SQLUser
**Columnas:** 84
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Admisión de Pacientes**. Registra episodios de atención hospitalaria.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CONTACT_ParRef | varchar | PK |  | NO | PA_AdmInsurance Parent Reference |
| CONTACT_AccountName | varchar |  |  | SI | Bank Account Name |
| CONTACT_AccountNumber | varchar |  |  | SI | Bank Account Number |
| CONTACT_Address1 | varchar |  |  | SI | Address1 |
| CONTACT_Address2 | varchar |  |  | SI | Address2 |
| CONTACT_BSBCode | varchar |  |  | SI | BSB Code |
| CONTACT_Childsub | double |  |  | NO | Childsub |
| CONTACT_City_DR | bigint |  | FK | SI | Des Ref City |
| CONTACT_ContType_DR | bigint |  | FK | SI | Des Ref ContType |
| CONTACT_Country_DR | bigint |  | FK | SI | Country |
| CONTACT_DOB | date |  |  | SI | Date Of Birth |
| CONTACT_Email | varchar |  |  | SI | Email |
| CONTACT_ForeignCity | varchar |  |  | SI | Foreign City |
| CONTACT_MedicareCardNo | varchar |  |  | SI | Medicare Card No |
| CONTACT_Name | varchar |  |  | SI | Name |
| CONTACT_Name2 | varchar |  |  | SI | Name2 |
| CONTACT_PayingShare | varchar |  |  | SI | PayingShare |
| CONTACT_Phone | varchar |  |  | SI | Phone |
| CONTACT_Province_DR | bigint |  | FK | SI | Des Ref Province |
| CONTACT_ReferenceNo | varchar |  |  | SI | Reference No |
| CONTACT_RequestCheque | varchar |  |  | SI | Request Cheque |
| CONTACT_RowId | varchar |  |  | NO | - |
| CONTACT_Sex_DR | bigint |  | FK | SI | Des Ref to CTSex |
| CONTACT_UpdateDate | date |  |  | SI | UpdateDate |
| CONTACT_UpdateTime | time |  |  | SI | UpdateTime |
| CONTACT_UpdateUserHospital_DR | bigint |  | FK | SI | Des Ref UpdateUserHospital |
| CONTACT_UpdateUser_DR | bigint |  | FK | SI | Des Ref UpdateUser |
| CONTACT_Zip_DR | bigint |  | FK | SI | Des Ref Zip |
| Q01 | - |  |  | SI | Date of test |
| Q02 | - |  |  | SI | Time of test	 |
| Q03 | - |  |  | SI | Steps - left leg	 |
| Q04 | - |  |  | SI | Steps - right leg	 |
| Q05 | - |  |  | SI | Step height (cm) |
| Q06 | - |  |  | SI | Comments	 |
| Q07 | - |  |  | SI | General Information |
| Q08 | - |  |  | SI | 1. Start timing on the word go and stop after 15 s... |
| Q09 | - |  |  | SI | 2. The score is the number of steps completed in t... |
| Q10 | - |  |  | SI | 3. Repeat the test on both legs. |
| Q11 | - |  |  | SI | 4. Demonstrate the movement prior to commencing th... |
| Q12 | - |  |  | SI | Note: Step should be 7.5cm in height |
| Q13 | - |  |  | SI | Patient Instructions |
| Q14 | - |  |  | SI | I am going to time how many times you can step up ... |
| Q15 | - |  |  | SI | My commands will be ‘ready, set, go’ and then you ... |
| Q16 | - |  |  | SI | I will keep track of the number of steps during th... |
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