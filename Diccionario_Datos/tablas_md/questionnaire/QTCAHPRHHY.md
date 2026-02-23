# questionnaire.QTCAHPRHHY

> Hydrotherapy Referral Form

**Schema:** questionnaire
**Columnas:** 65
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Hydrotherapy Referral Form

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Reason for referral |
| Q02 | varchar |  |  | SI | Risk Management: |
| Q03 | varchar |  |  | SI | Transfers |
| Q04 | varchar |  |  | SI | Gait |
| Q05 | varchar |  |  | SI | Gait Aid |
| Q06 | varchar |  |  | SI | Footwear |
| Q07 | varchar |  |  | SI | Weight bearing status |
| Q08 | varchar |  |  | SI | Steps |
| Q09 | varchar |  |  | SI | Hoist |
| Q10 | varchar |  |  | SI | Rails |
| Q11 | varchar |  |  | SI | Mobility in Pool |
| Q12 | varchar |  |  | SI | Assessment Notes |
| Q13 | varchar |  |  | SI | Orientation of Pool area |
| Q14 | varchar |  |  | SI | Hydrotherapy booklet provided |
| Q15 | longvarbinary |  |  | SI | Patient Signature |
| Q15UDt | date |  |  | SI | Patient Signature Last Updated Date |
| Q15UTm | time |  |  | SI | Patient Signature Last Updated Time |
| Q16 | date |  |  | SI | Patient Signature Date |
| Q17 | longvarbinary |  |  | SI | Therapist Signature |
| Q17UDt | date |  |  | SI | Therapist Signature Last Updated Date |
| Q17UTm | time |  |  | SI | Therapist Signature Last Updated Time |
| Q18 | date |  |  | SI | Therapist Signature Date |
| Q19 | varchar |  |  | SI | Care Provider |
| Q20 | varchar |  |  | SI | Communication / Cognitive / Psychosocial |
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