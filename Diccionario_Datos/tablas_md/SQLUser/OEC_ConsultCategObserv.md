# SQLUser.OEC_ConsultCategObserv

**Schema:** SQLUser
**Columnas:** 78
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Entry Orders**. Tipos y estados de órdenes.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| OBS_ParRef | bigint | PK |  | NO | OEC_ConsultCateg Parent Reference |
| OBS_Childsub | double |  |  | NO | Childsub |
| OBS_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| OBS_CreatedDate | date |  |  | SI | Created Date |
| OBS_CreatedTime | time |  |  | SI | Created Time |
| OBS_CreatedUser_DR | bigint |  | FK | SI | Created User |
| OBS_ObservGroup_DR | bigint |  | FK | SI | Des Ref ObservGroup |
| OBS_RowId | varchar |  |  | NO | - |
| OBS_UpdatedDate | date |  |  | SI | Updated Date |
| OBS_UpdatedTime | time |  |  | SI | Updated Time |
| OBS_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Safety checks |
| Q02 | - |  |  | SI | Invasive lines |
| Q03 | - |  |  | SI | Patient ID |
| Q04 | - |  |  | SI | Allergies reviewed |
| Q05 | - |  |  | SI | Clinical handover received from |
| Q06 | - |  |  | SI | Note |
| Q07 | - |  |  | SI | ETT length at lip |
| Q07ObsDR | - |  |  | SI | ETT length at lip DR |
| Q08 | - |  |  | SI | PA catheter length |
| Q08ObsDR | - |  |  | SI | PA catheter length DR |
| Q09 | - |  |  | SI | Does the Patient have 2 ID bands? |
| Q10 | - |  |  | SI | Yankauer sucker changed |
| Q11 | - |  |  | SI | Heat and moisture exchange filter changed |
| Q12 | - |  |  | SI | In-Line circuit |
| Q13 | - |  |  | SI | Humidified circuit |
| Q14 | - |  |  | SI | Arterial line |
| Q15 | - |  |  | SI | Central line |
| Q16 | - |  |  | SI | ICP catheter |
| Q17 | - |  |  | SI | PA catheter |
| Q18 | - |  |  | SI | Due date |
| Q19 | - |  |  | SI | Due date |
| Q20 | - |  |  | SI | Due date |
| Q21 | - |  |  | SI | Due date |
| Q22 | - |  |  | SI | Pacemaker |
| Q23 | - |  |  | SI | Date |
| Q24 | - |  |  | SI | Time |
| Q25 | - |  |  | SI | Invasive devices reviewed and documented |
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