# SQLUser.ARC_ItemHospPayorAppr

**Schema:** SQLUser
**Columnas:** 88
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Arquetipo de configuración**. Definición base del sistema. Items/líneas de detalle.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| HPA_ParRef | varchar | PK |  | NO | ARC_ItmMast Parent Reference |
| HPA_Childsub | double |  |  | NO | Childsub |
| HPA_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| HPA_CreatedDate | date |  |  | SI | Created Date |
| HPA_CreatedTime | time |  |  | SI | Created Time |
| HPA_CreatedUser_DR | bigint |  | FK | SI | Created User |
| HPA_EpisodeTypes | varchar |  |  | SI | Episode Types |
| HPA_Hospital_DR | bigint |  | FK | SI | Des Ref Hospital |
| HPA_RowId | varchar |  |  | NO | - |
| HPA_UpdatedDate | date |  |  | SI | Updated Date |
| HPA_UpdatedTime | time |  |  | SI | Updated Time |
| HPA_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | Select the option for each that is most applicable... |
| Q04 | - |  |  | SI | Observations |
| Q05 | - |  |  | SI | Early warning score |
| Q06 | - |  |  | SI | Conscious state |
| Q07 | - |  |  | SI | Behaviour |
| Q08 | - |  |  | SI | Communication |
| Q09 | - |  |  | SI | Respiratory status |
| Q10 | - |  |  | SI | Pain management |
| Q11 | - |  |  | SI | Wound Care |
| Q12 | - |  |  | SI | Medication management |
| Q13 | - |  |  | SI | ADL's |
| Q14 | - |  |  | SI | Isolation |
| Q15 | - |  |  | SI | Safety |
| Q16 | - |  |  | SI | Complexity |
| Q17 | - |  |  | SI | Admission / Discharge / Transfer |
| Q18 | - |  |  | SI | Acuity remarks |
| Q19 | - |  |  | SI | Score |
| Q20 | - |  |  | SI | Classification |
| Q21 | - |  |  | SI | 0 |
| Q22 | - |  |  | SI | 1 - 7 |
| Q23 | - |  |  | SI | 8 - 14 |
| Q24 | - |  |  | SI | 15 - 28 |
| Q25 | - |  |  | SI | ≥ 29 |
| Q26 | - |  |  | SI | Level 0 - Minimal / Sub-Acute Care |
| Q27 | - |  |  | SI | Level 1 - Acute Care |
| Q28 | - |  |  | SI | Level 2 - Intermediate Acute Care |
| Q29 | - |  |  | SI | Level 3 - Complex / High - Dependency Care |
| Q30 | - |  |  | SI | Level 4 - Maximum Care |
| Q31 | - |  |  | SI | 0: Level 0 - Minimal / Sub-Acute Care |
| Q32 | - |  |  | SI | 1 - 7: Level 1 - Acute Care |
| Q33 | - |  |  | SI | 8 - 14: Level 2 - Intermediate Acute Care |
| Q34 | - |  |  | SI | 15 - 28: Level 3 - Complex / High - Dependency Car... |
| Q35 | - |  |  | SI | ≥ 29: Level 4 - Maximum Care |
| Q36 | - |  |  | SI | This scored questionnaire is a tool used to help n... |
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