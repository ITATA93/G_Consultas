# questionnaire.QCLXXESVIFR

> Escala Visual de Fragilidad (EVF)

**Schema:** questionnaire
**Columnas:** 62
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Escala Visual de Fragilidad (EVF)

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Escala Visual de Fragilidad (EVF) |
| Q02 | varchar |  |  | SI | Actividades Básicas de la Vida Diaria (ABVD) |
| Q03 | varchar |  |  | SI | Comer |
| Q04 | varchar |  |  | SI | Vestirse |
| Q05 | varchar |  |  | SI | Bañarse |
| Q06 | varchar |  |  | SI | Usar el retrete |
| Q07 | varchar |  |  | SI | Arreglarse (lavado de dientes, peinado) |
| Q08 | varchar |  |  | SI | Continencia de esfínter (Independiente v/s uso pañ... |
| Q09 | varchar |  |  | SI | Trasnferencia a sillón |
| Q10 | varchar |  |  | SI | Marcha |
| Q11 | varchar |  |  | SI | Subir escaleras |
| Q12 | varchar |  |  | SI | Actividades Instrumentales de la Vida Diaria (AIVD... |
| Q13 | varchar |  |  | SI | Comprar |
| Q14 | varchar |  |  | SI | Tomar medicamentos |
| Q15 | varchar |  |  | SI | Usar teléfono |
| Q16 | varchar |  |  | SI | Manejar su dinero |
| Q17 | varchar |  |  | SI | Usar transporte público |
| Q18 | varchar |  |  | SI | Prepara alimentos |
| Q19 | varchar |  |  | SI | Hacer aseo |
| Q20 | varchar |  |  | SI | Lavar su ropa |
| Q21 | varchar |  |  | SI | Imagen EVF |
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