# SQLUser.PAC_OutcomeOfPregnancy

**Schema:** SQLUser
**Columnas:** 104
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| OPREG_RowId | bigint | PK |  | NO | - |
| OPREG_AddToLiving | varchar |  |  | SI | Add To Living Children |
| OPREG_AddToPreterm | varchar |  |  | SI | Add To Preterm Birth |
| OPREG_AutoAdmit | varchar |  |  | SI | Automatic Admission |
| OPREG_AutoRegister | varchar |  |  | SI | Automatic Registration |
| OPREG_Code | varchar |  |  | NO | Code |
| OPREG_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| OPREG_CreatedDate | date |  |  | SI | Created Date |
| OPREG_CreatedTime | time |  |  | SI | Created Time |
| OPREG_CreatedUser_DR | bigint |  | FK | SI | Created User |
| OPREG_DateFrom | date |  |  | SI | Date From |
| OPREG_DateTo | date |  |  | SI | Date To |
| OPREG_Desc | varchar |  |  | NO | Description |
| OPREG_NationalCode | varchar |  |  | SI | National code |
| OPREG_OutcomeType | varchar |  |  | SI | Outcome type |
| OPREG_OutcomeTypeText | varchar |  |  | SI | OutcomeTypeText |
| OPREG_Owner | varchar |  |  | SI | Owner |
| OPREG_ParaDisplayUK | varchar |  |  | SI | ParaDisplayUK |
| OPREG_UpdatedDate | date |  |  | SI | Updated Date |
| OPREG_UpdatedTime | time |  |  | SI | Updated Time |
| OPREG_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| OPREG_UseForPara | varchar |  |  | SI | Para condition flag |
| OPREG_UsePretermCondition | varchar |  |  | SI | Use Preterm Condition |
| Q01 | - |  |  | SI | I stay at home most of the time because of my back |
| Q02 | - |  |  | SI | I change position frequently to try to get my back... |
| Q03 | - |  |  | SI | I walk more slowly than usual because of my back |
| Q04 | - |  |  | SI | Because of my back, I am not doing any jobs that I... |
| Q05 | - |  |  | SI | Because of my back, I use a handrail to get upstai... |
| Q06 | - |  |  | SI | Because of my back, I lie down to rest more often |
| Q07 | - |  |  | SI | Because of my back, I have to hold on to something... |
| Q08 | - |  |  | SI | Because of my back, I try to get other people to d... |
| Q09 | - |  |  | SI | I get dressed more slowly than usual because of my... |
| Q10 | - |  |  | SI | I only stand up for short periods of time because ... |
| Q11 | - |  |  | SI | Because of my back, I try not to bend or kneel dow... |
| Q12 | - |  |  | SI | I find it difficult to get out of a chair because ... |
| Q13 | - |  |  | SI | My back is painful almost all of the time |
| Q14 | - |  |  | SI | I find it difficult to turn over in bed because of... |
| Q15 | - |  |  | SI | My appetite is not very good because of my back |
| Q16 | - |  |  | SI | I have trouble putting on my sock (or stockings) b... |
| Q17 | - |  |  | SI | I can only walk short distances because of my back... |
| Q18 | - |  |  | SI | I sleep less well because of my back |
| Q19 | - |  |  | SI | Because of my back pain, I get dressed with the he... |
| Q20 | - |  |  | SI | I sit down for most of the day because of my back |
| Q21 | - |  |  | SI | I avoid heavy jobs around the house because of my ... |
| Q22 | - |  |  | SI | Because of back pain, I am more irritable and bad ... |
| Q23 | - |  |  | SI | Because of my back, I go upstairs more slowly than... |
| Q24 | - |  |  | SI | I stay in bed most of the time because of my back |
| Q25 | - |  |  | SI | The Roland-Morris Disability Questionnaire (RMDQ) ... |
| Q26 | - |  |  | SI | Questionnaire consists of 24 questions which are r... |
| Q27 | - |  |  | SI | Scores under 4 and over 20 may not show significan... |
| Q28 | - |  |  | SI | 0 - 11: No disability |
| Q29 | - |  |  | SI | 12 - 17: Moderate disability |
| Q30 | - |  |  | SI | 18 - 24: Maximum disability |
| Q31 | - |  |  | SI | 0 = No Disability & 24 = Maximum Disability |
| Q32 | - |  |  | SI | Date |
| Q33 | - |  |  | SI | Time |
| Q34 | - |  |  | SI | Score |
| Q35 | - |  |  | SI | Classification |
| Q36 | - |  |  | SI | 0 - 11 |
| Q37 | - |  |  | SI | No disability |
| Q38 | - |  |  | SI | 12 - 17 |
| Q39 | - |  |  | SI | Moderate disability |
| Q40 | - |  |  | SI | 18 - 24 |
| Q41 | - |  |  | SI | Maximum disability |
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