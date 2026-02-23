# questionnaire.QTCEVACUNA

**Schema:** questionnaire
**Columnas:** 60
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Cuestionario/Formulario**. Plantilla de evaluación clínica estructurada.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | bit | PK |  | SI | BCG Recién Nacido |
| Q02 | varchar | PK |  | SI | BCG Comentario |
| Q03 | bit | PK |  | SI | Polio + Pentavalente + Antineumocócica 2 meses |
| Q04 | varchar | PK |  | SI | Pentavalente 2 meses Comentario |
| Q05 | bit | PK |  | SI | Polio + Pentavalente + Antineumocócica 4 meses |
| Q06 | varchar | PK |  | SI | Pentavalente 4 meses Comentario |
| Q07 | bit | PK |  | SI | Polio + Pentavalente + Antineumocócica 6 meses |
| Q08 | varchar | PK |  | SI | Polio + Pentavalente + Antineumocócia 6 meses Come... |
| Q09 | bit | PK |  | SI | Tresvírica + Antineumocócica 1 año |
| Q10 | varchar | PK |  | SI | Tresvírica + Antineumocócica 1 año Comentario |
| Q11 | bit | PK |  | SI | Polio - Pentavalente 18 meses (Primer Refuerzo) |
| Q12 | varchar | PK |  | SI | Polio - Pentavalente (Primer Refuerzo) Comentario |
| Q15 | bit | PK |  | SI | Tresvírica 1° Básico |
| Q16 | varchar | PK |  | SI | Tresvírica 1° Básico Comentario |
| Q17 | bit | PK |  | SI | Toxoide DT 2° Básico |
| Q18 | varchar | PK |  | SI | Toxoide DT 2° Básico Comentario |
| Q19 | varchar | PK |  | SI | Observaciones |
| Q20 | varchar | PK |  | SI | Vacunas |
| Q21Q1 | varchar | PK |  | SI | Vacuna |
| Q21Q2 | date | PK |  | SI | Fecha |
| Q21Q3 | numeric | PK |  | SI | Edad |
| Q21Q4 | varchar | PK |  | SI | Observaciones |
| QUESAnaDR | varchar | PK | FK | SI | Anaesthesia |
| QUESAnaOperationDR | varchar | PK | FK | SI | Operation |
| QUESConsultDR | varchar | PK | FK | SI | Consult |
| QUESCopiedComments | varchar | PK |  | SI | Copied Comments |
| QUESCopiedDate | date | PK |  | SI | Copied Date |
| QUESCopiedEpDR | bigint | PK | FK | SI | Copied Episode |
| QUESCopiedSourceDR | bigint | PK | FK | SI | Copied Source DR |
| QUESCopiedTime | time | PK |  | SI | Copied Time |
| QUESCopiedUserDR | bigint | PK | FK | SI | Copied User |
| QUESCreateDate | date | PK |  | SI | Creation Date |
| QUESCreateTime | time | PK |  | SI | Creation Time |
| QUESCreateUserDR | bigint | PK | FK | SI | Creation User |
| QUESDate | date | PK |  | SI | Last Update Date |
| QUESErrorReasonDR | bigint | PK | FK | SI | Error Reason |
| QUESFHResidentDR | bigint | PK | FK | SI | Resident |
| QUESMRClinicalPathWaysDR | varchar | PK | FK | SI | Clinical Pathway |
| QUESNRCarePlanIssuesDR | varchar | PK | FK | SI | Nurse Care Plan Issues |
| QUESOEOrdExecDR | varchar | PK | FK | SI | Order Execution |
| QUESORPreanaestheticConsultDR | bigint | PK | FK | SI | Preanaesthetic Consultation |
| QUESObsEntryDR | varchar | PK | FK | SI | Observation Entry |
| QUESOperRoomDR | bigint | PK | FK | SI | Operating Room |
| QUESPAAdmDR | bigint | PK | FK | SI | Admission |
| QUESPAPatMasDR | bigint | PK | FK | SI | Patient |
| QUESPAPregnancyDR | bigint | PK | FK | SI | Pregnancy |
| QUESPAWaitingListDR | bigint | PK | FK | SI | Waiting List |
| QUESPathwayItemDR | varchar | PK | FK | SI | Pathway Item |
| QUESPrePostExamOEOrdItemDR | varchar | PK | FK | SI | Pre/Post Exam OrdItem |
| QUESRBAppointmentDR | varchar | PK | FK | SI | Appointments |
| QUESRBApptOutcomeDR | varchar | PK | FK | SI | Appointment Outcome |
| QUESReasonForCorrectionDR | bigint | PK | FK | SI | Reason for Correction |
| QUESSSUserDefWindowDR | bigint | PK | FK | SI | Questionnaire |
| QUESScore | varchar | PK |  | SI | Score |
| QUESStatusDR | bigint | PK | FK | SI | Status |
| QUESTextResultDR | bigint | PK | FK | SI | Text Result |
| QUESTime | time | PK |  | SI | Last Update Time |
| QUESTransactionDR | varchar | PK | FK | SI | Transaction |
| QUESUserDR | bigint | PK | FK | SI | Last Update User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*