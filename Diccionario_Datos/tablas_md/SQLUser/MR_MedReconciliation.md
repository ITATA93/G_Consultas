# SQLUser.MR_MedReconciliation

**Schema:** SQLUser
**Columnas:** 116
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Medicamentos**. Prescripción y administración de fármacos.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| MEDREC_ParRef | bigint | PK |  | NO | MR_Adm Parent Reference |
| MEDREC_Childsub | double |  |  | NO | Childsub |
| MEDREC_Comments | varchar |  |  | SI | Comments |
| MEDREC_CommitDate | date |  |  | SI | Commit Date |
| MEDREC_CommitHospital_DR | bigint |  | FK | SI | Commit Hospital |
| MEDREC_CommitTime | time |  |  | SI | Commit Time |
| MEDREC_CommitUser_DR | bigint |  | FK | SI | Commit User |
| MEDREC_CreatedDate | date |  |  | SI | Created Date |
| MEDREC_CreatedHospital_DR | bigint |  | FK | SI | Des Ref Created Hospital |
| MEDREC_CreatedTime | time |  |  | SI | Created Time |
| MEDREC_CreatedUser_DR | bigint |  | FK | SI | Created User |
| MEDREC_Date | date |  |  | SI | Date |
| MEDREC_DischStatus | varchar |  |  | SI | Discharge Reconciliation Status |
| MEDREC_ErrorReason_DR | bigint |  | FK | SI | Des Ref Error Reason |
| MEDREC_Reason | varchar |  |  | SI | Reason for Reconciliation or Plan |
| MEDREC_RowId | varchar |  |  | NO | - |
| MEDREC_SnapshotDate | date |  |  | SI | Snapshot Date |
| MEDREC_SnapshotHospital_DR | bigint |  | FK | SI | Snapshot Hospital |
| MEDREC_SnapshotTime | time |  |  | SI | Snapshot Time |
| MEDREC_SnapshotUser_DR | bigint |  | FK | SI | Snapshot User |
| MEDREC_Status | varchar |  |  | SI | Reconciliation Status |
| MEDREC_Time | time |  |  | SI | Time |
| MEDREC_Type | varchar |  |  | SI | Type |
| MEDREC_UpdateHospital_DR | bigint |  | FK | SI | Des Ref LastUpdateHospital |
| MEDREC_User_DR | bigint |  | FK | SI | Des Ref User |
| Q01 | - |  |  | SI | Has the patient’s environment been assessed as saf... |
| Q02 | - |  |  | SI | Risk Factor |
| Q03 | - |  |  | SI | Has the patient been oriented to the ward and rout... |
| Q04 | - |  |  | SI | Has the patient had a fall in the last 12 months? |
| Q05 | - |  |  | SI | Does the patient have an altered cognitive state? |
| Q06 | - |  |  | SI | Is it acute, fluctuating or chronic? |
| Q07 | - |  |  | SI | Is the patient affected by any of the following? |
| Q08 | - |  |  | SI | Score together |
| Q09 | - |  |  | SI | Is the patient aware of their own limitations when... |
| Q10 | - |  |  | SI | Does the patient, upon observation, appear unstead... |
| Q11 | - |  |  | SI | Yes - severely unsteady (needs constant hands on a... |
| Q12 | - |  |  | SI | Is it when standing, transferring or walking? |
| Q13 | - |  |  | SI | Risk Factor |
| Q14 | - |  |  | SI | No Scoring required on this page |
| Q15 | - |  |  | SI | Is the patient affected acutely or chronically, by... |
| Q16 | - |  |  | SI | Does the patient have impaired vision, which limit... |
| Q17 | - |  |  | SI | Does the patient have impaired hearing, which limi... |
| Q18 | - |  |  | SI | Does the patient have problems with the sensation ... |
| Q19 | - |  |  | SI | Does the patient have foot problems? E.g. Corns, b... |
| Q20 | - |  |  | SI | Does the patient have communication difficulties? ... |
| Q21 | - |  |  | SI | Does the patient have intravenous therapy / idc / ... |
| Q22 | - |  |  | SI | Is the patient within 24 hours post surgery / anae... |
| Q23 | - |  |  | SI | How many medications does the patient have prescri... |
| Q24 | - |  |  | SI | Include all listed on drug chart, PRN Meds = 1 med... |
| Q25 | - |  |  | SI | Does the patient take any of the following type of... |
| Q26 | - |  |  | SI | Does the patient wear appropriate, accurate fittin... |
| Q26a | - |  |  | SI | Does the patient wear appropriate, accurate fittin... |
| Q27 | - |  |  | SI | Is the patient’s clothing too long or loose fittin... |
| Q28 | - |  |  | SI | Has the patient had a weight loss or decline in fo... |
| Q29 | - |  |  | SI | More than one response is possible, but max score ... |
| Q30 | - |  |  | SI | Does the patient, upon observation, appear unstead... |
| Q31 | - |  |  | SI | Date |
| Q32 | - |  |  | SI | 10 - 19:  Patient is at potential risk for falls |
| Q33 | - |  |  | SI | 0 - 9: Patient is NOT at potential risk for falls |
| Q34 | - |  |  | SI | The Falls Risk Assessment Tool (FRAT)  assesses th... |
| Q36 | - |  |  | SI | Score |
| Q37 | - |  |  | SI | Classification |
| Q38 | - |  |  | SI | 10 - 19 |
| Q39 | - |  |  | SI | Patient is at potential risk for falls |
| Q40 | - |  |  | SI | 0 - 9 |
| Q41 | - |  |  | SI | Patient is NOT at potential risk for falls |
| Q42 | - |  |  | SI | Is this a daycase patient? |
| Q43 | - |  |  | SI | Age 65 or over? |
| Q44 | - |  |  | SI | Age |
| Q45 | - |  |  | SI | Does the patient have a fear of falling? |
| Q46 | - |  |  | SI | Does the patient have problems with balance or fur... |
| Q47 | - |  |  | SI | Is the patient bed bound? |
| Q48 | - |  |  | SI | Does the patient have any cognitive Impairment e.g... |
| Q49 | - |  |  | SI | Has the patient tried to walk alone but unsteady /... |
| Q50 | - |  |  | SI | Are the patient or relative anxious about falls? |
| Q51 | - |  |  | SI | In your professional judgement, is the patient at ... |
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