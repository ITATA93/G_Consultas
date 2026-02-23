# questionnaire.QTCHRST

> High Risk Screening Tool

**Schema:** questionnaire
**Columnas:** 104
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* High Risk Screening Tool

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q1 | date |  |  | SI | Date |
| Q10 | varchar |  |  | SI | Others (specify) |
| Q11 | varchar |  |  | SI | Screening outcome |
| Q12 | date |  |  | SI | Date social worker notified |
| Q13 | time |  |  | SI | Time social worker notified |
| Q14 | varchar |  |  | SI | Screening for chronic pain |
| Q15 | varchar |  |  | SI | If Yes, please notify the pain management clinic |
| Q16 | varchar |  |  | SI | Chronic pain |
| Q17 | varchar |  |  | SI | Disability screening |
| Q18 | varchar |  |  | SI | If screening is positive for any of the disabiliti... |
| Q19 | varchar |  |  | SI | Disability |
| Q19a | varchar |  |  | SI | Others (specify) |
| Q2 | time |  |  | SI | Time |
| Q20 | varchar |  |  | SI | Functional screening and learning needs |
| Q21 | varchar |  |  | SI | Physical therapy |
| Q22 | varchar |  |  | SI | Occupational therapy |
| Q23 | varchar |  |  | SI | Speech language practitioner |
| Q24 | varchar |  |  | SI | Learning needs |
| Q25 | varchar |  |  | SI | Referral needed |
| Q26 | varchar |  |  | SI | Referral to |
| Q27 | varchar |  |  | SI | Immunocompromised screening |
| Q28 | varchar |  |  | SI | Medication induced |
| Q28a | varchar |  |  | SI | If screening is positive for any of the Immunocomp... |
| Q29 | varchar |  |  | SI | Therapies |
| Q3 | varchar |  |  | SI | Nutritional screening |
| Q30 | varchar |  |  | SI | Malnutrition |
| Q31 | varchar |  |  | SI | Diseases |
| Q31a | varchar |  |  | SI | Others (specify) |
| Q32 | varchar |  |  | SI | Abuse and neglect screening |
| Q32a | varchar |  |  | SI | If screening is positive for abuse or neglect, ple... |
| Q33 | varchar |  |  | SI | Have you relied on people for any of the following... |
| Q34 | varchar |  |  | SI | Has anyone prevented you from getting food, clothe... |
| Q35 | varchar |  |  | SI | Has anyone prevented you from being with people yo... |
| Q36 | varchar |  |  | SI | Have you been upset because someone talked to you ... |
| Q37 | varchar |  |  | SI | Has anyone tried to force you to sign papers or to... |
| Q38 | varchar |  |  | SI | Has anyone made you afraid, touched you in ways th... |
| Q39 | varchar |  |  | SI | Signs of abuse - nurse observation |
| Q4 | varchar |  |  | SI | Please notify the clinical nutritionist if the pat... |
| Q40 | varchar |  |  | SI | Others (specify) |
| Q41 | varchar |  |  | SI | Environmental screening |
| Q42 | varchar |  |  | SI | Does the patient suffer from any functional defici... |
| Q43 | varchar |  |  | SI | Please describe the patient's home |
| Q44 | varchar |  |  | SI | Living arrangements |
| Q45 | varchar |  |  | SI | Home access type |
| Q46 | numeric |  |  | SI | Floor number |
| Q47 | numeric |  |  | SI | Number of stairs/ stair cases |
| Q48 | varchar |  |  | SI | Doorways leading to patient room |
| Q49 | numeric |  |  | SI | Doorways width (cm) |
| Q5 | varchar |  |  | SI | Conditions |
| Q50 | varchar |  |  | SI | Does the patient have access to any of the followi... |
| Q51 | varchar |  |  | SI | Shower |
| Q52 | varchar |  |  | SI | Tub |
| Q53 | varchar |  |  | SI | Refrigerator |
| Q54 | varchar |  |  | SI | Cool, dry place |
| Q55 | varchar |  |  | SI | Toilet |
| Q56 | varchar |  |  | SI | Toilet type |
| Q57 | varchar |  |  | SI | Others (specify) |
| Q58 | varchar |  |  | SI | Additional details |
| Q6 | varchar |  |  | SI | If nutritional screening is positive for any of th... |
| Q7 | varchar |  |  | SI | Findings |
| Q7a | varchar |  |  | SI | Comments |
| Q8 | varchar |  |  | SI | Psychosocial screening |
| Q9 | varchar |  |  | SI | Issues |
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