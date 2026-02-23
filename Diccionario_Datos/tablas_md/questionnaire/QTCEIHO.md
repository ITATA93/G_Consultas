# questionnaire.QTCEIHO

**Schema:** questionnaire
**Columnas:** 61
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Cuestionario/Formulario**. Plantilla de evaluación clínica estructurada.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar | PK |  | SI | Pieza1 |
| Q02 | varchar | PK |  | SI | Pieza2 |
| Q03 | varchar | PK |  | SI | Pieza3 |
| Q04 | varchar | PK |  | SI | Pieza4 |
| Q05 | varchar | PK |  | SI | Pieza5 |
| Q06 | varchar | PK |  | SI | Pieza6 |
| Q07 | varchar | PK |  | SI | Cara1 |
| Q08 | varchar | PK |  | SI | Cara2 |
| Q09 | varchar | PK |  | SI | Cara3 |
| Q10 | varchar | PK |  | SI | Cara4 |
| Q11 | varchar | PK |  | SI | Cara5 |
| Q12 | varchar | PK |  | SI | Cara6 |
| Q13 | varchar | PK |  | SI | Nombre Pieza |
| Q14 | varchar | PK |  | SI | Nombre pieza2 |
| Q15 | varchar | PK |  | SI | Nombre pieza3 |
| Q16 | varchar | PK |  | SI | Nombre pieza4 |
| Q17 | varchar | PK |  | SI | Nombre pieza5 |
| Q18 | varchar | PK |  | SI | Nombre pieza6 |
| Q19 | varchar | PK |  | SI | Criterio IHO |
| Q20 | varchar | PK |  | SI | Criterio IHO1 |
| Q21 | varchar | PK |  | SI | Criterio IHO2 |
| Q22 | varchar | PK |  | SI | Criterio IHO3 |
| Q23 | varchar | PK |  | SI | Criterio IHO4 |
| Q24 | varchar | PK |  | SI | Criterio IHO5 |
| Q25 | varchar | PK |  | SI | Criterio IHO6 |
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
| QUESObsEntryDR | varchar | PK | FK | SI | Observation Entry |
| QUESOperRoomDR | bigint | PK | FK | SI | Operating Room |
| QUESPAAdmDR | bigint | PK | FK | SI | Admission |
| QUESPAPatMasDR | bigint | PK | FK | SI | Patient |
| QUESPAPregnancyDR | bigint | PK | FK | SI | Pregnancy |
| QUESPAWaitingListDR | bigint | PK | FK | SI | Waiting List |
| QUESPathwayItemDR | varchar | PK | FK | SI | Pathway Item |
| QUESPrePostExamOEOrdItemDR | varchar | PK | FK | SI | Pre/Post Exam OrdItem |
| QUESRBAppointmentDR | varchar | PK | FK | SI | Appointments |
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