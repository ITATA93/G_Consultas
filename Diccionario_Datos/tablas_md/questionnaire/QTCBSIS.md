# questionnaire.QTCBSIS

> Bloodstream Infection (BSI) Surveillance

**Schema:** questionnaire
**Columnas:** 76
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Bloodstream Infection (BSI) Surveillance

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Facility |
| Q02 | varchar |  |  | SI | Department |
| Q03 | varchar |  |  | SI | Admission diagnosis |
| Q04 | varchar |  |  | SI | Date admitted |
| Q05 | date |  |  | SI | Date readmitted |
| Q06 | varchar |  |  | SI | Date of discharge |
| Q07 | date |  |  | SI | Date of onset |
| Q08 | varchar |  |  | SI | Attending physician |
| Q09 | varchar |  |  | SI | Infection detected on |
| Q10 | varchar |  |  | SI | Location |
| Q11 | varchar |  |  | SI | Central line |
| Q12 | varchar |  |  | SI | Central line type |
| Q13 | varchar |  |  | SI | Central line (including umbilical catheter) |
| Q14 | numeric |  |  | SI | Birth weight (g) |
| Q15 | varchar |  |  | SI | Reason for device insertion |
| Q16 | varchar |  |  | SI | Location of device Insertion |
| Q16ObsDR | varchar |  | FK | SI | Location of device Insertion DR |
| Q17 | varchar |  |  | SI | Hemodialysis catheter present |
| Q18 | date |  |  | SI | Date of device insertion |
| Q19 | date |  |  | SI | Date device removed |
| Q20 | varchar |  |  | SI | Event details |
| Q21 | varchar |  |  | SI | Criteria used |
| Q22 | varchar |  |  | SI | Any patient |
| Q23 | varchar |  |  | SI | ≤ 1 year old |
| Q24 | varchar |  |  | SI | Laboratory |
| Q25 | varchar |  |  | SI | Clinical diagnosis |
| Q26 | varchar |  |  | SI | Pathogens identified |
| Q27 | varchar |  |  | SI | Patient status |
| Q28 | varchar |  |  | SI | HAI confirmed by the attending physician |
| Q29 | varchar |  |  | SI | Investigation |
| Q30 | varchar |  |  | SI | • Bloodstream infection is a serious infection req... |
| Q31 | varchar |  |  | SI | • Bloodstream Infection Surveillance allows clinic... |
| Q32 | varchar |  |  | SI | • The questionnaire allows documentation of when t... |
| Q33 | date |  |  | SI | Date |
| Q34 | time |  |  | SI | Time |
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