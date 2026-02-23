# SQLUser.PAC_AllergyCertainty

**Schema:** SQLUser
**Columnas:** 68
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ALRGCER_RowId | bigint | PK |  | NO | - |
| ALRGCER_Code | varchar |  |  | NO | Code |
| ALRGCER_CreatedDate | date |  |  | SI | Created Date |
| ALRGCER_CreatedTime | time |  |  | SI | Created Time |
| ALRGCER_CreatedUser_DR | bigint |  | FK | SI | Created User |
| ALRGCER_DateFrom | date |  |  | SI | Date From |
| ALRGCER_DateTo | date |  |  | SI | Date To |
| ALRGCER_Desc | varchar |  |  | NO | Description |
| ALRGCER_UpdatedDate | date |  |  | SI | Updated Date |
| ALRGCER_UpdatedTime | time |  |  | SI | Updated Time |
| ALRGCER_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Adequate heating |
| Q02 | - |  |  | SI | Adequate lighting |
| Q03 | - |  |  | SI | Adequate access to property |
| Q04 | - |  |  | SI | Adequate phone signal |
| Q05 | - |  |  | SI | Waterbirth |
| Q06 | - |  |  | SI | Pool hire |
| Q07 | - |  |  | SI | Notes |
| Q08 | - |  |  | SI | Discussed obstetric emergencies |
| Q09 | - |  |  | SI | Equipment available |
| Q10 | - |  |  | SI | Resuscitation equipment available |
| Q11 | - |  |  | SI | Availability of medical assistance |
| Q12 | - |  |  | SI | Transfer to hospital in event of deviation from no... |
| Q13 | - |  |  | SI | Notes |
| Q14 | - |  |  | SI | Fetal heart monitoring |
| Q15 | - |  |  | SI | Method of monitoring |
| Q16 | - |  |  | SI | Is fetal heart monitoring equipment available? |
| Q17 | - |  |  | SI | Notes |
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