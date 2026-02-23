# SQLUser.PAC_NationalPPP

**Schema:** SQLUser
**Columnas:** 81
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| NPPP_RowId | bigint | PK |  | NO | - |
| NPPP_Code | varchar |  |  | NO | Code |
| NPPP_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| NPPP_CreatedDate | date |  |  | SI | Created Date |
| NPPP_CreatedTime | time |  |  | SI | Created Time |
| NPPP_CreatedUser_DR | bigint |  | FK | SI | Created User |
| NPPP_Desc | varchar |  |  | NO | Description |
| NPPP_EndDate | date |  |  | SI | End Date |
| NPPP_Owner | varchar |  |  | SI | Owner |
| NPPP_StartDate | date |  |  | SI | Start Date |
| NPPP_StatutoryReportable | varchar |  |  | SI | Statutory Reportable |
| NPPP_UpdatedDate | date |  |  | SI | Updated Date |
| NPPP_UpdatedTime | time |  |  | SI | Updated Time |
| NPPP_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Depressed mood |
| Q02 | - |  |  | SI | Feelings of guilt |
| Q03 | - |  |  | SI | Suicide |
| Q04 | - |  |  | SI | Insomnia - Initial |
| Q05 | - |  |  | SI | Insomnia - Middle |
| Q06 | - |  |  | SI | Insomnia - Delayed |
| Q07 | - |  |  | SI | Work and interests |
| Q08 | - |  |  | SI | Retardation |
| Q09 | - |  |  | SI | Agitation |
| Q10 | - |  |  | SI | Anxiety - Psychic |
| Q11 | - |  |  | SI | Anxiety-Somatic |
| Q12 | - |  |  | SI | Somatic symptoms - Gastrointestinal |
| Q13 | - |  |  | SI | Somatic symptoms - General |
| Q14 | - |  |  | SI | Genital symptoms |
| Q15 | - |  |  | SI | Hypochondriasis |
| Q16 | - |  |  | SI | Weight loss |
| Q17 | - |  |  | SI | Insight |
| Q18 | - |  |  | SI | Score 0 - 7: Normal |
| Q19 | - |  |  | SI | Score 8 - 13: Mild Depression |
| Q20 | - |  |  | SI | Score 14 - 18: Moderate Depression |
| Q21 | - |  |  | SI | Score 19 - 22: Severe Depression |
| Q22 | - |  |  | SI | Score > 23: Very Severe Depression |
| Q23 | - |  |  | SI | The Hamilton Depression Rating Scale (HAM-D) is us... |
| Q24 | - |  |  | SI | The standard version of the HAM-D is designed to b... |
| Q25 | - |  |  | SI | The scale contains 17 items rated on either a 3- o... |
| Q26 | - |  |  | SI | Date |
| Q27 | - |  |  | SI | Time |
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