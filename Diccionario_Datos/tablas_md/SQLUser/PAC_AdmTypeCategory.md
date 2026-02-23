# SQLUser.PAC_AdmTypeCategory

**Schema:** SQLUser
**Columnas:** 80
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Tipos/categorías disponibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ADMTC_RowId | bigint | PK |  | NO | - |
| ADMTC_Code | varchar |  |  | NO | Code |
| ADMTC_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| ADMTC_CreatedDate | date |  |  | SI | Created Date |
| ADMTC_CreatedTime | time |  |  | SI | Created Time |
| ADMTC_CreatedUser_DR | bigint |  | FK | SI | Created User |
| ADMTC_DateFrom | date |  |  | SI | Date From |
| ADMTC_DateTo | date |  |  | SI | Date To |
| ADMTC_Desc | varchar |  |  | NO | Description |
| ADMTC_Owner | varchar |  |  | SI | Owner |
| ADMTC_UpdatedDate | date |  |  | SI | Updated Date |
| ADMTC_UpdatedTime | time |  |  | SI | Updated Time |
| ADMTC_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Fecha |
| Q02 | - |  |  | SI | Hora |
| Q03 | - |  |  | SI | Confusión / Desorientación / Impulsividad |
| Q04 | - |  |  | SI | Depresión sintomática |
| Q05 | - |  |  | SI | Alteraciones de la eliminación |
| Q06 | - |  |  | SI | Mareos / Vértigo |
| Q07 | - |  |  | SI | Sexo masculino |
| Q08 | - |  |  | SI | Medicación antiepiléptica |
| Q09 | - |  |  | SI | Anticonvulsants |
| Q10 | - |  |  | SI | Administración de benzodiacepinas |
| Q11 | - |  |  | SI | Benzodiazepines medications |
| Q12 | - |  |  | SI | Test Levántese y Camine |
| Q13 | - |  |  | SI | If unable to assess, monitor for change in activit... |
| Q14 | - |  |  | SI | Additional detail where patient was unable to be a... |
| Q15 | - |  |  | SI | Puntaje |
| Q16 | - |  |  | SI | Clasificación |
| Q17 | - |  |  | SI | 5 - 16 |
| Q18 | - |  |  | SI | Indica un alto riesgo de caída |
| Q19 | - |  |  | SI | 5 - 16: Indicates a high risk of falling |
| Q20 | - |  |  | SI | The Hendrich II Fall Risk Model™ is widely validat... |
| Q21 | - |  |  | SI | 0 - 4 |
| Q22 | - |  |  | SI | Indica un bajo riesgo de caída |
| Q23 | - |  |  | SI | 0 - 4: Indicates a low risk of falling |
| Q24 | - |  |  | SI | 5 - 16 |
| Q25 | - |  |  | SI | Indicates a high risk of falling |
| Q26 | - |  |  | SI | 5 - 16: Indicates a high risk of falling |
| Q27 | - |  |  | SI | A score of 5 or greater indicates a high risk of f... |
| QUESAnaDR | - |  |  | SI | Anaesthesia |
| QUESAnaOperationDR | - |  |  | SI | Operation |
| QUESConsultDR | - |  |  | SI | Consult |
| QUESCopiedComments | - |  |  | SI | Copied Comments |
| QUESCopiedDate | - |  |  | SI | Copied Date |
| QUESCopiedEpDR | - |  |  | SI | Copied Episode |
| QUESCopiedSourceDR | - |  |  | SI | Copied Source DR |
| QUESCopiedTime | - |  |  | SI | Copied Time |
| QUESCopiedUserDR | - |  |  | SI | Copied User |
| QUESCreateDate | - |  |  | SI | Creation Date |
| QUESCreateTime | - |  |  | SI | Creation Time |
| QUESCreateUserDR | - |  |  | SI | Creation User |
| QUESDate | - |  |  | SI | Last Update Date |
| QUESErrorReasonDR | - |  |  | SI | Error Reason |
| QUESFHResidentDR | - |  |  | SI | Resident |
| QUESMRClinicalPathWaysDR | - |  |  | SI | Clinical Pathway |
| QUESNRCarePlanIssuesDR | - |  |  | SI | Nurse Care Plan Issues |
| QUESOEOrdExecDR | - |  |  | SI | Order Execution |
| QUESORPreanaestheticConsultDR | - |  |  | SI | Preanaesthetic Consultation |
| QUESObsEntryDR | - |  |  | SI | Observation Entry |
| QUESOperRoomDR | - |  |  | SI | Operating Room |
| QUESPAAdmDR | - |  |  | SI | Admission |
| QUESPAAdverseEventDR | - |  |  | SI | Adverse Event |
| QUESPAPatMasDR | - |  |  | SI | Patient |
| QUESPAPregnancyDR | - |  |  | SI | Pregnancy |
| QUESPAWaitingListDR | - |  |  | SI | Waiting List |
| QUESPathwayItemDR | - |  |  | SI | Pathway Item |
| QUESPrePostExamOEOrdItemDR | - |  |  | SI | Pre/Post Exam OrdItem |
| QUESRBAppointmentDR | - |  |  | SI | Appointments |
| QUESRBApptOutcomeDR | - |  |  | SI | Appointment Outcome |
| QUESRBApptSlotDR | - |  |  | SI | Appointment Slot |
| QUESReasonForCorrectionDR | - |  |  | SI | Reason for Correction |
| QUESSSUserDefWindowDR | - |  |  | SI | Questionnaire |
| QUESScore | - |  |  | SI | Score |
| QUESSecondUserDR | - |  |  | SI | Second Signature |
| QUESStatusDR | - |  |  | SI | Status |
| QUESTextResultDR | - |  |  | SI | Text Result |
| QUESTime | - |  |  | SI | Last Update Time |
| QUESTransactionDR | - |  |  | SI | Transaction |
| QUESUserDR | - |  |  | SI | Last Update User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*