# questionnaire.QTCBR

> Monitoreo de la calidad clínica

**Schema:** questionnaire
**Columnas:** 87
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Monitoreo de la calidad clínica

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Has a diagnosis recorded |
| Q02 | varchar |  |  | SI | Diagnosis type |
| Q03 | varchar |  |  | SI | Has allergy recorded (includes nil known) - patien... |
| Q04 | varchar |  |  | SI | Has patient alert recorded |
| Q05 | varchar |  |  | SI | Has a problem recorded |
| Q06 | varchar |  |  | SI | Has a family history recorded |
| Q07 | varchar |  |  | SI | Has a current condition recorded |
| Q08 | varchar |  |  | SI | Has a past condition recorded |
| Q09 | varchar |  |  | SI | Has a medication history recorded |
| Q10 | varchar |  |  | SI | Has a surgical history recorded |
| Q11 | varchar |  |  | SI | Has social history recorded |
| Q12 | varchar |  |  | SI | Has at least one clinical note |
| Q13 | varchar |  |  | SI | Clinical note care provider type |
| Q14 | varchar |  |  | SI | Has at least one observation recorded |
| Q15 | varchar |  |  | SI | Observations within one hour of admission or arriv... |
| Q16 | varchar |  |  | SI | Has at least one active clinical note (ACN) entry |
| Q17 | varchar |  |  | SI | ACN Entry by care provider type |
| Q18 | varchar |  |  | SI | Has at least one order placed |
| Q19 | varchar |  |  | SI | Orders by category |
| Q20 | varchar |  |  | SI | Orders by care provider |
| Q21 | varchar |  |  | SI | Order alerts overriden (excluding duplication) |
| Q22 | varchar |  |  | SI | Duplication alerts overriden |
| Q23 | varchar |  |  | SI | Order alerts by severity |
| Q24 | varchar |  |  | SI | Has scanned document attached |
| Q25 | varchar |  |  | SI | Fall risk assessment completed |
| Q26 | varchar |  |  | SI | VTE risk assessment completed |
| Q27 | varchar |  |  | SI | Nutrition screening assessment completed |
| Q28 | varchar |  |  | SI | Patient safety incident completed |
| Q29 | varchar |  |  | SI | Patient safety incident type |
| Q30 | varchar |  |  | SI | Pain assessment completed |
| Q31 | varchar |  |  | SI | Braden assessment completed (Adults) |
| Q32 | varchar |  |  | SI | Braden assessment completed (Child) |
| Q33 | varchar |  |  | SI | Braden severity |
| Q34 | varchar |  |  | SI | Waterlow assessment completed |
| Q35 | varchar |  |  | SI | Waterlow assessment severity |
| Q36 | varchar |  |  | SI | Central line bundle checklist completed |
| Q37 | varchar |  |  | SI | Catheter insertion bundle checklist completed |
| Q38 | varchar |  |  | SI | Ventilator acquired pneumonia checklist completed |
| Q39 | varchar |  |  | SI | Other bundle |
| Q40 | varchar |  |  | SI | Review of systems completed |
| Q41 | varchar |  |  | SI | Physical exam completed |
| Q42 | varchar |  |  | SI | Clinical pathway initiated	 |
| Q43 | varchar |  |  | SI | Nursing care plans initiated |
| Q44 | varchar |  |  | SI | Discharge summary  completed |
| Q45 | varchar |  |  | SI | Handover completed(at least one) |
| Q46 | varchar |  |  | SI | The Benefits realisation questionnaire is created ... |
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