# questionnaire.QTCEESI

> Índice de Severidad de Emergencias (ESI)

**Schema:** questionnaire
**Columnas:** 66
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Índice de Severidad de Emergencias (ESI)

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Pregunta A: ¿Este paciente presenta una amenaza re... |
| Q02 | varchar |  |  | SI | Pregunta B: ¿Se trata de un paciente que no debe e... |
| Q03 | varchar |  |  | SI | Pregunta C: ¿Cuántos recursos se necesitan para la... |
| Q04 | varchar |  |  | SI | Pregunta D: ¿Signos vitales en zona de riesgo? |
| Q05 | varchar |  |  | SI | ESI |
| Q06 | bit |  |  | SI | Condición 1 |
| Q07 | bit |  |  | SI | Condición 2 |
| Q08 | varchar |  |  | SI | Profesión |
| Q09 | varchar |  |  | SI | Profesional Ejecutor |
| Q10 | varchar |  |  | SI | AVDI |
| Q11 | varchar |  |  | SI | Distrés / ¿situación de alto riesgo?  |
| Q12 | varchar |  |  | SI | Dolor, EVA |
| Q13 | varchar |  |  | SI | Saturometría |
| Q13ObsDR | varchar |  | FK | SI | Saturometría DR |
| Q14 | varchar |  |  | SI | Frecuencia Respiratoria |
| Q14ObsDR | varchar |  | FK | SI | Frecuencia Respiratoria DR |
| Q15 | varchar |  |  | SI | Frecuencia Cardiaca |
| Q15ObsDR | varchar |  | FK | SI | Frecuencia Cardiaca DR |
| Q16 | varchar |  |  | SI | Temperatura |
| Q16ObsDR | varchar |  | FK | SI | Temperatura DR |
| Q17 | bit |  |  | SI | Condición 3 |
| Q18 | varchar |  |  | SI | Esquema de inmunizaciones incompleto |
| Q19 | varchar |  |  | SI | Fiebre de origen no evidente a la evaluación |
| Q20 | bit |  |  | SI | Asignar Nivel de Categorización C4 |
| Q21 | bit |  |  | SI | Asignar Nivel de Categorización C5 |
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