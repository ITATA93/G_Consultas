# questionnaire.QTCBRA

> Bed Rail Assessment

**Schema:** questionnaire
**Columnas:** 65
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Bed Rail Assessment

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Patient mobility	 |
| Q02 | varchar |  |  | SI | Patient mental state 	 |
| Q03 | varchar |  |  | SI | Bed type in use	 |
| Q04 | varchar |  |  | SI | Are bed rails required?	 |
| Q05 | varchar |  |  | SI | Rationale	 |
| Q06 | date |  |  | SI | Review date	 |
| Q07 | varchar |  |  | SI | Ensure that the appropriate use of bed rails is as... |
| Q08 | varchar |  |  | SI | Bumpers used	 |
| Q09 | varchar |  |  | SI | Has the use of bed rails been discussed 	 |
| Q10 | varchar |  |  | SI | Do bed rails click into place and are secure	 |
| Q11 | varchar |  |  | SI | Have you ensured both bed rails in use (even if ag... |
| Q12 | varchar |  |  | SI | Confirm that an overlay mattress is NOT in use	 |
| Q13 | varchar |  |  | SI | Call bell explained and in reach	 |
| Q14 | varchar |  |  | SI | Is an alternative call method required	 |
| Q15 | varchar |  |  | SI | State the alternative used	 |
| Q16 | varchar |  |  | SI | Is there sufficient space surrounding the bed to u... |
| Q17 | varchar |  |  | SI | Has the patient been assessed for care rounding	 |
| Q18 | varchar |  |  | SI | Does the patient require reasonable adjustments to... |
| Q19 | varchar |  |  | SI | Is the appropriate care plan in place	 |
| Q20 | varchar |  |  | SI | Ensure patient information leaflet is given	 |
| Q21 | varchar |  |  | SI | Ensure the need for the use of bedrails is communi... |
| Q22 | date |  |  | SI | Date of bed rail discontinuation	 |
| Q23 | varchar |  |  | SI | Please state the reason why the use of bedrails is... |
| Q24 | varchar |  |  | SI | Ensure that the appropriate use of bed rails is as... |
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