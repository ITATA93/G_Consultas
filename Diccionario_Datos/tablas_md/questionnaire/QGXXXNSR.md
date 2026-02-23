# questionnaire.QGXXXNSR

**Schema:** questionnaire
**Columnas:** 85
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Cuestionario/Formulario**. Plantilla de evaluación clínica estructurada.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar | PK |  | SI | State of vigilance |
| Q01N | varchar | PK |  | SI | Note |
| Q01ObsDR | varchar | PK | FK | SI | State of vigilance DR |
| Q03 | varchar | PK |  | SI | Confusion |
| Q03N | varchar | PK |  | SI | Note |
| Q03ObsDR | varchar | PK | FK | SI | Confusion DR |
| Q05 | varchar | PK |  | SI | Agitation |
| Q05N | varchar | PK |  | SI | Note |
| Q05ObsDR | varchar | PK | FK | SI | Agitation DR |
| Q07 | varchar | PK |  | SI | Aggression |
| Q07N | varchar | PK |  | SI | Note |
| Q07ObsDR | varchar | PK | FK | SI | Aggression DR |
| Q09 | varchar | PK |  | SI | Coma |
| Q09N | varchar | PK |  | SI | Note |
| Q09ObsDR | varchar | PK | FK | SI | Coma DR |
| Q11 | varchar | PK |  | SI | Motor deficits |
| Q11N | varchar | PK |  | SI | Note |
| Q11ObsDR | varchar | PK | FK | SI | Motor deficits DR |
| Q13 | varchar | PK |  | SI | Sensory deficits |
| Q13N | varchar | PK |  | SI | Note |
| Q13ObsDR | varchar | PK | FK | SI | Sensory deficits DR |
| Q15 | varchar | PK |  | SI | Disorientation |
| Q15N | varchar | PK |  | SI | Note |
| Q15ObsDR | varchar | PK | FK | SI | Disorientation DR |
| Q17 | varchar | PK |  | SI | Cognitive status |
| Q17N | varchar | PK |  | SI | Note |
| Q17ObsDR | varchar | PK | FK | SI | Cognitive status DR |
| Q19 | varchar | PK |  | SI | Rigor |
| Q19N | varchar | PK |  | SI | Note |
| Q19ObsDR | varchar | PK | FK | SI | Rigor DR |
| Q21 | varchar | PK |  | SI | Pathological reflexes |
| Q21N | varchar | PK |  | SI | Note |
| Q21ObsDR | varchar | PK | FK | SI | Pathological reflexes DR |
| Q23 | varchar | PK |  | SI | Pupil difference |
| Q23N | varchar | PK |  | SI | Note |
| Q23ObsDR | varchar | PK | FK | SI | Pupil difference DR |
| Q25 | varchar | PK |  | SI | Superior functions abnormalities |
| Q25N | varchar | PK |  | SI | Note |
| Q25ObsDR | varchar | PK | FK | SI | Superior functions abnormalities DR |
| Q27 | varchar | PK |  | SI | Cranial nerves abnormalities |
| Q27N | varchar | PK |  | SI | Note |
| Q27ObsDR | varchar | PK | FK | SI | Cranial nerves abnormalities DR |
| Q29 | varchar | PK |  | SI | Neurological  abnormalities |
| Q29N | varchar | PK |  | SI | Note |
| Q29ObsDR | varchar | PK | FK | SI | Neurological  abnormalities DR |
| Q31 | varchar | PK |  | SI | Dizziness |
| Q31N | varchar | PK |  | SI | Note |
| Q31ObsDR | varchar | PK | FK | SI | Dizziness DR |
| Q33 | varchar | PK |  | SI | Fainting |
| Q33N | varchar | PK |  | SI | Note |
| Q33ObsDR | varchar | PK | FK | SI | Fainting DR |
| Q35 | varchar | PK |  | SI | Faint |
| Q35N | varchar | PK |  | SI | Note |
| Q35ObsDR | varchar | PK | FK | SI | Faint DR |
| Q37 | varchar | PK |  | SI | Other |
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