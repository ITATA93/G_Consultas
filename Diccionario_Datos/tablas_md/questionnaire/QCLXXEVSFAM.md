# questionnaire.QCLXXEVSFAM

> Evaluación Socio Familiar

**Schema:** questionnaire
**Columnas:** 74
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Evaluación Socio Familiar

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date |  |  | SI | Fecha Evaluación |
| Q02 | time |  |  | SI | Hora Evaluación |
| Q03 | varchar |  |  | SI | Tipo de Familia |
| Q04 | numeric |  |  | SI | Número de Familia Casa o Sitio |
| Q05 | numeric |  |  | SI | Número de Personas |
| Q06 | numeric |  |  | SI | Número de Mujeres |
| Q07 | numeric |  |  | SI | Número de Hombres |
| Q08 | numeric |  |  | SI | Número de Adulto Mayor |
| Q09 | numeric |  |  | SI | Número de Niños |
| Q10 | numeric |  |  | SI | Número de Adolescentes |
| Q11 | numeric |  |  | SI | Número de Menores de 1 Año |
| Q12 | varchar |  |  | SI | Jefatura Hogar |
| Q13 | numeric |  |  | SI | Autónomo Grupo Familiar ($) |
| Q14 | numeric |  |  | SI | Aporte Estado ($) |
| Q15 | varchar |  |  | SI | Total ($) |
| Q16 | varchar |  |  | SI | Tenencia de la Vivienda |
| Q17 | varchar |  |  | SI | Tipo de Vivienda |
| Q18 | numeric |  |  | SI | Número de Dormitorios |
| Q19 | numeric |  |  | SI | Número de Camas |
| Q20 | varchar |  |  | SI | Participación Sub-Sistemas |
| Q21 | varchar |  |  | SI | Factores de Riesgo Otros Integrantes |
| Q22 | varchar |  |  | SI | Existencia de más de una familia dentro de la Vivi... |
| Q23 | varchar |  |  | SI | Existencia de más de una familia dentro del sitio |
| Q24 | varchar |  |  | SI | Comentarios |
| Q25 | varchar |  |  | SI | Antecedentes de Consumo |
| Q26 | varchar |  |  | SI | Comentarios - Antecedentes de Consumo |
| Q27 | varchar |  |  | SI | Antecedentes Judiciales |
| Q28 | varchar |  |  | SI | Materias |
| Q29 | varchar |  |  | SI | Vigentes |
| Q30 | varchar |  |  | SI | Comentarios - Antecedentes Judiciales |
| Q31 | varchar |  |  | SI | Situación Salud Actual |
| Q32 | varchar |  |  | SI | Síntesis Diagnóstica |
| Q33 | varchar |  |  | SI | Profesional Evaluador |
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