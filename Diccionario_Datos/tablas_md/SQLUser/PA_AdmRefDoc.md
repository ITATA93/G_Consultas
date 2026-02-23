# SQLUser.PA_AdmRefDoc

**Schema:** SQLUser
**Columnas:** 84
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Admisión de Pacientes**. Registra episodios de atención hospitalaria.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| REFD_ParRef | bigint | PK |  | NO | PA_Adm Parent Reference |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | Initiate |
| Q04 | - |  |  | SI | TIME |
| Q05 | - |  |  | SI | within 2 hours |
| Q06 | - |  |  | SI | Review observations |
| Q07 | - |  |  | SI | Think sepsis |
| Q08 | - |  |  | SI | Blood glucose |
| Q09 | - |  |  | SI | Medication history |
| Q10 | - |  |  | SI | Identify new medications / change of dose / medica... |
| Q11 | - |  |  | SI | Pain review (Abbey pain scale) |
| Q12 | - |  |  | SI | Alcohol history |
| Q13 | - |  |  | SI | Consider withdrawal / intoxication |
| Q14 | - |  |  | SI | Assess for urinary retention |
| Q15 | - |  |  | SI | Assess for constipation |
| Q16 | - |  |  | SI | Notes |
| Q17 | - |  |  | SI | Assess hydration and start fluid balance chart |
| Q18 | - |  |  | SI | Bloods |
| Q19 | - |  |  | SI | Full blood count, urea and electrolytes, liver fun... |
| Q20 | - |  |  | SI | Look for symptoms / signs of infection and perform... |
| Q21 | - |  |  | SI | Consider signs and symptoms: skin, chest, urine, c... |
| Q22 | - |  |  | SI | Electrocardiogram |
| Q23 | - |  |  | SI | Consider Acute Coronary Syndrome |
| Q24 | - |  |  | SI | Notes |
| Q25 | - |  |  | SI | Initiate treatment of all underlying causes found ... |
| Q26 | - |  |  | SI | Notes |
| Q27 | - |  |  | SI | Complete within 2 hours or if family / carer not p... |
| Q28 | - |  |  | SI | Engage with patient / family / carer – explore if ... |
| Q29 | - |  |  | SI | Ask: How would you like to be involved? |
| Q30 | - |  |  | SI | Explain diagnoses of delirium to patient and famil... |
| Q31 | - |  |  | SI | Document diagnosis of delirium |
| Q32 | - |  |  | SI | Notes |
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
| REFD_Childsub | double |  |  | NO | Childsub |
| REFD_Consent | varchar |  |  | SI | Consent |
| REFD_DateFrom | date |  |  | SI | Date From |
| REFD_DateTo | date |  |  | SI | DateTo |
| REFD_RefDocClinic_DR | varchar |  | FK | SI | Des Ref RefDocClinic |
| REFD_RefDoc_DR | bigint |  | FK | SI | Des Ref RefDoc |
| REFD_RowId | varchar |  |  | NO | - |
| REFD_UpdateDate | date |  |  | SI | UpdateDate |
| REFD_UpdateTime | time |  |  | SI | UpdateTime |
| REFD_UpdateUserHospital_DR | bigint |  | FK | SI | Des Ref UpdateUserHospital |
| REFD_UpdateUser_DR | bigint |  | FK | SI | Des Ref UpdateUser |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*