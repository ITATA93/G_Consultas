# SQLUser.DICOM_Workflow

**Schema:** SQLUser
**Columnas:** 126
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Imágenes Diagnósticas**. Radiología y estudios de imagen.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| WF_RowId | bigint | PK |  | NO | - |
| Q01 | - |  |  | SI | Age (years) |
| Q02 | - |  |  | SI | Type of surgery |
| Q03 | - |  |  | SI | Recent (<1 month) event |
| Q04 | - |  |  | SI | Venous disease or clotting disorder |
| Q05 | - |  |  | SI | Mobility |
| Q06 | - |  |  | SI | Other present and past history |
| Q07 | - |  |  | SI | 0: Risk Category: Lowest |
| Q08 | - |  |  | SI | Risk Percent: Minimal |
| Q09 | - |  |  | SI | Recommended Prophylaxis: |
| Q10 | - |  |  | SI | Early frequent ambulation only, OR at discretion o... |
| Q11 | - |  |  | SI | Pneumatic compression devices OR graduated compres... |
| Q12 | - |  |  | SI | Duration of Chemoprophylaxis: |
| Q13 | - |  |  | SI | During hospitalization |
| Q14 | - |  |  | SI | 1 - 2: Risk Category: Low |
| Q15 | - |  |  | SI | Risk Percent: Minimal |
| Q16 | - |  |  | SI | Recommended Prophylaxis: |
| Q17 | - |  |  | SI | Pneumatic compression devices ± graduated compress... |
| Q18 | - |  |  | SI | Duration of Chemoprophylaxis: |
| Q19 | - |  |  | SI | During hospitalization |
| Q20 | - |  |  | SI | 3 - 4: Risk Category: Moderate |
| Q21 | - |  |  | SI | Risk Percent: 0.7% |
| Q22 | - |  |  | SI | Recommended Prophylaxis: |
| Q23 | - |  |  | SI | Pneumatic compression devices ± graduated compress... |
| Q24 | - |  |  | SI | Duration of Chemoprophylaxis: |
| Q25 | - |  |  | SI | During hospitalization |
| Q26 | - |  |  | SI | 5 - 6: Risk Category: High |
| Q27 | - |  |  | SI | Risk Percent: 1.8% |
| Q28 | - |  |  | SI | Recommended Prophylaxis: |
| Q29 | - |  |  | SI | Pneumatic compression devices AND low dose heparin... |
| Q30 | - |  |  | SI | Duration of Chemoprophylaxis: |
| Q31 | - |  |  | SI | 7–10 days total |
| Q32 | - |  |  | SI | 7–10 days total |
| Q33 | - |  |  | SI | Risk Percent: 4.0% |
| Q34 | - |  |  | SI | Recommended Prophylaxis: |
| Q35 | - |  |  | SI | Pneumatic compression devices AND low dose heparin... |
| Q36 | - |  |  | SI | Duration of Chemoprophylaxis: |
| Q37 | - |  |  | SI | 7–10 days total |
| Q38 | - |  |  | SI | ≥ 9: Risk Category: Highest |
| Q39 | - |  |  | SI | Risk Percent: 10.7%la |
| Q40 | - |  |  | SI | Recommended Prophylaxis: |
| Q41 | - |  |  | SI | Pneumatic compression devices AND low dose heparin... |
| Q42 | - |  |  | SI | Duration of Chemoprophylaxis: |
| Q43 | - |  |  | SI | 30 days total |
| Q44 | - |  |  | SI | Caprini Score for Venous Thromboembolism Stratifie... |
| Q45 | - |  |  | SI | Score |
| Q46 | - |  |  | SI | Classification	 |
| Q47 | - |  |  | SI | 0 |
| Q48 | - |  |  | SI | Risk Category: Lowest |
| Q49 | - |  |  | SI | Risk Percent: Minimal |
| Q50 | - |  |  | SI | 1 - 2 |
| Q51 | - |  |  | SI | Risk Category: Low |
| Q52 | - |  |  | SI | Risk Percent: Minimal |
| Q53 | - |  |  | SI | 3 - 4 |
| Q54 | - |  |  | SI | Risk Category: Moderate |
| Q55 | - |  |  | SI | Risk Percent: 0.7% |
| Q56 | - |  |  | SI | 5- 6 |
| Q57 | - |  |  | SI | Risk Category: High |
| Q58 | - |  |  | SI | Risk Percent: 1.8% |
| Q59 | - |  |  | SI | 7 - 8 |
| Q60 | - |  |  | SI | Risk Category: High |
| Q61 | - |  |  | SI | Risk Percent: 4.0% |
| Q62 | - |  |  | SI | ≥ 9 |
| Q63 | - |  |  | SI | Risk Category: Highest |
| Q64 | - |  |  | SI | Risk Percent: 10.7% |
| Q65 | - |  |  | SI | 0: Risk Category: Lowest, Risk Percent: Minimal |
| Q66 | - |  |  | SI | 1 - 2: Risk Category: Low, Risk Percent: Minimal |
| Q67 | - |  |  | SI | 3 - 4: Risk Category: Moderate, Risk Percent: 0.7% |
| Q68 | - |  |  | SI | 5 - 6: Risk Category: High, Risk Percent: 1.8% |
| Q69 | - |  |  | SI | 7 - 8: Risk Category: High, Risk Percent: 4.0% |
| Q70 | - |  |  | SI | >= 9: Risk Category: Highest, Risk Percent: 10.7% |
| Q71 | - |  |  | SI | Date |
| Q72 | - |  |  | SI | Time |
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
| WF_Date | date |  |  | SI | Date |
| WF_ErrorMessage | varchar |  |  | SI | Error Message |
| WF_FileName | varchar |  |  | SI | FileName |
| WF_FinishTime | time |  |  | SI | Finish Time |
| WF_Modality | varchar |  |  | SI | Modality |
| WF_OEORI_DR | varchar |  | FK | SI | Des Ref OEORI |
| WF_PACS | varchar |  |  | SI | PACS to rectrieve the images from |
| WF_Priority | double |  |  | SI | Priority for retrieving images |
| WF_StartTime | time |  |  | SI | Start Time |
| WF_Status | varchar |  |  | SI | Status |
| WF_StudyInstanceUID | varchar |  |  | SI | Study Instance UID |
| WF_Time | double |  |  | SI | Time |
| WF_TimeEntry | time |  |  | SI | Time of Entry |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*