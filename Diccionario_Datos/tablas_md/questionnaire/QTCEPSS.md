# questionnaire.QTCEPSS

> Epworth Sleepiness Scale

**Schema:** questionnaire
**Columnas:** 72
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Epworth Sleepiness Scale

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Situación |
| Q02 | varchar |  |  | SI | Probabilidad de cabecear o quedarse dormido |
| Q03 | varchar |  |  | SI | Sentado leyendo un periódico, una revista, un libr... |
| Q04 | varchar |  |  | SI | Viendo televisión |
| Q05 | varchar |  |  | SI | Sentado inactivo en un lugar público (cine, reunió... |
| Q06 | varchar |  |  | SI | En auto, como pasajero en un viaje de una hora sin... |
| Q07 | varchar |  |  | SI | Recostado descansando en la tarde, cuando las circ... |
| Q08 | varchar |  |  | SI | Sentado y conversando con alguien |
| Q09 | varchar |  |  | SI | Sentado y tranquilo después de almuerzo (sin tomar... |
| Q10 | varchar |  |  | SI | En auto, detenido por unos minutos&nbsp;por&nbsp;e... |
| Q11 | varchar |  |  | SI | Puntaje |
| Q12 | varchar |  |  | SI | Clasificación |
| Q13 | varchar |  |  | SI | ¿Qué probabilidad hay de que usted se quede dormid... |
| Q14 | varchar |  |  | SI | Esto se refiere a tu estilo de vida habitual en lo... |
| Q15 | varchar |  |  | SI | Utilice esta escala para elegir la opción&nbsp;más... |
| Q16 | varchar |  |  | SI | La puntuación de la Escala de Somnolencia de Epwor... |
| Q17 | varchar |  |  | SI | 0-5 |
| Q18 | varchar |  |  | SI | Somnolencia diurna normal baja |
| Q19 | varchar |  |  | SI | 6-10 |
| Q20 | varchar |  |  | SI | Somnolencia diurna normal alta |
| Q21 | varchar |  |  | SI | 11-12 |
| Q22 | varchar |  |  | SI | Somnolencia diurna leve y excesiva |
| Q23 | varchar |  |  | SI | 13-15 |
| Q24 | varchar |  |  | SI | Somnolencia diurna excesiva y moderada |
| Q25 | varchar |  |  | SI | 16-24 |
| Q26 | varchar |  |  | SI | Somnolencia diurna excesiva y grave |
| Q27 | date |  |  | SI | Fecha |
| Q28 | time |  |  | SI | Hora |
| Q30 | varchar |  |  | SI | El Dr. Murray Johns desarrolló por primera vez la ... |
| Q31 | varchar |  |  | SI | La ESE-CHAD está sujeta a derechos de autor (© MW ... |
| Q32 | varchar |  |  | SI | Johns MW. Un nuevo método para medir la somnolenci... |
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