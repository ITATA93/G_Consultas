# questionnaire.QCLXXGUSS

> Screening de Deglución (GUSS)

**Schema:** questionnaire
**Columnas:** 68
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Screening de Deglución (GUSS)

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | 1. Investigación Preliminar / Prueba Indirecta de ... |
| Q02 | varchar |  |  | SI | Vigilancia |
| Q03 | varchar |  |  | SI | Tos y/o carraspeo (tos voluntaria) |
| Q04 | varchar |  |  | SI | Deglución exitosa |
| Q05 | varchar |  |  | SI | Sialorrea |
| Q06 | varchar |  |  | SI | Cambios en la voz (ronca, húmeda, débil) |
| Q07 | varchar |  |  | SI | Total Preliminar |
| Q08 | varchar |  |  | SI | 2. Prueba Directa de Deglución |
| Q09 | varchar |  |  | SI | SEMISÓLIDO |
| Q10 | varchar |  |  | SI | Deglución SS |
| Q11 | varchar |  |  | SI | Tos (involuntaria) SS |
| Q12 | varchar |  |  | SI | Sialorrea SS |
| Q13 | varchar |  |  | SI | Cambios en la voz SS |
| Q14 | varchar |  |  | SI | Total Semisólido |
| Q15 | varchar |  |  | SI | LÍQUIDO |
| Q16 | varchar |  |  | SI | Deglución L |
| Q17 | varchar |  |  | SI | Tos (involuntaria) L |
| Q18 | varchar |  |  | SI | Sialorrea L |
| Q19 | varchar |  |  | SI | Cambios en la voz L |
| Q20 | varchar |  |  | SI | Total Líquido |
| Q21 | varchar |  |  | SI | SÓLIDO |
| Q22 | varchar |  |  | SI | Deglución S |
| Q23 | varchar |  |  | SI | Tos (involuntaria) S |
| Q24 | varchar |  |  | SI | Sialorrea S |
| Q25 | varchar |  |  | SI | Cambios en la voz S |
| Q26 | varchar |  |  | SI | Total Sólido |
| Q27 | date |  |  | SI | Fecha de Evaluación |
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