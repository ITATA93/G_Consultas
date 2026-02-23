# SQLUser.MRC_ShortStayFlag

**Schema:** SQLUser
**Columnas:** 73
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Registros Médicos**. Parámetros de historia clínica.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SHSTFL_RowId | bigint | PK |  | NO | - |
| Q01 | - |  |  | SI | Nombre del Paciente |
| Q02 | - |  |  | SI | Rut |
| Q03 | - |  |  | SI | Edad |
| Q04 | - |  |  | SI | Fecha |
| Q05 | - |  |  | SI | S: Sexo Masculino |
| Q06 | - |  |  | SI | A: Edad < 20 ó >45 años. |
| Q07 | - |  |  | SI | D: Depresión |
| Q08 | - |  |  | SI | P: Tentativa Suicida Previa |
| Q09 | - |  |  | SI | E: Abuso de Alcohol |
| Q10 | - |  |  | SI | R: Falta de Pensamiento Racional (psicosis o trast... |
| Q11 | - |  |  | SI | S. Carencia de Apoyo Social |
| Q12 | - |  |  | SI | O: Plan Organizado de Suicidio |
| Q13 | - |  |  | SI | N: Sin Pareja o Cónyuge |
| Q14 | - |  |  | SI | S: Enfermedad Somática |
| Q15 | - |  |  | SI | Ideación Suicida Activa y/o Persistente |
| Q16 | - |  |  | SI | Falta de Enjuiciamiento del Intento Suicida |
| Q17 | - |  |  | SI | Ausencia de Planes o Proyectos de Futuro |
| Q18 | - |  |  | SI | Resultado SAD Persons |
| Q18ObsDR | - |  |  | SI | Resultado SAD Persons DR |
| Q19 | - |  |  | SI | Hospitalización |
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
| SHSTFL_Code | varchar |  |  | NO | Code |
| SHSTFL_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| SHSTFL_CreatedDate | date |  |  | SI | Created Date |
| SHSTFL_CreatedTime | time |  |  | SI | Created Time |
| SHSTFL_CreatedUser_DR | bigint |  | FK | SI | Created User |
| SHSTFL_DateFrom | date |  |  | SI | Date From |
| SHSTFL_DateTo | date |  |  | SI | Date To |
| SHSTFL_Desc | varchar |  |  | NO | Description |
| SHSTFL_Owner | varchar |  |  | SI | Owner |
| SHSTFL_UpdatedDate | date |  |  | SI | Updated Date |
| SHSTFL_UpdatedTime | time |  |  | SI | Updated Time |
| SHSTFL_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*