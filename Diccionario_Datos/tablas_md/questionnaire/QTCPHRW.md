# questionnaire.QTCPHRW

> Pharmacist Review

**Schema:** questionnaire
**Columnas:** 75
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Pharmacist Review

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date |  |  | SI | Date |
| Q02 | time |  |  | SI | Time |
| Q03 | varchar |  |  | SI | Medication usually managed by |
| Q04 | varchar |  |  | SI | If other specify |
| Q05 | varchar |  |  | SI | Preferred administration method? |
| Q06 | varchar |  |  | SI | If other specify |
| Q07 | varchar |  |  | SI | Did the patient bring own medicines? |
| Q08 | varchar |  |  | SI | Location of own medicines |
| Q09 | varchar |  |  | SI | Patient's immunisation up to date? |
| Q10 | varchar |  |  | SI | Community pharmacy details |
| Q11 | varchar |  |  | SI | General practitioner details |
| Q12 | varchar |  |  | SI | Level of independence |
| Q13 | varchar |  |  | SI | Lives alone |
| Q14 | varchar |  |  | SI | Lives in residential care facility |
| Q15 | varchar |  |  | SI | Residential care facility details |
| Q16 | varchar |  |  | SI | Uses dose administration device? |
| Q17 | varchar |  |  | SI | Administration device |
| Q18 | varchar |  |  | SI | Uses a dose administration aid? |
| Q19 | varchar |  |  | SI | Dose administration aid |
| Q20 | varchar |  |  | SI | Uses a medication list? |
| Q21 | varchar |  |  | SI | Swallowing issues |
| Q22 | varchar |  |  | SI | Impairment(s) |
| Q23 | varchar |  |  | SI | Other information |
| Q24 | varchar |  |  | SI | Patient Assessment |
| Q25 | varchar |  |  | SI | Can read / comprehend labels? |
| Q26 | varchar |  |  | SI | Can understand english? |
| Q27 | varchar |  |  | SI | Language spoken |
| Q28 | varchar |  |  | SI | Can open bottles? |
| Q29 | varchar |  |  | SI | Can measure liquids? |
| Q30 | varchar |  |  | SI | Recent home medicines review? |
| Q31 | date |  |  | SI | Home medicines review date |
| Q32 | varchar |  |  | SI | Supply medication list on discharge? |
| Q33 | varchar |  |  | SI | Suspected non-adherence? |
| Q34 | varchar |  |  | SI | Other information |
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