# questionnaire.QTCMBC

> Maternity Bereavement Checklist

**Schema:** questionnaire
**Columnas:** 93
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Maternity Bereavement Checklist

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date |  |  | SI | Date |
| Q02 | time |  |  | SI | Time |
| Q03 | varchar |  |  | SI | Clinical context |
| Q04 | varchar |  |  | SI | Social worker contacted |
| Q05 | varchar |  |  | SI | Notes |
| Q06 | varchar |  |  | SI | Dummy1 |
| Q07 | varchar |  |  | SI | Dummy2 |
| Q08 | varchar |  |  | SI | Chaplain / Religious delegate contacted |
| Q09 | varchar |  |  | SI | Notes |
| Q10 | varchar |  |  | SI | Clinical photographs |
| Q11 | varchar |  |  | SI | Notes |
| Q12 | varchar |  |  | SI | Consent for clinical photos, if applicable |
| Q13 | varchar |  |  | SI | Notes |
| Q14 | varchar |  |  | SI | Parent's wishes |
| Q15 | varchar |  |  | SI | Notes |
| Q16 | varchar |  |  | SI | Memento photographs downloaded to USB |
| Q17 | varchar |  |  | SI | Notes |
| Q18 | varchar |  |  | SI | USB given to parents |
| Q19 | varchar |  |  | SI | Notes |
| Q20 | varchar |  |  | SI | Memory booklet |
| Q21 | varchar |  |  | SI | Notes |
| Q22 | varchar |  |  | SI | Follow up organised |
| Q23 | varchar |  |  | SI | Follow up details |
| Q24 | varchar |  |  | SI | Additional notes |
| Q25 | varchar |  |  | SI | Stillbirth |
| Q26 | varchar |  |  | SI | Discussion with parents |
| Q27 | varchar |  |  | SI | Notes |
| Q28 | varchar |  |  | SI | Midwifery care and documentation |
| Q29 | varchar |  |  | SI | Notes |
| Q30 | varchar |  |  | SI | Medical officer responsibilities |
| Q31 | varchar |  |  | SI | Additional notes |
| Q32 | varchar |  |  | SI | Neonatal Death |
| Q33 | varchar |  |  | SI | Discussion with parents |
| Q34 | varchar |  |  | SI | Notes |
| Q35 | varchar |  |  | SI | Midwifery care and documentation |
| Q36 | varchar |  |  | SI | Notes |
| Q37 | varchar |  |  | SI | Medical officer responsibilities |
| Q38 | varchar |  |  | SI | Additional notes |
| Q39 | varchar |  |  | SI | Second Trimester Termination (Registerable) |
| Q40 | varchar |  |  | SI | Discussion with parents |
| Q41 | varchar |  |  | SI | Notes |
| Q42 | varchar |  |  | SI | Midwifery care and documentation |
| Q43 | varchar |  |  | SI | Midwifery care and documentation notes |
| Q44 | varchar |  |  | SI | Medical officer responsibilities |
| Q45 | varchar |  |  | SI | Additional notes |
| Q46 | varchar |  |  | SI | Second Trimester Miscarriage / Termination (Non-Re... |
| Q47 | varchar |  |  | SI | Discussion with parents |
| Q48 | varchar |  |  | SI | Notes |
| Q49 | varchar |  |  | SI | Midwifery care and documentation |
| Q50 | varchar |  |  | SI | Notes |
| Q51 | varchar |  |  | SI | Medical officer responsibilities |
| Q52 | varchar |  |  | SI | Additional notes |
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