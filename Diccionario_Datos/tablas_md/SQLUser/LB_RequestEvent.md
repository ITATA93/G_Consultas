# SQLUser.LB_RequestEvent

**Schema:** SQLUser
**Columnas:** 76
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Laboratorio**. Módulo de laboratorio clínico.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBRQE_RowID | bigint | PK |  | NO | - |
| LBRQE_Date | date |  |  | SI | Date of the event |
| LBRQE_Group_DR | bigint |  | FK | SI | Security Group |
| LBRQE_InstrumentSchProcedures | varchar |  |  | SI | Instrument Schedule Procedures  |
| LBRQE_InstrumentSchTestItems | varchar |  |  | SI | Instrument Schedule Test Items  |
| LBRQE_InstrumentScheduleStatus | varchar |  |  | SI | Instrument Schedule Status |
| LBRQE_InstrumentSchedule_DR | bigint |  | FK | SI | Instrument Schedule |
| LBRQE_Instrument_DR | bigint |  | FK | SI | Instrument  |
| LBRQE_LBCTestSets | varchar |  |  | SI | List of LBCTestSets in event |
| LBRQE_LabSiteFrom_DR | bigint |  | FK | SI | From Lab Site |
| LBRQE_LabSiteTo_DR | bigint |  | FK | SI | To Lab Site |
| LBRQE_NewSpcAnatomSite | varchar |  |  | SI | New Anatomical Site |
| LBRQE_NewSpcAnatomSiteQualifier | varchar |  |  | SI | New Anatomical Site Qualifier |
| LBRQE_NewSpcLesion | varchar |  |  | SI | New Lesion |
| LBRQE_OldSpcAnatomSite | varchar |  |  | SI | Old Anatomical Site |
| LBRQE_OldSpcAnatomSiteQualifier | varchar |  |  | SI | Old Anatomical Site Qualifier |
| LBRQE_OldSpcLesion | varchar |  |  | SI | Old Lesion |
| LBRQE_OldSpecimenNumber | varchar |  |  | SI | Old Specimen Number |
| LBRQE_Request_DR | bigint |  | FK | NO | Lab Request |
| LBRQE_SpecimenContainerDetails | varchar |  |  | SI | Request Specimen Container DetailsID List |
| LBRQE_SpecimenContainers | varchar |  |  | SI | List of SpecimenContainer in event |
| LBRQE_TestSets | varchar |  |  | SI | List of affected Request Test Sets |
| LBRQE_Time | time |  |  | SI | Time of the event |
| LBRQE_Type_DR | bigint |  | FK | SI | Type of the event  |
| LBRQE_User_DR | bigint |  | FK | SI | User |
| Q01 | - |  |  | SI | Objetivo Registro |
| Q02 | - |  |  | SI | Dificultad para dormir |
| Q03 | - |  |  | SI | Cansancio al levantarse |
| Q04 | - |  |  | SI | Horas de Sueño |
| Q05 | - |  |  | SI | Conductas que favorecen el descanzo |
| Q06 | - |  |  | SI | Adecuado para la edad |
| Q07 | - |  |  | SI | Especificar |
| Q08 | - |  |  | SI | Diagnostico 1 |
| Q09 | - |  |  | SI | Diagnostico 2 |
| Q10 | - |  |  | SI | Conclusion |
| Q11 | - |  |  | SI | Sueño y Descanso |
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