# questionnaire.QTCEFRMPEND

> Protocolo de Evaluación de Neurodesarrollo

**Schema:** questionnaire
**Columnas:** 66
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Protocolo de Evaluación de Neurodesarrollo

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| QCC | varchar |  |  | SI | Circunferencia cráneo |
| QCD | varchar |  |  | SI | Conducta |
| QCO | varchar |  |  | SI | Control cefálico |
| QCS | varchar |  |  | SI | Consolabilidad |
| QDE | varchar |  |  | SI | Deglución |
| QDI | varchar |  |  | SI | Diagnóstico Protocolo de Neurodesarrollo |
| QDIObsDR | varchar |  | FK | SI | Diagnóstico Protocolo de Neurodesarrollo DR |
| QFL | varchar |  |  | SI | Fija la vista y sigue objeto 90° |
| QHA | varchar |  |  | SI | Habituación |
| QLL | varchar |  |  | SI | Llanto |
| QMA | varchar |  |  | SI | Manos |
| QME | varchar |  |  | SI | Movimientos de extremidades |
| QMF | varchar |  |  | SI | Movilidad Facial |
| QMFE | varchar |  |  | SI | Mira fijamente al examinador |
| QMO | varchar |  |  | SI | Moro |
| QPE | varchar |  |  | SI | Peso |
| QPI | varchar |  |  | SI | Piel |
| QRF | varchar |  |  | SI | Reacciona frente a ruido fuerte |
| QRP | varchar |  |  | SI | Rojo pupilar |
| QSD | varchar |  |  | SI | Se dirige hacia sonido |
| QSS | varchar |  |  | SI | Sonrisa Social |
| QSU | varchar |  |  | SI | Succión |
| QTA | varchar |  |  | SI | Talla |
| QTAX | varchar |  |  | SI | Tono axial |
| QTO | varchar |  |  | SI | Tónico - nucal |
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