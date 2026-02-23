# questionnaire.QTCEAF

> Emergency Assessment Form

**Schema:** questionnaire
**Columnas:** 106
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Emergency Assessment Form

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Incident data |
| Q02 | date |  |  | SI | Incident date |
| Q03 | time |  |  | SI | Incident time |
| Q04 | varchar |  |  | SI | Incident location |
| Q05 | varchar |  |  | SI | Responder one name |
| Q06 | varchar |  |  | SI | Responder one role |
| Q07 | varchar |  |  | SI | Responder two name |
| Q08 | varchar |  |  | SI | Responder two role |
| Q09 | varchar |  |  | SI | Responder three name |
| Q10 | varchar |  |  | SI | Responder three role |
| Q11 | varchar |  |  | SI | Scene assessment |
| Q12 | varchar |  |  | SI | Scene is safe? |
| Q13 | varchar |  |  | SI | Environment and hazard |
| Q14 | varchar |  |  | SI | Mechanism of injury |
| Q15 | varchar |  |  | SI | Additional resource required |
| Q16 | varchar |  |  | SI | Personal Protective Equipment (PPE) specify |
| Q17 | varchar |  |  | SI | Comments |
| Q18 | varchar |  |  | SI | Primary survey |
| Q19 | varchar |  |  | SI | Alert, Verbal, Pain, Unresponsive (AVPU) |
| Q19ObsDR | varchar |  | FK | SI | Alert, Verbal, Pain, Unresponsive (AVPU) DR |
| Q20 | varchar |  |  | SI | Airway |
| Q20ObsDR | varchar |  | FK | SI | Airway DR |
| Q21 | varchar |  |  | SI | C-spine protection |
| Q22 | varchar |  |  | SI | C-spine protection specify |
| Q23 | varchar |  |  | SI | Breathing |
| Q23ObsDR | varchar |  | FK | SI | Breathing DR |
| Q24 | varchar |  |  | SI | Breathing patterns |
| Q24ObsDR | varchar |  | FK | SI | Breathing patterns DR |
| Q25 | varchar |  |  | SI | Ventilation |
| Q26 | varchar |  |  | SI | Ventilation specify |
| Q27 | varchar |  |  | SI | Circulation |
| Q28 | varchar |  |  | SI | Skin Colour |
| Q28ObsDR | varchar |  | FK | SI | Skin Colour DR |
| Q29 | varchar |  |  | SI | Bleeding |
| Q29ObsDR | varchar |  | FK | SI | Bleeding DR |
| Q30 | varchar |  |  | SI | Bleeding specify |
| Q31 | varchar |  |  | SI | Capillary refill |
| Q31ObsDR | varchar |  | FK | SI | Capillary refill DR |
| Q32 | varchar |  |  | SI | Disability |
| Q33 | varchar |  |  | SI | Exposure (comment) |
| Q34 | varchar |  |  | SI | Secondary survey |
| Q35 | varchar |  |  | SI | Chief complaint |
| Q36 | varchar |  |  | SI | Allergies checked |
| Q37 | varchar |  |  | SI | Medication history checked |
| Q38 | varchar |  |  | SI | Medical history checked |
| Q39 | varchar |  |  | SI | Provoking factor |
| Q40 | time |  |  | SI | Last meal |
| Q41 | date |  |  | SI | Last menstruation period (female patients) |
| Q42 | varchar |  |  | SI | Is the patient pregnant? |
| Q43 | varchar |  |  | SI | Events |
| Q44 | varchar |  |  | SI | Facial weakness |
| Q45 | varchar |  |  | SI | Affected facial side |
| Q46 | varchar |  |  | SI | Arm weakness |
| Q47 | varchar |  |  | SI | Affected arm side |
| Q48 | varchar |  |  | SI | Speech difficulties |
| Q49 | varchar |  |  | SI | Other comments |
| Q50 | varchar |  |  | SI | Body map |
| Q51 | varchar |  |  | SI | Observation |
| Q53 | varchar |  |  | SI | Cardio pulmonary resuscitation |
| Q54 | time |  |  | SI | Cardio Pulmonary Resuscitation (CPR) time |
| Q55 | varchar |  |  | SI | Automated External Defibrillator (AED) |
| Q56 | varchar |  |  | SI | Other comments |
| Q57 | date |  |  | SI | Date |
| Q58 | time |  |  | SI | Time |
| Q59 | varchar |  |  | SI | Body Map |
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