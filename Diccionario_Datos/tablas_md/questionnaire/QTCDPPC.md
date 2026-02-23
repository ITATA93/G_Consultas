# questionnaire.QTCDPPC

> Dying Patient Plan of Care

**Schema:** questionnaire
**Columnas:** 89
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Dying Patient Plan of Care

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date |  |  | SI | Date |
| Q02 | time |  |  | SI | Time |
| Q03 | varchar |  |  | SI | All involved parties in consensus for cessation of... |
| Q04 | varchar |  |  | SI | Religious / spiritual / cultural needs considered |
| Q05 | varchar |  |  | SI | Pastoral care brochure provided |
| Q06 | varchar |  |  | SI | Referral flowchart followed, if required |
| Q07 | varchar |  |  | SI | Social worker / Bereavement team notified or refer... |
| Q08 | varchar |  |  | SI | Bereavement information provided to family / signi... |
| Q09 | varchar |  |  | SI | Patient / Family meeting documented in medical rec... |
| Q10 | varchar |  |  | SI | Notes |
| Q11 | varchar |  |  | SI | Resuscitation record up to date |
| Q12 | varchar |  |  | SI | Donation service contacted for potential organ / c... |
| Q13 | varchar |  |  | SI | Nurse Donation Specialist (NDS) contacted to arran... |
| Q14 | varchar |  |  | SI | Organ donation process commenced |
| Q15 | varchar |  |  | SI | Notes |
| Q16 | varchar |  |  | SI | Medication prescribed for symptom control |
| Q17 | varchar |  |  | SI | Pressure care attended with consideration of press... |
| Q18 | varchar |  |  | SI | Notes |
| Q19 | varchar |  |  | SI | Bedside monitor display off |
| Q20 | varchar |  |  | SI | Ventilation ceased |
| Q21 | varchar |  |  | SI | Patient extubated |
| Q22 | varchar |  |  | SI | Oxygen therapy ceased |
| Q23 | varchar |  |  | SI | Inotropes and vasopressors ceased |
| Q24 | varchar |  |  | SI | Intravascular fluids ceased |
| Q25 | varchar |  |  | SI | Enteral feeding / Total parenteral nutrition cease... |
| Q26 | varchar |  |  | SI | Continuous renal replacement therapy ceased |
| Q27 | varchar |  |  | SI | Medications ceased (except comfort measures) |
| Q28 | varchar |  |  | SI | Active vital sign monitoring ceased |
| Q29 | varchar |  |  | SI | Implantable defibrillator deactivated |
| Q30 | varchar |  |  | SI | Unnecessary vascular access removed |
| Q31 | varchar |  |  | SI | Notes |
| Q32 | varchar |  |  | SI | Unnecessary medical equipment removed from the  ro... |
| Q33 | varchar |  |  | SI | Consideration of personalisation / ambience measur... |
| Q34 | varchar |  |  | SI | Notes |
| Q35 | varchar |  |  | SI | Palliative care referral made (patient likely to s... |
| Q36 | varchar |  |  | SI | Parent team aware of palliative plan |
| Q37 | varchar |  |  | SI | General practitioner aware of palliative plan |
| Q38 | varchar |  |  | SI | Notes |
| Q39 | varchar |  |  | SI | Coroner notified |
| Q40 | varchar |  |  | SI | Family notified of coronial referral |
| Q41 | varchar |  |  | SI | Statement of identification obtained (if family do... |
| Q42 | varchar |  |  | SI | Notes |
| Q43 | varchar |  |  | SI | Verification of death completed |
| Q44 | varchar |  |  | SI | Death Notification questionnaire completed |
| Q45 | varchar |  |  | SI | Notes |
| Q46 | varchar |  |  | SI | This document guides medical and nursing managemen... |
| Q47 | varchar |  |  | SI | Nutrition and hydration plan formulated and implem... |
| Q48 | varchar |  |  | SI | Referral to pastoral care for bereavement support |
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