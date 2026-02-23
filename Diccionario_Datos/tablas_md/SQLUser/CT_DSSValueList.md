# SQLUser.CT_DSSValueList

**Schema:** SQLUser
**Columnas:** 102
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de configuración**. Tabla de referencia del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| DSSVAL_RowId | bigint | PK |  | NO | - |
| ChildQ03DR | - |  |  | SI | Child Reference: Review attended by |
| DSSVAL_Code | varchar |  |  | NO | Code |
| DSSVAL_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| DSSVAL_CreatedDate | date |  |  | SI | Created Date |
| DSSVAL_CreatedTime | time |  |  | SI | Created Time |
| DSSVAL_CreatedUser_DR | bigint |  | FK | SI | Created User |
| DSSVAL_DateFrom | date |  |  | SI | Date From |
| DSSVAL_DateTo | date |  |  | SI | Date To |
| DSSVAL_Desc | varchar |  |  | NO | Description |
| DSSVAL_Owner | varchar |  |  | SI | Owner |
| DSSVAL_UpdatedDate | date |  |  | SI | Updated Date |
| DSSVAL_UpdatedTime | time |  |  | SI | Updated Time |
| DSSVAL_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| DSSVAL_Values | varchar |  |  | SI | Values |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q04 | - |  |  | SI | Review pain at rest / movement scores in vital sig... |
| Q05 | - |  |  | SI | How has your pain been since last review |
| Q06 | - |  |  | SI | Location of pain |
| Q07 | - |  |  | SI | Pain categorisation |
| Q08 | - |  |  | SI | How did you sleep last night |
| Q09 | - |  |  | SI | Sleep details |
| Q10 | - |  |  | SI | Functional Activity |
| Q11 | - |  |  | SI | Activity (Coughing) |
| Q12 | - |  |  | SI | Activity (Deep breathing) |
| Q13 | - |  |  | SI | Triflow result |
| Q14 | - |  |  | SI | Activity (Sitting out of bed) |
| Q15 | - |  |  | SI | Activity (Mobilising) |
| Q16 | - |  |  | SI | Sedation State |
| Q17 | - |  |  | SI | Has the patient had a sedation score of ≥ 2 since ... |
| Q18 | - |  |  | SI | Sedation state since the last review, has the pati... |
| Q19 | - |  |  | SI | Reports of hallucinations |
| Q20 | - |  |  | SI | Vivid dreams |
| Q21 | - |  |  | SI | Other Neurological Symptoms |
| Q22 | - |  |  | SI | Do you have any itching |
| Q23 | - |  |  | SI | Itching (puritis) severity |
| Q24 | - |  |  | SI | Is the itching resolved with medications |
| Q25 | - |  |  | SI | Neurological notes |
| Q26 | - |  |  | SI | Since the last review, has the patient's respirato... |
| Q27 | - |  |  | SI | Since the last review, has the patient developed a... |
| Q28 | - |  |  | SI | Has the patient had opioid induced ventilatory imp... |
| Q29 | - |  |  | SI | Ventilatory impairment:&nbsp |
| Q30 | - |  |  | SI | Respiratory notes |
| Q31 | - |  |  | SI | Since the last review, has the patient had a mean ... |
| Q32 | - |  |  | SI | Since the last review has the patient been given a... |
| Q33 | - |  |  | SI | Has analgesia significantly contributed to hypoten... |
| Q34 | - |  |  | SI | Cardiovascular notes |
| Q35 | - |  |  | SI | Oral intake status |
| Q36 | - |  |  | SI | Intake method |
| Q37 | - |  |  | SI | Do you have any nausea or vomiting |
| Q38 | - |  |  | SI | Has your nausea and/or vomiting prevented oral int... |
| Q39 | - |  |  | SI | Has your nausea and/or vomiting resolved with medi... |
| Q40 | - |  |  | SI | Is the patient taking aperients |
| Q41 | - |  |  | SI | Bowels (since last review) |
| Q42 | - |  |  | SI | Days since last bowel movement |
| Q43 | - |  |  | SI | Gastrointestinal notes |
| Q44 | - |  |  | SI | Type of analgesia |
| Q45 | - |  |  | SI | Site appears |
| Q46 | - |  |  | SI | Site check notes |
| Q47 | - |  |  | SI | Acute pain service plan |
| Q48 | - |  |  | SI | Dummy1 |
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