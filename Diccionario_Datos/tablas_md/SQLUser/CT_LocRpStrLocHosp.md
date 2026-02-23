# SQLUser.CT_LocRpStrLocHosp

**Schema:** SQLUser
**Columnas:** 93
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de Ubicaciones**. Servicios, salas, unidades del hospital.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LOCHOSP_ParRef | bigint | PK |  | NO | CT_LocReportStructure Parent Reference |
| LOCHOSP_Childsub | double |  |  | NO | Childsub |
| LOCHOSP_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| LOCHOSP_CreatedDate | date |  |  | SI | Created Date |
| LOCHOSP_CreatedTime | time |  |  | SI | Created Time |
| LOCHOSP_CreatedUser_DR | bigint |  | FK | SI | Created User |
| LOCHOSP_DateFrom | date |  |  | SI | Date From |
| LOCHOSP_DateTo | date |  |  | SI | Date To |
| LOCHOSP_Hospital_DR | bigint |  | FK | SI | Des Ref CTHospital |
| LOCHOSP_Loc_DR | bigint |  | FK | SI | Des Ref CTLoc |
| LOCHOSP_RowId | varchar |  |  | NO | - |
| LOCHOSP_UpdatedDate | date |  |  | SI | Updated Date |
| LOCHOSP_UpdatedTime | time |  |  | SI | Updated Time |
| LOCHOSP_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Have you ever smoked |
| Q02 | - |  |  | SI | How many cigarettes a day do you smoke |
| Q03 | - |  |  | SI | CO level taken |
| Q03A | - |  |  | SI | CO Level |
| Q03AObsDR | - |  |  | SI | CO Level DR |
| Q04 | - |  |  | SI | Referral to stop smoking service |
| Q04T | - |  |  | SI | Other action taken |
| Q05 | - |  |  | SI | Does your partner smoke |
| Q06 | - |  |  | SI | Cigarettes per day |
| Q07 | - |  |  | SI | Are there other smokers in the household |
| Q07T | - |  |  | SI | Details |
| Q08 | - |  |  | SI | How many units of alcohol did you drink before pre... |
| Q09 | - |  |  | SI | How many units of alcohol do you drink now |
| Q10 | - |  |  | SI | When did you stop drinking alcohol |
| Q11 | - |  |  | SI | Action taken for alcohol use |
| Q11A | - |  |  | SI | Action taken |
| Q11T | - |  |  | SI | Details |
| Q12 | - |  |  | SI | Have you used any substances before becoming pregn... |
| Q12A | - |  |  | SI | Substances used |
| Q12T | - |  |  | SI | Details |
| Q13 | - |  |  | SI | Are you using any substances currently |
| Q13A | - |  |  | SI | Substances used |
| Q13T | - |  |  | SI | Details |
| Q14 | - |  |  | SI | Action taken for current substance use |
| Q14A | - |  |  | SI | Action taken |
| Q14T | - |  |  | SI | Details |
| Q15 | - |  |  | SI | IV drug user |
| Q15T | - |  |  | SI | Details |
| Q28 | - |  |  | SI | How many units of alcohol does your partner drink ... |
| Q28ObsDR | - |  |  | SI | How many units of alcohol does your partner drink ... |
| Q29 | - |  |  | SI | Does you partner currently use any oral street dru... |
| Q29ObsDR | - |  |  | SI | Does you partner currently use any oral street dru... |
| Q30 | - |  |  | SI | Does your current partner ever inject drugs |
| Q30ObsDR | - |  |  | SI | Does your current partner ever inject drugs DR |
| Q31 | - |  |  | SI | Carbon Monoxide (Exhaled Breath) |
| Q31ObsDR | - |  |  | SI | Carbon Monoxide (Exhaled Breath) DR |
| Q32 | - |  |  | SI | Date |
| Q33 | - |  |  | SI | Time |
| Q34 | - |  |  | SI | ppm |
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