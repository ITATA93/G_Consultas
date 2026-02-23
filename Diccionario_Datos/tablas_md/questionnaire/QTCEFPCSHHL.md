# questionnaire.QTCEFPCSHHL

> Formulario para confirmación serológica hidatidosis humana laboratorio clínico.

**Schema:** questionnaire
**Columnas:** 76
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Formulario para confirmación serológica hidatidosis humana laboratorio clínico.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Nombres |
| Q02 | varchar |  |  | SI | Apellido Paterno |
| Q03 | varchar |  |  | SI | Apellido Materno |
| Q04 | date |  |  | SI | Fecha Envío |
| Q05 | varchar |  |  | SI | Rut |
| Q06 | varchar |  |  | SI | Fecha de Nacimiento |
| Q07 | varchar |  |  | SI | Sexo |
| Q08 | varchar |  |  | SI | Previsión |
| Q09 | varchar |  |  | SI | Dirección |
| Q10 | varchar |  |  | SI | Teléfono |
| Q11 | varchar |  |  | SI | Profesional Responsable |
| Q12 | varchar |  |  | SI | Establecimiento |
| Q13 | varchar |  |  | SI | Unidad |
| Q14 | varchar |  |  | SI | Dirección |
| Q15 | varchar |  |  | SI | Ciudad |
| Q16 | varchar |  |  | SI | Teléfono |
| Q17 | varchar |  |  | SI | Fax |
| Q18 | varchar |  |  | SI | Correo |
| Q19 | date |  |  | SI | Fecha Obtención |
| Q20 | varchar |  |  | SI | Tipo de Muestra |
| Q21 | time |  |  | SI | Hora Obteción |
| Q22 | bit |  |  | SI | ELISA |
| Q23 | varchar |  |  | SI | Otra |
| Q24 | varchar |  |  | SI | Resultado |
| Q25 | varchar |  |  | SI | Lectura |
| Q26 | varchar |  |  | SI | Punto Corte |
| Q27 | varchar |  |  | SI | Marca Comercial |
| Q28 | varchar |  |  | SI | Lote |
| Q29 | varchar |  |  | SI | Antecedentes Clínico / Epidemiologico |
| Q30 | varchar |  |  | SI | Técnica Realizada |
| Q31 | varchar |  |  | SI | Tipo de Muestra |
| Q32 | varchar |  |  | SI | Resultado |
| Q33 | varchar |  |  | SI | Tipo de Muestra |
| Q34 | varchar |  |  | SI | Técnica Realizada |
| Q35 | varchar |  |  | SI | Resultado |
| QUESAnaDR | varchar |  | FK | SI | Anaesthesia |
| QUESAnaOperationDR | varchar |  | FK | SI | Operation |
| QUESConsultDR | varchar |  | FK | SI | Consult |
| QUESCopiedComments | varchar |  |  | SI | Copied Comments |
| QUESCopiedDate | date |  |  | SI | Copied Date |
| QUESCopiedEpDR | bigint |  | FK | SI | Copied Episode |
| QUESCopiedSourceDR | bigint |  | FK | SI | Copied Source DR |
| QUESCopiedTime | time |  |  | SI | Copied Time |
| QUESCopiedUserDR | bigint |  | FK | SI | Copied User |
| QUESCreateDate | date |  |  | SI | Creation Date |
| QUESCreateTime | time |  |  | SI | Creation Time |
| QUESCreateUserDR | bigint |  | FK | SI | Creation User |
| QUESDate | date |  |  | SI | Last Update Date |
| QUESErrorReasonDR | bigint |  | FK | SI | Error Reason |
| QUESFHResidentDR | bigint |  | FK | SI | Resident |
| QUESMRClinicalPathWaysDR | varchar |  | FK | SI | Clinical Pathway |
| QUESNRCarePlanIssuesDR | varchar |  | FK | SI | Nurse Care Plan Issues |
| QUESOEOrdExecDR | varchar |  | FK | SI | Order Execution |
| QUESORPreanaestheticConsultDR | bigint |  | FK | SI | Preanaesthetic Consultation |
| QUESObsEntryDR | varchar |  | FK | SI | Observation Entry |
| QUESOperRoomDR | bigint |  | FK | SI | Operating Room |
| QUESPAAdmDR | bigint |  | FK | SI | Admission |
| QUESPAAdverseEventDR | varchar |  | FK | SI | Adverse Event |
| QUESPAPatMasDR | bigint |  | FK | SI | Patient |
| QUESPAPregnancyDR | bigint |  | FK | SI | Pregnancy |
| QUESPAWaitingListDR | bigint |  | FK | SI | Waiting List |
| QUESPathwayItemDR | varchar |  | FK | SI | Pathway Item |
| QUESPrePostExamOEOrdItemDR | varchar |  | FK | SI | Pre/Post Exam OrdItem |
| QUESRBAppointmentDR | varchar |  | FK | SI | Appointments |
| QUESRBApptOutcomeDR | varchar |  | FK | SI | Appointment Outcome |
| QUESRBApptSlotDR | varchar |  | FK | SI | Appointment Slot |
| QUESReasonForCorrectionDR | bigint |  | FK | SI | Reason for Correction |
| QUESSSUserDefWindowDR | bigint |  | FK | SI | Questionnaire |
| QUESScore | varchar |  |  | SI | Score |
| QUESSecondUserDR | bigint |  | FK | SI | Second Signature |
| QUESStatusDR | bigint |  | FK | SI | Status |
| QUESTextResultDR | bigint |  | FK | SI | Text Result |
| QUESTime | time |  |  | SI | Last Update Time |
| QUESTransactionDR | varchar |  | FK | SI | Transaction |
| QUESUserDR | bigint |  | FK | SI | Last Update User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*