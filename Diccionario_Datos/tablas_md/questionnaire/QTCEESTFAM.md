# questionnaire.QTCEESTFAM

> Estructura y Dinámica Familiar

**Schema:** questionnaire
**Columnas:** 70
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Estructura y Dinámica Familiar

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Equipo Responsable |
| Q02 | date |  |  | SI | Fecha de cierre del Estudio de Familia |
| Q07 | varchar |  |  | SI | Síntesis de la dinámica Familiar  |
| Q08 | varchar |  |  | SI | Genograma |
| Q09 | varchar |  |  | SI | Ecomapa |
| Q10 | varchar |  |  | SI | Apgar Familiar |
| Q11 | varchar |  |  | SI | Círculo Familiar |
| Q12 | varchar |  |  | SI | Otro, Especificar |
| Q13 | varchar |  |  | SI | Acerca de la estructura y dinámica familiardel cas... |
| Q14 | varchar |  |  | SI | Subsistemas Observados |
| Q15 | varchar |  |  | SI | Comportamiento del Poder, Autoridad y Jerarquías e... |
| Q16 | varchar |  |  | SI | Coaliciones o Alianzas |
| Q17 | varchar |  |  | SI | Límites |
| Q18 | varchar |  |  | SI | Comunicación |
| Q19 | varchar |  |  | SI | Roles significativo |
| Q20 | varchar |  |  | SI | Normas o Reglas Observadas en la Familia |
| Q21 | varchar |  |  | SI | Dinámica Familiar |
| Q22 | varchar |  |  | SI | Ciclo Vital del caso índice |
| Q23 | varchar |  |  | SI | Ciclo Vital Familiar |
| Q24 | varchar |  |  | SI | Estructura Familiar |
| Q25 | varchar |  |  | SI | Acerca de la Estructura y Dinámica Familiar del Ca... |
| Q26 | varchar |  |  | SI | Breve Síntesis de la historia Familiar |
| Q28 | varchar |  |  | SI | Motivo del Estudio de la Familia |
| Q29 | varchar |  |  | SI | Identificación del Caso |
| Q30 | varchar |  |  | SI | Identificación de la Familia |
| Q31 | varchar |  |  | SI | Tipo de Familia |
| Q32 | numeric |  |  | SI | N° de Ficha Familia |
| Q33 | varchar |  |  | SI | Territorio |
| Q34 | varchar |  |  | SI | Círculo Familiar y Ecomapa |
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