# questionnaire.QTCERCV

> Estimación del Riesgo Cardiovascular

**Schema:** questionnaire
**Columnas:** 65
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Estimación del Riesgo Cardiovascular

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Criterios de un Paciente con Alto Riesgo Cardiovas... |
| Q02 | varchar |  |  | SI | Criterios que Aumentan una Categoría de Riesgo |
| Q03 | varchar |  |  | SI | Fumador (a) |
| Q04 | varchar |  |  | SI | Diabetes Mellitus |
| Q05 | numeric |  |  | SI | Colesterol Total (mg/dl) |
| Q06 | numeric |  |  | SI | Colesterol HDL (mg/dl) |
| Q07 | numeric |  |  | SI | Presión Arterial Sistólica (mmHg) |
| Q08 | numeric |  |  | SI | Presión Arterial Diastólica (mmHg) |
| Q09 | varchar |  |  | SI | Porcentaje de Riesgo Cardiovascular |
| Q09ObsDR | varchar |  | FK | SI | Porcentaje de Riesgo Cardiovascular DR |
| Q10 | varchar |  |  | SI | Riesgo Cardiovascular |
| Q10ObsDR | varchar |  | FK | SI | Riesgo Cardiovascular DR |
| Q11 | numeric |  |  | SI | Albuminuria |
| Q12 | varchar |  |  | SI | Etapa ERC |
| Q13 | numeric |  |  | SI | Circunferencia Cintura |
| Q14 | numeric |  |  | SI | Triglicéridos |
| Q15 | numeric |  |  | SI | Glicemia |
| Q16 | numeric |  |  | SI | RAC |
| Q17 | numeric |  |  | SI | VFG MDRD-4 |
| Q18 | numeric |  |  | SI | VFG Cockroft-Gault |
| Q19 | numeric |  |  | SI | Colesterol LDL |
| Q20 | varchar |  |  | SI | Categoría ERC |
| Q21 | varchar |  |  | SI | Age |
| Q22 | varchar |  |  | SI | Sex |
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