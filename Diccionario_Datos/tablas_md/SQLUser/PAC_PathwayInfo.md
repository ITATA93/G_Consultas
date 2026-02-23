# SQLUser.PAC_PathwayInfo

**Schema:** SQLUser
**Columnas:** 93
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| PACPIN_ParRef | bigint | PK |  | NO | Parent Reference |
| PACPIN_COPYR_DR | bigint |  | FK | SI | Copyright |
| PACPIN_Childsub | double |  |  | NO | Childsub |
| PACPIN_CodeTableTags | varchar |  |  | SI | Code Table Tags |
| PACPIN_CreatedDate | date |  |  | SI | Created Date |
| PACPIN_CreatedTime | time |  |  | SI | Created Time |
| PACPIN_CreatedUser_DR | bigint |  | FK | SI | Created User |
| PACPIN_Desc | varchar |  |  | NO | Description |
| PACPIN_FileName | varchar |  |  | SI | File Name |
| PACPIN_RowId | varchar |  |  | NO | - |
| PACPIN_StreamData | bigint |  |  | SI | epr.CTFile |
| PACPIN_UpdatedDate | date |  |  | SI | Updated Date |
| PACPIN_UpdatedTime | time |  |  | SI | Updated Time |
| PACPIN_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | Parent / Guardian received the Neonatal Screening ... |
| Q04 | - |  |  | SI | Explanation / Education about the NST provided to ... |
| Q05 | - |  |  | SI | Information provided notes |
| Q06 | - |  |  | SI | Parent / Guardian consents to the NST being perfor... |
| Q07 | - |  |  | SI | Parent / Guardian informed of the following: |
| Q08 | - |  |  | SI | Benefits & risks of the NST and the risks of not c... |
| Q09 | - |  |  | SI | If the baby becomes unwell, they should inform the... |
| Q10 | - |  |  | SI | They can change their mind at any stage and were e... |
| Q11 | - |  |  | SI | The telephone number of the newborn screening prog... |
| Q12 | - |  |  | SI | Care provider who discussed importance of NST with... |
| Q13 | - |  |  | SI | Parent / Guardian confirmed the newborn screening ... |
| Q14 | - |  |  | SI | Notes |
| Q15 | - |  |  | SI | Parent / Guardian name |
| Q16 | - |  |  | SI | Parent / Guardian signature |
| Q16UDt | - |  |  | SI | Parent / Guardian signature Last Updated Date |
| Q16UTm | - |  |  | SI | Parent / Guardian signature Last Updated Time |
| Q17 | - |  |  | SI | NST due between dates |
| Q18 | - |  |  | SI | and |
| Q19 | - |  |  | SI | Date NST performed |
| Q20 | - |  |  | SI | Time NST performed |
| Q21 | - |  |  | SI | Performed by |
| Q22 | - |  |  | SI | Notes |
| Q23 | - |  |  | SI | The information handout MUST BE DISCUSSED with par... |
| Q24 | - |  |  | SI | • Conditions screened, benefits / importance of te... |
| Q25 | - |  |  | SI | • Collection of personal information and what happ... |
| Q26 | - |  |  | SI | • Personal information is collected and stored, as... |
| Q27 | - |  |  | SI | • There is no stored data about DNA except as a di... |
| Q28 | - |  |  | SI | • Bloodspot sample cards are retained for 18 years... |
| Q29 | - |  |  | SI | • After 2 years the parents can request the card t... |
| Q30 | - |  |  | SI | • All cards are destroyed after 18 years |
| Q31 | - |  |  | SI | • Stored identified bloodspots are not used / test... |
| Q32 | - |  |  | SI | • Small amount of the bloodspots may be used in no... |
| Q33 | - |  |  | SI | normal quality control, laboratory audit, developi... |
| Q34 | - |  |  | SI | • Parents / Guardians have rights in relation to a... |
| Q35 | - |  |  | SI | • Test results - are usually available 1 working d... |
| Q36 | - |  |  | SI | • Individual reports are not issued for results th... |
| Q37 | - |  |  | SI | • Verbal consent / Written consent |
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