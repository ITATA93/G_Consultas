# SQLUser.MR_MedRecLink

**Schema:** SQLUser
**Columnas:** 79
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Medicamentos**. Prescripción y administración de fármacos. Relación entre entidades.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| MRL_ParRef | varchar | PK |  | NO | MR_Adm Parent Reference |
| MRL_Childsub | double |  |  | NO | Childsub |
| MRL_ClassifiedVia_DR | bigint |  | FK | SI | Classified Via |
| MRL_Comments | varchar |  |  | SI | Comments |
| MRL_Decision | varchar |  |  | SI | Decision |
| MRL_DecisionCommitted | bit |  |  | SI | Decision Committed |
| MRL_Discrepancy | varchar |  |  | SI | Discrepancy |
| MRL_LastUpdateDate | date |  |  | SI | LastUpdateDate |
| MRL_LastUpdateHospital_DR | bigint |  | FK | SI | Des Ref LastUpdateHospital |
| MRL_LastUpdateTime | time |  |  | SI | LastUpdateTime |
| MRL_LastUpdateUser_DR | bigint |  | FK | SI | Des Ref LastUpdateUser |
| MRL_RowId | varchar |  |  | NO | - |
| MRL_VarianceReason_DR | bigint |  | FK | SI | Variance Reason |
| Q01 | - |  |  | SI | Is your patient being fed enterally (PO/NG)? |
| Q01a | - |  |  | SI | Feeding |
| Q01b | - |  |  | SI | Early feeding significantly reduces ICU mortality |
| Q02 | - |  |  | SI | Have you documented the RASS and Pain Score at lea... |
| Q02a | - |  |  | SI | Analgesia and Sedation |
| Q02b | - |  |  | SI | Appropriate analgesia and sedation ensures patient... |
| Q03 | - |  |  | SI | Is your patient receiving pharmacologic DVT Prophy... |
| Q03a | - |  |  | SI | Thromboprophylaxis |
| Q03b | - |  |  | SI | DVT prophylaxis reduces the risk of DVTs and poten... |
| Q04 | - |  |  | SI | Does your patient have TEDS or PCDs on? |
| Q04a | - |  |  | SI | Head of Bed |
| Q04b | - |  |  | SI | Elevating the head of the patient's bed greater th... |
| Q05 | - |  |  | SI | Is the patient receiving GI Prophylaxis? |
| Q05a | - |  |  | SI | Ulcer Prophylaxis |
| Q05b | - |  |  | SI | GI ulcer prophylaxis significantly reduces GI Blee... |
| Q06 | - |  |  | SI | Glycaemic Control - Has your patient's blood gluco... |
| Q06a | - |  |  | SI | Glycaemic Control |
| Q06b | - |  |  | SI | Controlling a patient's blood glucose can signific... |
| Q07 | - |  |  | SI | Has the bed head been elevated to at least 30 degr... |
| Q07a | - |  |  | SI | Ulcer Prophylaxis |
| Q07b | - |  |  | SI | GI ulcer prophylaxis significantly reduces GI Blee... |
| Q08 | - |  |  | SI | Sedative interruption implemented? |
| Q08a | - |  |  | SI | Ventilator Component |
| Q09 | - |  |  | SI | Is the patient ready for extubation? |
| Q25 | - |  |  | SI | FAST HUG is a mnemonic used in the Intensive Care ... |
| Q26 | - |  |  | SI | help identify and prevent medication errors, promo... |
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