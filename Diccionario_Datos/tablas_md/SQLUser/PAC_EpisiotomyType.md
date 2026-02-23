# SQLUser.PAC_EpisiotomyType

**Schema:** SQLUser
**Columnas:** 80
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Tipos/categorías disponibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| EPIT_RowId | bigint | PK |  | NO | - |
| EPIT_Code | varchar |  |  | NO | Code |
| EPIT_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| EPIT_CreatedDate | date |  |  | SI | Created Date |
| EPIT_CreatedTime | time |  |  | SI | Created Time |
| EPIT_CreatedUser_DR | bigint |  | FK | SI | Created User |
| EPIT_DateFrom | date |  |  | SI | Date From |
| EPIT_DateTo | date |  |  | SI | Date To |
| EPIT_Desc | varchar |  |  | NO | Description |
| EPIT_Owner | varchar |  |  | SI | Owner |
| EPIT_UpdatedDate | date |  |  | SI | Updated Date |
| EPIT_UpdatedTime | time |  |  | SI | Updated Time |
| EPIT_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Patient has Toothbrush |
| Q02 | - |  |  | SI | Patient has Toothpaste |
| Q03 | - |  |  | SI | Patient has Upper Denture |
| Q04 | - |  |  | SI | Patient has Lower Denture |
| Q05 | - |  |  | SI | Patient has Denture Pot |
| Q06 | - |  |  | SI | Patient has no Teeth but still requires mouth care |
| Q07 | - |  |  | SI | Mouth care assessment is required |
| Q08 | - |  |  | SI | Patient has severe dry mouth |
| Q09 | - |  |  | SI | Patient has Ulcers |
| Q10 | - |  |  | SI | Patient has Painful mouth |
| Q11 | - |  |  | SI | Patient has Painful teeth |
| Q12 | - |  |  | SI | Patient has Sore tongue |
| Q13 | - |  |  | SI | Other issues |
| Q14 | - |  |  | SI | Mouth care assessment is required |
| Q15 | - |  |  | SI | Please specify |
| Q16 | - |  |  | SI | Additional Assessment Criteria |
| Q17 | - |  |  | SI | Patient is fully dependent on others for mouth car... |
| Q18 | - |  |  | SI | Mouth care assessment is required - Record all mou... |
| Q19 | - |  |  | SI | Patient requires some assistance |
| Q20 | - |  |  | SI | Unable to get to a sink or needs help with mouth c... |
| Q21 | - |  |  | SI | Please state the assistance patient requires (i.e:... |
| Q22 | - |  |  | SI | Patient is independent |
| Q23 | - |  |  | SI | Able to walk to a sink and needs no assistance wit... |
| Q24 | - |  |  | SI | Mouth care assessment is required |
| Q25 | - |  |  | SI | Mouth care assessment is required |
| Q26 | - |  |  | SI | Mouth care assessment is required |
| Q27 | - |  |  | SI | Mouth care assessment is required |
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