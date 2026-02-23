# questionnaire.QTCIFCI

> Inpatient Functional Communication Inventory Screening

**Schema:** questionnaire
**Columnas:** 64
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Inpatient Functional Communication Inventory Screening

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Completion of this screening tool is recommended i... |
| Q02 | varchar |  |  | SI | NOTE: If the patient is non-English speaking this ... |
| Q03 | varchar |  |  | SI | Name of family member who helped gather informatio... |
| Q04 | varchar |  |  | SI | Relationship |
| Q05 | varchar |  |  | SI | Patient is able to get other people's attention, i... |
| Q06 | varchar |  |  | SI | Patient is able to inform me of what happened to b... |
| Q07 | varchar |  |  | SI | Patient is able to understand their medical condit... |
| Q08 | varchar |  |  | SI | Patient is able to understand the implications of ... |
| Q09 | varchar |  |  | SI | Patient is able to follow instructions e.g. “lean ... |
| Q10 | varchar |  |  | SI | Patient is able to express their feelings |
| Q11 | varchar |  |  | SI | Patient is able to provide information about their... |
| Q12 | varchar |  |  | SI | Patient is able to understand and remember informa... |
| Q13 | varchar |  |  | SI | Patient is able to  ask questions about their care |
| Q14 | varchar |  |  | SI | Patient is able to inform me about any medical con... |
| Q15 | varchar |  |  | SI | Patient is able to inform me of any pain or discom... |
| Q16 | varchar |  |  | SI | Patient is able to inform me of what they do or do... |
| Q17 | varchar |  |  | SI | Patient is able to call a nurse if they need to |
| Q18 | varchar |  |  | SI | Patient is able to speak without slurring their sp... |
| Q19 | varchar |  |  | SI | Any score of 1 or above : Please contact the speec... |
| Q20 | varchar |  |  | SI | Relationship |
| Q21 | varchar |  |  | SI | The Inpatient Functional Communication Inventory f... |
| Q22 | varchar |  |  | SI | Score = 0 : No speech pathologist follow-up requir... |
| Q23 | varchar |  |  | SI | Instructions |
| QUESAnaDR | varchar |  | FK | SI | Anaesthesia |
| QUESAnaOperationDR | varchar |  | FK | SI | Operation |
| QUESConsultDR | varchar |  | FK | SI | Consult |
| QUESCopiedComments | varchar |  |  | SI | Copied Comments |
| QUESCopiedDate | date |  |  | SI | Copied Date |
| QUESCopiedEpDR | bigint |  | FK | SI | Copied Episode |
| QUESCopiedSourceDR | bigint |  | FK | SI | Copied Source DR |
| QUESCopiedTime | time |  |  | SI | Copied Time |
| QUESCopiedUserDR | bigint |  | FK | SI | Copied User |
| QUESCreateDate | date |  |  | SI | Creation Date |
| QUESCreateTime | time |  |  | SI | Creation Time |
| QUESCreateUserDR | bigint |  | FK | SI | Creation User |
| QUESDate | date |  |  | SI | Last Update Date |
| QUESErrorReasonDR | bigint |  | FK | SI | Error Reason |
| QUESFHResidentDR | bigint |  | FK | SI | Resident |
| QUESMRClinicalPathWaysDR | varchar |  | FK | SI | Clinical Pathway |
| QUESNRCarePlanIssuesDR | varchar |  | FK | SI | Nurse Care Plan Issues |
| QUESOEOrdExecDR | varchar |  | FK | SI | Order Execution |
| QUESORPreanaestheticConsultDR | bigint |  | FK | SI | Preanaesthetic Consultation |
| QUESObsEntryDR | varchar |  | FK | SI | Observation Entry |
| QUESOperRoomDR | bigint |  | FK | SI | Operating Room |
| QUESPAAdmDR | bigint |  | FK | SI | Admission |
| QUESPAAdverseEventDR | varchar |  | FK | SI | Adverse Event |
| QUESPAPatMasDR | bigint |  | FK | SI | Patient |
| QUESPAPregnancyDR | bigint |  | FK | SI | Pregnancy |
| QUESPAWaitingListDR | bigint |  | FK | SI | Waiting List |
| QUESPathwayItemDR | varchar |  | FK | SI | Pathway Item |
| QUESPrePostExamOEOrdItemDR | varchar |  | FK | SI | Pre/Post Exam OrdItem |
| QUESRBAppointmentDR | varchar |  | FK | SI | Appointments |
| QUESRBApptOutcomeDR | varchar |  | FK | SI | Appointment Outcome |
| QUESRBApptSlotDR | varchar |  | FK | SI | Appointment Slot |
| QUESReasonForCorrectionDR | bigint |  | FK | SI | Reason for Correction |
| QUESSSUserDefWindowDR | bigint |  | FK | SI | Questionnaire |
| QUESScore | varchar |  |  | SI | Score |
| QUESSecondUserDR | bigint |  | FK | SI | Second Signature |
| QUESStatusDR | bigint |  | FK | SI | Status |
| QUESTextResultDR | bigint |  | FK | SI | Text Result |
| QUESTime | time |  |  | SI | Last Update Time |
| QUESTransactionDR | varchar |  | FK | SI | Transaction |
| QUESUserDR | bigint |  | FK | SI | Last Update User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*