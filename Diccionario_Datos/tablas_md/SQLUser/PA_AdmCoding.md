# SQLUser.PA_AdmCoding

**Schema:** SQLUser
**Columnas:** 72
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Admisión de Pacientes**. Registra episodios de atención hospitalaria.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| COD_ParRef | bigint | PK |  | NO | PA_Adm Parent Reference |
| COD_AdminCategory_DR | bigint |  | FK | SI | Des Ref AccountClass |
| COD_AutoAssignedFlg | varchar |  |  | SI | Auto Assigned Flag |
| COD_AuxInsType_DR | bigint |  | FK | SI | Des Ref to AuxInsType |
| COD_Bed_DR | varchar |  | FK | SI | Des Ref Bed |
| COD_CTLOC_DR | bigint |  | FK | SI | Des Ref CTLOC |
| COD_CareProv_DR | varchar |  | FK | SI | Des Ref CareProv |
| COD_Childsub | double |  |  | NO | Childsub |
| COD_CommReportedDate | date |  |  | SI | Commissioning Reported Date |
| COD_EndDate | date |  |  | SI | End Date |
| COD_EndTime | time |  |  | SI | End Time |
| COD_InsType_DR | bigint |  | FK | SI | Des Ref to InsType |
| COD_PayByResult | varchar |  |  | SI | Payment By Result |
| COD_RowId | varchar |  |  | NO | - |
| COD_StartDate | date |  |  | SI | Start Date |
| COD_StartTime | time |  |  | SI | Start Time |
| COD_Status | varchar |  |  | SI | Status |
| COD_Transaction_DR | varchar |  | FK | SI | Des Ref Transaction |
| COD_ValidationStatus | varchar |  |  | SI | Validation Status |
| COD_Ward_DR | bigint |  | FK | SI | Des Ref Ward |
| Q01 | - |  |  | SI | Firooz A., Rajabi-Estarabadi A., Zartab H., Hassan... |
| Q02 | - |  |  | SI | In: Humbert P., Fanian F., Maibach H., Agache P. (... |
| Q03 | - |  |  | SI | Grade 1 |
| Q04 | - |  |  | SI | Grade 2 |
| Q05 | - |  |  | SI | Grade 3 |
| Q06 | - |  |  | SI | Grade 4 |
| Q07 | - |  |  | SI | Grade 5 |
| Q08 | - |  |  | SI | Sinclair grade |
| Q09 | - |  |  | SI | Comments |
| Q10 | - |  |  | SI | The Sinclair Scale is a 5 point visual analogue sc... |
| Q11 | - |  |  | SI | Date |
| Q12 | - |  |  | SI | Time |
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