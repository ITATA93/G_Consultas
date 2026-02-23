# questionnaire.QTCCBRS

> Child Behavior Rating Scale

**Schema:** questionnaire
**Columnas:** 71
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Child Behavior Rating Scale

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Father / Mother's name |
| Q02 | varchar |  |  | SI | This scale enables you to indicate the kinds of pr... |
| Q03 | varchar |  |  | SI | My child wets the bed |
| Q04 | varchar |  |  | SI | My child hits other children |
| Q05 | varchar |  |  | SI | My child runs away from home |
| Q06 | varchar |  |  | SI | My child disobeys me |
| Q07 | varchar |  |  | SI | My child tells lies |
| Q08 | varchar |  |  | SI | My child steals things from others |
| Q09 | varchar |  |  | SI | My child screams very loudly |
| Q10 | varchar |  |  | SI | My child bites other children |
| Q11 | varchar |  |  | SI | My child hits me when I try to administer discipli... |
| Q12 | varchar |  |  | SI | My child demands constant attention |
| Q13 | varchar |  |  | SI | My child is afraid of other children |
| Q14 | varchar |  |  | SI | My child is afraid of strangers |
| Q15 | varchar |  |  | SI | My child has nightmare |
| Q16 | varchar |  |  | SI | My child misbehaves when we go out |
| Q17 | varchar |  |  | SI | My child will not let me out of his or her sight |
| Q18 | varchar |  |  | SI | My child is very timid or shy |
| Q19 | varchar |  |  | SI | My child is destructive |
| Q20 | varchar |  |  | SI | My child has temper tantrums |
| Q21 | varchar |  |  | SI | My child has accidents or gets hurt |
| Q22 | varchar |  |  | SI | My child bangs his or her head or engages in other... |
| Q23 | longvarbinary |  |  | SI | Physician signature |
| Q23UDt | date |  |  | SI | Physician signature Last Updated Date |
| Q23UTm | time |  |  | SI | Physician signature Last Updated Time |
| Q24 | varchar |  |  | SI | 19 - 38: Potential behavioral anomalies |
| Q25 | varchar |  |  | SI | 39 - 76: Behavioral anomalies |
| Q26 | varchar |  |  | SI | 77 - 100: Critical behavioral anomalies |
| Q27 | date |  |  | SI | Date |
| Q28 | time |  |  | SI | Time |
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