# SQLUser.PAC_WLReviewOutcome

**Schema:** SQLUser
**Columnas:** 83
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| WLROU_RowId | bigint | PK |  | NO | - |
| Q01 | - |  |  | SI | Type of Admission |
| Q02 | - |  |  | SI | Chronic Disease |
| Q03 | - |  |  | SI | Glasgow Coma Scale |
| Q04 | - |  |  | SI | Age, years |
| Q05 | - |  |  | SI | Systolic Blood Pressure, mmHg |
| Q06 | - |  |  | SI | White Blood Cells, 10E9/L |
| Q07 | - |  |  | SI | Heart Rate, bpm |
| Q08 | - |  |  | SI | Temperature, °C |
| Q09a | - |  |  | SI | Mechanical Ventilation or CPAP |
| Q09b | - |  |  | SI | PaO2/FiO2, mmHg (kPa) |
| Q10 | - |  |  | SI | Urine Output, L/d |
| Q11 | - |  |  | SI | Potassium, mmol/L |
| Q12 | - |  |  | SI | Sodium, mmol/L |
| Q13 | - |  |  | SI | Bicarbonate, mEq/L |
| Q14 | - |  |  | SI | Bilirubin, micromol/L (mg/dL) |
| Q15 | - |  |  | SI | Serum urea concentration, mmol/L (mg/dL) |
| Q17 | - |  |  | SI | Use the worst value for each physiological variabl... |
| Q18 | - |  |  | SI | SAPS II is a severity of disease classification sy... |
| Q19 | - |  |  | SI | 163 - High severity / 0 - Low severity |
| Q20 | - |  |  | SI | A higher number is associated with a greater sever... |
| Q21 | - |  |  | SI | Primary Source |
| Q22 | - |  |  | SI | Le Gall J, Lemeshow S, Saulnier F. A New Simplifie... |
| Q23 | - |  |  | SI | Validation |
| Q24 | - |  |  | SI | Beck DH, Smith GB, Pappachan JV, Millar B. Externa... |
| Q25 | - |  |  | SI | Capuzzo M, Valpondi V, Sgarbi A, Bortolazzi S, Pav... |
| Q26 | - |  |  | SI | Date |
| Q27 | - |  |  | SI | Time |
| Q28 | - |  |  | SI | SAPS 2 Score |
| Q29 | - |  |  | SI | Estimated hospital mortality |
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
| WLROU_Code | varchar |  |  | NO | Code |
| WLROU_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| WLROU_CreatedDate | date |  |  | SI | Created Date |
| WLROU_CreatedTime | time |  |  | SI | Created Time |
| WLROU_CreatedUser_DR | bigint |  | FK | SI | Created User |
| WLROU_DateFrom | date |  |  | SI | Date From |
| WLROU_DateTo | date |  |  | SI | Date To |
| WLROU_Desc | varchar |  |  | NO | Decription |
| WLROU_Owner | varchar |  |  | SI | Owner |
| WLROU_ResetReviewDate | varchar |  |  | SI | ResetReviewDate |
| WLROU_UpdatedDate | date |  |  | SI | Updated Date |
| WLROU_UpdatedTime | time |  |  | SI | Updated Time |
| WLROU_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*