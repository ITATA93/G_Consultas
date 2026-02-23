# questionnaire.QTCOTPC

> Perioperative - Property Checklist

**Schema:** questionnaire
**Columnas:** 77
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Perioperative - Property Checklist

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Procedure |
| Q02 | varchar |  |  | SI | Medication with patient (e.g. patches / inhalers e... |
| Q03 | varchar |  |  | SI | Contact lenses / glasses with patient - Leaving Wa... |
| Q04 | varchar |  |  | SI | Jewellery including body piercings removed or jewe... |
| Q05 | varchar |  |  | SI | Dentures - Leaving Ward |
| Q06 | varchar |  |  | SI | Hearing aid with patient - Leaving Ward |
| Q07 | varchar |  |  | SI | Slippers - Leaving Ward |
| Q08 | varchar |  |  | SI | Medication with patient (e.g. patches / inhalers e... |
| Q09 | varchar |  |  | SI | Contact lenses / glasses with patient - Theatre Re... |
| Q10 | varchar |  |  | SI | Jewellery including body piercings removed or jewe... |
| Q11 | varchar |  |  | SI | Dentures - Theatre Reception |
| Q12 | varchar |  |  | SI | Hearing aid with patient - Theatre Reception |
| Q13 | varchar |  |  | SI | Slippers - Theatre Reception |
| Q14 | varchar |  |  | SI | Medication with patient (e.g. patches / inhalers e... |
| Q15 | varchar |  |  | SI | Contact lenses / glasses with patient - Anaestheti... |
| Q16 | varchar |  |  | SI | Jewellery including body piercings removed or jewe... |
| Q17 | varchar |  |  | SI | Dentures - Anaesthetic Room |
| Q18 | varchar |  |  | SI | Hearing aid with patient - Anaesthetic Room |
| Q19 | varchar |  |  | SI | Slippers - Anaesthetic Room |
| Q20 | varchar |  |  | SI | Medication with patient (e.g. patches / inhalers e... |
| Q21 | varchar |  |  | SI | Contact lenses / glasses with patient - Leaving Ro... |
| Q22 | varchar |  |  | SI | Jewellery including body piercings removed or jewe... |
| Q23 | varchar |  |  | SI | Dentures - Leaving Room |
| Q24 | varchar |  |  | SI | Hearing aid with patient - Leaving Room |
| Q25 | varchar |  |  | SI | Slippers - Leaving Room |
| Q26 | varchar |  |  | SI | Medication with patient (e.g. patches / inhalers e... |
| Q27 | varchar |  |  | SI | Contact lenses / glasses with patient |
| Q28 | varchar |  |  | SI | Jewellery including body piercings removed or jewe... |
| Q29 | varchar |  |  | SI | Dentures |
| Q30 | varchar |  |  | SI | Hearing aid with patient |
| Q31 | varchar |  |  | SI | Slippers |
| Q32 | varchar |  |  | SI | Leaving Ward |
| Q33 | varchar |  |  | SI | Arrival in Theatre Reception |
| Q34 | varchar |  |  | SI | Arrival in Anaesthetic Room |
| Q35 | varchar |  |  | SI | Leaving Recovery |
| Q36 | varchar |  |  | SI | Notes |
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