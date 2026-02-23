# SQLUser.ARC_PatientShare

**Schema:** SQLUser
**Columnas:** 66
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Arquetipo de configuración**. Definición base del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| PATSH_RowId | bigint | PK |  | NO | - |
| PATSH_AuxInsType_DR | bigint |  | FK | SI | Des Ref to AuxInsType |
| PATSH_CreatedDate | date |  |  | SI | Created Date |
| PATSH_CreatedTime | time |  |  | SI | Created Time |
| PATSH_CreatedUser_DR | bigint |  | FK | SI | Created User |
| PATSH_DateFrom | date |  |  | SI | Date From |
| PATSH_DateTo | date |  |  | SI | Date To |
| PATSH_IPGovernPerc | double |  |  | SI | IP Govern % |
| PATSH_IPPatPerc | double |  |  | SI | IP Patient % |
| PATSH_InsTyp_DR | bigint |  | FK | SI | Des Ref to ARCInsTyp |
| PATSH_OPGovernPerc | double |  |  | SI | OP Government % |
| PATSH_OPPatPerc | double |  |  | SI | OP Patient % |
| PATSH_UpdatedDate | date |  |  | SI | Updated Date |
| PATSH_UpdatedTime | time |  |  | SI | Updated Time |
| PATSH_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Fecha |
| Q02 | - |  |  | SI | Hora |
| Q03 | - |  |  | SI | Evaluar cada 10 minutos hasta que el puntaje sea&n... |
| Q04 | - |  |  | SI | 1. Conciencia |
| Q05 | - |  |  | SI | 2. Actividad |
| Q06 | - |  |  | SI | 3. Hemodinamia |
| Q07 | - |  |  | SI | 4. Respiración |
| Q08 | - |  |  | SI | 5. Dolor |
| Q09 | - |  |  | SI | 6. Saturación de O2 |
| Q10 | - |  |  | SI | 7. Náuseas y Vómitos |
| Q11 | - |  |  | SI | Observaciones |
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