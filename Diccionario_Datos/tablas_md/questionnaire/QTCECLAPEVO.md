# questionnaire.QTCECLAPEVO

> CLAP Evolución

**Schema:** questionnaire
**Columnas:** 82
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* CLAP Evolución

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Establecimiento |
| Q03 | numeric |  |  | SI | Evolución N° |
| Q04 | date |  |  | SI | Fecha |
| Q05 | varchar |  |  | SI | Edad años |
| Q051 | varchar |  |  | SI | Edad Meses |
| Q051b | varchar |  |  | SI | Edad Meses Database |
| Q06 | varchar |  |  | SI | Acompañante |
| Q07 | varchar |  |  | SI | Estado Civil |
| Q08 | varchar |  |  | SI | Fecha de la última menstruación |
| Q09 | date |  |  | SI | Fecha  |
| Q10 | varchar |  |  | SI | Peso (Kg) |
| Q10ObsDR | varchar |  | FK | SI | Peso (Kg) DR |
| Q11 | varchar |  |  | SI | Celtil Peso/Talla (IMC) |
| Q11ObsDR | varchar |  | FK | SI | Celtil Peso/Talla (IMC) DR |
| Q12 | varchar |  |  | SI | Talla (cm) |
| Q12ObsDR | varchar |  | FK | SI | Talla (cm) DR |
| Q13 | varchar |  |  | SI | Centil Talla/Edad |
| Q13ObsDR | varchar |  | FK | SI | Centil Talla/Edad DR |
| Q14 | varchar |  |  | SI | Centil Peso/Edad |
| Q14ObsDR | varchar |  | FK | SI | Centil Peso/Edad DR |
| Q15 | varchar |  |  | SI | Presión Sistólica mmHg |
| Q15ObsDR | varchar |  | FK | SI | Presión Sistólica mmHg DR |
| Q16 | varchar |  |  | SI | Presión Distólica mmHg |
| Q16ObsDR | varchar |  | FK | SI | Presión Distólica mmHg DR |
| Q17 | varchar |  |  | SI | Frecuencia Cardiaca |
| Q17ObsDR | varchar |  | FK | SI | Frecuencia Cardiaca DR |
| Q19 | varchar |  |  | SI | Mamas |
| Q19ObsDR | varchar |  | FK | SI | Mamas DR |
| Q20 | varchar |  |  | SI | Vello púbico |
| Q20ObsDR | varchar |  | FK | SI | Vello púbico DR |
| Q21 | varchar |  |  | SI | Genitales |
| Q21ObsDR | varchar |  | FK | SI | Genitales DR |
| Q22 | numeric |  |  | SI | Volumen testicular derecho (cm3) |
| Q23 | numeric |  |  | SI | Volumen testicular izquierdo (cm3) |
| Q26 | varchar |  |  | SI | Cambios relevantes/observaciones |
| Q27 | varchar |  |  | SI | Diagnóstico integral |
| Q28 | varchar |  |  | SI | Indicaciones e Interconsultas |
| Q29 | varchar |  |  | SI | Responsable |
| Q30 | date |  |  | SI | Fecha próxima visita |
| Q31 | varchar |  |  | SI | IMC |
| QIIM | bit |  |  | SI | Ingreso información manualmente |
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