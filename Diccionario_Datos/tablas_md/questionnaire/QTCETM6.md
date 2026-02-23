# questionnaire.QTCETM6

> Test de Marcha (TM6)

**Schema:** questionnaire
**Columnas:** 93
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Test de Marcha (TM6)

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | numeric |  |  | SI | FC Basal |
| Q02 | numeric |  |  | SI | FC Final |
| Q03 | numeric |  |  | SI | FC 5 Min. |
| Q04 | numeric |  |  | SI | FC 10 Min. |
| Q05 | numeric |  |  | SI | FR Basal |
| Q06 | numeric |  |  | SI | FR Final |
| Q07 | numeric |  |  | SI | FR 5 Min. |
| Q08 | numeric |  |  | SI | FR 10 Min. |
| Q09 | numeric |  |  | SI | PA Sistólica Basal |
| Q10 | numeric |  |  | SI | PA Sistólica Final |
| Q11 | numeric |  |  | SI | PA Sistólica 5 Min |
| Q12 | numeric |  |  | SI | PA Sistólica 10 Min. |
| Q13 | numeric |  |  | SI | SAT Basal |
| Q14 | numeric |  |  | SI | SAT Final |
| Q15 | numeric |  |  | SI | SAT 5 Min. |
| Q16 | numeric |  |  | SI | SAT 10 Min. |
| Q17 | numeric |  |  | SI | BORG Fatiga Basal |
| Q18 | numeric |  |  | SI | BORG Fatiga Final |
| Q19 | numeric |  |  | SI | BORG Fatiga 5 Min. |
| Q20 | numeric |  |  | SI | BORG Fatiga 10 Min. |
| Q21 | numeric |  |  | SI | Longitud del Trazo (Mts.) |
| Q22 | numeric |  |  | SI | N° de Vueltas |
| Q23 | varchar |  |  | SI | Distancia Recorrida |
| Q24 | varchar |  |  | SI | Metros Teóricos Hombres (Mts.) |
| Q25 | varchar |  |  | SI | % del Valor Teórico Hombres |
| Q26 | varchar |  |  | SI | Detenciones |
| Q27 | varchar |  |  | SI | Completa Test |
| Q28 | varchar |  |  | SI | Causa Detenciones |
| Q29 | varchar |  |  | SI | Causa Completa Test |
| Q30 | varchar |  |  | SI | Observaciones |
| Q31 | varchar |  |  | SI | Conclusión |
| Q32 | numeric |  |  | SI | PA Diastólica Basal |
| Q33 | numeric |  |  | SI | PA Diastólica 5 Min |
| Q34 | numeric |  |  | SI | PA Diastólica 10 Min |
| Q35 | numeric |  |  | SI | PA Diastólica Final |
| Q36 | varchar |  |  | SI | Metros Teóricos Mujeres (Mts.) |
| Q37 | varchar |  |  | SI | % del Valor Teórico Mujeres |
| Q38 | varchar |  |  | SI | Sexo |
| Q39 | varchar |  |  | SI | Resultado Test Marcha 6 Min |
| Q39ObsDR | varchar |  | FK | SI | Resultado Test Marcha 6 Min DR |
| Q40 | varchar |  |  | SI | Talla |
| Q40ObsDR | varchar |  | FK | SI | Talla DR |
| Q41 | varchar |  |  | SI | Edad |
| Q42 | varchar |  |  | SI | Peso |
| Q42ObsDR | varchar |  | FK | SI | Peso DR |
| Q43 | numeric |  |  | SI | BORG Disnea Basal |
| Q44 | numeric |  |  | SI | BORG Disnea Final |
| Q45 | numeric |  |  | SI | BORG Disnea 5 Min |
| Q46 | numeric |  |  | SI | BORG Disnea 10 Min |
| Q47 | varchar |  |  | SI | Kg |
| Q48 | varchar |  |  | SI | cm |
| Q49 | varchar |  |  | SI | años |
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