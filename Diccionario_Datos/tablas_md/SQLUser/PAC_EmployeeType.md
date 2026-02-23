# SQLUser.PAC_EmployeeType

**Schema:** SQLUser
**Columnas:** 84
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Tipos/categorías disponibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| EPE_RowId | bigint | PK |  | NO | - |
| EPE_Code | varchar |  |  | NO | Code |
| EPE_CreatedDate | date |  |  | SI | Created Date |
| EPE_CreatedTime | time |  |  | SI | Created Time |
| EPE_CreatedUser_DR | bigint |  | FK | SI | Created User |
| EPE_Desc | varchar |  |  | NO | Description |
| EPE_UpdatedDate | date |  |  | SI | Updated Date |
| EPE_UpdatedTime | time |  |  | SI | Updated Time |
| EPE_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Decision to be made |
| Q02 | - |  |  | SI | Decision maker - first |
| Q03 | - |  |  | SI | Decision maker - second |
| Q04 | - |  |  | SI | When does the decision need to be made? |
| Q05 | - |  |  | SI | When does the decision need to be made? - time |
| Q06 | - |  |  | SI | Who is concerned that this patient lacks capacity? |
| Q07 | - |  |  | SI | What is their concern? |
| Q08 | - |  |  | SI | Has the patient given consent for this assessment ... |
| Q09 | - |  |  | SI | Please, give reason |
| Q10 | - |  |  | SI | Part 1 - Impairment Test |
| Q11 | - |  |  | SI | Does the patient have an impairment or disturbance... |
| Q12 | - |  |  | SI | Please, give reason |
| Q13 | - |  |  | SI | Is the impairment or disturbance: |
| Q14 | - |  |  | SI | Comment |
| Q15 | - |  |  | SI | Does the impairment or disturbance affect the pati... |
| Q16 | - |  |  | SI | Evidence |
| Q17 | - |  |  | SI | Part 2 - Functional Test |
| Q18 | - |  |  | SI | Can the patient understand the information? |
| Q19 | - |  |  | SI | Evidence |
| Q20 | - |  |  | SI | What information has been given in what format? |
| Q21 | - |  |  | SI | Confusion Assessment Method (CAM) - ICU Delirium p... |
| Q22 | - |  |  | SI | Details of sedation assessment	 |
| Q23 | - |  |  | SI | Why do you suspect the patient may lack capacity t... |
| Q24 | - |  |  | SI | Other (please specify]	 |
| Q25 | - |  |  | SI | Does the patient have an impairment or disturbance... |
| Q26 | - |  |  | SI | What is the nature of the problem is? 	 |
| Q27 | - |  |  | SI | Does patient have 	 |
| Q28 | - |  |  | SI | Details |
| Q29 | - |  |  | SI | Can the patient understand the information provide... |
| Q30 | - |  |  | SI | Can the patient weigh up the information provided?... |
| Q31 | - |  |  | SI | Can the patient retain the information?	 |
| Q32 | - |  |  | SI | Can the patient communicate their decision?	 |
| Q33 | - |  |  | SI | Please provide details to support your conclusion	 |
| Q34 | - |  |  | SI | Date |
| Q35 | - |  |  | SI | Time |
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