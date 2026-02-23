# SQLUser.ARC_DiscType

**Schema:** SQLUser
**Columnas:** 88
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Arquetipo de configuración**. Definición base del sistema. Tipos/categorías disponibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ARCDI_RowId | bigint | PK |  | NO | - |
| ARCDI_Acct_DR | bigint |  | FK | SI | Des Ref to GLCAC |
| ARCDI_Code | varchar |  |  | NO | Discount Type |
| ARCDI_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| ARCDI_CreatedDate | date |  |  | SI | Created Date |
| ARCDI_CreatedTime | time |  |  | SI | Created Time |
| ARCDI_CreatedUser_DR | bigint |  | FK | SI | Created User |
| ARCDI_Desc | varchar |  |  | NO | Discount Description |
| ARCDI_Owner | varchar |  |  | SI | Owner |
| ARCDI_RcFlag | varchar |  |  | SI | Archived Flag |
| ARCDI_UpdatedDate | date |  |  | SI | Updated Date |
| ARCDI_UpdatedTime | time |  |  | SI | Updated Time |
| ARCDI_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Descripción Examen Físico General |
| Q02 | - |  |  | SI | Presión Arterial Sistólica |
| Q02ObsDR | - |  |  | SI | Presión Arterial Sistólica DR |
| Q03 | - |  |  | SI | Presión Arterial Diastólica |
| Q03ObsDR | - |  |  | SI | Presión Arterial Diastólica DR |
| Q04 | - |  |  | SI | Frecuencia Cardiaca |
| Q04ObsDR | - |  |  | SI | Frecuencia Cardiaca DR |
| Q05 | - |  |  | SI | Frecuencia Respiratoria |
| Q05ObsDR | - |  |  | SI | Frecuencia Respiratoria DR |
| Q06 | - |  |  | SI | Temperatura Axilar |
| Q06ObsDR | - |  |  | SI | Temperatura Axilar DR |
| Q07 | - |  |  | SI | Saturación O2 |
| Q07ObsDR | - |  |  | SI | Saturación O2 DR |
| Q08 | - |  |  | SI | FiO2 |
| Q08ObsDR | - |  |  | SI | FiO2 DR |
| Q09 | - |  |  | SI | Escala del Dolor (EVA) |
| Q09ObsDR | - |  |  | SI | Escala del Dolor (EVA) DR |
| Q10 | - |  |  | SI | Anamnesis Próxima |
| Q11 | - |  |  | SI | Ocupación |
| Q12 | - |  |  | SI | Descripción (SNOMED) |
| Q13 | - |  |  | SI | Motivo de consulta |
| Q14 | - |  |  | SI | Anamnesis Remota |
| Q15 | - |  |  | SI | Flujo |
| Q16 | - |  |  | SI | Peso (kg) |
| Q16ObsDR | - |  |  | SI | Peso (kg) DR |
| Q17 | - |  |  | SI | Talla (cm) |
| Q17ObsDR | - |  |  | SI | Talla (cm) DR |
| Q18 | - |  |  | SI | Circunferencia Craneana (cm) |
| Q18ObsDR | - |  |  | SI | Circunferencia Craneana (cm) DR |
| Q19 | - |  |  | SI | Circunferencia Torácica (cm) |
| Q19ObsDR | - |  |  | SI | Circunferencia Torácica (cm) DR |
| Q20 | - |  |  | SI | Circunferencia Abdominal (cm) |
| Q20ObsDR | - |  |  | SI | Circunferencia Abdominal (cm) DR |
| Q21 | - |  |  | SI | Estado Nutricional |
| Q21ObsDR | - |  |  | SI | Estado Nutricional DR |
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