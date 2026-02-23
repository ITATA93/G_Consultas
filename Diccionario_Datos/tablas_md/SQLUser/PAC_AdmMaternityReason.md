# SQLUser.PAC_AdmMaternityReason

**Schema:** SQLUser
**Columnas:** 80
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ADMMR_RowId | bigint | PK |  | NO | - |
| ADMMR_Code | varchar |  |  | NO | Code |
| ADMMR_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| ADMMR_CreatedDate | date |  |  | SI | Created Date |
| ADMMR_CreatedTime | time |  |  | SI | Created Time |
| ADMMR_CreatedUser_DR | bigint |  | FK | SI | Created User |
| ADMMR_DateFrom | date |  |  | SI | Date From |
| ADMMR_DateTo | date |  |  | SI | Date To |
| ADMMR_Desc | varchar |  |  | NO | Description |
| ADMMR_Owner | varchar |  |  | SI | Owner |
| ADMMR_UpdatedDate | date |  |  | SI | Updated Date |
| ADMMR_UpdatedTime | time |  |  | SI | Updated Time |
| ADMMR_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Hypertension (uncontrolled, >160 mmHg systolic) |
| Q02 | - |  |  | SI | Renal disease (dialysis, transplant, Creatinine >2... |
| Q03 | - |  |  | SI | Liver disease (cirrhosis or bilirubin >2x normal w... |
| Q04 | - |  |  | SI | Stroke history	 |
| Q05 | - |  |  | SI | Prior major bleeding or predisposition to bleeding... |
| Q06 | - |  |  | SI | Labile International Normalized Ratio (INR) (unsta... |
| Q07 | - |  |  | SI | Age > 65 years |
| Q08 | - |  |  | SI | Medication usage predisposing to bleeding |
| Q09 | - |  |  | SI | (e.g. Aspirin, Clopidogrel, Non-steroidal anti-inf... |
| Q10 | - |  |  | SI | Alcohol use (≥ 8 drinks/week) |
| Q11 | - |  |  | SI | 1. Maximum Total Score: 9 |
| Q12 | - |  |  | SI | 2. The score estimates the risk of major bleeding ... |
| Q13 | - |  |  | SI | Score |
| Q14 | - |  |  | SI | Classification	 |
| Q15 | - |  |  | SI | 0 points: Major bleeding risk 1% per year |
| Q16 | - |  |  | SI | 1 points: Major bleeding risk 3.4% per year |
| Q17 | - |  |  | SI | 2 points: Major bleeding risk 4.1% per year |
| Q18 | - |  |  | SI | 3 points: Major bleeding risk 5.8% per year |
| Q19 | - |  |  | SI | 4 points: Major bleeding risk 8.9% per year |
| Q20 | - |  |  | SI | 5 points: Major bleeding risk 9.1% per year |
| Q21 | - |  |  | SI | > 5 points: Major bleeding risk 12-15% per year |
| Q22 | - |  |  | SI | HAS-BLED Score is a tool to potentially guide the ... |
| Q23 | - |  |  | SI | The HAS-BLED Score was developed as a practical ri... |
| Q24 | - |  |  | SI | Date |
| Q25 | - |  |  | SI | Time |
| Q26 | - |  |  | SI | Date |
| Q27 | - |  |  | SI | Time |
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