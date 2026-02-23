# questionnaire.QCLXXCADO

> Evaluación Crecimiento Adolescente

**Schema:** questionnaire
**Columnas:** 83
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Evaluación Crecimiento Adolescente

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Peso |
| Q01ObsDR | varchar |  | FK | SI | Peso DR |
| Q02 | varchar |  |  | SI | Talla |
| Q02ObsDR | varchar |  | FK | SI | Talla DR |
| Q03 | varchar |  |  | SI | Perímetro de Cintura |
| Q03ObsDR | varchar |  | FK | SI | Perímetro de Cintura DR |
| Q04 | varchar |  |  | SI | IMC |
| Q05 | varchar |  |  | SI | Estatura Madre |
| Q05ObsDR | varchar |  | FK | SI | Estatura Madre DR |
| Q06 | varchar |  |  | SI | Estatura Padre |
| Q06ObsDR | varchar |  | FK | SI | Estatura Padre DR |
| Q07 | varchar |  |  | SI | Talla Diana Hombres |
| Q08 | varchar |  |  | SI | Talla Diana Mujeres |
| Q09 | varchar |  |  | SI | Talla por Edad |
| Q09ObsDR | varchar |  | FK | SI | Talla por Edad DR |
| Q10 | varchar |  |  | SI | IMC por Edad |
| Q10ObsDR | varchar |  | FK | SI | IMC por Edad DR |
| Q11 | varchar |  |  | SI | Puntaje Z Talla/Edad |
| Q11ObsDR | varchar |  | FK | SI | Puntaje Z Talla/Edad DR |
| Q12 | varchar |  |  | SI | Puntaje Z IMC/Edad |
| Q12ObsDR | varchar |  | FK | SI | Puntaje Z IMC/Edad DR |
| Q13 | bit |  |  | SI | Ingresar información en forma manual (deshabilita ... |
| Q14 | varchar |  |  | SI | Calificación Estatura |
| Q14ObsDR | varchar |  | FK | SI | Calificación Estatura DR |
| Q15 | varchar |  |  | SI | Tanner Genitales |
| Q15ObsDR | varchar |  | FK | SI | Tanner Genitales DR |
| Q16 | varchar |  |  | SI | Tanner Mamas |
| Q16ObsDR | varchar |  | FK | SI | Tanner Mamas DR |
| Q17 | varchar |  |  | SI | Tanner Vello Púbico |
| Q17ObsDR | varchar |  | FK | SI | Tanner Vello Púbico DR |
| Q18 | varchar |  |  | SI | Percentil de Cicunferencia Cintura |
| Q18ObsDR | varchar |  | FK | SI | Percentil de Cicunferencia Cintura DR |
| Q19 | varchar |  |  | SI | Indice Cintura/Estatura |
| Q20 | varchar |  |  | SI | Obesidad Abdominal Según Circunferencia de Cintura |
| Q20ObsDR | varchar |  | FK | SI | Obesidad Abdominal Según Circunferencia de Cintura... |
| Q21 | varchar |  |  | SI | Diagnóstico Nutricional |
| Q21ObsDR | varchar |  | FK | SI | Diagnóstico Nutricional DR |
| Q22 | varchar |  |  | SI | Corregir cálculos según edad biológica |
| Q23 | numeric |  |  | SI | Edad (Años) |
| Q24 | numeric |  |  | SI | Edad (Meses) |
| Q25 | varchar |  |  | SI | Ingrese edad biológica estimada |
| QSEN | varchar |  |  | SI | Usuario bajo algún programa del SENAME [REM] |
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