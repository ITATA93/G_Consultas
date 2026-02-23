# SQLUser.CT_LocBorrowPref

**Schema:** SQLUser
**Columnas:** 77
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de Ubicaciones**. Servicios, salas, unidades del hospital.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| BORPR_ParRef | bigint | PK |  | NO | CT_Loc Parent Reference |
| BORPR_CTLOC_DR | bigint |  | FK | SI | Des Ref CTLOC |
| BORPR_Childsub | double |  |  | NO | Childsub |
| BORPR_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| BORPR_CreatedDate | date |  |  | SI | Created Date |
| BORPR_CreatedTime | time |  |  | SI | Created Time |
| BORPR_CreatedUser_DR | bigint |  | FK | SI | Created User |
| BORPR_RowId | varchar |  |  | NO | - |
| BORPR_UpdatedDate | date |  |  | SI | Updated Date |
| BORPR_UpdatedTime | time |  |  | SI | Updated Time |
| BORPR_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Síntomas respiratorios (Disnea, tos, sibilancias, ... |
| Q02 | - |  |  | SI | Observaciones Síntomas Respiratorios |
| Q03 | - |  |  | SI | Crisis obstructivas recurrentes |
| Q04 | - |  |  | SI | Observaciones Crisis Obstructivas |
| Q05 | - |  |  | SI | Síntomas diurnos |
| Q06 | - |  |  | SI | Observaciones síntomas diurnos |
| Q07 | - |  |  | SI | Síntomas nocturnos |
| Q08 | - |  |  | SI | Observaciones síntomas nocturnos |
| Q09 | - |  |  | SI | Síntomas Estacionales Primavera-Verano |
| Q10 | - |  |  | SI | Observaciones P-V |
| Q11 | - |  |  | SI | Síntomas Estacionales Otoño-Invierno |
| Q12 | - |  |  | SI | Observaciones O-I |
| Q13 | - |  |  | SI | Tiempo de aparición más 6 meses |
| Q14 | - |  |  | SI | Observaciones Aparición |
| Q15 | - |  |  | SI | Alergenos ocupacionales |
| Q16 | - |  |  | SI | Observaciones Alergenos |
| Q17 | - |  |  | SI | Tos con ejercicio |
| Q18 | - |  |  | SI | Observaciones ejercicio |
| Q19 | - |  |  | SI | Tos con humo |
| Q20 | - |  |  | SI | Observaciones humo |
| Q21 | - |  |  | SI | Tos con frío |
| Q22 | - |  |  | SI | Observaciones frío |
| Q23 | - |  |  | SI | Tos con risa |
| Q24 | - |  |  | SI | Observaciones risa |
| Q25 | - |  |  | SI | Tos con IRA |
| Q26 | - |  |  | SI | Observaciones IRA |
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