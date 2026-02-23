# questionnaire.QTCGAI20

> Geriatric Anxiety Inventory (20)

**Schema:** questionnaire
**Columnas:** 67
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Geriatric Anxiety Inventory (20)

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date |  |  | SI | Date |
| Q02 | time |  |  | SI | Time |
| Q03 | varchar |  |  | SI | Choose the best answer for how you have felt over ... |
| Q04 | varchar |  |  | SI | I worry a lot of the time |
| Q05 | varchar |  |  | SI | I find it difficult to make a decision |
| Q06 | varchar |  |  | SI | I often feel jumpy |
| Q07 | varchar |  |  | SI | I find it hard to relax |
| Q08 | varchar |  |  | SI | I often cannot enjoy things because of my worries |
| Q09 | varchar |  |  | SI | Little things bother me a lot |
| Q10 | varchar |  |  | SI | I often feel like I have butterflies in my stomach |
| Q11 | varchar |  |  | SI | I think of myself as a worrier |
| Q12 | varchar |  |  | SI | I can't help worrying about even trivial things |
| Q13 | varchar |  |  | SI | I often feel nervous |
| Q14 | varchar |  |  | SI | My own thoughts often make me anxious |
| Q15 | varchar |  |  | SI | I get an upset stomach due to my worrying |
| Q16 | varchar |  |  | SI | I think of myself as a nervous person |
| Q17 | varchar |  |  | SI | I always anticipate the worst will happen |
| Q18 | varchar |  |  | SI | I often feel shaky inside |
| Q19 | varchar |  |  | SI | I think that my worries interfere with my life |
| Q20 | varchar |  |  | SI | My worries often overwhelm me |
| Q21 | varchar |  |  | SI | I sometimes feel a great knot in my stomach |
| Q22 | varchar |  |  | SI | I miss out on things because I worry too much |
| Q23 | varchar |  |  | SI | I often feel upset |
| Q24 | varchar |  |  | SI | Total score |
| Q25 | varchar |  |  | SI | Pachana NA, Byrne GJ, Siddle H, Koloski N, Harley ... |
| Q26 | varchar |  |  | SI | The Geriatric Anxiety Inventory (GAI) is a 20-item... |
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