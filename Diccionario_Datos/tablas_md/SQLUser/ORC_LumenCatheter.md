# SQLUser.ORC_LumenCatheter

**Schema:** SQLUser
**Columnas:** 101
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Órdenes**. Parámetros de órdenes médicas.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LUMEN_RowId | bigint | PK |  | NO | - |
| LUMEN_Code | varchar |  |  | NO | Code |
| LUMEN_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| LUMEN_CreatedDate | date |  |  | SI | Created Date |
| LUMEN_CreatedTime | time |  |  | SI | Created Time |
| LUMEN_CreatedUser_DR | bigint |  | FK | SI | Created User |
| LUMEN_DateFrom | date |  |  | SI | Date From |
| LUMEN_DateTo | date |  |  | SI | Date To |
| LUMEN_Desc | varchar |  |  | NO | Description |
| LUMEN_Owner | varchar |  |  | SI | Owner |
| LUMEN_UpdatedDate | date |  |  | SI | Updated Date |
| LUMEN_UpdatedTime | time |  |  | SI | Updated Time |
| LUMEN_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | All involved parties in consensus for cessation of... |
| Q04 | - |  |  | SI | Religious / spiritual / cultural needs considered |
| Q05 | - |  |  | SI | Pastoral care brochure provided |
| Q06 | - |  |  | SI | Referral flowchart followed, if required |
| Q07 | - |  |  | SI | Social worker / Bereavement team notified or refer... |
| Q08 | - |  |  | SI | Bereavement information provided to family / signi... |
| Q09 | - |  |  | SI | Patient / Family meeting documented in medical rec... |
| Q10 | - |  |  | SI | Notes |
| Q11 | - |  |  | SI | Resuscitation record up to date |
| Q12 | - |  |  | SI | Donation service contacted for potential organ / c... |
| Q13 | - |  |  | SI | Nurse Donation Specialist (NDS) contacted to arran... |
| Q14 | - |  |  | SI | Organ donation process commenced |
| Q15 | - |  |  | SI | Notes |
| Q16 | - |  |  | SI | Medication prescribed for symptom control |
| Q17 | - |  |  | SI | Pressure care attended with consideration of press... |
| Q18 | - |  |  | SI | Notes |
| Q19 | - |  |  | SI | Bedside monitor display off |
| Q20 | - |  |  | SI | Ventilation ceased |
| Q21 | - |  |  | SI | Patient extubated |
| Q22 | - |  |  | SI | Oxygen therapy ceased |
| Q23 | - |  |  | SI | Inotropes and vasopressors ceased |
| Q24 | - |  |  | SI | Intravascular fluids ceased |
| Q25 | - |  |  | SI | Enteral feeding / Total parenteral nutrition cease... |
| Q26 | - |  |  | SI | Continuous renal replacement therapy ceased |
| Q27 | - |  |  | SI | Medications ceased (except comfort measures) |
| Q28 | - |  |  | SI | Active vital sign monitoring ceased |
| Q29 | - |  |  | SI | Implantable defibrillator deactivated |
| Q30 | - |  |  | SI | Unnecessary vascular access removed |
| Q31 | - |  |  | SI | Notes |
| Q32 | - |  |  | SI | Unnecessary medical equipment removed from the  ro... |
| Q33 | - |  |  | SI | Consideration of personalisation / ambience measur... |
| Q34 | - |  |  | SI | Notes |
| Q35 | - |  |  | SI | Palliative care referral made (patient likely to s... |
| Q36 | - |  |  | SI | Parent team aware of palliative plan |
| Q37 | - |  |  | SI | General practitioner aware of palliative plan |
| Q38 | - |  |  | SI | Notes |
| Q39 | - |  |  | SI | Coroner notified |
| Q40 | - |  |  | SI | Family notified of coronial referral |
| Q41 | - |  |  | SI | Statement of identification obtained (if family do... |
| Q42 | - |  |  | SI | Notes |
| Q43 | - |  |  | SI | Verification of death completed |
| Q44 | - |  |  | SI | Death Notification questionnaire completed |
| Q45 | - |  |  | SI | Notes |
| Q46 | - |  |  | SI | This document guides medical and nursing managemen... |
| Q47 | - |  |  | SI | Nutrition and hydration plan formulated and implem... |
| Q48 | - |  |  | SI | Referral to pastoral care for bereavement support |
| QUESAnaDR | - |  |  | SI | Anaesthesia |
| QUESAnaOperationDR | - |  |  | SI | Operation |
| QUESConsultDR | - |  |  | SI | Consult |
| QUESCopiedComments | - |  |  | SI | Copied Comments |
| QUESCopiedDate | - |  |  | SI | Copied Date |
| QUESCopiedEpDR | - |  |  | SI | Copied Episode |
| QUESCopiedSourceDR | - |  |  | SI | Copied Source DR |
| QUESCopiedTime | - |  |  | SI | Copied Time |
| QUESCopiedUserDR | - |  |  | SI | Copied User |
| QUESCreateDate | - |  |  | SI | Creation Date |
| QUESCreateTime | - |  |  | SI | Creation Time |
| QUESCreateUserDR | - |  |  | SI | Creation User |
| QUESDate | - |  |  | SI | Last Update Date |
| QUESErrorReasonDR | - |  |  | SI | Error Reason |
| QUESFHResidentDR | - |  |  | SI | Resident |
| QUESMRClinicalPathWaysDR | - |  |  | SI | Clinical Pathway |
| QUESNRCarePlanIssuesDR | - |  |  | SI | Nurse Care Plan Issues |
| QUESOEOrdExecDR | - |  |  | SI | Order Execution |
| QUESORPreanaestheticConsultDR | - |  |  | SI | Preanaesthetic Consultation |
| QUESObsEntryDR | - |  |  | SI | Observation Entry |
| QUESOperRoomDR | - |  |  | SI | Operating Room |
| QUESPAAdmDR | - |  |  | SI | Admission |
| QUESPAAdverseEventDR | - |  |  | SI | Adverse Event |
| QUESPAPatMasDR | - |  |  | SI | Patient |
| QUESPAPregnancyDR | - |  |  | SI | Pregnancy |
| QUESPAWaitingListDR | - |  |  | SI | Waiting List |
| QUESPathwayItemDR | - |  |  | SI | Pathway Item |
| QUESPrePostExamOEOrdItemDR | - |  |  | SI | Pre/Post Exam OrdItem |
| QUESRBAppointmentDR | - |  |  | SI | Appointments |
| QUESRBApptOutcomeDR | - |  |  | SI | Appointment Outcome |
| QUESRBApptSlotDR | - |  |  | SI | Appointment Slot |
| QUESReasonForCorrectionDR | - |  |  | SI | Reason for Correction |
| QUESSSUserDefWindowDR | - |  |  | SI | Questionnaire |
| QUESScore | - |  |  | SI | Score |
| QUESSecondUserDR | - |  |  | SI | Second Signature |
| QUESStatusDR | - |  |  | SI | Status |
| QUESTextResultDR | - |  |  | SI | Text Result |
| QUESTime | - |  |  | SI | Last Update Time |
| QUESTransactionDR | - |  |  | SI | Transaction |
| QUESUserDR | - |  |  | SI | Last Update User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*