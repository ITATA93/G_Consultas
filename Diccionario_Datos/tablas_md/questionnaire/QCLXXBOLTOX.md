# questionnaire.QCLXXBOLTOX

> Boleta de Toma de Muestra Toxicológica

**Schema:** questionnaire
**Columnas:** 63
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Boleta de Toma de Muestra Toxicológica

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | numeric |  |  | SI | Nro. de Frasco |
| Q02 | numeric |  |  | SI | Año |
| Q03 | date |  |  | SI | Fecha Toma de Muestra |
| Q04 | time |  |  | SI | Hora Toma de Muestra |
| Q05 | varchar |  |  | SI | II. BREVE APRECIACIÓN CLÍNICA |
| Q06 | varchar |  |  | SI | Breve Apreciación Clínica |
| Q07 | varchar |  |  | SI | III. OBSERVACIONES |
| Q08 | varchar |  |  | SI | Presencia de TEC |
| Q09 | varchar |  |  | SI | Rechaza Toma de Muestra |
| Q10 | varchar |  |  | SI | Sospecha Presencia de Drogas |
| Q11 | varchar |  |  | SI | Resultado Test de Droga en Saliva (-/+ sustancia d... |
| Q12 | varchar |  |  | SI | IV. IDENTIFICACIÓN DEL PROFESIONAL QUE TOMA LA MUE... |
| Q13 | varchar |  |  | SI | Nombre |
| Q14 | varchar |  |  | SI | V. IDENTIFICACIÓN DEL PARTE POLICIAL |
| Q15 | varchar |  |  | SI | Nro. Placa Func. Policial |
| Q16 | varchar |  |  | SI | Nro. De Parte Policial |
| Q17 | date |  |  | SI | Fecha y Hora del Suceso que motiva el Examen |
| Q18 | time |  |  | SI | Hora |
| Q19 | varchar |  |  | SI | Comisaría o Unidad Policial Emisora del Parte |
| Q20 | varchar |  |  | SI | Fiscalía o Tribunal receptor del Parte |
| Q21 | varchar |  |  | SI | VI. IDENTIFICACIÓN DEL MÉDICO RESPONSABLE DEL PROC... |
| Q22 | varchar |  |  | SI | Nombre |
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