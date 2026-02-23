# SQLUser.PAC_WaitingListEntryRules

**Schema:** SQLUser
**Columnas:** 93
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| WLERULES_RowId | bigint | PK |  | NO | - |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | Body surface area - rule of nines |
| Q04 | - |  |  | SI | Figures within parentheses are used for children u... |
| Q05 | - |  |  | SI | Percentage of area involved |
| Q06 | - |  |  | SI | Erythema |
| Q07 | - |  |  | SI | Oedema / Papulation |
| Q08 | - |  |  | SI | Oozing / Crusting |
| Q09 | - |  |  | SI | Excoriations (scratch marks) |
| Q10 | - |  |  | SI | Lichenification (skin thickening) |
| Q11 | - |  |  | SI | Dryness (is evaluated on uninvolved skin) |
| Q12 | - |  |  | SI | Intensity |
| Q13 | - |  |  | SI | Visual analogue scale (itch / sleeplessness) |
| Q14 | - |  |  | SI | 0 = None |
| Q15 | - |  |  | SI | 10 = Worst imaginable |
| Q16 | - |  |  | SI | Score based on average for the last 3 days or nigh... |
| Q17 | - |  |  | SI | Pruritus |
| Q18 | - |  |  | SI | Sleep loss |
| Q19 | - |  |  | SI | Subjective symptoms |
| Q20 | - |  |  | SI | SCORAD (Section A / 5 + 7 * Section B / 2 + Sectio... |
| Q21 | - |  |  | SI | Score |
| Q22 | - |  |  | SI | Classification |
| Q23 | - |  |  | SI | < 25 |
| Q24 | - |  |  | SI | 25 - 50 |
| Q25 | - |  |  | SI | > 50 |
| Q26 | - |  |  | SI | Mild |
| Q27 | - |  |  | SI | Moderate |
| Q28 | - |  |  | SI | Severe |
| Q29 | - |  |  | SI | < 25: Mild |
| Q30 | - |  |  | SI | 25 - 50: Moderate |
| Q31 | - |  |  | SI | > 50: Severe |
| Q32 | - |  |  | SI | Severity Scoring of Atopic Dermatitis is a composi... |
| Q33 | - |  |  | SI | Body surface area - rule of nines |
| Q34 | - |  |  | SI | SCORAD (Section A / 5 + 7 * Section B / 2 + Sectio... |
| Q35 | - |  |  | SI | Subjective symptoms |
| Q36 | - |  |  | SI | SCORAD (Section A / 5 + 7 * Section B / 2 + Sectio... |
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
| WLERULES_Code | varchar |  |  | NO | Code |
| WLERULES_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| WLERULES_CreatedDate | date |  |  | SI | Created Date |
| WLERULES_CreatedTime | time |  |  | SI | Created Time |
| WLERULES_CreatedUser_DR | bigint |  | FK | SI | Created User |
| WLERULES_DateFrom | date |  |  | SI | Date From |
| WLERULES_DateTo | date |  |  | SI | Date To |
| WLERULES_Desc | varchar |  |  | NO | Description |
| WLERULES_Owner | varchar |  |  | SI | Owner |
| WLERULES_ReasonForChange_DR | bigint |  | FK | SI | Des Ref PACWaitListReasonForChange  |
| WLERULES_UpdatedDate | date |  |  | SI | Updated Date |
| WLERULES_UpdatedTime | time |  |  | SI | Updated Time |
| WLERULES_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| WLERULES_WLPrintStatus_DR | bigint |  | FK | SI | Des Ref PACWaitingListStatus |
| WLERULES_WLStatus_DR | bigint |  | FK | SI | Des Ref PACWaitingListStatus |
| WLERULES_WLType_DR | bigint |  | FK | SI | Des Ref PACWaitingListType |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*