# questionnaire.QGXXXSMO

**Schema:** questionnaire
**Columnas:** 50
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Cuestionario/Formulario**. Plantilla de evaluación clínica estructurada.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar | PK |  | SI | Head Ortho |
| Q01N | varchar | PK |  | SI | Note |
| Q01ObsDR | varchar | PK | FK | SI | Head Ortho DR |
| Q03 | varchar | PK |  | SI | Rachis |
| Q03N | varchar | PK |  | SI | Note |
| Q03ObsDR | varchar | PK | FK | SI | Rachis DR |
| Q05 | varchar | PK |  | SI | Pelvis |
| Q05N | varchar | PK |  | SI | Note |
| Q05ObsDR | varchar | PK | FK | SI | Pelvis DR |
| Q07 | varchar | PK |  | SI | Upper limbs |
| Q07N | varchar | PK |  | SI | Note |
| Q07ObsDR | varchar | PK | FK | SI | Upper limbs DR |
| Q09 | varchar | PK |  | SI | Lower limbs |
| Q09N | varchar | PK |  | SI | Note |
| Q09ObsDR | varchar | PK | FK | SI | Lower limbs DR |
| Q11 | varchar | PK |  | SI | Other |
| Q13 | varchar | PK |  | SI | Skeletal Muscle |
| Q13N | bigint | PK |  | SI | Note |
| Q13NTxtOnly | bigint | PK |  | SI | Note Plain Text Only |
| Q13ObsDR | varchar | PK | FK | SI | Skeletal Muscle DR |
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