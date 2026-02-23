# SQLUser.PAC_Ventilation

**Schema:** SQLUser
**Columnas:** 89
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| VENT_RowId | bigint | PK |  | NO | - |
| Q01 | - |  |  | SI | Cyanosis |
| Q02 | - |  |  | SI | Pressure areas intact |
| Q03 | - |  |  | SI | Water based gel in use |
| Q04 | - |  |  | SI | Skin assessment notes |
| Q05 | - |  |  | SI | Peripheral oedema present |
| Q06 | - |  |  | SI | Loss of sensation in peripheries |
| Q07 | - |  |  | SI | Peripheral oedema notes |
| Q08 | - |  |  | SI | Bladder |
| Q09 | - |  |  | SI | Bowel |
| Q10 | - |  |  | SI | Elimination notes |
| Q11 | - |  |  | SI | Mental state |
| Q12 | - |  |  | SI | Mental state notes |
| Q13 | - |  |  | SI | Hygiene |
| Q14 | - |  |  | SI | Requires help with hygiene |
| Q15 | - |  |  | SI | Hygiene help required |
| Q16 | - |  |  | SI | Hygiene and mobility aids in use |
| Q17 | - |  |  | SI | Other aids |
| Q18 | - |  |  | SI | Hygiene and mobility notes |
| Q19 | - |  |  | SI | Sleep |
| Q20 | - |  |  | SI | Is the patient on CPAP / BiPAP? |
| Q21 | - |  |  | SI | Sleep notes |
| Q22 | - |  |  | SI | Description of patient's diet |
| Q23 | - |  |  | SI | Diet texture |
| Q23ObsDR | - |  |  | SI | Diet texture DR |
| Q24 | - |  |  | SI | Is the patient short of breath on eating? |
| Q25 | - |  |  | SI | Is the patient using a meal delivery service? |
| Q26 | - |  |  | SI | Diet notes |
| Q27 | - |  |  | SI | Does the patient have pain? |
| Q28 | - |  |  | SI | Location and description of pain |
| Q29 | - |  |  | SI | Pain score |
| Q29ObsDR | - |  |  | SI | Pain score DR |
| Q30 | - |  |  | SI | Pain notes |
| Q31 | - |  |  | SI | Goals of care discussed with patient |
| Q32 | - |  |  | SI | Goals of care notes |
| Q33 | - |  |  | SI | Date |
| Q34 | - |  |  | SI | Time |
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
| VENT_Code | varchar |  |  | NO | Code |
| VENT_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| VENT_CreatedDate | date |  |  | SI | Created Date |
| VENT_CreatedTime | time |  |  | SI | Created Time |
| VENT_CreatedUser_DR | bigint |  | FK | SI | Created User |
| VENT_DateFrom | date |  |  | SI | Date From |
| VENT_DateTo | date |  |  | SI | Date To |
| VENT_Desc | varchar |  |  | NO | Description |
| VENT_Owner | varchar |  |  | SI | Owner |
| VENT_UpdatedDate | date |  |  | SI | Updated Date |
| VENT_UpdatedTime | time |  |  | SI | Updated Time |
| VENT_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*