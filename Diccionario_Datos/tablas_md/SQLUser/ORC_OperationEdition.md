# SQLUser.ORC_OperationEdition

**Schema:** SQLUser
**Columnas:** 118
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Órdenes**. Parámetros de órdenes médicas.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ED_ParRef | bigint | PK |  | NO | ORC_Operation Parent Reference |
| ED_Childsub | double |  |  | NO | Childsub |
| ED_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| ED_CreatedDate | date |  |  | SI | Created Date |
| ED_CreatedTime | time |  |  | SI | Created Time |
| ED_CreatedUser_DR | bigint |  | FK | SI | Created User |
| ED_DateFrom | date |  |  | SI | Date From |
| ED_DateTo | date |  |  | SI | Date To |
| ED_Edition_DR | bigint |  | FK | SI | Des Ref Edition |
| ED_RowId | varchar |  |  | NO | - |
| ED_UpdatedDate | date |  |  | SI | Updated Date |
| ED_UpdatedTime | time |  |  | SI | Updated Time |
| ED_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Incident data |
| Q02 | - |  |  | SI | Incident date |
| Q03 | - |  |  | SI | Incident time |
| Q04 | - |  |  | SI | Incident location |
| Q05 | - |  |  | SI | Responder one name |
| Q06 | - |  |  | SI | Responder one role |
| Q07 | - |  |  | SI | Responder two name |
| Q08 | - |  |  | SI | Responder two role |
| Q09 | - |  |  | SI | Responder three name |
| Q10 | - |  |  | SI | Responder three role |
| Q11 | - |  |  | SI | Scene assessment |
| Q12 | - |  |  | SI | Scene is safe? |
| Q13 | - |  |  | SI | Environment and hazard |
| Q14 | - |  |  | SI | Mechanism of injury |
| Q15 | - |  |  | SI | Additional resource required |
| Q16 | - |  |  | SI | Personal Protective Equipment (PPE) specify |
| Q17 | - |  |  | SI | Comments |
| Q18 | - |  |  | SI | Primary survey |
| Q19 | - |  |  | SI | Alert, Verbal, Pain, Unresponsive (AVPU) |
| Q19ObsDR | - |  |  | SI | Alert, Verbal, Pain, Unresponsive (AVPU) DR |
| Q20 | - |  |  | SI | Airway |
| Q20ObsDR | - |  |  | SI | Airway DR |
| Q21 | - |  |  | SI | C-spine protection |
| Q22 | - |  |  | SI | C-spine protection specify |
| Q23 | - |  |  | SI | Breathing |
| Q23ObsDR | - |  |  | SI | Breathing DR |
| Q24 | - |  |  | SI | Breathing patterns |
| Q24ObsDR | - |  |  | SI | Breathing patterns DR |
| Q25 | - |  |  | SI | Ventilation |
| Q26 | - |  |  | SI | Ventilation specify |
| Q27 | - |  |  | SI | Circulation |
| Q28 | - |  |  | SI | Skin Colour |
| Q28ObsDR | - |  |  | SI | Skin Colour DR |
| Q29 | - |  |  | SI | Bleeding |
| Q29ObsDR | - |  |  | SI | Bleeding DR |
| Q30 | - |  |  | SI | Bleeding specify |
| Q31 | - |  |  | SI | Capillary refill |
| Q31ObsDR | - |  |  | SI | Capillary refill DR |
| Q32 | - |  |  | SI | Disability |
| Q33 | - |  |  | SI | Exposure (comment) |
| Q34 | - |  |  | SI | Secondary survey |
| Q35 | - |  |  | SI | Chief complaint |
| Q36 | - |  |  | SI | Allergies checked |
| Q37 | - |  |  | SI | Medication history checked |
| Q38 | - |  |  | SI | Medical history checked |
| Q39 | - |  |  | SI | Provoking factor |
| Q40 | - |  |  | SI | Last meal |
| Q41 | - |  |  | SI | Last menstruation period (female patients) |
| Q42 | - |  |  | SI | Is the patient pregnant? |
| Q43 | - |  |  | SI | Events |
| Q44 | - |  |  | SI | Facial weakness |
| Q45 | - |  |  | SI | Affected facial side |
| Q46 | - |  |  | SI | Arm weakness |
| Q47 | - |  |  | SI | Affected arm side |
| Q48 | - |  |  | SI | Speech difficulties |
| Q49 | - |  |  | SI | Other comments |
| Q50 | - |  |  | SI | Body map |
| Q51 | - |  |  | SI | Observation |
| Q53 | - |  |  | SI | Cardio pulmonary resuscitation |
| Q54 | - |  |  | SI | Cardio Pulmonary Resuscitation (CPR) time |
| Q55 | - |  |  | SI | Automated External Defibrillator (AED) |
| Q56 | - |  |  | SI | Other comments |
| Q57 | - |  |  | SI | Date |
| Q58 | - |  |  | SI | Time |
| Q59 | - |  |  | SI | Body Map |
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