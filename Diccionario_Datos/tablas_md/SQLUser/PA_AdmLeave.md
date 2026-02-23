# SQLUser.PA_AdmLeave

**Schema:** SQLUser
**Columnas:** 116
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Admisión de Pacientes**. Registra episodios de atención hospitalaria.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ADML_ParRef | bigint | PK |  | NO | PA_Adm Parent Reference |
| ADML_ActualDateReturn | date |  |  | SI | Actual Date of Return |
| ADML_ActualTimeReturn | time |  |  | SI | Actual Time of Return |
| ADML_CancelDate | date |  |  | SI | CancelDate |
| ADML_CancelTime | time |  |  | SI | CancelTime |
| ADML_Childsub | double |  |  | NO | Childsub |
| ADML_Comments | varchar |  |  | SI | Comments |
| ADML_ContractPatientNumber | varchar |  |  | SI | Contract Patient Number |
| ADML_ContractRole_DR | bigint |  | FK | SI | Des Ref ContractRole |
| ADML_ContractType_DR | bigint |  | FK | SI | Des Ref ContractType |
| ADML_DoctorApprove_DR | varchar |  | FK | SI | Doctor Approving Des Ref to CTCP |
| ADML_ExpectedDateReturn | date |  |  | SI | Expected Date of Return |
| ADML_ExpectedTimeReturn | time |  |  | SI | Expected Time of Return |
| ADML_GoingOutDate | date |  |  | SI | Going Out Date |
| ADML_GoingOutTime | time |  |  | SI | Going Out Time |
| ADML_LeaveCategory_DR | bigint |  | FK | SI | Des Ref LeaveCategory |
| ADML_LeaveType_DR | bigint |  | FK | SI | Des Ref LeaveType |
| ADML_NurseReturn_DR | varchar |  | FK | SI | Des Ref CTCP |
| ADML_Nurse_DR | varchar |  | FK | SI | Nurse Des Ref to CTCP |
| ADML_PAAdmContractedCare_DR | varchar |  | FK | SI | Des Ref PAAdmContractedCare |
| ADML_Reason_DR | bigint |  | FK | SI | Reason Des Rrf to PACReas |
| ADML_Room_DR | bigint |  | FK | SI | Room Des Ref to PARoom |
| ADML_RowId | varchar |  |  | NO | - |
| ADML_TempAddress_DR | varchar |  | FK | SI | Des Ref TempAddress |
| ADML_UpdateDate | date |  |  | SI | UpdateDate |
| ADML_UpdateTime | time |  |  | SI | UpdateTime |
| ADML_UpdateUserHospital_DR | bigint |  | FK | SI | Des Ref UpdateUserHospital |
| ADML_UpdateUser_DR | bigint |  | FK | SI | Des Ref UpdateUser |
| Q01 | - |  |  | SI | Patient seated on a hard, armless chair |
| Q02 | - |  |  | SI | Sitting balance |
| Q03 | - |  |  | SI | Rising from chair |
| Q04 | - |  |  | SI | Attempts to rise |
| Q05 | - |  |  | SI | Immediate standing balance (first 5 seconds) |
| Q06 | - |  |  | SI | Standing balance |
| Q07 | - |  |  | SI | Sternal nudge (feet close together) |
| Q08 | - |  |  | SI | Eyes closed (feet together) |
| Q09 | - |  |  | SI | Turning 360 degrees |
| Q09b | - |  |  | SI | Turning 360 degress |
| Q10 | - |  |  | SI | Sitting down |
| Q11 | - |  |  | SI | Balance Score |
| Q13 | - |  |  | SI | Patient stands with therapist, walks across room (... |
| Q14 | - |  |  | SI | Initiation of gait (Immediately after told to ‘go’... |
| Q15 | - |  |  | SI | Step length and height |
| Q16 | - |  |  | SI | Foot clearance |
| Q17 | - |  |  | SI | Step symmetry |
| Q18 | - |  |  | SI | Step continuity |
| Q19 | - |  |  | SI | Path |
| Q20 | - |  |  | SI | Trunk |
| Q21 | - |  |  | SI | Walking time |
| Q22 | - |  |  | SI | Gait Score |
| Q23 | - |  |  | SI | Total Score (Balance + Gait) |
| Q24 | - |  |  | SI | Risk Indicators: |
| Q25 | - |  |  | SI | Tinetti Total Score |
| Q26 | - |  |  | SI | ≤ 18 |
| Q27 | - |  |  | SI | 19 - 23 |
| Q28 | - |  |  | SI | ≥ 24 |
| Q29 | - |  |  | SI | Risk for Falls |
| Q30 | - |  |  | SI | High |
| Q31 | - |  |  | SI | Moderate |
| Q32 | - |  |  | SI | Low |
| Q33 | - |  |  | SI | Signature |
| Q33UDt | - |  |  | SI | Signature Last Updated Date |
| Q33UTm | - |  |  | SI | Signature Last Updated Time |
| Q34 | - |  |  | SI | Evaluated Function |
| Q35 | - |  |  | SI | Evaluated Function |
| Q36 | - |  |  | SI | Scoring |
| Q37 | - |  |  | SI | Scoring |
| Q38 | - |  |  | SI | / 12 |
| Q39 | - |  |  | SI | / 16 |
| Q40 | - |  |  | SI | / 28 |
| Q41 | - |  |  | SI | The Tinetti Balance Assesssment Tool, or Performan... |
| Q42 | - |  |  | SI | ≤ 18: High |
| Q43 | - |  |  | SI | 19 - 23: Moderate |
| Q44 | - |  |  | SI | ≥ 24: Low |
| Q45 | - |  |  | SI | Date |
| Q46 | - |  |  | SI | Time |
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