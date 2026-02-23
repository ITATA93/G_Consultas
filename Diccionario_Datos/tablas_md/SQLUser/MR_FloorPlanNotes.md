# SQLUser.MR_FloorPlanNotes

**Schema:** SQLUser
**Columnas:** 131
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Módulo del Sistema**. Componente interno de TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| FLOOR_ParRef | bigint | PK |  | NO | MR_Adm Parent Reference |
| FLOOR_Childsub | double |  |  | NO | Childsub |
| FLOOR_Date | date |  |  | SI | Date |
| FLOOR_RowId | varchar |  |  | NO | - |
| FLOOR_Text | varchar |  |  | SI | Text |
| FLOOR_Time | time |  |  | SI | Time |
| FLOOR_UpdateDate | date |  |  | SI | Update Date |
| FLOOR_UpdateHospital_DR | bigint |  | FK | SI | Des Ref UpdateHospital |
| FLOOR_UpdateTime | time |  |  | SI | Update Time |
| FLOOR_UpdateUser_DR | bigint |  | FK | SI | Des Ref UpdateUser |
| Q01 | - |  |  | SI | Temperature |
| Q01ObsDR | - |  |  | SI | Temperature DR |
| Q02 | - |  |  | SI | Pregnancy Test Result |
| Q02ObsDR | - |  |  | SI | Pregnancy Test Result DR |
| Q03 | - |  |  | SI | Pupil Size (L) |
| Q03ObsDR | - |  |  | SI | Pupil Size (L) DR |
| Q04 | - |  |  | SI | Pupil Size (R) |
| Q04ObsDR | - |  |  | SI | Pupil Size (R) DR |
| Q05 | - |  |  | SI | Respirations |
| Q05ObsDR | - |  |  | SI | Respirations DR |
| Q06 | - |  |  | SI | Systolic BP |
| Q06ObsDR | - |  |  | SI | Systolic BP DR |
| Q07 | - |  |  | SI | Pupil Reaction (R) |
| Q07ObsDR | - |  |  | SI | Pupil Reaction (R) DR |
| Q08 | - |  |  | SI | Pupil Reaction (L) |
| Q08ObsDR | - |  |  | SI | Pupil Reaction (L) DR |
| Q09 | - |  |  | SI | Diastolic BP |
| Q09ObsDR | - |  |  | SI | Diastolic BP DR |
| Q10 | - |  |  | SI | SpO2 |
| Q10ObsDR | - |  |  | SI | SpO2 DR |
| Q11 | - |  |  | SI | Comments |
| Q12 | - |  |  | SI | Height (cm) |
| Q12ObsDR | - |  |  | SI | Height (cm) DR |
| Q13 | - |  |  | SI | Weight (kg) |
| Q13ObsDR | - |  |  | SI | Weight (kg) DR |
| Q14 | - |  |  | SI | Peak Pressure |
| Q14ObsDR | - |  |  | SI | Peak Pressure DR |
| Q15 | - |  |  | SI | Mean Arterial Pressure |
| Q15ObsDR | - |  |  | SI | Mean Arterial Pressure DR |
| Q16 | - |  |  | SI | Eye opening |
| Q17 | - |  |  | SI | Verbal response |
| Q18 | - |  |  | SI | Motor response |
| Q19 | - |  |  | SI | Pulse |
| Q19ObsDR | - |  |  | SI | Pulse DR |
| Q20 | - |  |  | SI | Visual Acuity - With Correction |
| Q20ObsDR | - |  |  | SI | Visual Acuity - With Correction DR |
| Q21 | - |  |  | SI | Blood Glucose |
| Q21ObsDR | - |  |  | SI | Blood Glucose DR |
| Q22 | - |  |  | SI | Peak pressure expected |
| Q22ObsDR | - |  |  | SI | Peak pressure expected DR |
| Q23 | - |  |  | SI | Pain Score |
| Q23ObsDR | - |  |  | SI | Pain Score DR |
| Q24 | - |  |  | SI | Urine Glucose |
| Q24ObsDR | - |  |  | SI | Urine Glucose DR |
| Q25 | - |  |  | SI | Urine Ketones |
| Q25ObsDR | - |  |  | SI | Urine Ketones DR |
| Q26 | - |  |  | SI | Specific Gravity |
| Q26ObsDR | - |  |  | SI | Specific Gravity DR |
| Q27 | - |  |  | SI | Urine Blood |
| Q27ObsDR | - |  |  | SI | Urine Blood  DR |
| Q28 | - |  |  | SI | Urine pH |
| Q28ObsDR | - |  |  | SI | Urine pH DR |
| Q29 | - |  |  | SI | Urine Protein |
| Q29ObsDR | - |  |  | SI | Urine Protein DR |
| Q30 | - |  |  | SI | Urine Nitrates |
| Q30ObsDR | - |  |  | SI | Urine Nitrates DR |
| Q31 | - |  |  | SI | Urine Leucocytes |
| Q31ObsDR | - |  |  | SI | Urine Leucocytes DR |
| Q32 | - |  |  | SI | FiO2 |
| Q32ObsDR | - |  |  | SI | FiO2 DR |
| Q33 | - |  |  | SI | Visual Acuity (L) |
| Q33ObsDR | - |  |  | SI | Visual Acuity (L) DR |
| Q34 | - |  |  | SI | Visual Acuity (R) |
| Q34ObsDR | - |  |  | SI | Visual Acuity (R) DR |
| Q35 | - |  |  | SI | Verbal response <5 |
| Q36 | - |  |  | SI | Under 5 |
| Q37 | - |  |  | SI | Score |
| Q38 | - |  |  | SI | Score <5 |
| Q41 | - |  |  | SI | Tetanus cover |
| Q42 | - |  |  | SI | Tetanus Date |
| Q43 | - |  |  | SI | Fast Score |
| Q44 | - |  |  | SI | M.E.W.S Score |
| Q45 | - |  |  | SI | C.E.W.S Score |
| Q50 | - |  |  | SI | Vital Signs |
| Q51 | - |  |  | SI | Glasgow Coma Score |
| Q52 | - |  |  | SI | Visual Acuity |
| Q53 | - |  |  | SI | Urinanalysis |
| Q55 | - |  |  | SI | Mean Arterial Pressure |
| Q56 | - |  |  | SI | Re-Evaluation notes |
| Q57 | - |  |  | SI | Date |
| Q58 | - |  |  | SI | Time |
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