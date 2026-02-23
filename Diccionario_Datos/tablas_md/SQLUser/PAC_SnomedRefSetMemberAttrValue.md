# SQLUser.PAC_SnomedRefSetMemberAttrValue

**Schema:** SQLUser
**Columnas:** 65
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SNORFSAV_RowId | bigint | PK |  | NO | - |
| Q01 | - |  |  | SI | Please select sedation state |
| Q02 | - |  |  | SI | 0: Acceptable |
| Q02A | - |  |  | SI | No action necessary |
| Q02B | - |  |  | SI | 1: Acceptable |
| Q02C | - |  |  | SI | No action necessary |
| Q02D | - |  |  | SI | 2: Acceptable |
| Q02E | - |  |  | SI | No action necessary |
| Q02F | - |  |  | SI | 3: Unacceptable |
| Q02G | - |  |  | SI | 4: Unacceptable |
| Q03 | - |  |  | SI | Monitor respiratory status and sedation level clos... |
| Q04 | - |  |  | SI | Stop opioid |
| Q05 | - |  |  | SI | notify prescriber or anesthesiologist for orders |
| Q06 | - |  |  | SI | monitor respiratory status and sedation level clos... |
| Q07 | - |  |  | SI | Interventions |
| Q08 | - |  |  | SI | Sedation state |
| Q16 | - |  |  | SI | Pasero Opioid-induced Sedation Scale is a validate... |
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
| SNORFSAV_CreatedDate | date |  |  | SI | Created Date |
| SNORFSAV_CreatedTime | time |  |  | SI | Created Time |
| SNORFSAV_CreatedUser_DR | bigint |  | FK | SI | Created User |
| SNORFSAV_RefSetMember_DR | bigint |  | FK | SI | Des Ref PACSnomedRefSetMember |
| SNORFSAV_UpdatedDate | date |  |  | SI | Updated Date |
| SNORFSAV_UpdatedTime | time |  |  | SI | Updated Time |
| SNORFSAV_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| SNORFSAV_Value_DR | bigint |  | FK | SI | Value ID |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*