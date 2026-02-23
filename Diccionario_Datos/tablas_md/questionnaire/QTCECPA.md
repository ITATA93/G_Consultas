# questionnaire.QTCECPA

> Cedazo Presión Arterial

**Schema:** questionnaire
**Columnas:** 90
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Cedazo Presión Arterial

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | P° Palpatoria - Brazo |
| Q02 | numeric |  |  | SI | P° Palpatoria - PAS |
| Q03 | numeric |  |  | SI | P° Palpatoria - PAD |
| Q04 | varchar |  |  | SI | 1° Medición - Brazo |
| Q05 | numeric |  |  | SI | 1° Medición - PAS |
| Q06 | numeric |  |  | SI | 1° Medición - PAD |
| Q07 | varchar |  |  | SI | 2° Medición - Brazo |
| Q08 | numeric |  |  | SI | 2° Medición - PAS |
| Q09 | numeric |  |  | SI | 2° Medición - PAD |
| Q10 | varchar |  |  | SI | 3° Medición - Brazo |
| Q11 | numeric |  |  | SI | 3° Medición - PAS |
| Q12 | numeric |  |  | SI | 3° Medición - PAD |
| Q13 | varchar |  |  | SI | 4° Medición de Pié - Brazo	 |
| Q14 | numeric |  |  | SI | 4° Medición de Pié - PAS |
| Q15 | numeric |  |  | SI | 4° Medición de Pié - PAD |
| Q16 | varchar |  |  | SI | Promedio Primer Perfil PAS Estabilizada	 |
| Q17 | varchar |  |  | SI | Promedio Primer Perfil PAD Estabilizada |
| Q18 | varchar |  |  | SI | Responsable Primer Perfil |
| Q19 | date |  |  | SI | Fecha Primer Perfil |
| Q20 | varchar |  |  | SI | 1° Medición - Brazo |
| Q21 | numeric |  |  | SI | 1° Medición - PAS |
| Q22 | numeric |  |  | SI | 1° Medición - PAD |
| Q23 | varchar |  |  | SI | 2° Medición - Brazo |
| Q24 | numeric |  |  | SI | 2° Medición - PAS |
| Q25 | numeric |  |  | SI | 2° Medición - PAD |
| Q26 | varchar |  |  | SI | 3° Medición - Brazo |
| Q27 | numeric |  |  | SI | 3° Medición - PAS |
| Q28 | numeric |  |  | SI | 3° Medición - PAD |
| Q29 | varchar |  |  | SI | Promedio Segundo Perfil PAS Estabilizada |
| Q30 | varchar |  |  | SI | Promedio Segundo Perfil PAD Estabilizada  |
| Q31 | varchar |  |  | SI | Responsable Segundo Perfil |
| Q32 | date |  |  | SI | Fecha Segundo Perfil |
| Q33 | varchar |  |  | SI | 1° Medición - Brazo |
| Q34 | numeric |  |  | SI | 1° Medición - PAS |
| Q35 | numeric |  |  | SI | 1° Medición - PAD |
| Q36 | varchar |  |  | SI | 2° Medición - Brazo |
| Q37 | numeric |  |  | SI | 2° Medición - PAS |
| Q38 | numeric |  |  | SI | 2° Medición - PAD |
| Q39 | varchar |  |  | SI | 3° Medición - Brazo |
| Q40 | numeric |  |  | SI | 3° Medición - PAS |
| Q41 | numeric |  |  | SI | 3° Medición - PAD |
| Q42 | varchar |  |  | SI | Promedio Tercer Perfil PAS Estabilizada	 |
| Q43 | varchar |  |  | SI | Promedio Tercer Perfil PAD Estabilizada  |
| Q44 | varchar |  |  | SI | Responsable Tercer Perfil |
| Q45 | date |  |  | SI | Fecha Tercer Perfil |
| Q46 | varchar |  |  | SI | PROMEDIO DE PERFILES DE PRESION ARTERIAL DIASTÓLIC... |
| Q47 | varchar |  |  | SI | PROMEDIO DE PERFILES DE PRESION ARTERIAL SISTÓLICA |
| Q48 | varchar |  |  | SI | RESULTADO |
| Q49 | varchar |  |  | SI | CONDUCTA |
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