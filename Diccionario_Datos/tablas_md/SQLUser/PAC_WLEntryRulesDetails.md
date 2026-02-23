# SQLUser.PAC_WLEntryRulesDetails

**Schema:** SQLUser
**Columnas:** 89
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Detalle de la entidad padre.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| DET_ParRef | bigint | PK |  | NO | PAC_WaitingListEntryRules Parent Reference |
| DET_AssessIndicator1 | varchar |  |  | SI | AssessmentIndicator1 |
| DET_AssessIndicator2 | varchar |  |  | SI | AssessmentIndicator2 |
| DET_AssessIndicator3 | varchar |  |  | SI | AssessmentIndicator3 |
| DET_AssessIndicator4 | varchar |  |  | SI | AssessmentIndicator4 |
| DET_Childsub | double |  |  | NO | Childsub |
| DET_Code | varchar |  |  | SI | Code |
| DET_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| DET_CreatedDate | date |  |  | SI | Created Date |
| DET_CreatedTime | time |  |  | SI | Created Time |
| DET_CreatedUser_DR | bigint |  | FK | SI | Created User |
| DET_DateFrom | date |  |  | SI | Date From |
| DET_DateTo | date |  |  | SI | Date To |
| DET_Desc | varchar |  |  | SI | Description |
| DET_LocList_DR | bigint |  | FK | SI | Des Ref CTLocationList |
| DET_PrjType | varchar |  |  | SI | PrjType |
| DET_RowId | varchar |  |  | NO | - |
| DET_Sex_DR | bigint |  | FK | SI | Des Ref CTSex |
| DET_UpdatedDate | date |  |  | SI | Updated Date |
| DET_UpdatedTime | time |  |  | SI | Updated Time |
| DET_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| DET_Value1 | varchar |  |  | SI | Value1 |
| DET_Value2 | varchar |  |  | SI | Value2 |
| DET_Value3 | varchar |  |  | SI | Value3 |
| DET_Value4 | varchar |  |  | SI | Value4 |
| DET_Value5 | varchar |  |  | SI | Value5 |
| Q01 | - |  |  | SI | Fecha |
| Q02 | - |  |  | SI | Hora |
| Q03 | - |  |  | SI | Durante el mes pasado, ¿cómo le afectaron los sigu... |
| Q04 | - |  |  | SI | 0 = Sin Problema |
| Q05 | - |  |  | SI | 5 = Problema Severo |
| Q06 | - |  |  | SI | Disfonía u otro problema con su voz |
| Q07 | - |  |  | SI | Carraspera |
| Q08 | - |  |  | SI | Presencia de moco excesivo en su garganta o goteo ... |
| Q09 | - |  |  | SI | Dificultad para deglutir alimentos líquidos o past... |
| Q10 | - |  |  | SI | Tos después de comer o acostarse |
| Q11 | - |  |  | SI | Sensación de ahogo o atrancamiento |
| Q12 | - |  |  | SI | Tos ocasional o en accesos |
| Q13 | - |  |  | SI | Sensación de taco o una aguja en su garganta |
| Q14 | - |  |  | SI | Quemadura retroesternal, dolor en el pecho, indige... |
| Q15 | - |  |  | SI | Score |
| Q16 | - |  |  | SI | Classification |
| Q17 | - |  |  | SI | Score is not indicative of laryngopharyngeal reflu... |
| Q18 | - |  |  | SI | 0 - 13 |
| Q19 | - |  |  | SI | 14 - 45 |
| Q20 | - |  |  | SI | Score is indicative of laryngopharyngeal reflux |
| Q21 | - |  |  | SI | 0 - 13: Indicative of laryngopharyngeal reflux |
| Q22 | - |  |  | SI | 14 - 45: Indicative of laryngopharyngeal reflux |
| Q23 | - |  |  | SI | The Reflux Symptom Index (RSI) is a self-administe... |
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