# SQLUser.OEC_SPO2TargetRange

**Schema:** SQLUser
**Columnas:** 106
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Entry Orders**. Tipos y estados de órdenes.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SPO2_RowId | bigint | PK |  | NO | - |
| Q01 | - |  |  | SI | The Severe Sepsis Screening Tool is an optional to... |
| Q02 | - |  |  | SI | 0-1 Point: No suspicion of infection is present |
| Q03 | - |  |  | SI | 2 Points: Suspicion of infection is present |
| Q04 | - |  |  | SI | 3 Points: Severe sepsis is present |
| Q05 | - |  |  | SI | Is the patient’s history suggestive of a new infec... |
| Q06 | - |  |  | SI | Pneumonia, empyema |
| Q07 | - |  |  | SI | Urinary tract infection |
| Q08 | - |  |  | SI | Acute abdominal infection |
| Q09 | - |  |  | SI | Meningitis |
| Q10 | - |  |  | SI | Skin/soft tissue infection |
| Q11 | - |  |  | SI | Bone / joint infection |
| Q12 | - |  |  | SI | Wound infection |
| Q13 | - |  |  | SI | Bloodstream catheter infection |
| Q14 | - |  |  | SI | Endocarditis |
| Q15 | - |  |  | SI | Implantable device infection |
| Q16 | - |  |  | SI | Other |
| Q16a | - |  |  | SI | Other |
| Q18 | - |  |  | SI | Are any two of following signs &amp |
| Q19 | - |  |  | SI | Note: laboratory values may have been obtained for... |
| Q20 | - |  |  | SI | Hyperthermia &gt |
| Q21 | - |  |  | SI | Hypothermia &lt |
| Q22 | - |  |  | SI | Tachycardia &gt |
| Q23 | - |  |  | SI | Tachypnea &gt |
| Q24 | - |  |  | SI | Altered mental status |
| Q25 | - |  |  | SI | Leukocytosis (WBC count &gt |
| Q26 | - |  |  | SI | Leukopenia (WBC count &lt |
| Q27 | - |  |  | SI | Hyperglycemia (plasma glucose &gt |
| Q28 | - |  |  | SI | Obtain: lactic acid, blood cultures, complete bloo... |
| Q30 | - |  |  | SI | Are any of the following organ dysfunction criteri... |
| Q31 | - |  |  | SI | Note: the remote site stipulation is waived in the... |
| Q32 | - |  |  | SI | Systolic BP &lt |
| Q33 | - |  |  | SI | SBP decrease &gt |
| Q34 | - |  |  | SI | Bilateral pulmonary infiltrates with a new (or inc... |
| Q35 | - |  |  | SI | Bilateral pulmonary infiltrates with PaO2/FiO2 rat... |
| Q36 | - |  |  | SI | Creatinine &gt |
| Q37 | - |  |  | SI | Bilirubin &gt |
| Q38 | - |  |  | SI | Platelet count &lt |
| Q39 | - |  |  | SI | Coagulopathy (INR &gt |
| Q40 | - |  |  | SI | Lactate &gt |
| Q41 | - |  |  | SI | If suspicion of infection is present AND organ dys... |
| Q42 | - |  |  | SI | If the answer is yes to both either question 1 and... |
| Q43 | - |  |  | SI | Yes / No |
| Q44 | - |  |  | SI | Yes / No |
| Q45 | - |  |  | SI | Yes / No |
| Q46 | - |  |  | SI | Date |
| Q47 | - |  |  | SI | Time |
| Q50 | - |  |  | SI | .... |
| Q51 | - |  |  | SI | .... |
| Q52 | - |  |  | SI | ................ |
| Q53 | - |  |  | SI | Schorr C, Odden A, Evans L,&nbsp |
| Q54 | - |  |  | SI | Are any two of following signs &amp |
| Q55 | - |  |  | SI | Are any of the following organ dysfunction criteri... |
| Q56 | - |  |  | SI | Is the patient’s history suggestive of a new infec... |
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
| SPO2_Code | varchar |  |  | NO | Code |
| SPO2_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| SPO2_CreatedDate | date |  |  | SI | Created Date |
| SPO2_CreatedTime | time |  |  | SI | Created Time |
| SPO2_CreatedUser_DR | bigint |  | FK | SI | Created User |
| SPO2_DateFrom | date |  |  | SI | Date From |
| SPO2_DateTo | date |  |  | SI | Date To |
| SPO2_Desc | varchar |  |  | NO | Description |
| SPO2_Owner | varchar |  |  | SI | Owner |
| SPO2_UpdatedDate | date |  |  | SI | Updated Date |
| SPO2_UpdatedTime | time |  |  | SI | Updated Time |
| SPO2_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*