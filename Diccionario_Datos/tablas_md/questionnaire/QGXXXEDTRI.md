# questionnaire.QGXXXEDTRI

> Triage ED

**Schema:** questionnaire
**Columnas:** 122
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Cuestionario/Formulario**. Plantilla de evaluación clínica estructurada. *(Triage ED)*

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Temperature |
| Q01ObsDR | varchar |  | FK | SI | Temperature DR |
| Q02 | varchar |  |  | SI | Pregnancy Test Result |
| Q02ObsDR | varchar |  | FK | SI | Pregnancy Test Result DR |
| Q03 | varchar |  |  | SI | Pupil Size (L) |
| Q03ObsDR | varchar |  | FK | SI | Pupil Size (L) DR |
| Q04 | varchar |  |  | SI | Pupil Size (R) |
| Q04ObsDR | varchar |  | FK | SI | Pupil Size (R) DR |
| Q05 | varchar |  |  | SI | Respirations |
| Q05ObsDR | varchar |  | FK | SI | Respirations DR |
| Q06 | varchar |  |  | SI | Systolic BP |
| Q06ObsDR | varchar |  | FK | SI | Systolic BP DR |
| Q07 | varchar |  |  | SI | Pupil Reaction (R) |
| Q07ObsDR | varchar |  | FK | SI | Pupil Reaction (R) DR |
| Q08 | varchar |  |  | SI | Pupil Reaction (L) |
| Q08ObsDR | varchar |  | FK | SI | Pupil Reaction (L) DR |
| Q09 | varchar |  |  | SI | Diastolic BP |
| Q09ObsDR | varchar |  | FK | SI | Diastolic BP DR |
| Q10 | varchar |  |  | SI | SpO2 |
| Q10ObsDR | varchar |  | FK | SI | SpO2 DR |
| Q11 | varchar |  |  | SI | Comments |
| Q12 | varchar |  |  | SI | Height (cm) |
| Q12ObsDR | varchar |  | FK | SI | Height (cm) DR |
| Q13 | varchar |  |  | SI | Weight (kg) |
| Q13ObsDR | varchar |  | FK | SI | Weight (kg) DR |
| Q14 | varchar |  |  | SI | Peak Pressure |
| Q14ObsDR | varchar |  | FK | SI | Peak Pressure DR |
| Q15 | varchar |  |  | SI | Mean Arterial Pressure |
| Q15ObsDR | varchar |  | FK | SI | Mean Arterial Pressure DR |
| Q16 | varchar |  |  | SI | Eye opening |
| Q17 | varchar |  |  | SI | Verbal response |
| Q18 | varchar |  |  | SI | Motor response |
| Q19 | varchar |  |  | SI | Pulse |
| Q19ObsDR | varchar |  | FK | SI | Pulse DR |
| Q20 | varchar |  |  | SI | Visual Acuity - With Correction |
| Q20ObsDR | varchar |  | FK | SI | Visual Acuity - With Correction DR |
| Q21 | varchar |  |  | SI | Blood Glucose |
| Q21ObsDR | varchar |  | FK | SI | Blood Glucose DR |
| Q22 | varchar |  |  | SI | Peak pressure expected |
| Q22ObsDR | varchar |  | FK | SI | Peak pressure expected DR |
| Q23 | varchar |  |  | SI | Pain Score |
| Q23ObsDR | varchar |  | FK | SI | Pain Score DR |
| Q24 | varchar |  |  | SI | Urine Glucose |
| Q24ObsDR | varchar |  | FK | SI | Urine Glucose DR |
| Q25 | varchar |  |  | SI | Urine Ketones |
| Q25ObsDR | varchar |  | FK | SI | Urine Ketones DR |
| Q26 | varchar |  |  | SI | Specific Gravity |
| Q26ObsDR | varchar |  | FK | SI | Specific Gravity DR |
| Q27 | varchar |  |  | SI | Urine Blood  |
| Q27ObsDR | varchar |  | FK | SI | Urine Blood  DR |
| Q28 | varchar |  |  | SI | Urine pH |
| Q28ObsDR | varchar |  | FK | SI | Urine pH DR |
| Q29 | varchar |  |  | SI | Urine Protein |
| Q29ObsDR | varchar |  | FK | SI | Urine Protein DR |
| Q30 | varchar |  |  | SI | Urine Nitrates |
| Q30ObsDR | varchar |  | FK | SI | Urine Nitrates DR |
| Q31 | varchar |  |  | SI | Urine Leucocytes |
| Q31ObsDR | varchar |  | FK | SI | Urine Leucocytes DR |
| Q32 | varchar |  |  | SI | FiO2 |
| Q32ObsDR | varchar |  | FK | SI | FiO2 DR |
| Q33 | varchar |  |  | SI | Visual Acuity (L) |
| Q33ObsDR | varchar |  | FK | SI | Visual Acuity (L) DR |
| Q34 | varchar |  |  | SI | Visual Acuity (R) |
| Q34ObsDR | varchar |  | FK | SI | Visual Acuity (R) DR |
| Q35 | varchar |  |  | SI | Verbal response <5 |
| Q36 | varchar |  |  | SI | Under 5 |
| Q37 | varchar |  |  | SI | Score |
| Q38 | varchar |  |  | SI | Score <5 |
| Q41 | varchar |  |  | SI | Tetanus cover |
| Q42 | date |  |  | SI | Tetanus Date |
| Q43 | numeric |  |  | SI | Fast Score |
| Q44 | numeric |  |  | SI | M.E.W.S Score |
| Q45 | numeric |  |  | SI | C.E.W.S Score |
| Q50 | varchar |  |  | SI | Vital Signs |
| Q51 | varchar |  |  | SI | Glasgow Coma Score |
| Q52 | varchar |  |  | SI | Visual Acuity |
| Q53 | varchar |  |  | SI | Urinanalysis |
| Q55 | varchar |  |  | SI | Mean Arterial Pressure |
| Q56 | varchar |  |  | SI | Re-Evaluation notes |
| Q57 | date |  |  | SI | Date |
| Q58 | time |  |  | SI | Time |
| QUESAnaDR | varchar |  | FK | SI | Anaesthesia |
| QUESAnaOperationDR | varchar |  | FK | SI | Operation |
| QUESConsultDR | varchar |  | FK | SI | Consult |
| QUESCopiedComments | varchar |  |  | SI | Copied Comments |
| QUESCopiedDate | date |  |  | SI | Copied Date |
| QUESCopiedEpDR | bigint |  | FK | SI | Copied Episode |
| QUESCopiedSourceDR | bigint |  | FK | SI | Copied Source DR |
| QUESCopiedTime | time |  |  | SI | Copied Time |
| QUESCopiedUserDR | bigint |  | FK | SI | Copied User |
| QUESCreateDate | date |  |  | SI | Creation Date |
| QUESCreateTime | time |  |  | SI | Creation Time |
| QUESCreateUserDR | bigint |  | FK | SI | Creation User |
| QUESDate | date |  |  | SI | Last Update Date |
| QUESErrorReasonDR | bigint |  | FK | SI | Error Reason |
| QUESFHResidentDR | bigint |  | FK | SI | Resident |
| QUESMRClinicalPathWaysDR | varchar |  | FK | SI | Clinical Pathway |
| QUESNRCarePlanIssuesDR | varchar |  | FK | SI | Nurse Care Plan Issues |
| QUESOEOrdExecDR | varchar |  | FK | SI | Order Execution |
| QUESORPreanaestheticConsultDR | bigint |  | FK | SI | Preanaesthetic Consultation |
| QUESObsEntryDR | varchar |  | FK | SI | Observation Entry |
| QUESOperRoomDR | bigint |  | FK | SI | Operating Room |
| QUESPAAdmDR | bigint |  | FK | SI | Admission |
| QUESPAAdverseEventDR | varchar |  | FK | SI | Adverse Event |
| QUESPAPatMasDR | bigint |  | FK | SI | Patient |
| QUESPAPregnancyDR | bigint |  | FK | SI | Pregnancy |
| QUESPAWaitingListDR | bigint |  | FK | SI | Waiting List |
| QUESPathwayItemDR | varchar |  | FK | SI | Pathway Item |
| QUESPrePostExamOEOrdItemDR | varchar |  | FK | SI | Pre/Post Exam OrdItem |
| QUESRBAppointmentDR | varchar |  | FK | SI | Appointments |
| QUESRBApptOutcomeDR | varchar |  | FK | SI | Appointment Outcome |
| QUESRBApptSlotDR | varchar |  | FK | SI | Appointment Slot |
| QUESReasonForCorrectionDR | bigint |  | FK | SI | Reason for Correction |
| QUESSSUserDefWindowDR | bigint |  | FK | SI | Questionnaire |
| QUESScore | varchar |  |  | SI | Score |
| QUESSecondUserDR | bigint |  | FK | SI | Second Signature |
| QUESStatusDR | bigint |  | FK | SI | Status |
| QUESTextResultDR | bigint |  | FK | SI | Text Result |
| QUESTime | time |  |  | SI | Last Update Time |
| QUESTransactionDR | varchar |  | FK | SI | Transaction |
| QUESUserDR | bigint |  | FK | SI | Last Update User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*