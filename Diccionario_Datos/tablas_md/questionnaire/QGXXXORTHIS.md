# questionnaire.QGXXXORTHIS

> Orthopedic History

**Schema:** questionnaire
**Columnas:** 82
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Orthopedic History

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Mechanism |
| Q01N | varchar |  |  | SI | Note |
| Q02 | varchar |  |  | SI | Describe injury |
| Q02N | varchar |  |  | SI | Note |
| Q03 | varchar |  |  | SI | Neck pain / injury |
| Q03N | varchar |  |  | SI | Note |
| Q04 | varchar |  |  | SI | Shouder pain / injury |
| Q04N | varchar |  |  | SI | Note |
| Q05 | varchar |  |  | SI | Upper arm pain / injury |
| Q05N | varchar |  |  | SI | Note |
| Q06 | varchar |  |  | SI | Elbow pain / injury |
| Q06N | varchar |  |  | SI | Note |
| Q07 | varchar |  |  | SI | Forearm pain / injury |
| Q07N | varchar |  |  | SI | Note |
| Q08 | varchar |  |  | SI | Hand or wrist pain / injury |
| Q08N | varchar |  |  | SI | Note |
| Q09 | varchar |  |  | SI | Hip / proximal femur pain / injury |
| Q09N | varchar |  |  | SI | Note |
| Q09Y | varchar |  |  | SI | If yes |
| Q11 | varchar |  |  | SI | Thigh and femur pain / injury |
| Q11N | varchar |  |  | SI | Note |
| Q12 | varchar |  |  | SI | Knee pain / injury |
| Q12N | varchar |  |  | SI | Note |
| Q13 | varchar |  |  | SI | Calf / lower leg pain / injury |
| Q13N | varchar |  |  | SI | Note |
| Q14 | varchar |  |  | SI | Ankle pain / injury |
| Q14N | varchar |  |  | SI | Note |
| Q15 | varchar |  |  | SI | Foot pain / injury |
| Q15N | varchar |  |  | SI | Note |
| Q16 | varchar |  |  | SI | Lacerations or abrasions |
| Q16N | varchar |  |  | SI | Note |
| Q17 | varchar |  |  | SI | Numbness or paresthesia distal to injury |
| Q17N | varchar |  |  | SI | Note |
| Q18 | varchar |  |  | SI | Weakness distal to injury |
| Q18N | varchar |  |  | SI | Note |
| Q19 | varchar |  |  | SI | Cyanosis or discolouration distal to injury |
| Q19N | varchar |  |  | SI | Note |
| Q20 | varchar |  |  | SI | Inability to grasp or lift |
| Q20N | varchar |  |  | SI | Note |
| Q21 | varchar |  |  | SI | Inability to walk or bear weight |
| Q21N | varchar |  |  | SI | Note |
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