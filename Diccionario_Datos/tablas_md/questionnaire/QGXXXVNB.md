# questionnaire.QGXXXVNB

**Schema:** questionnaire
**Columnas:** 73
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Cuestionario/Formulario**. Plantilla de evaluación clínica estructurada.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q00 | varchar | PK |  | SI | View |
| Q01 | bigint | PK |  | SI | Notes Eyes |
| Q01TxtOnly | bigint | PK |  | SI | Notes Eyes Plain Text Only |
| Q02 | varchar | PK |  | SI | Diffuse goiter |
| Q02N | varchar | PK |  | SI | Note |
| Q02ObsDR | varchar | PK | FK | SI | Diffuse goiter DR |
| Q03 | varchar | PK |  | SI | Neck |
| Q04 | varchar | PK |  | SI | Nodules |
| Q04N | varchar | PK |  | SI | Note |
| Q04ObsDR | varchar | PK | FK | SI | Nodules DR |
| Q06 | varchar | PK |  | SI | Palpable lymph nodes |
| Q06N | varchar | PK |  | SI | Note |
| Q06ObsDR | varchar | PK | FK | SI | Palpable lymph nodes DR |
| Q08 | varchar | PK |  | SI | Jugular venous distention |
| Q08N | varchar | PK |  | SI | Note |
| Q08ObsDR | varchar | PK | FK | SI | Jugular venous distention DR |
| Q09 | varchar | PK |  | SI | Carotid murmur |
| Q09N | varchar | PK |  | SI | Note |
| Q09ObsDR | varchar | PK | FK | SI | Carotid murmur DR |
| Q11 | varchar | PK |  | SI | Kyphosis |
| Q11N | varchar | PK |  | SI | Note |
| Q11ObsDR | varchar | PK | FK | SI | Kyphosis DR |
| Q13 | varchar | PK |  | SI | Other |
| Q14 | varchar | PK |  | SI | Breast |
| Q15 | varchar | PK |  | SI | Mamilla symmetries |
| Q15N | varchar | PK |  | SI | Note |
| Q15ObsDR | varchar | PK | FK | SI | Mamilla symmetries DR |
| Q17 | varchar | PK |  | SI | Mamilla secretion |
| Q17N | varchar | PK |  | SI | Note |
| Q17ObsDR | varchar | PK | FK | SI | Mamilla secretion DR |
| Q19 | varchar | PK |  | SI | Mamilla retraction |
| Q19N | varchar | PK |  | SI | Note |
| Q19ObsDR | varchar | PK | FK | SI | Mamilla retraction DR |
| Q21 | varchar | PK |  | SI | Breast skin |
| Q21N | varchar | PK |  | SI | Note |
| Q21ObsDR | varchar | PK | FK | SI | Breast skin DR |
| Q23 | varchar | PK |  | SI | Breast nodule |
| Q23N | varchar | PK |  | SI | Localization |
| Q23ObsDR | varchar | PK | FK | SI | Breast nodule DR |
| Q25 | varchar | PK |  | SI | Lymph nodes palpable |
| Q25N | varchar | PK |  | SI | Note |
| Q25ObsDR | varchar | PK | FK | SI | Lymph nodes palpable DR |
| Q27 | varchar | PK |  | SI | Other |
| QUESAnaDR | varchar | PK | FK | SI | Anaesthesia |
| QUESAnaOperationDR | varchar | PK | FK | SI | Operation |
| QUESConsultDR | varchar | PK | FK | SI | Consult |
| QUESCopiedComments | varchar | PK |  | SI | Copied Comments |
| QUESCopiedDate | date | PK |  | SI | Copied Date |
| QUESCopiedEpDR | bigint | PK | FK | SI | Copied Episode |
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
| QUESRBAppointmentDR | varchar | PK | FK | SI | Appointments |
| QUESReasonForCorrectionDR | bigint | PK | FK | SI | Reason for Correction |
| QUESSSUserDefWindowDR | bigint | PK | FK | SI | Questionnaire |
| QUESScore | varchar | PK |  | SI | Score |
| QUESStatusDR | bigint | PK | FK | SI | Status |
| QUESTextResultDR | bigint | PK | FK | SI | Text Result |
| QUESTime | time | PK |  | SI | Last Update Time |
| QUESUserDR | bigint | PK | FK | SI | Last Update User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*