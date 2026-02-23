# SQLUser.MRC_PictureCode

**Schema:** SQLUser
**Columnas:** 76
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Registros Médicos**. Parámetros de historia clínica.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| PIC_RowId | bigint | PK |  | NO | - |
| PIC_Annotated | varchar |  |  | SI | Annotations |
| PIC_BackgroundImageOnly | varchar |  |  | SI | Background Image Only |
| PIC_COPYR_DR | bigint |  | FK | SI | Copyright |
| PIC_CTLOC_DR | bigint |  | FK | SI | Des Ref to CTLOC |
| PIC_Categories | varchar |  |  | SI | Picture Categories |
| PIC_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| PIC_CreatedDate | date |  |  | SI | Created Date |
| PIC_CreatedTime | time |  |  | SI | Created Time |
| PIC_CreatedUser_DR | bigint |  | FK | SI | Created User |
| PIC_DateFrom | date |  |  | SI | Date From |
| PIC_DateTo | date |  |  | SI | Date To |
| PIC_Desc | varchar |  |  | NO | Description |
| PIC_FileName | varchar |  |  | SI | File Name |
| PIC_Owner | varchar |  |  | SI | Owner |
| PIC_StreamData | bigint |  |  | SI | - |
| PIC_UpdatedDate | date |  |  | SI | Updated Date |
| PIC_UpdatedTime | time |  |  | SI | Updated Time |
| PIC_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| PIC_websysDocument | bigint |  |  | SI | websysDocument |
| Q02 | - |  |  | SI | Mes |
| Q03 | - |  |  | SI | Año |
| Q04 | - |  |  | SI | TOTAL ATENCIÓN SOLICITADA 1 |
| Q05 | - |  |  | SI | TOTAL ATENCIÓN SOLICITADA 2 |
| Q06 | - |  |  | SI | RECHAZO 1 |
| Q07 | - |  |  | SI | RECHAZO 2 |
| Q08 | - |  |  | SI | TOTAL ATENCIÓN SOLICITADA 3 |
| Q09 | - |  |  | SI | TOTAL ATENCIÓN SOLICITADA 4 |
| Q10 | - |  |  | SI | RECHAZO 3 |
| Q11 | - |  |  | SI | RECHAZO 4 |
| Q12 | - |  |  | SI | HORARIO NORMAL |
| Q13 | - |  |  | SI | HORARIO CONTINUADO (Vespertina, Sábado) |
| Q14 | - |  |  | SI | TIPO JORNADA |
| Q15 | - |  |  | SI | < 19 Años |
| Q16 | - |  |  | SI | 20 y más |
| QHR | - |  |  | SI | Establecimiento |
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