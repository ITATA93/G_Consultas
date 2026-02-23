# SQLUser.CT_Acuity

**Schema:** SQLUser
**Columnas:** 70
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de configuración**. Tabla de referencia del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CTACU_RowId | bigint | PK |  | NO | - |
| CTACU_ActivityPoint | double |  |  | SI | Activity Point |
| CTACU_Code | varchar |  |  | NO | Acuity Level Code |
| CTACU_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| CTACU_Colour | varchar |  |  | SI | Colour |
| CTACU_CreatedDate | date |  |  | SI | Created Date |
| CTACU_CreatedTime | time |  |  | SI | Created Time |
| CTACU_CreatedUser_DR | bigint |  | FK | SI | Created User |
| CTACU_DateFrom | date |  |  | SI | Date From |
| CTACU_DateTo | date |  |  | SI | Date To |
| CTACU_Desc | varchar |  |  | NO | Acuity Level Description |
| CTACU_IconName | varchar |  |  | SI | Icon Name |
| CTACU_NationalCode | varchar |  |  | SI | NationalCode |
| CTACU_OPPriority | varchar |  |  | SI | OPPriority |
| CTACU_Owner | varchar |  |  | SI | Owner |
| CTACU_Subregion_DR | bigint |  | FK | SI | Subregion  |
| CTACU_TriageSequence | integer |  |  | SI | Triage Sequence |
| CTACU_UnreasonableTime | double |  |  | SI | Unreasonable Time |
| CTACU_UpdatedDate | date |  |  | SI | Updated Date |
| CTACU_UpdatedTime | time |  |  | SI | Updated Time |
| CTACU_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| CTACU_WaitIcon | varchar |  |  | SI | Wait Icon  |
| CTACU_WaitTime | double |  |  | SI | Waitnig Time (min) |
| CTACU_WarningTime | double |  |  | SI | Warning Time |
| Q01 | - |  |  | SI | Origen Principal de Discapacidad |
| Q02 | - |  |  | SI | Otros Orígenes |
| Q03 | - |  |  | SI | Índice de Discapacidad |
| Q04 | - |  |  | SI | Índice de Desempeño |
| Q05 | - |  |  | SI | Porcentaje de Discapacidad |
| Q06 | - |  |  | SI | Grado de Discapacidad |
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