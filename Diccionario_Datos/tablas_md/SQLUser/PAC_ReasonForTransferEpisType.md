# SQLUser.PAC_ReasonForTransferEpisType

**Schema:** SQLUser
**Columnas:** 100
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Tipos/categorías disponibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| EPIS_ParRef | bigint | PK |  | NO | PAC_ReasonForTransfer Parent Reference |
| EPIS_Childsub | double |  |  | NO | Childsub |
| EPIS_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| EPIS_CreatedDate | date |  |  | SI | Created Date |
| EPIS_CreatedTime | time |  |  | SI | Created Time |
| EPIS_CreatedUser_DR | bigint |  | FK | SI | Created User |
| EPIS_EpisSubType_DR | bigint |  | FK | SI | Des Ref to PACEpisodeSubType |
| EPIS_EpisodeType | varchar |  |  | NO | EpisodeType |
| EPIS_Rowid | varchar |  |  | NO | - |
| EPIS_UpdatedDate | date |  |  | SI | Updated Date |
| EPIS_UpdatedTime | time |  |  | SI | Updated Time |
| EPIS_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | Percentage of head and neck affected |
| Q04 | - |  |  | SI | Erythema (redness) |
| Q05 | - |  |  | SI | Induration (thickness) |
| Q06 | - |  |  | SI | Desquamation (scaling) |
| Q07 | - |  |  | SI | Percentage of arms affected |
| Q08 | - |  |  | SI | Erythema (redness) |
| Q09 | - |  |  | SI | Induration (thickness) |
| Q10 | - |  |  | SI | Desquamation (scaling) |
| Q11 | - |  |  | SI | Percentage of trunk affected |
| Q12 | - |  |  | SI | Erythema (redness) |
| Q13 | - |  |  | SI | Induration (thickness) |
| Q14 | - |  |  | SI | Desquamation (scaling) |
| Q15 | - |  |  | SI | Percentage of legs affected |
| Q16 | - |  |  | SI | Erythema (redness) |
| Q17 | - |  |  | SI | Induration (thickness) |
| Q18 | - |  |  | SI | Desquamation (scaling) |
| Q19 | - |  |  | SI | Total head score |
| Q20 | - |  |  | SI | Total trunk score |
| Q21 | - |  |  | SI | Total leg score |
| Q22 | - |  |  | SI | PASI Score |
| Q23 | - |  |  | SI | To use Psoriasis Area and Severity Index (PASI), t... |
| Q24 | - |  |  | SI | • Head -  10% of body surface area |
| Q25 | - |  |  | SI | • Trunk - 20% of body surface area |
| Q26 | - |  |  | SI | • Upper extremities - 30% of body surface area |
| Q27 | - |  |  | SI | • Lower extremities  - 40% of body surface area |
| Q28 | - |  |  | SI | The extent of psoriatic involvement of these four ... |
| Q29 | - |  |  | SI | 0 = No involvement |
| Q30 | - |  |  | SI | 1 = < 10 % |
| Q31 | - |  |  | SI | 2 = > 10 %, but < 30 % |
| Q32 | - |  |  | SI | 3 = > 30 %, but < 50 % |
| Q33 | - |  |  | SI | 4 = > 50 %, but < 70 % |
| Q34 | - |  |  | SI | 5 = > 70 %, but < 90 % |
| Q35 | - |  |  | SI | 6 = 90 – 100 % |
| Q36 | - |  |  | SI | The lesion severity is determined by assessing thr... |
| Q37 | - |  |  | SI | 0 = None |
| Q38 | - |  |  | SI | 1 = Slight |
| Q39 | - |  |  | SI | 2 = Moderate |
| Q40 | - |  |  | SI | 3 = Severe |
| Q41 | - |  |  | SI | 4 = Very severe |
| Q42 | - |  |  | SI | Total PASI = addition of PASI for each body region... |
| Q43 | - |  |  | SI | PASI for each body region = lesion severity x perc... |
| Q44 | - |  |  | SI | Lesion severity for each body region = erythema + ... |
| Q45 | - |  |  | SI | Psoriasis Area and Severity Index (PASI) is a wide... |
| Q46 | - |  |  | SI | PASI combines the assessment of the severity of le... |
| Q47 | - |  |  | SI | Higher the score, the more severe the disease |
| Q48 | - |  |  | SI | Total arm score |
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