# SQLUser.PA_DrugDescription

**Schema:** SQLUser
**Columnas:** 100
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Módulo del Sistema**. Componente interno de TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| DRD_ParRef | bigint | PK |  | NO | PA_PatMas Parent Reference |
| DRD_CTCP_DR | varchar |  | FK | SI | Des Ref CTCP |
| DRD_Childsub | double |  |  | NO | Childsub |
| DRD_DSReportFlag | varchar |  |  | SI | DSReportFlag |
| DRD_Date | date |  |  | SI | Date |
| DRD_Desc | varchar |  |  | SI | Description |
| DRD_DuratDays | double |  |  | SI | Duration in Days |
| DRD_DuratMonth | double |  |  | SI | Duration in Month |
| DRD_DuratYear | double |  |  | SI | Duration in Year |
| DRD_EndDate | date |  |  | SI | EndDate |
| DRD_ErrorReason_DR | bigint |  | FK | SI | Des Ref Error Reason |
| DRD_InActive | varchar |  |  | SI | InActive |
| DRD_Notes | varchar |  |  | SI | Notes |
| DRD_OnsetDate | date |  |  | SI | Onset Date |
| DRD_RowId | varchar |  |  | NO | - |
| DRD_Time | time |  |  | SI | Time |
| DRD_UpdateDate | date |  |  | SI | UpdateDate |
| DRD_UpdateHospital_DR | bigint |  | FK | SI | Des Ref UpdateHospital |
| DRD_UpdateTime | time |  |  | SI | UpdateTime |
| DRD_UpdateUser_DR | bigint |  | FK | SI | Des Ref User |
| Q01 | - |  |  | SI | Note: Scores should reflect the composite effect o... |
| Q02 | - |  |  | SI | Answer each question based on the average occurren... |
| Q03 | - |  |  | SI | How much of your time is occupied by obsessive tho... |
| Q04 | - |  |  | SI | How much do your obsessive thoughts interfere with... |
| Q05 | - |  |  | SI | How much distress do your obsessive thoughts cause... |
| Q06 | - |  |  | SI | How much of an effort do you make to resist the ob... |
| Q07 | - |  |  | SI | How much control do you have over your obsessive t... |
| Q08 | - |  |  | SI | How much time do you spend performing compulsive b... |
| Q09 | - |  |  | SI | How much do your compulsive behaviors interfere wi... |
| Q10 | - |  |  | SI | How anxious would you become if you were prevented... |
| Q11 | - |  |  | SI | How much of an effort do you make to resist the co... |
| Q12 | - |  |  | SI | How much control do you have over the compulsions? |
| Q13 | - |  |  | SI | Yale-Brown Obsessive Compulsive Scale (Y-BOCS) is ... |
| Q14 | - |  |  | SI | 0 - 7: Little or No OCD symptoms |
| Q15 | - |  |  | SI | 8 - 15: Mild OCD symptoms |
| Q16 | - |  |  | SI | 16 - 23: Moderate OCD symptoms |
| Q17 | - |  |  | SI | 24 - 31: Severe OCD symptoms |
| Q18 | - |  |  | SI | 32 - 40: Extreme OCD symptoms |
| Q19 | - |  |  | SI | Obsessive Thoughts Subtotal |
| Q20 | - |  |  | SI | Compulsive Behaviors Subtotal |
| Q21 | - |  |  | SI | Definitions and examples of “Obessions” and “Compu... |
| Q22 | - |  |  | SI | Obsessions are unwelcome or distressing ideas, tho... |
| Q23 | - |  |  | SI | They may seem to occur against your will. |
| Q24 | - |  |  | SI | They may be repugnant to you, are often senseless,... |
| Q25 | - |  |  | SI | (for example, the recurrent thought or impulse to ... |
| Q26 | - |  |  | SI | Compulsions are behaviors or acts that you feel dr... |
| Q27 | - |  |  | SI | At times, you may try to resist doing them, but th... |
| Q28 | - |  |  | SI | You may experience anxiety that does not diminish ... |
| Q29 | - |  |  | SI | Score |
| Q30 | - |  |  | SI | Classification |
| Q31 | - |  |  | SI | 0 - 7 |
| Q32 | - |  |  | SI | Little or No OCD symptoms |
| Q33 | - |  |  | SI | 8 - 15 |
| Q34 | - |  |  | SI | Mild OCD symptoms |
| Q35 | - |  |  | SI | 16 - 23 |
| Q36 | - |  |  | SI | Moderate OCD symptoms |
| Q37 | - |  |  | SI | 24 - 31 |
| Q38 | - |  |  | SI | Severe OCD symptoms |
| Q39 | - |  |  | SI | 32 - 40 |
| Q40 | - |  |  | SI | Extreme OCD symptoms |
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