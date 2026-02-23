# questionnaire.QGXXXWOUNDM

**Schema:** questionnaire
**Columnas:** 66
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Cuestionario/Formulario**. Plantilla de evaluación clínica estructurada.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CQ03 | varchar | PK |  | SI | - |
| CQ04 | varchar | PK |  | SI | - |
| CQ47 | varchar | PK |  | SI | - |
| ID | bigint | PK |  | NO | - |
| Q01 | varchar | PK |  | SI | Wound Assessment |
| Q02 | varchar | PK |  | SI | Location on body map |
| Q03 | varchar | PK |  | SI | Wound Site |
| Q04 | varchar | PK |  | SI | Type of Wound |
| Q17 | date | PK |  | SI | Expected date to heal |
| Q18 | date | PK |  | SI | Achieved healing date |
| Q20 | date | PK |  | SI | Established aetiology within 14 days Expected Date |
| Q21 | date | PK |  | SI | Established aetiology within 14 days Date achieved |
| Q22 | date | PK |  | SI | Established aetiology within 14 days Review Date |
| Q23 | date | PK |  | SI | Control underlyng factors within 14 days Expected ... |
| Q24 | date | PK |  | SI | Control underlyng factors within 14 days Date achi... |
| Q25 | date | PK |  | SI | Control underlyng factors within 14 days Review Da... |
| Q26 | date | PK |  | SI | Control pain within 7 days Expected Date |
| Q27 | date | PK |  | SI | Control pain within 7 days Date achieved |
| Q28 | date | PK |  | SI | Control pain within 7 days Review Date |
| Q29 | date | PK |  | SI | Absence of necrotic tissue within 14 days Expected... |
| Q30 | date | PK |  | SI | Absence of necrotic tissue within 14 days Date ach... |
| Q31 | date | PK |  | SI | Absence of necrotic tissue within 14 days Review D... |
| Q32 | date | PK |  | SI | Absence of Clinical Infections within 14 days Expe... |
| Q33 | date | PK |  | SI | Absence of Clinical Infections within 14 Date achi... |
| Q34 | date | PK |  | SI | Absence of Clinical Infections within 14 Review Da... |
| Q35 | date | PK |  | SI | Healthy surrounding tisue and reduction of edema w... |
| Q36 | date | PK |  | SI | Healthy surrounding tisue and reduction of edema w... |
| Q37 | date | PK |  | SI | Healthy surrounding tisue and reduction of edema w... |
| Q38 | date | PK |  | SI | Decreased wound surface area by 25% within 42 days... |
| Q39 | date | PK |  | SI | Decreased wound surface area by 25% within 42 days... |
| Q40 | date | PK |  | SI | Decreased wound surface area by 25% within 42 days... |
| Q41 | date | PK |  | SI | Decreased wound surface area by 50% within 60 days... |
| Q42 | date | PK |  | SI | Decreased wound surface area by 50% within 60 days... |
| Q43 | date | PK |  | SI | Decreased wound surface area by 50% within 60 days... |
| Q44 | date | PK |  | SI | Demonstration adherence to treatment/ prevetion re... |
| Q45 | date | PK |  | SI | Demonstration adherence to treatment/ prevetion re... |
| Q46 | date | PK |  | SI | Demonstration adherence to treatment/ prevetion re... |
| Q47 | varchar | PK |  | SI | Care Plan |
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