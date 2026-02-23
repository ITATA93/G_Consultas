# SQLUser.PAC_AllergySeverity

**Schema:** SQLUser
**Columnas:** 122
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ALRGSEV_RowId | bigint | PK |  | NO | - |
| ALRGSEV_Code | varchar |  |  | NO | Code |
| ALRGSEV_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| ALRGSEV_CodeTranslated | varchar |  |  | SI | - |
| ALRGSEV_Color | varchar |  |  | SI | Color |
| ALRGSEV_CreatedDate | date |  |  | SI | Created Date |
| ALRGSEV_CreatedTime | time |  |  | SI | Created Time |
| ALRGSEV_CreatedUser_DR | bigint |  | FK | SI | Created User |
| ALRGSEV_DateFrom | date |  |  | SI | Date From |
| ALRGSEV_DateTo | date |  |  | SI | Date To |
| ALRGSEV_Desc | varchar |  |  | NO | Description |
| ALRGSEV_DescTranslated | varchar |  |  | SI | - |
| ALRGSEV_LongDescription | varchar |  |  | SI | Long Description |
| ALRGSEV_MandatoryOverride | varchar |  |  | SI | MandatoryOverride |
| ALRGSEV_Owner | varchar |  |  | SI | Owner |
| ALRGSEV_Priority | double |  |  | SI | Priority |
| ALRGSEV_UpdatedDate | date |  |  | SI | Updated Date |
| ALRGSEV_UpdatedTime | time |  |  | SI | Updated Time |
| ALRGSEV_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q1 | - |  |  | SI | Date |
| Q10 | - |  |  | SI | Others (specify) |
| Q11 | - |  |  | SI | Screening outcome |
| Q12 | - |  |  | SI | Date social worker notified |
| Q13 | - |  |  | SI | Time social worker notified |
| Q14 | - |  |  | SI | Screening for chronic pain |
| Q15 | - |  |  | SI | If Yes, please notify the pain management clinic |
| Q16 | - |  |  | SI | Chronic pain |
| Q17 | - |  |  | SI | Disability screening |
| Q18 | - |  |  | SI | If screening is positive for any of the disabiliti... |
| Q19 | - |  |  | SI | Disability |
| Q19a | - |  |  | SI | Others (specify) |
| Q2 | - |  |  | SI | Time |
| Q20 | - |  |  | SI | Functional screening and learning needs |
| Q21 | - |  |  | SI | Physical therapy |
| Q22 | - |  |  | SI | Occupational therapy |
| Q23 | - |  |  | SI | Speech language practitioner |
| Q24 | - |  |  | SI | Learning needs |
| Q25 | - |  |  | SI | Referral needed |
| Q26 | - |  |  | SI | Referral to |
| Q27 | - |  |  | SI | Immunocompromised screening |
| Q28 | - |  |  | SI | Medication induced |
| Q28a | - |  |  | SI | If screening is positive for any of the Immunocomp... |
| Q29 | - |  |  | SI | Therapies |
| Q3 | - |  |  | SI | Nutritional screening |
| Q30 | - |  |  | SI | Malnutrition |
| Q31 | - |  |  | SI | Diseases |
| Q31a | - |  |  | SI | Others (specify) |
| Q32 | - |  |  | SI | Abuse and neglect screening |
| Q32a | - |  |  | SI | If screening is positive for abuse or neglect, ple... |
| Q33 | - |  |  | SI | Have you relied on people for any of the following... |
| Q34 | - |  |  | SI | Has anyone prevented you from getting food, clothe... |
| Q35 | - |  |  | SI | Has anyone prevented you from being with people yo... |
| Q36 | - |  |  | SI | Have you been upset because someone talked to you ... |
| Q37 | - |  |  | SI | Has anyone tried to force you to sign papers or to... |
| Q38 | - |  |  | SI | Has anyone made you afraid, touched you in ways th... |
| Q39 | - |  |  | SI | Signs of abuse - nurse observation |
| Q4 | - |  |  | SI | Please notify the clinical nutritionist if the pat... |
| Q40 | - |  |  | SI | Others (specify) |
| Q41 | - |  |  | SI | Environmental screening |
| Q42 | - |  |  | SI | Does the patient suffer from any functional defici... |
| Q43 | - |  |  | SI | Please describe the patient's home |
| Q44 | - |  |  | SI | Living arrangements |
| Q45 | - |  |  | SI | Home access type |
| Q46 | - |  |  | SI | Floor number |
| Q47 | - |  |  | SI | Number of stairs/ stair cases |
| Q48 | - |  |  | SI | Doorways leading to patient room |
| Q49 | - |  |  | SI | Doorways width (cm) |
| Q5 | - |  |  | SI | Conditions |
| Q50 | - |  |  | SI | Does the patient have access to any of the followi... |
| Q51 | - |  |  | SI | Shower |
| Q52 | - |  |  | SI | Tub |
| Q53 | - |  |  | SI | Refrigerator |
| Q54 | - |  |  | SI | Cool, dry place |
| Q55 | - |  |  | SI | Toilet |
| Q56 | - |  |  | SI | Toilet type |
| Q57 | - |  |  | SI | Others (specify) |
| Q58 | - |  |  | SI | Additional details |
| Q6 | - |  |  | SI | If nutritional screening is positive for any of th... |
| Q7 | - |  |  | SI | Findings |
| Q7a | - |  |  | SI | Comments |
| Q8 | - |  |  | SI | Psychosocial screening |
| Q9 | - |  |  | SI | Issues |
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