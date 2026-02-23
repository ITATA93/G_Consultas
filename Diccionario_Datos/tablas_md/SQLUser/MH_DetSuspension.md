# SQLUser.MH_DetSuspension

**Schema:** SQLUser
**Columnas:** 76
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Detalle de la entidad padre.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SUSP_ParRef | bigint | PK |  | NO | MH_Detention Parent Reference |
| Q1DSinf | - |  |  | SI | Cota Inferior -1DS |
| Q1DSsup | - |  |  | SI | Cota Superior 1DS |
| Q2DSinf | - |  |  | SI | Cota Inferior -2DS |
| Q2DSsup | - |  |  | SI | Cota Superior 2DS |
| Q3DSinf | - |  |  | SI | Cota Inferior -3DS |
| Q3DSsup | - |  |  | SI | Cota Superior 3DS |
| QDias | - |  |  | SI | Edad Corregida en Días |
| QMEDIA | - |  |  | SI | Mediana |
| QMeses | - |  |  | SI | Edad Corregida en Meses |
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
| SUSP_Childsub | double |  |  | NO | Childsub |
| SUSP_Conditions | varchar |  |  | SI | Conditions |
| SUSP_Continuous | varchar |  |  | SI | Continuous |
| SUSP_CreateDate | date |  |  | SI | CreateDate |
| SUSP_CreateTime | time |  |  | SI | CreateTime |
| SUSP_DaysPerMonth | double |  |  | SI | DaysPerMonth |
| SUSP_Deleted | varchar |  |  | SI | Deleted |
| SUSP_EndDate | date |  |  | SI | EndDate |
| SUSP_EndTime | time |  |  | SI | Endime |
| SUSP_GrantedAgent_DR | bigint |  | FK | SI | Des Ref MHCAgent |
| SUSP_GrantedDate | date |  |  | SI | GrantedDate |
| SUSP_GrantedDetAgent_DR | varchar |  | FK | SI | Des Ref MHDetAgent |
| SUSP_GrantedReason | varchar |  |  | SI | GrantedReason |
| SUSP_Hospital_DR | bigint |  | FK | SI | Des Ref CTHospital |
| SUSP_HoursPerDay | double |  |  | SI | HoursPerDay |
| SUSP_HoursPerWeek | double |  |  | SI | HoursPerWeek |
| SUSP_ReasonRevocation | varchar |  |  | SI | ReasonRevocation |
| SUSP_Regime | varchar |  |  | SI | Regime |
| SUSP_ReminderTask_DR | bigint |  | FK | SI | ReminderTask |
| SUSP_RevokedAgent_DR | bigint |  | FK | SI | Des Ref MHCAgent |
| SUSP_RevokedDate | date |  |  | SI | RevokedDate |
| SUSP_RevokedDetAgent_DR | varchar |  | FK | SI | Des Ref MHDetAgent |
| SUSP_RowId | varchar |  |  | NO | - |
| SUSP_StartDate | date |  |  | SI | StartDate |
| SUSP_StartTime | time |  |  | SI | StartTime |
| SUSP_Type_DR | bigint |  | FK | SI | Des Ref MHCSuspensionType |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*