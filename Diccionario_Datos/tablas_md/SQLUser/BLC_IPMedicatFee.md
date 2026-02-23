# SQLUser.BLC_IPMedicatFee

**Schema:** SQLUser
**Columnas:** 62
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Banco de Sangre**. Gestión de hemoderivados.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| IPMFEE_RowId | bigint | PK |  | NO | - |
| ChildQ04DR | - |  |  | SI | Child Reference: FAMILIAR |
| IPMFEE_CreatedDate | date |  |  | SI | Created Date |
| IPMFEE_CreatedTime | time |  |  | SI | Created Time |
| IPMFEE_CreatedUser_DR | bigint |  | FK | SI | Created User |
| IPMFEE_DateFrom | date |  |  | SI | Date From |
| IPMFEE_DateTo | date |  |  | SI | Date To |
| IPMFEE_FixedAmt | double |  |  | SI | Fixed Amt |
| IPMFEE_InsType_DR | bigint |  | FK | SI | Des Ref InsType_DR |
| IPMFEE_UpdatedDate | date |  |  | SI | Updated Date |
| IPMFEE_UpdatedTime | time |  |  | SI | Updated Time |
| IPMFEE_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Fecha Elaboración |
| Q07 | - |  |  | SI | Psiquiatra |
| Q08 | - |  |  | SI | Psicólogo/a |
| Q09 | - |  |  | SI | Terapeuta Ocupacional |
| Q10 | - |  |  | SI | Enfermero/a |
| Q11 | - |  |  | SI | Trabajador Social |
| Q12 | - |  |  | SI | Técnico en Rehabilitación |
| Q13 | - |  |  | SI | Fecha Evaluación |
| Q14 | - |  |  | SI | Hora Elaboración |
| Q15 | - |  |  | SI | Hora Evaluación |
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