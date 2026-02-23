# SQLUser.PAC_RefDoctorClinic

**Schema:** SQLUser
**Columnas:** 119
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CLN_ParRef | bigint | PK |  | NO | PAC_RefDoctor Parent Reference |
| CLN_Address1 | varchar |  |  | SI | Address 1 |
| CLN_Address2 | varchar |  |  | SI | Address2 |
| CLN_Alias | varchar |  |  | SI | Alias |
| CLN_BusPhone | varchar |  |  | SI | Business Phone |
| CLN_Childsub | double |  |  | NO | Childsub |
| CLN_City_DR | bigint |  | FK | SI | Des Ref City |
| CLN_Clinic_DR | bigint |  | FK | SI | Des Ref Clinic |
| CLN_Code | varchar |  |  | SI | Code |
| CLN_ConfidentialFax | varchar |  |  | SI | Confidential Fax |
| CLN_CreatedDate | date |  |  | SI | Created Date |
| CLN_CreatedTime | time |  |  | SI | Created Time |
| CLN_CreatedUser_DR | bigint |  | FK | SI | Created User |
| CLN_DateFrom | date |  |  | SI | Date From |
| CLN_DateTo | date |  |  | SI | Date To |
| CLN_DefaultSend | varchar |  |  | SI | Default Send |
| CLN_Email | varchar |  |  | SI | Email |
| CLN_Fax | varchar |  |  | SI | Fax |
| CLN_Location | varchar |  |  | SI | Location text |
| CLN_MobPhone | varchar |  |  | SI | Mob Phone |
| CLN_Phone | varchar |  |  | SI | Phone |
| CLN_PreferredContact | varchar |  |  | SI | Preferred Contact |
| CLN_ProviderNo | varchar |  |  | SI | ProviderNo |
| CLN_RowId | varchar |  |  | NO | - |
| CLN_System | varchar |  |  | SI | System |
| CLN_Text1 | varchar |  |  | SI | Text1 |
| CLN_Text2 | varchar |  |  | SI | Text2 |
| CLN_UpdatedDate | date |  |  | SI | Updated Date |
| CLN_UpdatedTime | time |  |  | SI | Updated Time |
| CLN_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| CLN_VEMD | varchar |  |  | SI | VEMD |
| CLN_Zip_DR | bigint |  | FK | SI | Des Ref Zip |
| ChildQ38DR | - |  |  | SI | Child Reference: Meal consumption |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | Has the patient tried to get out of bed and / or c... |
| Q04 | - |  |  | SI | Number of times |
| Q05 | - |  |  | SI | Comments |
| Q06 | - |  |  | SI | Did the patient try to remove any of their lines /... |
| Q07 | - |  |  | SI | Number of times |
| Q08 | - |  |  | SI | Comments |
| Q09 | - |  |  | SI | Has the patient tried to wander away from their wa... |
| Q10 | - |  |  | SI | Number of times |
| Q11 | - |  |  | SI | Comments |
| Q12 | - |  |  | SI | Has the patient been aggressive? |
| Q13 | - |  |  | SI | Number of times |
| Q14 | - |  |  | SI | Comments |
| Q15 | - |  |  | SI | Has nurse / security help been required for the pa... |
| Q16 | - |  |  | SI | Number of times |
| Q17 | - |  |  | SI | Comments |
| Q18 | - |  |  | SI | Additional behavioural notes |
| Q19 | - |  |  | SI | Has the patient complained of pain? |
| Q20 | - |  |  | SI | Number of times |
| Q21 | - |  |  | SI | Nurse informed about patient's pain? |
| Q22 | - |  |  | SI | Comments |
| Q23 | - |  |  | SI | Have any pressure areas (red areas) been seen on t... |
| Q24 | - |  |  | SI | Has nurse has been informed about the presence and... |
| Q25 | - |  |  | SI | Comments |
| Q26 | - |  |  | SI | Has the patient complained of pain / burning when ... |
| Q27 | - |  |  | SI | Number of times |
| Q28 | - |  |  | SI | Nurse informed about pain during urination? |
| Q29 | - |  |  | SI | Comments |
| Q30 | - |  |  | SI | Does the urine smell bad / offensive? |
| Q31 | - |  |  | SI | Number of times |
| Q32 | - |  |  | SI | Comments |
| Q33 | - |  |  | SI | Nurse informed about offensive urinary odour? |
| Q34 | - |  |  | SI | Has the patient opened their bowels? |
| Q35 | - |  |  | SI | Number of times |
| Q36 | - |  |  | SI | Comments |
| Q37 | - |  |  | SI | Additional observation notes |
| Q39 | - |  |  | SI | Additional notes about the shift |
| Q40 | - |  |  | SI | It is important that you (the PCA) tell the nurse ... |
| Q41 | - |  |  | SI | • Patient had a fall |
| Q42 | - |  |  | SI | • Pulled out their lines / drains / tubes |
| Q43 | - |  |  | SI | • Becomes more or less confused / sleepier / had d... |
| Q44 | - |  |  | SI | Please document anything unusual that has happened... |
| Q45 | - |  |  | SI | • Patient's likes / dislikes |
| Q46 | - |  |  | SI | • What makes the patient aggressive |
| Q47 | - |  |  | SI | • What settles the patient |
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