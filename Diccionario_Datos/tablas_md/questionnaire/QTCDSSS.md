# questionnaire.QTCDSSS

> Depression and Somatic Symptoms Scale

**Schema:** questionnaire
**Columnas:** 83
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Depression and Somatic Symptoms Scale

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Please evaluate the severity of these symptoms you... |
| Q02 | varchar |  |  | SI | Level |
| Q03 | varchar |  |  | SI | Absent - No symptoms	 |
| Q04 | varchar |  |  | SI | Mild - Slight discomfort or disturbance |
| Q05 | varchar |  |  | SI | Moderate - Significant discomfort or disturbance |
| Q06 | varchar |  |  | SI | Severe - Very significant discomfort of disturbanc... |
| Q07 | varchar |  |  | SI | Headache |
| Q08 | varchar |  |  | SI | Loss of interest in daily or leisure activities	 |
| Q09 | varchar |  |  | SI | Tightness in the chest	 |
| Q10 | varchar |  |  | SI | Insomnia |
| Q11 | varchar |  |  | SI | Muscle tension |
| Q12 | varchar |  |  | SI | Irritable mood	 |
| Q13 | varchar |  |  | SI | Back pain	 |
| Q14 | varchar |  |  | SI | Unable to feel happy or decreased ability to feel ... |
| Q15 | varchar |  |  | SI | Dizziness |
| Q16 | varchar |  |  | SI | Depressed mood or tearful	 |
| Q17 | varchar |  |  | SI | Chest pain	 |
| Q18 | varchar |  |  | SI | Feelings of self-reproach or guilt	 |
| Q19 | varchar |  |  | SI | Neck or shoulder pain (or soreness)	 |
| Q20 | varchar |  |  | SI | Loss of interest in sex	 |
| Q21 | varchar |  |  | SI | Shortness of breath or difficulty breathing	 |
| Q22 | varchar |  |  | SI | Unable to concentrate	 |
| Q23 | varchar |  |  | SI | Palpitations or increased heart rate	 |
| Q24 | varchar |  |  | SI | Anxious or nervous	 |
| Q25 | varchar |  |  | SI | Soreness in more than half of the body's muscles |
| Q26 | varchar |  |  | SI | Thoughts of death or suicidal ideas	 |
| Q27 | varchar |  |  | SI | Fatigue or loss of energy	 |
| Q28 | varchar |  |  | SI | Decreased appetite or loss of appetite |
| Q29 | varchar |  |  | SI | Minimum Score |
| Q30 | varchar |  |  | SI | 0 |
| Q31 | varchar |  |  | SI | Maximum Score	 |
| Q32 | varchar |  |  | SI | 66 |
| Q33 | varchar |  |  | SI | Higher scores indicate more severe depression and ... |
| Q34 | varchar |  |  | SI | The DSSS is a psychometrically sound measure of de... |
| Q35 | date |  |  | SI | Date |
| Q36 | time |  |  | SI | Time |
| Q37 | varchar |  |  | SI | Score |
| Q38 | varchar |  |  | SI | Classification |
| Q39 | varchar |  |  | SI | 0 |
| Q40 | varchar |  |  | SI | Minimum Score |
| Q41 | varchar |  |  | SI | 66 |
| Q42 | varchar |  |  | SI | Maximum Score |
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