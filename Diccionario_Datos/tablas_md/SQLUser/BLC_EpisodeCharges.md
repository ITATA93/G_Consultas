# SQLUser.BLC_EpisodeCharges

**Schema:** SQLUser
**Columnas:** 75
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Banco de Sangre**. Gestión de hemoderivados.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ADD_RowId | bigint | PK |  | NO | - |
| ADD_ARCIM_DR | varchar |  | FK | SI | Des Ref ARCIM |
| ADD_AuxilInsurType_DR | bigint |  | FK | SI | Des Ref To ARCAuxilInsurType |
| ADD_BedType_DR | bigint |  | FK | SI | Des Ref Bed Type |
| ADD_CTLOC_DR | bigint |  | FK | SI | Des Ref To CTLOC |
| ADD_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| ADD_CreatedDate | date |  |  | SI | Created Date |
| ADD_CreatedTime | time |  |  | SI | Created Time |
| ADD_CreatedUser_DR | bigint |  | FK | SI | Created User |
| ADD_DateFrom | date |  |  | NO | Date From |
| ADD_DateTo | date |  |  | SI | Date To |
| ADD_EpisSubType_DR | bigint |  | FK | SI | Des Ref Episode SubType |
| ADD_Hospital_DR | bigint |  | FK | SI | Des Ref To CTHospital |
| ADD_InsuranceType_DR | bigint |  | FK | SI | Des Ref To ARCInsuranceType |
| ADD_Owner | varchar |  |  | SI | Owner |
| ADD_Rank | double |  |  | SI | Rank |
| ADD_RoomType_DR | bigint |  | FK | SI | Des Ref Room Type |
| ADD_UpdatedDate | date |  |  | SI | Updated Date |
| ADD_UpdatedTime | time |  |  | SI | Updated Time |
| ADD_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| ChildQ09DR | - |  |  | SI | Child Reference: Plan de intervención Integral |
| Q01 | - |  |  | SI | Lugar de Procedencia |
| Q02 | - |  |  | SI | Fuente de Derivación |
| Q04 | - |  |  | SI | Diagnóstico de Ingreso |
| Q05 | - |  |  | SI | Diagnóstico Actual |
| Q06 | - |  |  | SI | Diagnóstico |
| Q07 | - |  |  | SI | Tratamiento |
| Q08 | - |  |  | SI | Otros |
| Q10 | - |  |  | SI | Fecha de Elaboración |
| Q11 | - |  |  | SI | Fecha de presentación en reunión clínica |
| Q12 | - |  |  | SI | Fecha de presentación a la persona |
| Q13 | - |  |  | SI | Fecha de presentación a la familia y/o red de apoy... |
| Q14 | - |  |  | SI | Fecha 1° revisión por equipo |
| Q15 | - |  |  | SI | Fecha 2° revisión por equipo |
| Q16 | - |  |  | SI | Fecha 3° revisión por equipo |
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