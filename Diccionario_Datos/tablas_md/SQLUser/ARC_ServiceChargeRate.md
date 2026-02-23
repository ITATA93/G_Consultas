# SQLUser.ARC_ServiceChargeRate

**Schema:** SQLUser
**Columnas:** 79
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Arquetipo de configuración**. Definición base del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| RATE_ParRef | bigint | PK |  | NO | ARC_ServiceCharge Parent Reference |
| Q01 | - |  |  | SI | Condición |
| Q02 | - |  |  | SI | Criterios |
| Q03 | - |  |  | SI | Inestabilidad postural que impide realizar la marc... |
| Q04 | - |  |  | SI | Observación |
| Q05 | - |  |  | SI | Amputado |
| Q06 | - |  |  | SI | Observación |
| Q07 | - |  |  | SI | Síndrome post caída |
| Q08 | - |  |  | SI | Observación |
| Q09 | - |  |  | SI | Enfermedad de Parkinson |
| Q10 | - |  |  | SI | Observación |
| Q11 | - |  |  | SI | Demencia en etapa inicial con antecedentes de caíd... |
| Q12 | - |  |  | SI | Observación |
| Q13 | - |  |  | SI | Consideraciones |
| Q14 | - |  |  | SI | Indemnidad de extremidades superiores |
| Q15 | - |  |  | SI | Observación |
| Q16 | - |  |  | SI | Adultos mayores con demencia en etapa inicial requ... |
| Q17 | - |  |  | SI | Observación |
| Q18 | - |  |  | SI | Compromiso moderado a severo del equilibrio |
| Q19 | - |  |  | SI | Observación |
| Q20 | - |  |  | SI | Cuadros de demencia en etapa inicial requerirán su... |
| Q21 | - |  |  | SI | Observación |
| Q22 | - |  |  | SI | No indicar en |
| Q23 | - |  |  | SI | Pacientes con hemiplejia |
| Q24 | - |  |  | SI | Observación |
| Q25 | - |  |  | SI | Otras Observaciones |
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
| RATE_Childsub | double |  |  | NO | Childsub |
| RATE_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| RATE_CreatedDate | date |  |  | SI | Created Date |
| RATE_CreatedTime | time |  |  | SI | Created Time |
| RATE_CreatedUser_DR | bigint |  | FK | SI | Created User |
| RATE_DateFrom | date |  |  | SI | DateFrom |
| RATE_DateTo | date |  |  | SI | DateTo |
| RATE_IPRate | double |  |  | SI | IP Rate |
| RATE_OPRate | double |  |  | SI | OP Rate |
| RATE_RowId | varchar |  |  | NO | - |
| RATE_UpdatedDate | date |  |  | SI | Updated Date |
| RATE_UpdatedTime | time |  |  | SI | Updated Time |
| RATE_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*