# questionnaire.QTCWQOL

> Wound Quality of Life

**Schema:** questionnaire
**Columnas:** 64
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Wound Quality of Life

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date |  |  | SI | Date |
| Q02 | time |  |  | SI | Time |
| Q03 | varchar |  |  | SI | 1.Blome C, Baade K, Debus ES, Price P, Augustin M.... |
| Q04 | varchar |  |  | SI | Wound Repair Regen 2014;22:504–514. |
| Q05 | varchar |  |  | SI | 2. Augustin M, Baade K, Herberger K, Protz K, Goep... |
| Q06 | varchar |  |  | SI | In the last 7 days... |
| Q07 | varchar |  |  | SI | My wound hurt |
| Q08 | varchar |  |  | SI | My wound had a bad smell |
| Q09 | varchar |  |  | SI | There was a disturbing discharge from the wound |
| Q10 | varchar |  |  | SI | The wound has affected my sleep |
| Q11 | varchar |  |  | SI | The treatment of the wound has been a burden to me |
| Q12 | varchar |  |  | SI | The wound has made me unhappy |
| Q13 | varchar |  |  | SI | I have felt frustrated because the wound is taking... |
| Q14 | varchar |  |  | SI | I have worried about my wound |
| Q15 | varchar |  |  | SI | I have been afraid of the wound getting worse or o... |
| Q16 | varchar |  |  | SI | I have been afraid of knocking the wound |
| Q17 | varchar |  |  | SI | I have had trouble moving about because of the wou... |
| Q18 | varchar |  |  | SI | Climbing stairs has been difficult because of the ... |
| Q19 | varchar |  |  | SI | I have had trouble with day-to-day activities beca... |
| Q20 | varchar |  |  | SI | The wound has limited my leisure activities |
| Q21 | varchar |  |  | SI | The wound has forced me to limit my activities wit... |
| Q22 | varchar |  |  | SI | I have felt dependent on help from others because ... |
| Q23 | varchar |  |  | SI | The wound has been a financial burden to me |
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