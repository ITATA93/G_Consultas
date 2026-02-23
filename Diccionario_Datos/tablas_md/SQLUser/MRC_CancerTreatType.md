# SQLUser.MRC_CancerTreatType

**Schema:** SQLUser
**Columnas:** 85
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Tipos/categorías disponibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CANTT_RowId | bigint | PK |  | NO | - |
| CANTT_Code | varchar |  |  | NO | Code |
| CANTT_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| CANTT_CreatedDate | date |  |  | SI | Created Date |
| CANTT_CreatedTime | time |  |  | SI | Created Time |
| CANTT_CreatedUser_DR | bigint |  | FK | SI | Created User |
| CANTT_DateFrom | date |  |  | SI | Date From |
| CANTT_DateTo | date |  |  | SI | Date To |
| CANTT_Desc | varchar |  |  | NO | Description |
| CANTT_Owner | varchar |  |  | SI | Owner |
| CANTT_UpdatedDate | date |  |  | SI | Updated Date |
| CANTT_UpdatedTime | time |  |  | SI | Updated Time |
| CANTT_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Técnica |
| Q02 | - |  |  | SI | Trocar |
| Q03 | - |  |  | SI | Nivel Metámera |
| Q04 | - |  |  | SI | Abordaje |
| Q05 | - |  |  | SI | Infiltración Local |
| Q06 | - |  |  | SI | Descripción |
| Q07 | - |  |  | SI | Observaciones |
| Q08 | - |  |  | SI | Número |
| Q09 | - |  |  | SI | ANANO |
| Q10 | - |  |  | SI | Posición Anestésica |
| Q11 | - |  |  | SI | Parestesis |
| Q12 | - |  |  | SI | Descripción |
| Q13 | - |  |  | SI | Posición Pcte. Inicio Anestesia |
| Q14 | - |  |  | SI | Descripción del Procedimiento |
| Q15 | - |  |  | SI | Técnica |
| Q16 | - |  |  | SI | Espinal punta lápiz |
| Q17 | - |  |  | SI | N° Espinal Punta lápiz |
| Q18 | - |  |  | SI | Tuohy |
| Q19 | - |  |  | SI | N° Tuohy |
| Q20 | - |  |  | SI | Otro |
| Q21 | - |  |  | SI | Texto libre Otro |
| Q22 | - |  |  | SI | Número Catéter |
| Q23 | - |  |  | SI | Direccción |
| Q24 | - |  |  | SI | Introducción |
| Q25 | - |  |  | SI | Sitio Punción |
| Q26 | - |  |  | SI | Registro Aspiración Líquido Céfalo Raquídeo |
| Q27 | - |  |  | SI | Registro Aspiración de sangre |
| Q28 | - |  |  | SI | Drogas se administran por: |
| Q29 | - |  |  | SI | Abordaje |
| Q30 | - |  |  | SI | Infiltración Local |
| Q31 | - |  |  | SI | Fecha Adm Analgesia |
| Q32 | - |  |  | SI | Hora Adm Analgesia |
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