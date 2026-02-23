# SQLUser.PAC_WLTriageOutcome

**Schema:** SQLUser
**Columnas:** 94
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| WLTRO_RowId | bigint | PK |  | NO | - |
| Q01 | - |  |  | SI | Upper chest retraction |
| Q02 | - |  |  | SI | Lower chest retraction |
| Q03 | - |  |  | SI | Xiphoid retraction |
| Q04 | - |  |  | SI | Nasal dilatation |
| Q05 | - |  |  | SI | Grunt |
| Q06 | - |  |  | SI | 0 - 3: Mild respiratory distress |
| Q07 | - |  |  | SI | 4 - 6: Moderate respiratory distress |
| Q08 | - |  |  | SI | 7 - 9: Impending respiratory failure |
| Q09 | - |  |  | SI | 10: Severe respiratory failure |
| Q10 | - |  |  | SI | The Silverman-Andersen Retraction Score (SAS) is u... |
| Q11 | - |  |  | SI | Score |
| Q12 | - |  |  | SI | Classification |
| Q13 | - |  |  | SI | 0 - 3 |
| Q14 | - |  |  | SI | Mild respiratory distress |
| Q15 | - |  |  | SI | 4 - 6 |
| Q16 | - |  |  | SI | Moderate respiratory distress |
| Q17 | - |  |  | SI | 7 - 9 |
| Q18 | - |  |  | SI | Impending respiratory failure |
| Q19 | - |  |  | SI | 10 |
| Q20 | - |  |  | SI | Severe respiratory failure |
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
| WLTRO_Code | varchar |  |  | NO | Code |
| WLTRO_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| WLTRO_CreatedDate | date |  |  | SI | Created Date |
| WLTRO_CreatedTime | time |  |  | SI | Created Time |
| WLTRO_CreatedUser_DR | bigint |  | FK | SI | Created User |
| WLTRO_DateFrom | date |  |  | SI | Date From |
| WLTRO_DateTo | date |  |  | SI | Date To |
| WLTRO_Desc | varchar |  |  | NO | Description |
| WLTRO_FreeText1 | varchar |  |  | SI | FreeText1 |
| WLTRO_FreeText10 | varchar |  |  | SI | FreeText10 |
| WLTRO_FreeText11 | varchar |  |  | SI | FreeText11 |
| WLTRO_FreeText12 | varchar |  |  | SI | FreeText12 |
| WLTRO_FreeText13 | varchar |  |  | SI | FreeText13 |
| WLTRO_FreeText14 | varchar |  |  | SI | FreeText14 |
| WLTRO_FreeText15 | varchar |  |  | SI | FreeText15 |
| WLTRO_FreeText2 | varchar |  |  | SI | FreeText2 |
| WLTRO_FreeText3 | varchar |  |  | SI | FreeText3 |
| WLTRO_FreeText4 | varchar |  |  | SI | FreeText4 |
| WLTRO_FreeText5 | varchar |  |  | SI | FreeText5 |
| WLTRO_FreeText6 | varchar |  |  | SI | FreeText6 |
| WLTRO_FreeText7 | varchar |  |  | SI | FreeText7 |
| WLTRO_FreeText8 | varchar |  |  | SI | FreeText8 |
| WLTRO_FreeText9 | varchar |  |  | SI | FreeText9 |
| WLTRO_Location_DR | bigint |  | FK | SI | Location |
| WLTRO_NationalCode | varchar |  |  | SI | National Code |
| WLTRO_Owner | varchar |  |  | SI | Owner |
| WLTRO_Questionnaire_DR | bigint |  | FK | SI | Des REf Questionnaire |
| WLTRO_RTTStatus_DR | bigint |  | FK | SI | Des Ref PACRefTreatPathRTTStatus |
| WLTRO_ReasOnList_DR | bigint |  | FK | SI | Location |
| WLTRO_Task_DR | bigint |  | FK | SI | Task |
| WLTRO_UpdatedDate | date |  |  | SI | Updated Date |
| WLTRO_UpdatedTime | time |  |  | SI | Updated Time |
| WLTRO_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*