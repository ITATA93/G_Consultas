# questionnaire.QTCHEART

> HEART Score

**Schema:** questionnaire
**Columnas:** 68
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* HEART Score

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | History of chest pain |
| Q02 | varchar |  |  | SI | Electrocardiogram (ECG) |
| Q03 | varchar |  |  | SI | Age |
| Q04 | varchar |  |  | SI | Risk factors for atherosclerotic disease	 |
| Q05 | varchar |  |  | SI | Troponin |
| Q06 | varchar |  |  | SI | Risk factors for atherosclerotic disease include:	 |
| Q07 | varchar |  |  | SI | Hypercholesterolemia, hypertension, diabetes melli... |
| Q08 | varchar |  |  | SI | Score |
| Q09 | varchar |  |  | SI | 0-3 holds a risk of 2.5% for an adverse outcome an... |
| Q10 | varchar |  |  | SI | 4-6 supports that immediate discharge is not an op... |
| Q11 | varchar |  |  | SI | ≥7 holds a risk of 72.7% and implies early aggress... |
| Q12 | varchar |  |  | SI | The HEART score is a tool for evaluating patients ... |
| Q13 | varchar |  |  | SI | treated as an acute coronary syndrome (ACS) awaiti... |
| Q14 | varchar |  |  | SI | Provides information that can correctly place pati... |
| Q15 | varchar |  |  | SI | Suspicious history of chest pain includes:	 |
| Q16 | varchar |  |  | SI | Retrosternal pain, pressure, radiation to jaw/left... |
| Q17 | varchar |  |  | SI | Low risk features of chest pain include: well loca... |
| Q18 | varchar |  |  | SI | 0 - 3 supports early discharge	 |
| Q19 | varchar |  |  | SI | 4 - 6 supports admission for clinical observation ... |
| Q20 | varchar |  |  | SI | ≥ 7 supports early invasive strategies for aggress... |
| Q21 | date |  |  | SI | Date |
| Q22 | time |  |  | SI | Time |
| Q23 | varchar |  |  | SI | Suspicious history of chest pain includes: |
| Q24 | varchar |  |  | SI | Risk factors for atherosclerotic disease: |
| Q25 | varchar |  |  | SI | Score interpretation: |
| Q26 | varchar |  |  | SI | Provenance Details |
| Q27 | varchar |  |  | SI | Source: Six AJ, Backus BE, Kelder JC. Chest pain i... |
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