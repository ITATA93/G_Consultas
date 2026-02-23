# questionnaire.QTCNBDSSM

> Newborn Discharge Summary

**Schema:** questionnaire
**Columnas:** 85
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Newborn Discharge Summary

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date |  |  | SI | Date |
| Q02 | time |  |  | SI | Time |
| Q03 | numeric |  |  | SI | Gestation weeks |
| Q04 | time |  |  | SI | Time of birth |
| Q05 | varchar |  |  | SI | Delivery / Birth method |
| Q06 | numeric |  |  | SI | APGAR score 1 minute |
| Q07 | numeric |  |  | SI | APGAR score 5 minutes |
| Q08 | numeric |  |  | SI | APGAR score |
| Q09 | numeric |  |  | SI | Minutes |
| Q10 | numeric |  |  | SI | Birth length (cm) |
| Q11 | numeric |  |  | SI | Birth weight (g) |
| Q12 | numeric |  |  | SI | Birth head circumference (cm) |
| Q13 | date |  |  | SI | Maximum value of Bilirubin on |
| Q14 | numeric |  |  | SI | Maximum value of Bilirubin (mg/dL) |
| Q15 | numeric |  |  | SI | Hematocrit (%) |
| Q16 | varchar |  |  | SI | Neurological examination |
| Q17 | varchar |  |  | SI | Comment |
| Q18 | varchar |  |  | SI | Additional notes |
| Q19 | varchar |  |  | SI | The Baby Birth Details section should only be fill... |
| Q20 | varchar |  |  | SI | APGAR Score Index |
| Q21 | varchar |  |  | SI | Score |
| Q22 | varchar |  |  | SI | 0 |
| Q23 | varchar |  |  | SI | 1 |
| Q24 | varchar |  |  | SI | 2 |
| Q25 | varchar |  |  | SI | Appearance |
| Q26 | varchar |  |  | SI | Blue/Pale |
| Q27 | varchar |  |  | SI | Body pink, limbs blue |
| Q28 | varchar |  |  | SI | Pink |
| Q29 | varchar |  |  | SI | Pulse |
| Q30 | varchar |  |  | SI | Absent |
| Q31 | varchar |  |  | SI | < 100 |
| Q32 | varchar |  |  | SI | > 100 |
| Q33 | varchar |  |  | SI | Grimace |
| Q34 | varchar |  |  | SI | No response |
| Q35 | varchar |  |  | SI | Some motion |
| Q36 | varchar |  |  | SI | Cry |
| Q37 | varchar |  |  | SI | Activity |
| Q38 | varchar |  |  | SI | Limp |
| Q39 | varchar |  |  | SI | Some flexion of extremities  |
| Q40 | varchar |  |  | SI | Well flexed |
| Q41 | varchar |  |  | SI | Respiration |
| Q42 | varchar |  |  | SI | Absent |
| Q43 | varchar |  |  | SI | Weak cry |
| Q44 | varchar |  |  | SI | Good strong cry |
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