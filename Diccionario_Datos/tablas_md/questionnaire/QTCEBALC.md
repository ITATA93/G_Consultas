# questionnaire.QTCEBALC

> Boleta de Alcoholemia

**Schema:** questionnaire
**Columnas:** 85
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Boleta de Alcoholemia

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| CQ33 | varchar |  |  | SI | - |
| CQ39 | varchar |  |  | SI | - |
| CQ6 | varchar |  |  | SI | - |
| Q1 | varchar |  |  | SI | Número o identificación de tubo |
| Q10 | varchar |  |  | SI | Otro |
| Q11 | bit |  |  | SI | Sobrio |
| Q12 | bit |  |  | SI | Aliento Etílico |
| Q13 | bit |  |  | SI | Ebriedad Manifiesta |
| Q14 | bit |  |  | SI | Estado de Coma |
| Q16 | bit |  |  | SI | Prescencia de Drogas old |
| Q17 | varchar |  |  | SI | Otras |
| Q19 | varchar |  |  | SI | RUT o RUN |
| Q2 | date |  |  | SI | Fecha toma de muestra |
| Q20 | varchar |  |  | SI | Persona que tomó la muestra |
| Q21 | varchar |  |  | SI | N° de parte policial |
| Q22 | varchar |  |  | SI | Fiscalía o tribunal receptor del parte |
| Q3 | time |  |  | SI | Hora de la toma de muestra |
| Q30 | bit |  |  | SI | Rechaza toma de muestra old |
| Q31 | time |  |  | SI | Hora del suceso que motiva el Exámen |
| Q33 | varchar |  |  | SI | Apreciación Clínica |
| Q34 | varchar |  |  | SI | Comisaria |
| Q35 | varchar |  |  | SI | Comuna |
| Q36 | varchar |  |  | SI | Número de Boleta |
| Q37 | varchar |  |  | SI | Provincia |
| Q38 | varchar |  |  | SI | Condición en el tránsito de la persona a quien se ... |
| Q39 | varchar |  |  | SI | Grado de Ebriedad old |
| Q4 | varchar |  |  | SI | Nombre Completo |
| Q40 | numeric |  |  | SI | Año |
| Q41 | date |  |  | SI | Fecha y hora del suceso que motiva el examen |
| Q42 | varchar |  |  | SI | Nombre |
| Q43 | varchar |  |  | SI | Comisaría o unidad policial emisora del parte |
| Q44 | varchar |  |  | SI | Respecto del grado de ebriedad |
| Q45 | varchar |  |  | SI | Presencia de TEC |
| Q46 | varchar |  |  | SI | Presencia de Drogas |
| Q47 | varchar |  |  | SI | Rechaza Toma de Muestra |
| Q5 | varchar |  |  | SI | Cédula de Identidad N° |
| Q6 | varchar |  |  | SI | Sexo |
| Q7 | varchar |  |  | SI | Edad |
| Q8 | bit |  |  | SI | Peatón |
| Q9 | bit |  |  | SI | Conductor |
| QCPN | varchar |  |  | SI | N° placa func. policial |
| QHospitalDR | varchar |  | FK | SI | Hospital ID |
| QNOMED | varchar |  |  | SI | Nombre del Médico |
| QOB | bit |  |  | SI | Presenta TEC old |
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