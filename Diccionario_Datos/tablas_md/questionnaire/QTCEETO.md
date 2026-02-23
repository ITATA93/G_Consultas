# questionnaire.QTCEETO

> Evaluación de Terapia Ocupacional

**Schema:** questionnaire
**Columnas:** 113
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Evaluación de Terapia Ocupacional

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Antecedentes/Historia Clínica |
| Q01a | varchar |  |  | SI | Flexión |
| Q01b | varchar |  |  | SI | Flexión |
| Q02 | varchar |  |  | SI | Escala de EVA |
| Q02a | varchar |  |  | SI | Extensión |
| Q02b | varchar |  |  | SI | Extensión |
| Q03 | varchar |  |  | SI | Localización |
| Q03a | varchar |  |  | SI | Abducción |
| Q03b | varchar |  |  | SI | Abducción |
| Q04a | varchar |  |  | SI | Aducción |
| Q04b | varchar |  |  | SI | Aducción |
| Q05a | varchar |  |  | SI | Rot interna |
| Q05b | varchar |  |  | SI | Rot interna |
| Q06a | varchar |  |  | SI | Rot externa |
| Q06b | varchar |  |  | SI | Rot externa |
| Q07 | varchar |  |  | SI | Comentarios |
| Q08a | varchar |  |  | SI | Flexión |
| Q08b | varchar |  |  | SI | Flexión |
| Q09a | varchar |  |  | SI | Extensión |
| Q09b | varchar |  |  | SI | Extensión |
| Q10a | varchar |  |  | SI | Pronación |
| Q10b | varchar |  |  | SI | Pronación |
| Q11a | varchar |  |  | SI | Supinación |
| Q11b | varchar |  |  | SI | Supinación |
| Q12 | varchar |  |  | SI | Comentarios |
| Q13a | varchar |  |  | SI | Flexión |
| Q13b | varchar |  |  | SI | Flexión |
| Q14a | varchar |  |  | SI | Extensión |
| Q14b | varchar |  |  | SI | Extensión |
| Q15a | varchar |  |  | SI | Desv cubital |
| Q15b | varchar |  |  | SI | Desv cubital |
| Q16a | varchar |  |  | SI | Desv Radial |
| Q16b | varchar |  |  | SI | Desv Radial |
| Q17 | varchar |  |  | SI | Comentarios |
| Q18 | varchar |  |  | SI | Puño |
| Q19a | varchar |  |  | SI | Fuerza de Garra |
| Q19b | varchar |  |  | SI | Fuerza de Garra |
| Q20a | varchar |  |  | SI | Fuerza de Pinza |
| Q20b | varchar |  |  | SI | Fuerza de Pinza |
| Q21 | varchar |  |  | SI | Movilidad de EESS |
| Q22 | varchar |  |  | SI | Alineación Postural |
| Q23 | varchar |  |  | SI | Equilibrio Estático y Dinámico |
| Q24 | varchar |  |  | SI | Prehensiones Gruesas y Pinzas |
| Q25 | varchar |  |  | SI | Tono |
| Q26 | varchar |  |  | SI | Sensibilidad Superficial/Profundo |
| Q27 | varchar |  |  | SI | Movilidad de EEII |
| Q28 | varchar |  |  | SI | Deformidad y Calidad de Piel |
| Q28a | varchar |  |  | SI | Fibrosis |
| Q28a1 | varchar |  |  | SI | Hiperplasia |
| Q28a2 | varchar |  |  | SI | Coloración |
| Q28a3 | varchar |  |  | SI | Temperatura |
| Q28a4 | varchar |  |  | SI | Adherencias |
| Q29 | varchar |  |  | SI | Centímetros |
| Q30 | varchar |  |  | SI | Localización |
| Q31 | varchar |  |  | SI | Uso de AT o adaptaciones |
| Q32 | varchar |  |  | SI | Básicas |
| Q33 | varchar |  |  | SI | Instrumentales |
| Q34 | varchar |  |  | SI | Independencia (Barthel/Otra) |
| Q35 | varchar |  |  | SI | Descripción |
| Q36 | varchar |  |  | SI | Se Reincorpora a Misma u Otra Actividad |
| Q37 | varchar |  |  | SI | Tiempo Transcurrido |
| Q38 | varchar |  |  | SI | Manejo en el Hogar/Cuidado de Otros |
| Q39 | varchar |  |  | SI | Tipo de Actividades |
| Q40 | varchar |  |  | SI | Reincorporación a Actividades Anteriores |
| Q41 | varchar |  |  | SI | Nuevas Actividades |
| Q42 | varchar |  |  | SI | Observaciones / Grado de Satisfacción con Proceso |
| Q67 | varchar |  |  | SI | Puño |
| Q68 | varchar |  |  | SI | Movimientos de Hombro |
| Q69 | varchar |  |  | SI | Movimientos de Codo |
| Q70 | varchar |  |  | SI | Movimientos de Muñeca |
| Q71 | varchar |  |  | SI | Movimientos Funcionales de Mano |
| Q72 | varchar |  |  | SI | Evaluación General |
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