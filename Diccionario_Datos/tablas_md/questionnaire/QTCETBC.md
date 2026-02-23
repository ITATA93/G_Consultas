# questionnaire.QTCETBC

> Formulario para Envío de Muestras y/o Cultivos Laboratorio  Referencia  Micobacterias

**Schema:** questionnaire
**Columnas:** 84
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Formulario para Envío de Muestras y/o Cultivos Laboratorio  Referencia  Micobacterias

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | NOMBRE |
| Q02 | varchar |  |  | SI | APELLIDO PATERNO |
| Q03 | varchar |  |  | SI | APELLIDO MATERNO |
| Q04 | varchar |  |  | SI | Sexo |
| Q05 | varchar |  |  | SI | RUT |
| Q06 | varchar |  |  | SI | Fecha de Nacimiento |
| Q07 | varchar |  |  | SI | Edad |
| Q08 | varchar |  |  | SI | Nacionalidad |
| Q09 | varchar |  |  | SI | Coinfección Retroviral |
| Q10 | varchar |  |  | SI | Dirección  |
| Q11 | varchar |  |  | SI | Comuna |
| Q12 | varchar |  |  | SI | Ciudad  |
| Q13 | varchar |  |  | SI | Teléfono |
| Q14 | bit |  |  | SI | V.T |
| Q15 | bit |  |  | SI | C.T |
| Q16 | bit |  |  | SI | N° DE MESES C.T. |
| Q17 | bit |  |  | SI | A.T.RECAIDA |
| Q18 | bit |  |  | SI | A.T. ABANDONO |
| Q19 | varchar |  |  | SI | Medicamentos |
| Q20 | varchar |  |  | SI | N° de Muestra |
| Q21 | varchar |  |  | SI | Tipo de Muestra |
| Q22 | date |  |  | SI | Fecha Toma de Muestra |
| Q23 | time |  |  | SI | Hora Toma de Muestra |
| Q24 | date |  |  | SI | Fecha de Envío Muestra |
| Q25 | time |  |  | SI | Hora de Envío Muestra |
| Q26 | varchar |  |  | SI | Baciloscopía |
| Q27 | varchar |  |  | SI | Cultivo |
| Q28 | varchar |  |  | SI | N° de Cultivo |
| Q29 | varchar |  |  | SI | Tipo Muestra del Cultivo |
| Q30 | varchar |  |  | SI | Resultado de Baciloscopia |
| Q31 | date |  |  | SI | Fecha de Siembra Cultivo  |
| Q32 | date |  |  | SI | Fecha de Lectura Cultivo  |
| Q33 | date |  |  | SI | Fecha de Envío Cultivo  |
| Q34 | varchar |  |  | SI | Identificación  |
| Q35 | varchar |  |  | SI | Suceptibilidad |
| Q36 | varchar |  |  | SI | Responsable del Envío |
| Q37 | varchar |  |  | SI | Establecimiento |
| Q38 | varchar |  |  | SI | Teléfono/Red Minsal |
| Q39 | varchar |  |  | SI | E-Mail |
| Q40 | varchar |  |  | SI | Descripción |
| Q41 | varchar |  |  | SI | Técnica |
| Q42 | varchar |  |  | SI | Región |
| Q43 | varchar |  |  | SI | Previsión |
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