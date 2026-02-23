# SQLUser.LBC_Interpretation

**Schema:** SQLUser
**Columnas:** 100
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Laboratorio**. Parámetros del módulo de laboratorio.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBCINT_RowID | bigint | PK |  | NO | - |
| LBCINT_Code | varchar |  |  | NO | Code |
| LBCINT_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| LBCINT_CodeTranslated | varchar |  |  | SI | - |
| LBCINT_CreatedDate | date |  |  | SI | Created Date |
| LBCINT_CreatedTime | time |  |  | SI | Created Time |
| LBCINT_CreatedUser_DR | bigint |  | FK | SI | Created User |
| LBCINT_DateFrom | date |  |  | SI | From Date |
| LBCINT_DateTo | date |  |  | SI | To Date |
| LBCINT_Desc | varchar |  |  | NO | Description |
| LBCINT_DescTranslated | varchar |  |  | SI | - |
| LBCINT_InterpretationText | longvarchar |  |  | SI | Interpretation
HTMLRichText |
| LBCINT_Owner | varchar |  |  | SI | Owner |
| LBCINT_Reportable | varchar |  |  | SI | Reportable fag |
| LBCINT_Type | varchar |  |  | SI | Interpretation Type
TSI = Test Item
TS = Test Se... |
| LBCINT_UpdatedDate | date |  |  | SI | Updated Date |
| LBCINT_UpdatedTime | time |  |  | SI | Updated Time |
| LBCINT_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Please evaluate the severity of these symptoms you... |
| Q02 | - |  |  | SI | Level |
| Q03 | - |  |  | SI | Absent - No symptoms	 |
| Q04 | - |  |  | SI | Mild - Slight discomfort or disturbance |
| Q05 | - |  |  | SI | Moderate - Significant discomfort or disturbance |
| Q06 | - |  |  | SI | Severe - Very significant discomfort of disturbanc... |
| Q07 | - |  |  | SI | Headache |
| Q08 | - |  |  | SI | Loss of interest in daily or leisure activities	 |
| Q09 | - |  |  | SI | Tightness in the chest	 |
| Q10 | - |  |  | SI | Insomnia |
| Q11 | - |  |  | SI | Muscle tension |
| Q12 | - |  |  | SI | Irritable mood	 |
| Q13 | - |  |  | SI | Back pain	 |
| Q14 | - |  |  | SI | Unable to feel happy or decreased ability to feel ... |
| Q15 | - |  |  | SI | Dizziness |
| Q16 | - |  |  | SI | Depressed mood or tearful	 |
| Q17 | - |  |  | SI | Chest pain	 |
| Q18 | - |  |  | SI | Feelings of self-reproach or guilt	 |
| Q19 | - |  |  | SI | Neck or shoulder pain (or soreness)	 |
| Q20 | - |  |  | SI | Loss of interest in sex	 |
| Q21 | - |  |  | SI | Shortness of breath or difficulty breathing	 |
| Q22 | - |  |  | SI | Unable to concentrate	 |
| Q23 | - |  |  | SI | Palpitations or increased heart rate	 |
| Q24 | - |  |  | SI | Anxious or nervous	 |
| Q25 | - |  |  | SI | Soreness in more than half of the body's muscles |
| Q26 | - |  |  | SI | Thoughts of death or suicidal ideas	 |
| Q27 | - |  |  | SI | Fatigue or loss of energy	 |
| Q28 | - |  |  | SI | Decreased appetite or loss of appetite |
| Q29 | - |  |  | SI | Minimum Score |
| Q30 | - |  |  | SI | 0 |
| Q31 | - |  |  | SI | Maximum Score	 |
| Q32 | - |  |  | SI | 66 |
| Q33 | - |  |  | SI | Higher scores indicate more severe depression and ... |
| Q34 | - |  |  | SI | The DSSS is a psychometrically sound measure of de... |
| Q35 | - |  |  | SI | Date |
| Q36 | - |  |  | SI | Time |
| Q37 | - |  |  | SI | Score |
| Q38 | - |  |  | SI | Classification |
| Q39 | - |  |  | SI | 0 |
| Q40 | - |  |  | SI | Minimum Score |
| Q41 | - |  |  | SI | 66 |
| Q42 | - |  |  | SI | Maximum Score |
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