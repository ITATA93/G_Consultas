# SQLUser.ARC_ItemHosp

**Schema:** SQLUser
**Columnas:** 114
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Arquetipo de configuración**. Definición base del sistema. Items/líneas de detalle.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| HOSP_ParRef | varchar | PK |  | NO | ARC_ItmMast Parent Reference |
| HOSP_Childsub | double |  |  | NO | Childsub |
| HOSP_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| HOSP_CreatedDate | date |  |  | SI | Created Date |
| HOSP_CreatedTime | time |  |  | SI | Created Time |
| HOSP_CreatedUser_DR | bigint |  | FK | SI | Created User |
| HOSP_DateFrom | date |  |  | SI | Date From |
| HOSP_DateTo | date |  |  | SI | Date To |
| HOSP_Hospital_DR | bigint |  | FK | SI | Des Ref Hospital |
| HOSP_RowId | varchar |  |  | NO | - |
| HOSP_UpdatedDate | date |  |  | SI | Updated Date |
| HOSP_UpdatedTime | time |  |  | SI | Updated Time |
| HOSP_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Systolic BP |
| Q01N | - |  |  | SI | Note |
| Q01ObsDR | - |  |  | SI | Systolic BP DR |
| Q03 | - |  |  | SI | Diastolic BP |
| Q03ObsDR | - |  |  | SI | Diastolic BP DR |
| Q04 | - |  |  | SI | Temperature |
| Q04ObsDR | - |  |  | SI | Temperature DR |
| Q05 | - |  |  | SI | Pulse |
| Q05N | - |  |  | SI | Note |
| Q05ObsDR | - |  |  | SI | Pulse DR |
| Q05Q | - |  |  | SI | Pulse quality |
| Q05QObsDR | - |  |  | SI | Pulse quality DR |
| Q05R | - |  |  | SI | Pulse rhythm |
| Q05RObsDR | - |  |  | SI | Pulse rhythm DR |
| Q06 | - |  |  | SI | Respiration |
| Q06ObsDR | - |  |  | SI | Respiration DR |
| Q07 | - |  |  | SI | Mean Arterial Pressure |
| Q08 | - |  |  | SI | Pain cardio |
| Q08ObsDR | - |  |  | SI | Pain cardio DR |
| Q12 | - |  |  | SI | Pacemaker |
| Q12N | - |  |  | SI | Note |
| Q12ObsDR | - |  |  | SI | Pacemaker DR |
| Q14 | - |  |  | SI | Oxygen Saturation |
| Q14ObsDR | - |  |  | SI | Oxygen Saturation DR |
| Q15 | - |  |  | SI | Oxygen l/min |
| Q15N | - |  |  | SI | Note |
| Q15ObsDR | - |  |  | SI | Oxygen l/min DR |
| Q17 | - |  |  | SI | Dyspnoea |
| Q17N | - |  |  | SI | Note |
| Q17ObsDR | - |  |  | SI | Dyspnoea DR |
| Q19 | - |  |  | SI | Superficial |
| Q19N | - |  |  | SI | Note |
| Q19ObsDR | - |  |  | SI | Superficial DR |
| Q21 | - |  |  | SI | Rapid |
| Q21N | - |  |  | SI | Note |
| Q21ObsDR | - |  |  | SI | Rapid DR |
| Q23 | - |  |  | SI | Cough |
| Q23N | - |  |  | SI | Note |
| Q23ObsDR | - |  |  | SI | Cough DR |
| Q25 | - |  |  | SI | Oxygene at home |
| Q25N | - |  |  | SI | Note |
| Q25ObsDR | - |  |  | SI | Oxygene at home DR |
| Q27 | - |  |  | SI | Tracheotomy |
| Q27N | - |  |  | SI | Note |
| Q27ObsDR | - |  |  | SI | Tracheotomy DR |
| Q29 | - |  |  | SI | Paralysis |
| Q29N | - |  |  | SI | Note |
| Q29ObsDR | - |  |  | SI | Paralysis DR |
| Q31 | - |  |  | SI | Amputation |
| Q31N | - |  |  | SI | Note |
| Q31ObsDR | - |  |  | SI | Amputation DR |
| Q33 | - |  |  | SI | Mobilization at home |
| Q33N | - |  |  | SI | Note |
| Q33ObsDR | - |  |  | SI | Mobilization at home DR |
| Q35 | - |  |  | SI | Mobilization |
| Q35N | - |  |  | SI | Note |
| Q35ObsDR | - |  |  | SI | Mobilization DR |
| Q37 | - |  |  | SI | Mobilization limited |
| Q37N | - |  |  | SI | Note |
| Q37ObsDR | - |  |  | SI | Mobilization limited DR |
| Q8N | - |  |  | SI | Note |
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