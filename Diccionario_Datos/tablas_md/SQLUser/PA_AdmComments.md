# SQLUser.PA_AdmComments

**Schema:** SQLUser
**Columnas:** 103
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Admisión de Pacientes**. Registra episodios de atención hospitalaria.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CMT_ParRef | bigint | PK |  | NO | PA_Adm Parent Reference |
| CMT_ARPBL_DR | bigint |  | FK | SI | Des Ref ARPBL |
| CMT_Actioned | varchar |  |  | SI | Actioned   |
| CMT_Childsub | double |  |  | NO | Childsub |
| CMT_Comments | varchar |  |  | SI | Comments |
| CMT_Date | date |  |  | SI | Date |
| CMT_DiscretOutstType_DR | bigint |  | FK | SI | Des Ref DiscretOutstType |
| CMT_FutureActionOnHold | varchar |  |  | SI | Future Action on Hold |
| CMT_FutureAction_DR | bigint |  | FK | SI | Des Ref ARCFutureAction |
| CMT_FutureDate | date |  |  | SI | Future Date |
| CMT_Hospital_DR | bigint |  | FK | SI | Des Ref Hospital |
| CMT_InvoiceOnHold | varchar |  |  | SI | Invoice On Hold |
| CMT_LastUpateDate | date |  |  | SI | LastUpateDate |
| CMT_LastUpdateHospital_DR | bigint |  | FK | SI | Des Ref LastUpdateHospital |
| CMT_LastUpdateTime | time |  |  | SI | LastUpdateTime |
| CMT_LastUpdateUser_DR | bigint |  | FK | SI | Des Ref LastUpdateUser |
| CMT_RowId | varchar |  |  | NO | - |
| CMT_Time | time |  |  | SI | Time |
| CMT_User_DR | bigint |  | FK | SI | Des Ref User |
| Q01 | - |  |  | SI | Surgical Procedure |
| Q02 | - |  |  | SI | Preparation |
| Q03 | - |  |  | SI | Pre-Operative |
| Q04 | - |  |  | SI | Intra-Operative |
| Q05 | - |  |  | SI | Post-Operative |
| Q06 | - |  |  | SI | Booked procedure |
| Q07 | - |  |  | SI | Date of procedure |
| Q08 | - |  |  | SI | Type of operation |
| Q09 | - |  |  | SI | Pre-operative chlorhexidine bath supplied |
| Q10 | - |  |  | SI | Bath taken night prior to surgery |
| Q11 | - |  |  | SI | Bath taken on the day of surgery |
| Q12 | - |  |  | SI | Prophylactic antibiotic prescribed |
| Q13 | - |  |  | SI | Comments (Preparation) |
| Q14 | - |  |  | SI | Type of hair removal |
| Q15 | - |  |  | SI | Other hair removal type |
| Q16 | - |  |  | SI | Antibiotic prophylaxis given |
| Q17 | - |  |  | SI | Given in |
| Q18 | - |  |  | SI | If not given 30-60 min before incision, give reaso... |
| Q19 | - |  |  | SI | Skin antisepsis done with |
| Q20 | - |  |  | SI | Other skin antiseptic |
| Q21 | - |  |  | SI | Type of surgery |
| Q22 | - |  |  | SI | Maintaining normothermia (>36 C) |
| Q23 | - |  |  | SI | Blood glucose level controlled |
| Q24 | - |  |  | SI | Pre-Operative comments |
| Q25 | - |  |  | SI | Intra-Operative comments |
| Q26 | - |  |  | SI | Post-Operative comments |
| Q27 | - |  |  | SI | Bundle compliance percentage |
| Q28 | - |  |  | SI | Target |
| Q29 | - |  |  | SI | Date audit completed |
| Q30 | - |  |  | SI | Infection control comments |
| Q31 | - |  |  | SI | Name of surgeon |
| Q32 | - |  |  | SI | Actual procedure |
| Q33 | - |  |  | SI | Theatre No: |
| Q34 | - |  |  | SI | Time of procedure: From |
| Q35 | - |  |  | SI | To |
| Q36 | - |  |  | SI | 30 days |
| Q37 | - |  |  | SI | 90 days |
| Q38 | - |  |  | SI | Evaluated by IC officer |
| Q39 | - |  |  | SI | Follow-up by IC officer |
| Q40 | - |  |  | SI | Temperature at end of procedure |
| Q40ObsDR | - |  |  | SI | Temperature at end of procedure DR |
| Q41 | - |  |  | SI | Date |
| Q42 | - |  |  | SI | Time |
| Q43 | - |  |  | SI | Antibiotic prophylaxis given |
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