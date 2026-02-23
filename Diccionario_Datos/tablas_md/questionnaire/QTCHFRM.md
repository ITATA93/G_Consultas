# questionnaire.QTCHFRM

> Valoración de Riesgo de Caídas Hendrich II

**Schema:** questionnaire
**Columnas:** 68
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Valoración de Riesgo de Caídas Hendrich II

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date |  |  | SI | Fecha |
| Q02 | time |  |  | SI | Hora |
| Q03 | varchar |  |  | SI | Confusión / Desorientación / Impulsividad |
| Q04 | varchar |  |  | SI | Depresión sintomática |
| Q05 | varchar |  |  | SI | Alteraciones de la eliminación |
| Q06 | varchar |  |  | SI | Mareos / Vértigo |
| Q07 | varchar |  |  | SI | Sexo masculino |
| Q08 | varchar |  |  | SI | Medicación antiepiléptica |
| Q09 | varchar |  |  | SI | Anticonvulsants |
| Q10 | varchar |  |  | SI | Administración de benzodiacepinas |
| Q11 | varchar |  |  | SI | Benzodiazepines medications |
| Q12 | varchar |  |  | SI | Test Levántese y Camine |
| Q13 | varchar |  |  | SI | If unable to assess, monitor for change in activit... |
| Q14 | varchar |  |  | SI | Additional detail where patient was unable to be a... |
| Q15 | varchar |  |  | SI | Puntaje |
| Q16 | varchar |  |  | SI | Clasificación |
| Q17 | varchar |  |  | SI | 5 - 16 |
| Q18 | varchar |  |  | SI | Indica un alto riesgo de caída |
| Q19 | varchar |  |  | SI | 5 - 16: Indicates a high risk of falling |
| Q20 | varchar |  |  | SI | The Hendrich II Fall Risk Model™ is widely validat... |
| Q21 | varchar |  |  | SI | 0 - 4 |
| Q22 | varchar |  |  | SI | Indica un bajo riesgo de caída |
| Q23 | varchar |  |  | SI | 0 - 4: Indicates a low risk of falling |
| Q24 | varchar |  |  | SI | 5 - 16 |
| Q25 | varchar |  |  | SI | Indicates a high risk of falling |
| Q26 | varchar |  |  | SI | 5 - 16: Indicates a high risk of falling |
| Q27 | varchar |  |  | SI | A score of 5 or greater indicates a high risk of f... |
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