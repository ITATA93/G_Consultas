# questionnaire.QTCENUTCALS

> Cálculo de Fórmula SEDILE

**Schema:** questionnaire
**Columnas:** 86
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Cálculo de Fórmula SEDILE

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Producto |
| Q01ObsDR | varchar |  | FK | SI | Producto DR |
| Q02 | varchar |  |  | SI | Producto 2 |
| Q02ObsDR | varchar |  | FK | SI | Producto 2 DR |
| Q03 | varchar |  |  | SI | Producto 3 |
| Q03ObsDR | varchar |  | FK | SI | Producto 3 DR |
| Q04 | varchar |  |  | SI | Producto 4 |
| Q04ObsDR | varchar |  | FK | SI | Producto 4 DR |
| Q05 | varchar |  |  | SI | Producto 5 |
| Q05ObsDR | varchar |  | FK | SI | Producto 5 DR |
| Q06 | numeric |  |  | SI | Porcentaje  |
| Q07 | numeric |  |  | SI | Porcentaje 2 |
| Q08 | numeric |  |  | SI | Porcentaje 3 |
| Q09 | numeric |  |  | SI | Porcentaje 4 |
| Q10 | numeric |  |  | SI | Porcentaje 5 |
| Q11 | numeric |  |  | SI | Vol / Unidad cc |
| Q12 | numeric |  |  | SI | Vol / Unidad cc 2 |
| Q13 | numeric |  |  | SI | Vol / Unidad cc 3 |
| Q14 | numeric |  |  | SI | Vol / Unidad cc 4 |
| Q15 | numeric |  |  | SI | Vol / Unidad cc 5 |
| Q16 | numeric |  |  | SI | Nº Veces |
| Q17 | numeric |  |  | SI | Nº Veces 2 |
| Q18 | numeric |  |  | SI | Nº Veces 3 |
| Q19 | numeric |  |  | SI | Nº Veces 4 |
| Q20 | numeric |  |  | SI | Nº Veces 5 |
| Q21 | varchar |  |  | SI | Vol. Total cc |
| Q22 | varchar |  |  | SI | Vol. Total cc 2 |
| Q23 | varchar |  |  | SI | Vol. Total cc 3 |
| Q24 | varchar |  |  | SI | Vol. Total cc 4 |
| Q25 | varchar |  |  | SI | Vol. Total cc 5 |
| Q40 | varchar |  |  | SI | Via de administración |
| Q41 | varchar |  |  | SI | Observación |
| Q42 | time |  |  | SI | Hora de Termino |
| Q43 | varchar |  |  | SI | Vol / Unidad cc |
| Q44 | varchar |  |  | SI | Gr. Unidad 1 |
| Q45 | varchar |  |  | SI | Gr. Totales 1 |
| Q46 | varchar |  |  | SI | Gr. Unidad 2 |
| Q47 | varchar |  |  | SI | Gr. Unidad 3 |
| Q48 | varchar |  |  | SI | Gr. Unidad 4 |
| Q49 | varchar |  |  | SI | Gr. Unidad 5 |
| Q50 | varchar |  |  | SI | Gr. Totales 2 |
| Q51 | varchar |  |  | SI | Gr. Totales 3 |
| Q52 | varchar |  |  | SI | Gr. Totales 4 |
| Q53 | varchar |  |  | SI | Gr. Totales 5 |
| QNUT050 | date |  |  | SI | Fecha Despacho |
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