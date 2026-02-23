# SQLUser.PAC_SmokerDuringPregn

**Schema:** SQLUser
**Columnas:** 71
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SMOKDP_RowId | bigint | PK |  | NO | - |
| Q01 | - |  |  | SI | Patient |
| Q02 | - |  |  | SI | Sterility / Cleanliness |
| Q03 | - |  |  | SI | Pump |
| Q04 | - |  |  | SI | Electrical |
| Q05 | - |  |  | SI | Cardioplegia |
| Q06 | - |  |  | SI | Gas Supply |
| Q07 | - |  |  | SI | Lines / Pump Tubing |
| Q08 | - |  |  | SI | Safety Mechanisms |
| Q09 | - |  |  | SI | Assisted Venous Return |
| Q10 | - |  |  | SI | Monitoring |
| Q11 | - |  |  | SI | Anticoagulation |
| Q12 | - |  |  | SI | Temperature Control |
| Q13 | - |  |  | SI | Supplies |
| Q14 | - |  |  | SI | Backup |
| Q15 | - |  |  | SI | Emergent Restart Of Bypass |
| Q16 | - |  |  | SI | Termination Checklist |
| Q17 | - |  |  | SI | Postbypass Checklist |
| Q18 | - |  |  | SI | Notes |
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
| SMOKDP_Code | varchar |  |  | NO | Code |
| SMOKDP_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| SMOKDP_CreatedDate | date |  |  | SI | Created Date |
| SMOKDP_CreatedTime | time |  |  | SI | Created Time |
| SMOKDP_CreatedUser_DR | bigint |  | FK | SI | Created User |
| SMOKDP_DateFrom | date |  |  | SI | Date From |
| SMOKDP_DateTo | date |  |  | SI | Date To |
| SMOKDP_Desc | varchar |  |  | NO | Description |
| SMOKDP_Owner | varchar |  |  | SI | Owner |
| SMOKDP_UpdatedDate | date |  |  | SI | Updated Date |
| SMOKDP_UpdatedTime | time |  |  | SI | Updated Time |
| SMOKDP_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*