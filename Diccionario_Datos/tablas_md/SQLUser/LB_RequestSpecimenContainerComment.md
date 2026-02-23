# SQLUser.LB_RequestSpecimenContainerComment

**Schema:** SQLUser
**Columnas:** 72
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Laboratorio**. Módulo de laboratorio clínico.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBRQSPCC_ParRef | bigint | PK |  | NO | Parent |
| LBRQSPCC_Reportable | varchar |  |  | SI | Reportable |
| LBRQSPCC_RowID | varchar |  |  | NO | - |
| LBRQSPCC_SpecimenComment_DR | bigint |  | FK | SI | Comment |
| Q01 | - |  |  | SI | Mes |
| Q02 | - |  |  | SI | Año |
| Q03 | - |  |  | SI | N° Total de Servicios |
| Q04 | - |  |  | SI | Unidad Municipal de Personas Mayores |
| Q05 | - |  |  | SI | Unidad Municipal de Atención Social |
| Q06 | - |  |  | SI | Unidad Municipal de Deportes |
| Q07 | - |  |  | SI | Unidad Municipal Turismo |
| Q08 | - |  |  | SI | Unidad Municipal Educación |
| Q09 | - |  |  | SI | Biblioteca Municipal |
| Q10 | - |  |  | SI | Unidad Cultura Municipal |
| Q11 | - |  |  | SI | Otras Unidades Municipales |
| Q12 | - |  |  | SI | Escuelas o Colegios |
| Q13 | - |  |  | SI | Universidades |
| Q14 | - |  |  | SI | Otras Unidades Externas al Municipio |
| Q15 | - |  |  | SI | N° Total de Servicios |
| Q16 | - |  |  | SI | Unidad Municipal de Personas Mayores |
| Q17 | - |  |  | SI | Unidad Municipal de Atención Social |
| Q18 | - |  |  | SI | Unidad Municipal de Deportes |
| Q19 | - |  |  | SI | Unidad Municipal Turismo |
| Q20 | - |  |  | SI | Unidad Municipal Educación |
| Q21 | - |  |  | SI | Biblioteca Municipal |
| Q22 | - |  |  | SI | Unidad Cultura Municipal |
| Q23 | - |  |  | SI | Otras Unidades Municipales |
| Q24 | - |  |  | SI | Escuelas o Colegios |
| Q25 | - |  |  | SI | Universidades |
| Q26 | - |  |  | SI | Otras Unidades Externas al Municipio |
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
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*