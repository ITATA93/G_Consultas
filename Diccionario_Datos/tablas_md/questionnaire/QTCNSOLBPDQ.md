# questionnaire.QTCNSOLBPDQ

> Índice de Discapacidad Lumbar de Oswestry

**Schema:** questionnaire
**Columnas:** 75
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Índice de Discapacidad Lumbar de Oswestry

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Intensidad del Dolor |
| Q02 | varchar |  |  | SI | Cuidado personal (lavarse, vestirse, etc) |
| Q03 | varchar |  |  | SI | Levantamiento de objetos |
| Q04 | varchar |  |  | SI | Caminar |
| Q05 | varchar |  |  | SI | Sentarse |
| Q06 | varchar |  |  | SI | Permanecer de pie |
| Q07 | varchar |  |  | SI | Dormir |
| Q08 | varchar |  |  | SI | Vida sexual |
| Q09 | varchar |  |  | SI | Vida social |
| Q10 | varchar |  |  | SI | Viajar |
| Q11 | varchar |  |  | SI | Tipo de Visita |
| Q12 | varchar |  |  | SI | 0% - 20%: Discapacidad mínima |
| Q13 | varchar |  |  | SI | 21% – 40%: Discapacidad moderada |
| Q14 | varchar |  |  | SI | 41% – 60%: Discapacidad severa |
| Q15 | varchar |  |  | SI | 61% – 80%: Dolor de espalda invalidante |
| Q16 | varchar |  |  | SI | 81% – 100%:&nbsp;Estos pacientes están postrados e... |
| Q17 | varchar |  |  | SI | Each section is scored on a 0–5 scale, 5 represent... |
| Q18 | varchar |  |  | SI | The index is calculated by dividing the summed sco... |
| Q19 | varchar |  |  | SI | To assess symptoms and severity of low back pain i... |
| Q20 | varchar |  |  | SI | Score |
| Q21 | varchar |  |  | SI | Classification |
| Q22 | varchar |  |  | SI | 0% - 20% |
| Q23 | varchar |  |  | SI | Minimal disability |
| Q24 | varchar |  |  | SI | 21% – 40% |
| Q25 | varchar |  |  | SI | Moderate disability |
| Q26 | varchar |  |  | SI | 41% – 60% |
| Q27 | varchar |  |  | SI | Severe disability |
| Q28 | varchar |  |  | SI | 61% – 80% |
| Q29 | varchar |  |  | SI | Crippling back pain |
| Q30 | varchar |  |  | SI | 81% – 100% |
| Q31 | varchar |  |  | SI | These patients are either bed-bound or have an exa... |
| Q32 | varchar |  |  | SI | Score |
| Q33 | varchar |  |  | SI | Percentage |
| Q34 | varchar |  |  | SI | All sections are 'Not applicable' |
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