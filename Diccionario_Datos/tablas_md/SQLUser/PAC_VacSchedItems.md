# SQLUser.PAC_VacSchedItems

**Schema:** SQLUser
**Columnas:** 96
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Items/líneas de detalle.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ITM_ParRef | bigint | PK |  | NO | PAC_VaccinationDesease Parent Reference |
| ITM_Childsub | double |  |  | NO | Childsub |
| ITM_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| ITM_CreatedDate | date |  |  | SI | Created Date |
| ITM_CreatedTime | time |  |  | SI | Created Time |
| ITM_CreatedUser_DR | bigint |  | FK | SI | Created User |
| ITM_DateFrom | date |  |  | SI | Date From |
| ITM_DateTo | date |  |  | SI | Date To |
| ITM_RowId | varchar |  |  | NO | - |
| ITM_UpdatedDate | date |  |  | SI | Updated Date |
| ITM_UpdatedTime | time |  |  | SI | Updated Time |
| ITM_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| ITM_VacDisease_DR | bigint |  | FK | SI | Des Ref PACVacDis |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | Pre-Assessment Conditions |
| Q04 | - |  |  | SI | Symptom onset date |
| Q05 | - |  |  | SI | Symptom onset time |
| Q06 | - |  |  | SI | Glasgow Coma Score (GCS) |
| Q07 | - |  |  | SI | Eye opening |
| Q07ObsDR | - |  |  | SI | Eye opening DR |
| Q08 | - |  |  | SI | Verbal |
| Q08ObsDR | - |  |  | SI | Verbal DR |
| Q09 | - |  |  | SI | Motor |
| Q09ObsDR | - |  |  | SI | Motor DR |
| Q10 | - |  |  | SI | Systolic non invasive blood pressure (mmHg) |
| Q10ObsDR | - |  |  | SI | Systolic non invasive blood pressure (mmHg) DR |
| Q11 | - |  |  | SI | Diastolic non invasive blood pressure (mmHg) |
| Q11ObsDR | - |  |  | SI | Diastolic non invasive blood pressure (mmHg) DR |
| Q12 | - |  |  | SI | Blood glucose level (mmol/L) |
| Q12ObsDR | - |  |  | SI | Blood glucose level (mmol/L) DR |
| Q13 | - |  |  | SI | If blood glucose level < 3·5 mmol/L treat urgently... |
| Q14 | - |  |  | SI | ROSIER Scale |
| Q15 | - |  |  | SI | Has there been loss of consciousness or syncope? |
| Q16 | - |  |  | SI | Has there been seizure activity? |
| Q17 | - |  |  | SI | Is there a NEW ACUTE onset of the following (or on... |
| Q18 | - |  |  | SI | I. Asymmetric facial weakness |
| Q19 | - |  |  | SI | II. Asymmetric arm weakness |
| Q20 | - |  |  | SI | III. Asymmetric leg weakness |
| Q21 | - |  |  | SI | IV. Speech disturbance |
| Q22 | - |  |  | SI | V. Visual field defect |
| Q23 | - |  |  | SI | Provisional Diagnosis |
| Q24 | - |  |  | SI | Provisional diagnosis |
| Q25 | - |  |  | SI | Specify |
| Q26 | - |  |  | SI | Guidelines |
| Q27 | - |  |  | SI | Stroke is unlikely but not completely excluded if ... |
| Q28 | - |  |  | SI | Dummy 1 |
| Q29 | - |  |  | SI | Dummy 2 |
| Q30 | - |  |  | SI | Dummy 3 |
| Q31 | - |  |  | SI | Dummy 4 |
| Q32 | - |  |  | SI | Score |
| Q33 | - |  |  | SI | Interpretation |
| Q34 | - |  |  | SI | >0 |
| Q35 | - |  |  | SI | Stroke is likely |
| Q36 | - |  |  | SI | ≤0 |
| Q37 | - |  |  | SI | Low probability of stroke but not excluded |
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