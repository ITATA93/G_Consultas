# SQLUser.PAC_PatientFlag

**Schema:** SQLUser
**Columnas:** 110
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| PACPF_RowID | bigint | PK |  | NO | - |
| PACPF_Code | varchar |  |  | NO | Code |
| PACPF_CodeTableTags | varchar |  |  | SI | List of code table tags |
| PACPF_CreatedDate | date |  |  | SI | Created Date |
| PACPF_CreatedTime | time |  |  | SI | Created Time |
| PACPF_CreatedUser_DR | bigint |  | FK | SI | Created User |
| PACPF_DateFrom | date |  |  | SI | Effective date for the record |
| PACPF_DateTo | date |  |  | SI | Last day the record is active |
| PACPF_Desc | varchar |  |  | NO | Description |
| PACPF_ExcludeFromElectronicIssue | varchar |  |  | SI | Exclude Patient From Electronic Issue
This flag a... |
| PACPF_Owner | varchar |  |  | SI | Owner |
| PACPF_ReportDisplay | varchar |  |  | SI | Lab Doctor Report Patient Flag Display |
| PACPF_UpdatedDate | date |  |  | SI | Updated Date |
| PACPF_UpdatedTime | time |  |  | SI | Updated Time |
| PACPF_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | Assess the patient’s oral cavity and their ability... |
| Q04 | - |  |  | SI | Voice |
| Q05 | - |  |  | SI | Swallow |
| Q06 | - |  |  | SI | Mucous membranes |
| Q07 | - |  |  | SI | Saliva |
| Q08 | - |  |  | SI | Tongue |
| Q09 | - |  |  | SI | Lips |
| Q10 | - |  |  | SI | Gums |
| Q11 | - |  |  | SI | Teeth / Dentures |
| Q12 | - |  |  | SI | Ability to maintain nutrition |
| Q13 | - |  |  | SI | Analgesic requirements |
| Q14 | - |  |  | SI | Evidence of infection |
| Q15 | - |  |  | SI | Taste |
| Q16 | - |  |  | SI | Self care assessments |
| Q17 | - |  |  | SI | Patient has head and neck cancer or receiving high... |
| Q18 | - |  |  | SI | Score |
| Q19 | - |  |  | SI | Documentation of the oral mucosa pertaining to can... |
| Q20 | - |  |  | SI | Assess and identify the risks of oral complication... |
| Q21 | - |  |  | SI | Assessment score |
| Q22 | - |  |  | SI | Intervention level |
| Q23 | - |  |  | SI | Assessment |
| Q24 | - |  |  | SI | Frequency of mouth care |
| Q25 | - |  |  | SI | Analgesia |
| Q26 | - |  |  | SI | 13 - 20 |
| Q27 | - |  |  | SI | Level 1 |
| Q28 | - |  |  | SI | At least once daily |
| Q29 | - |  |  | SI | 4 times a day |
| Q30 | - |  |  | SI | As required |
| Q31 | - |  |  | SI | 21 - 26 |
| Q32 | - |  |  | SI | Level 2 |
| Q33 | - |  |  | SI | At least twice daily |
| Q34 | - |  |  | SI | 2 to 4 hourly |
| Q35 | - |  |  | SI | Regular and breakthrough |
| Q36 | - |  |  | SI | 27 - 39 |
| Q37 | - |  |  | SI | Level 3 |
| Q38 | - |  |  | SI | At least 8 hourly (each shift) |
| Q39 | - |  |  | SI | 1 to 2 hourly |
| Q40 | - |  |  | SI | Regular and breakthrough or continuous and breakth... |
| Q41 | - |  |  | SI | Nursing interventions |
| Q42 | - |  |  | SI | Level 1 interventions |
| Q43 | - |  |  | SI | • Brush teeth or dentures after each meal and befo... |
| Q44 | - |  |  | SI | • Dentures should be removed when the patient is a... |
| Q45 | - |  |  | SI | • Rinse with sodium bicarbonate or salt water for ... |
| Q46 | - |  |  | SI | • Keep lips lubricated, e.g. with lip balm or lip ... |
| Q47 | - |  |  | SI | Level 2 interventions in addition to level 1 |
| Q48 | - |  |  | SI | • Increase the frequency of level 1 interventions ... |
| Q49 | - |  |  | SI | • Refer to dietician |
| Q50 | - |  |  | SI | • Provide regular analgesia as required |
| Q51 | - |  |  | SI | • Any ulcerations and visible infection should be ... |
| Q52 | - |  |  | SI | Level 3 interventions in addition to level 2 |
| Q53 | - |  |  | SI | • Increase the frequency of level 2 interventions ... |
| Q54 | - |  |  | SI | • Use sponge sticks instead of soft toothbrush |
| Q55 | - |  |  | SI | • Medical review |
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