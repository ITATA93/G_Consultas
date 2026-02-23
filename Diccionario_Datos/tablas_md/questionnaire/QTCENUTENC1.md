# questionnaire.QTCENUTENC1

> Encuesta de Tendencia

**Schema:** questionnaire
**Columnas:** 105
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Encuesta de Tendencia

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Cereales |
| Q11 | varchar |  |  | SI | Verduras y Frutas |
| Q26 | varchar |  |  | SI | Carnes y Leguminosas |
| Q37 | varchar |  |  | SI | Aceites y Azúcares |
| Q60 | varchar |  |  | SI | Total Frutas |
| Q61 | varchar |  |  | SI | Encuesta de Consumo 24 horas |
| Q62 | varchar |  |  | SI | Total Azúcares |
| Q70 | varchar |  |  | SI | Total Cereales |
| QQ01 | varchar |  |  | SI | Total Verduras |
| QQ02 | numeric |  |  | SI | Arroz Frecuencia |
| QQ03 | numeric |  |  | SI | Arroz Porción |
| QQ05 | numeric |  |  | SI | Papas Frecuencia |
| QQ06 | numeric |  |  | SI | Papas Porción  |
| QQ08 | numeric |  |  | SI | Pan Frecuencia |
| QQ09 | numeric |  |  | SI | Pan Porción |
| QQ12 | numeric |  |  | SI | Legumbres Frescas Frecuencia |
| QQ13 | numeric |  |  | SI | Legumbres Frescas Porción |
| QQ15 | varchar |  |  | SI | Lácteos |
| QQ16 | numeric |  |  | SI | Leche Frecuencia  |
| QQ17 | numeric |  |  | SI | Leche Porción  |
| QQ19 | numeric |  |  | SI | Leche Entera Frecuencia  |
| QQ20 | numeric |  |  | SI | Leche Entera Porción |
| QQ22 | numeric |  |  | SI | Leche Semidescremada Frecuencia  |
| QQ23 | numeric |  |  | SI | Leche Semidescremada Porción  |
| QQ25 | numeric |  |  | SI | Leche Descremada Frecuencia  |
| QQ26 | numeric |  |  | SI | Leche Descremada Porción  |
| QQ27 | varchar |  |  | SI | Total Lácteos |
| QQ28 | numeric |  |  | SI | Quesos Frecuencia  |
| QQ29 | numeric |  |  | SI | Quesos Porción  |
| QQ30 | numeric |  |  | SI | Quesillo Frecuencia  |
| QQ31 | numeric |  |  | SI | Quesillo Porción  |
| QQ32 | numeric |  |  | SI | Legumbres Frecuencia |
| QQ33 | numeric |  |  | SI | Legumbres Porción |
| QQ34 | numeric |  |  | SI | Carnes Rojas Frecuencia  |
| QQ35 | numeric |  |  | SI | Carnes Rojas Porción  |
| QQ36 | numeric |  |  | SI | Huevos Frecuencia |
| QQ37 | numeric |  |  | SI | Huevos Porción |
| QQ38 | numeric |  |  | SI | Pescados Frecuencia |
| QQ39 | numeric |  |  | SI | Pescados Porción |
| QQ40 | numeric |  |  | SI | Aves Frecuencia |
| QQ41 | numeric |  |  | SI | Aves Porción |
| QQ42 | numeric |  |  | SI | Aceite Frecuencia  |
| QQ43 | numeric |  |  | SI | Aceite Porción |
| QQ44 | numeric |  |  | SI | Palta - Aceitunas - Frutos Secos Frecuencia  |
| QQ45 | numeric |  |  | SI | Palta - Aceitunas - Frutos Secos Porción  |
| QQ46 | numeric |  |  | SI | Mantequilla - Margarina - Mayonesa Frecuencia |
| QQ47 | numeric |  |  | SI | Mantequilla - Margarina - Mayonesa Porción |
| QQ48 | numeric |  |  | SI | Manteca - Paté Frecuencia |
| QQ49 | numeric |  |  | SI | Manteca - Paté Porción |
| QQ50 | numeric |  |  | SI | Azúcar Frecuencia |
| QQ51 | numeric |  |  | SI | Azúcar Porción |
| QQ52 | numeric |  |  | SI | Miel - Mermelada Frecuencia |
| QQ53 | numeric |  |  | SI | Miel - Mermelada Porción |
| QQ54 | numeric |  |  | SI | Bebidas Azucaradas Frecuencia |
| QQ55 | numeric |  |  | SI | Bebidas Azucaradas Porción |
| QQ56 | numeric |  |  | SI | Verduras Frecuencia |
| QQ57 | numeric |  |  | SI | Verduras Porción |
| QQ58 | numeric |  |  | SI | Frutas Frecuencia |
| QQ59 | numeric |  |  | SI | Frutas Porción |
| QQ62 | varchar |  |  | SI | Total Carnes y Leguminosas |
| QQ63 | varchar |  |  | SI | Total Aceites |
| QQ80 | numeric |  |  | SI | Fideos Frecuencia |
| QQ82 | numeric |  |  | SI | Fideos Porcion |
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
| Qtestcalc | varchar |  |  | SI | Test Calculo |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*