# SQLUser.LBC_DiffCounterRule

**Schema:** SQLUser
**Columnas:** 77
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Laboratorio**. Parámetros del módulo de laboratorio.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBCDCR_ParRef | bigint | PK |  | NO | Parent table |
| LBCDCR_AbsTestItem_DR | bigint |  | FK | SI | Test Set Item for Calculation of Absolute Values
... |
| LBCDCR_AbsTestSet_DR | bigint |  | FK | NO | Trigger Test Set for Calculation of Absolute Value... |
| LBCDCR_AlertSound | varchar |  |  | SI | Sound file to be played when total count is exceed... |
| LBCDCR_AllowMoreThanMax | varchar |  |  | SI | Allow more than Maximum Count |
| LBCDCR_AtlasLink | varchar |  |  | SI | Altas Link
a Url that can contain photographs and... |
| LBCDCR_BeepAtMaxCount | varchar |  |  | SI | Beep at Maximum Count |
| LBCDCR_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| LBCDCR_MaxCount | integer |  |  | SI | Maximum Count |
| LBCDCR_MinCount | integer |  |  | SI | Minimum Count |
| LBCDCR_RowID | varchar |  |  | NO | - |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | Confusion |
| Q04 | - |  |  | SI | Blood Urea Nitrogen (BUN) > 19 mg/dL (> 7 mmol/L) |
| Q05 | - |  |  | SI | Respiratory rate ≥ 30 bpm |
| Q06 | - |  |  | SI | Systolic BP < 90 mmHg or Diastolic BP ≤ 60 mmHg |
| Q07 | - |  |  | SI | Age ≥ 65 years |
| Q08 | - |  |  | SI | Score |
| Q09 | - |  |  | SI | Classification |
| Q10 | - |  |  | SI | CURB-65 Score estimates mortality of community-acq... |
| Q11 | - |  |  | SI | 0 |
| Q12 | - |  |  | SI | Low risk groups: 0.6% 30-days mortality. Consider ... |
| Q13 | - |  |  | SI | 1 |
| Q14 | - |  |  | SI | Low risk groups: 2.7% 30-days mortality. Consider ... |
| Q15 | - |  |  | SI | 2 |
| Q16 | - |  |  | SI | Moderate risk groups: 6.8% 30-days mortality. Cons... |
| Q17 | - |  |  | SI | 3 |
| Q18 | - |  |  | SI | Moderate risk groups: 14% 30-days mortality. Consi... |
| Q19 | - |  |  | SI | 4 - 5 |
| Q20 | - |  |  | SI | Highest risk groups: 27.8% 30-days mortality. Cons... |
| Q21 | - |  |  | SI | 0: 	Low risk groups: 0.6% 30-days mortality. Consi... |
| Q22 | - |  |  | SI | 1: Low risk groups: 2.7% 30-days mortality. Consid... |
| Q23 | - |  |  | SI | 2: Moderate risk groups: 6.8% 30-days mortality. C... |
| Q24 | - |  |  | SI | 3:  Moderate risk groups: 14% 30-days mortality. C... |
| Q25 | - |  |  | SI | 4 - 5: Highest risk groups: 27.8% 30-days mortalit... |
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
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*