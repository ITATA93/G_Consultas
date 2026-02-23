# SQLUser.OEC_Priority

**Schema:** SQLUser
**Columnas:** 96
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Entry Orders**. Tipos y estados de órdenes.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| OECPR_RowId | bigint | PK |  | NO | - |
| OECPR_AllowPRN | varchar |  |  | SI | Allow PRN |
| OECPR_Code | varchar |  |  | NO | Priority Code |
| OECPR_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| OECPR_Color | varchar |  |  | SI | Color |
| OECPR_CreatedDate | date |  |  | SI | Created Date |
| OECPR_CreatedTime | time |  |  | SI | Created Time |
| OECPR_CreatedUser_DR | bigint |  | FK | SI | Created User |
| OECPR_DateFrom | date |  |  | SI | Date From |
| OECPR_DateTo | date |  |  | SI | Date To |
| OECPR_Desc | varchar |  |  | NO | Priority Description |
| OECPR_LabUse | varchar |  |  | SI | Lab Use Restriction |
| OECPR_Owner | varchar |  |  | SI | Owner |
| OECPR_Priority | varchar |  |  | SI | Priority |
| OECPR_System | varchar |  |  | SI | System Flag |
| OECPR_UpdatedDate | date |  |  | SI | Updated Date |
| OECPR_UpdatedTime | time |  |  | SI | Updated Time |
| OECPR_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | PACU comments |
| Q02 | - |  |  | SI | Discharge agreed by anaesthetist (only if discharg... |
| Q02a | - |  |  | SI | Discharge agreed by anaesthetist (only if discharg... |
| Q03 | - |  |  | SI | Ward notified / Bed available |
| Q03a | - |  |  | SI | Ward notified / Bed available |
| Q04 | - |  |  | SI | Lines checked and flushed |
| Q04a | - |  |  | SI | Lines checked and flushed |
| Q05 | - |  |  | SI | Dressings checked |
| Q05a | - |  |  | SI | Dressings checked |
| Q06 | - |  |  | SI | Drains checked |
| Q06a | - |  |  | SI | Drains checked |
| Q07 | - |  |  | SI | Nursing discharge summary completed |
| Q07a | - |  |  | SI | Nursing discharge summary completed |
| Q08 | - |  |  | SI | Clinical indicators completed if applicable |
| Q08a | - |  |  | SI | Clinical indicators completed if applicable |
| Q09 | - |  |  | SI | Post operative medications charted |
| Q09a | - |  |  | SI | Post operative medications charted |
| Q11 | - |  |  | SI | Glasses |
| Q12 | - |  |  | SI | Dentures |
| Q13 | - |  |  | SI | Hearing aides |
| Q14 | - |  |  | SI | X-Rays |
| Q15 | - |  |  | SI | Temperature > 36 degrees |
| Q15a | - |  |  | SI | Temperature > 36 degrees |
| Q16 | - |  |  | SI | Comments |
| Q17 | - |  |  | SI | Script sent to pharmacy |
| Q19 | - |  |  | SI | Clinical indicators completed if applicable |
| Q27 | - |  |  | SI | Personal belongings |
| Q28 | - |  |  | SI | Supplementary oxygen required |
| Q29 | - |  |  | SI | Lines removed |
| Q30 | - |  |  | SI | Lines removed comments |
| Q31 | - |  |  | SI | Return of body part / metalware |
| Q32 | - |  |  | SI | Patient care plan follows post op instructions |
| Q33 | - |  |  | SI | Handover received by |
| Q34 | - |  |  | SI | Handover date and time |
| Q35 | - |  |  | SI | Handover time |
| Q36 | - |  |  | SI | Other belongings |
| Q38 | - |  |  | SI | Date |
| Q39 | - |  |  | SI | Time |
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