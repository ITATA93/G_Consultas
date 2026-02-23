# SQLUser.ARC_PayAgreemPackage

**Schema:** SQLUser
**Columnas:** 78
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Pagos**. Tarifas y facturación.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| PK_ParRef | bigint | PK |  | NO | ARC_PaymentAgreement Parent Reference |
| PK_Childsub | double |  |  | NO | Childsub |
| PK_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| PK_CreatedDate | date |  |  | SI | Created Date |
| PK_CreatedTime | time |  |  | SI | Created Time |
| PK_CreatedUser_DR | bigint |  | FK | SI | Created User |
| PK_DateFrom | date |  |  | SI | DateFrom |
| PK_DateTo | date |  |  | SI | DateTo |
| PK_FixedPrice | double |  |  | SI | FixedPrice |
| PK_NumberOfDays | double |  |  | SI | NumberOfDays |
| PK_NumberOfVisits | varchar |  |  | SI | NumberOfVisits |
| PK_Repeat | varchar |  |  | SI | Repeat |
| PK_RowId | varchar |  |  | NO | - |
| PK_UpdatedDate | date |  |  | SI | Updated Date |
| PK_UpdatedTime | time |  |  | SI | Updated Time |
| PK_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Fecha de Ingreso UTO |
| Q02 | - |  |  | SI | Fecha de Egreso UTO |
| Q03 | - |  |  | SI | Fecha de Aplicación |
| Q04 | - |  |  | SI | Tipo de Residencia |
| Q05 | - |  |  | SI | Condición Económica |
| Q06 | - |  |  | SI | Patología Psiquiátrica/Adicciones |
| Q07 | - |  |  | SI | Redes de Apoyo |
| Q08 | - |  |  | SI | Disponibilidad Cuidador |
| Q09 | - |  |  | SI | Grado de protección social a entregar por el estad... |
| Q10 | - |  |  | SI | Trabajador/a Social |
| Q11 | - |  |  | SI | Tipos de Dependencia Social |
| Q12 | - |  |  | SI | Alta dependencia social - Riesgo Severo |
| Q13 | - |  |  | SI | Mediana dependencia social - Riesgo Moderado |
| Q14 | - |  |  | SI | Baja o Nula dependencia social - Riesgo Leve |
| Q15 | - |  |  | SI | Rangos de Clasificación |
| Q16 | - |  |  | SI | 11 a 15 |
| Q17 | - |  |  | SI | 6 a 10 |
| Q18 | - |  |  | SI | 1 a 5 |
| Q19 | - |  |  | SI | Grados de protección Social a entregar por el Esta... |
| Q20 | - |  |  | SI | Alta |
| Q21 | - |  |  | SI | Mediana |
| Q22 | - |  |  | SI | Baja |
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