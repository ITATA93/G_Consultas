# questionnaire.QTCERDII

> Registro de Dispositivos Invasivos Instalados

**Schema:** questionnaire
**Columnas:** 87
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Registro de Dispositivos Invasivos Instalados

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Registro de Dispositivos Instalados |
| Q02 | numeric |  |  | SI | Nº Bránula |
| Q03 | varchar |  |  | SI | Ubicaciòn |
| Q04 | numeric |  |  | SI | Nº días |
| Q05 | numeric |  |  | SI | Nº Bránula |
| Q06 | varchar |  |  | SI | Ubicación |
| Q07 | numeric |  |  | SI | Nº días |
| Q08 | numeric |  |  | SI | Nº Bránula |
| Q09 | varchar |  |  | SI | Ubicaciòn |
| Q10 | numeric |  |  | SI | Nº días |
| Q11 | numeric |  |  | SI | Nº Tubo |
| Q12 | numeric |  |  | SI | cm |
| Q13 | numeric |  |  | SI | Pº Cuf |
| Q14 | numeric |  |  | SI | Nº días |
| Q15 | numeric |  |  | SI | Nº Tubo |
| Q16 | numeric |  |  | SI | Nº dìas |
| Q17 | numeric |  |  | SI | Nº lùmenes |
| Q18 | numeric |  |  | SI | cm |
| Q19 | numeric |  |  | SI | Nº dìas |
| Q20 | numeric |  |  | SI | cm |
| Q21 | numeric |  |  | SI | Nº dìas |
| Q22 | varchar |  |  | SI | Ubicaciòn |
| Q23 | numeric |  |  | SI | Nº dìas  |
| Q24 | numeric |  |  | SI | Nº |
| Q25 | varchar |  |  | SI | Ubicaciòn |
| Q26 | numeric |  |  | SI | Nº dìas |
| Q27 | numeric |  |  | SI | Nº |
| Q28 | varchar |  |  | SI | Ubicaciòn |
| Q29 | numeric |  |  | SI | Nº dìas |
| Q30 | numeric |  |  | SI | Nº |
| Q31 | numeric |  |  | SI | cc Cuf |
| Q32 | numeric |  |  | SI | Nº dìas |
| Q33 | numeric |  |  | SI | cm H2O |
| Q34 | numeric |  |  | SI | Nº dìas |
| Q35 | varchar |  |  | SI | Ubicaciòn |
| Q36 | numeric |  |  | SI | Nº dìas |
| Q37 | varchar |  |  | SI | Ubicaciòn |
| Q38 | numeric |  |  | SI | Nº dìas |
| Q39 | varchar |  |  | SI | Ubicaciòn |
| Q40 | numeric |  |  | SI | Nº dìas |
| Q41 | numeric |  |  | SI | Nº dìas |
| Q42 | numeric |  |  | SI | Nº |
| Q43 | varchar |  |  | SI | Ubicaciòn  |
| Q44 | numeric |  |  | SI | Nº |
| Q45 | varchar |  |  | SI | Ubicaciòn |
| Q46 | varchar |  |  | SI | Cúal |
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