# SQLUser.PA_AdmSNAPDetails

**Schema:** SQLUser
**Columnas:** 98
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Admisión de Pacientes**. Registra episodios de atención hospitalaria. Detalle de la entidad padre.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SNAPD_ParRef | varchar | PK |  | NO | PA_AdmSNAP Parent Reference |
| Q1 | - |  |  | SI | Date |
| Q10 | - |  |  | SI | Anterior ST-segment elevation or left bundle branc... |
| Q11 | - |  |  | SI | Time to treatment > 4 hours |
| Q12 | - |  |  | SI | Score |
| Q13 | - |  |  | SI | Classification |
| Q14 | - |  |  | SI | 0 |
| Q15 | - |  |  | SI | 1 |
| Q16 | - |  |  | SI | 2 |
| Q17 | - |  |  | SI | 3 |
| Q18 | - |  |  | SI | 4 |
| Q19 | - |  |  | SI | 5 |
| Q2 | - |  |  | SI | Time |
| Q20 | - |  |  | SI | 6 |
| Q21 | - |  |  | SI | 7 |
| Q22 | - |  |  | SI | 8 |
| Q23 | - |  |  | SI | 9 - 14 |
| Q24 | - |  |  | SI | 0.8% risk of all-cause mortality at 30 days |
| Q25 | - |  |  | SI | 1.6% risk of all-cause mortality at 30 days |
| Q26 | - |  |  | SI | 2.2% risk of all-cause mortality at 30 days |
| Q27 | - |  |  | SI | 4.4% risk of all-cause mortality at 30 days |
| Q28 | - |  |  | SI | 7.3% risk of all-cause mortality at 30 days |
| Q29 | - |  |  | SI | 12.4% risk of all-cause mortality at 30 days |
| Q3 | - |  |  | SI | Patient age range |
| Q30 | - |  |  | SI | 16.1% risk of all-cause mortality at 30 days |
| Q31 | - |  |  | SI | 23.4% risk of all-cause mortality at 30 days |
| Q32 | - |  |  | SI | 26.8% risk of all-cause mortality at 30 days |
| Q33 | - |  |  | SI | 35.9% risk of all-cause mortality at 30 days |
| Q34 | - |  |  | SI | 0: 0.8% risk of all-cause mortality at 30 days |
| Q35 | - |  |  | SI | 1: 1.6% risk of all-cause mortality at 30 days |
| Q36 | - |  |  | SI | 2: 2.2% risk of all-cause mortality at 30 days |
| Q37 | - |  |  | SI | 3: 4.4% risk of all-cause mortality at 30 days |
| Q38 | - |  |  | SI | 4: 7.3% risk of all-cause mortality at 30 days |
| Q39 | - |  |  | SI | 5: 12.4% risk of all-cause mortality at 30 days |
| Q4 | - |  |  | SI | Diabetes, hypertension or angina |
| Q40 | - |  |  | SI | 6: 16.1% risk of all-cause mortality at 30 days |
| Q41 | - |  |  | SI | 7: 23.4% risk of all-cause mortality at 30 days |
| Q42 | - |  |  | SI | 8: 26.8% risk of all-cause mortality at 30 days |
| Q43 | - |  |  | SI | 9 - 14: 35.9% risk of all-cause mortality at 30 da... |
| Q44 | - |  |  | SI | The TIMI Risk Score for STEMI is a simple integer ... |
| Q45 | - |  |  | SI | with ST-elevation acute coronary syndromes. |
| Q5 | - |  |  | SI | Systolic BP < 100 mmHg |
| Q6 | - |  |  | SI | Heart rate > 100 b/min |
| Q7 | - |  |  | SI | Killip Class II-IV |
| Q8 | - |  |  | SI | Jugular Vein Distention (JVD) or any pulmonary exa... |
| Q9 | - |  |  | SI | Weight < 67kg (147.7 lbs) |
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
| SNAPD_ADLSubType_DR | bigint |  | FK | SI | Des Ref ADLSubType |
| SNAPD_Childsub | double |  |  | NO | Childsub |
| SNAPD_Converted | varchar |  |  | SI | Converted |
| SNAPD_Date | date |  |  | SI | Date |
| SNAPD_Phase_DR | bigint |  | FK | SI | Des Ref Phase |
| SNAPD_RowId | varchar |  |  | NO | - |
| SNAPD_Score | varchar |  |  | SI | Score |
| SNAPD_Time | time |  |  | SI | Time |
| SNAPD_UpdateDate | date |  |  | SI | UpdateDate |
| SNAPD_UpdateTime | time |  |  | SI | UpdateTime |
| SNAPD_UpdateUserHospital_DR | bigint |  | FK | SI | Des Ref UpdateUserHospital |
| SNAPD_UpdateUser_DR | bigint |  | FK | SI | Des Ref UpdateUser |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*