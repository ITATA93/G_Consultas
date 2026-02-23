# SQLUser.FHC_AddressType

**Schema:** SQLUser
**Columnas:** 82
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Tipos/categorías disponibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| FHCAT_RowId | bigint | PK |  | NO | - |
| FHCAT_Code | varchar |  |  | NO | Address Type Code |
| FHCAT_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| FHCAT_CreatedDate | date |  |  | SI | Created Date |
| FHCAT_CreatedTime | time |  |  | SI | Created Time |
| FHCAT_CreatedUser_DR | bigint |  | FK | SI | Created User |
| FHCAT_DateFrom | date |  |  | NO | Date From |
| FHCAT_DateTo | date |  |  | SI | Date To |
| FHCAT_Desc | varchar |  |  | NO | Address Type Description |
| FHCAT_NationalCode | varchar |  |  | SI | National Code |
| FHCAT_Owner | varchar |  |  | SI | Owner |
| FHCAT_UpdatedDate | date |  |  | SI | Updated Date |
| FHCAT_UpdatedTime | time |  |  | SI | Updated Time |
| FHCAT_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Result Findings |
| Q01TxtOnly | - |  |  | SI | Result Findings Plain Text Only |
| Q02 | - |  |  | SI | Frequency (Hz) |
| Q03 | - |  |  | SI | Saple Time (Sec) |
| Q04 | - |  |  | SI | Heart Rate (bpm) |
| Q05 | - |  |  | SI | P Duration (ms) |
| Q06 | - |  |  | SI | QRS Duration (ms) |
| Q07 | - |  |  | SI | T Duration (ms) |
| Q08 | - |  |  | SI | PR Interval (ms) |
| Q09 | - |  |  | SI | QT Interval (ms) |
| Q10 | - |  |  | SI | QTc Interval (ms) |
| Q11 | - |  |  | SI | P axis |
| Q12 | - |  |  | SI | QRS Axis |
| Q13 | - |  |  | SI | T Axis |
| Q14 | - |  |  | SI | Suggestion |
| Q15 | - |  |  | SI | Left atrial size—M-mode on echocardiography |
| Q16 | - |  |  | SI | Left atrial volume on echocardiography |
| Q17 | - |  |  | SI | Left ventricular diastolic diameter |
| Q18 | - |  |  | SI | Left ventricular systolic function Subjective asse... |
| Q19 | - |  |  | SI | Ejection Fraction |
| Q20 | - |  |  | SI | Left ventricular diastolic function Categories |
| Q21 | - |  |  | SI | Left ventricular wall thickness |
| Q22 | - |  |  | SI | Thrombus with location |
| Q23 | - |  |  | SI | Mitral valve morphology |
| Q24 | - |  |  | SI | Mitral valve mmorphology (other) |
| Q25 | - |  |  | SI | Mitral stenosis |
| Q26 | - |  |  | SI | Mitral regurgitation |
| Q27 | - |  |  | SI | Additional Result Information |
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