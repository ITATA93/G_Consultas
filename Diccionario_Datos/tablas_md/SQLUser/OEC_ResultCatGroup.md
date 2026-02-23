# SQLUser.OEC_ResultCatGroup

**Schema:** SQLUser
**Columnas:** 94
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Entry Orders**. Tipos y estados de órdenes.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| RESCATG_RowId | bigint | PK |  | NO | - |
| Q01 | - |  |  | SI | Regional |
| Q07 | - |  |  | SI | Anaesthesia Performed By: |
| Q08 | - |  |  | SI | Time Performed |
| Q14 | - |  |  | SI | Position |
| Q16 | - |  |  | SI | Other |
| Q17 | - |  |  | SI | Date performed |
| Q18 | - |  |  | SI | GA |
| Q18ObsDR | - |  |  | SI | GA DR |
| Q18a | - |  |  | SI | Note |
| Q19 | - |  |  | SI | Sedation |
| Q19ObsDR | - |  |  | SI | Sedation DR |
| Q19a | - |  |  | SI | Note |
| Q20 | - |  |  | SI | Awake |
| Q20ObsDR | - |  |  | SI | Awake DR |
| Q20a | - |  |  | SI | Note |
| Q21 | - |  |  | SI | Local infiltration |
| Q21ObsDR | - |  |  | SI | Local infiltration DR |
| Q21a | - |  |  | SI | Note |
| Q22 | - |  |  | SI | Antisepsis |
| Q22ObsDR | - |  |  | SI | Antisepsis DR |
| Q23 | - |  |  | SI | Surface landmark |
| Q23ObsDR | - |  |  | SI | Surface landmark DR |
| Q24 | - |  |  | SI | Parasthesia |
| Q24ObsDR | - |  |  | SI | Parasthesia DR |
| Q25 | - |  |  | SI | Ultrasound guided |
| Q25ObsDR | - |  |  | SI | Ultrasound guided DR |
| Q26 | - |  |  | SI | Neurostimulation - Stimulating current |
| Q26ObsDR | - |  |  | SI | Neurostimulation - Stimulating current DR |
| Q27 | - |  |  | SI | Access intravascular |
| Q28 | - |  |  | SI | Type |
| Q28ObsDR | - |  |  | SI | Type DR |
| Q29 | - |  |  | SI | Localization |
| Q29ObsDR | - |  |  | SI | Localization DR |
| Q30 | - |  |  | SI | Size / Color |
| Q30ObsDR | - |  |  | SI | Size / Color DR |
| Q31 | - |  |  | SI | Characteristics |
| Q31ObsDR | - |  |  | SI | Characteristics DR |
| Q32 | - |  |  | SI | Material |
| Q32ObsDR | - |  |  | SI | Material DR |
| Q33 | - |  |  | SI | Position |
| Q33ObsDR | - |  |  | SI | Position DR |
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
| RESCATG_Code | varchar |  |  | NO | Code |
| RESCATG_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| RESCATG_CreatedDate | date |  |  | SI | Created Date |
| RESCATG_CreatedTime | time |  |  | SI | Created Time |
| RESCATG_CreatedUser_DR | bigint |  | FK | SI | Created User |
| RESCATG_DateFrom | date |  |  | SI | Date From |
| RESCATG_DateTo | date |  |  | SI | Date To |
| RESCATG_Desc | varchar |  |  | NO | Description |
| RESCATG_Owner | varchar |  |  | SI | Owner |
| RESCATG_UpdatedDate | date |  |  | SI | Updated Date |
| RESCATG_UpdatedTime | time |  |  | SI | Updated Time |
| RESCATG_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*