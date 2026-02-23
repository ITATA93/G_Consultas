# questionnaire.QGXXXDISCHK

**Schema:** questionnaire
**Columnas:** 70
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Cuestionario/Formulario**. Plantilla de evaluación clínica estructurada.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar | PK |  | SI | IV Cannula Removed |
| Q02 | varchar | PK |  | SI | ID Band Removed  |
| Q03 | varchar | PK |  | SI | Medication Prescription |
| Q04 | varchar | PK |  | SI | Discharge Summary Note  |
| Q05 | varchar | PK |  | SI | Nursing Advice Instruction  |
| Q06 | varchar | PK |  | SI | Result of Investigation  |
| Q07 | varchar | PK |  | SI | Appointment Card  |
| Q08 | varchar | PK |  | SI | Last Vital Sign Documented |
| Q09 | varchar | PK |  | SI | Health Education  |
| Q10 | varchar | PK |  | SI | Diagnosis Entered |
| Q11 | date | PK |  | SI | Last TET |
| Q12 | bit | PK |  | SI | TET Toxoid |
| Q13 | bit | PK |  | SI | T.I.G  |
| Q14 | varchar | PK |  | SI | RN Sign  |
| Q15 | varchar | PK |  | SI | Bodymap  |
| Q16 | varchar | PK |  | SI | Blood |
| Q17 | varchar | PK |  | SI | Glucose  |
| Q18 | varchar | PK |  | SI | Protiens  |
| Q19 | varchar | PK |  | SI | Ketone  |
| Q20 | varchar | PK |  | SI | Bilirubin  |
| Q21 | varchar | PK |  | SI | Nitrate  |
| Q22 | varchar | PK |  | SI | Micro  |
| Q23 | varchar | PK |  | SI | FIO2  |
| Q23ObsDR | varchar | PK | FK | SI | FIO2  DR |
| Q24 | varchar | PK |  | SI | pH |
| Q24ObsDR | varchar | PK | FK | SI | pH DR |
| Q25 | varchar | PK |  | SI | pCO2  |
| Q26 | varchar | PK |  | SI | pO2  |
| Q27 | varchar | PK |  | SI | SAT |
| Q27ObsDR | varchar | PK | FK | SI | SAT DR |
| Q28 | varchar | PK |  | SI | FIO2 |
| Q28ObsDR | varchar | PK | FK | SI | FIO2 DR |
| Q29 | varchar | PK |  | SI | pH |
| Q29ObsDR | varchar | PK | FK | SI | pH DR |
| Q30 | varchar | PK |  | SI | pCO2  |
| Q31 | varchar | PK |  | SI | pO2 |
| Q32 | varchar | PK |  | SI | SAT |
| Q32ObsDR | varchar | PK | FK | SI | SAT DR |
| Q33 | varchar | PK |  | SI | Pat. Valubles |
| Q34 | varchar | PK |  | SI | Pat. Instructions  |
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