# questionnaire.QTCSTAMP

> Screening Tool for the Assessment of Malnutrition in Paediatrics (STAMP)

**Schema:** questionnaire
**Columnas:** 116
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Screening Tool for the Assessment of Malnutrition in Paediatrics (STAMP)

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Step 1 - Diagnosis: Does the child have a diagnosi... |
| Q02 | varchar |  |  | SI | Step 2 - Nutritional intake: What is the child’s n... |
| Q03 | varchar |  |  | SI | Step 3 - Weight and height: Use a growth chart or ... |
| Q04 | varchar |  |  | SI | STAMP care plan note |
| Q05 | varchar |  |  | SI | Care plan |
| Q06 | varchar |  |  | SI | Use management guidelines and/or local nutrition p... |
| Q07 | varchar |  |  | SI | High risk care plan |
| Q08 | varchar |  |  | SI | • Take action |
| Q09 | varchar |  |  | SI | • Refer the child to a dietitian, nutritional supp... |
| Q10 | varchar |  |  | SI | • Monitor as per care plan |
| Q11 | varchar |  |  | SI | Medium risk care plan |
| Q12 | varchar |  |  | SI | • Monitor the child's nuttritional intake for 3 da... |
| Q13 | varchar |  |  | SI | • Repeat the STAMP screening after 3 days |
| Q14 | varchar |  |  | SI | • Amend care plan as required |
| Q15 | varchar |  |  | SI | Low risk rare plan |
| Q16 | varchar |  |  | SI | • Continue routine clinical care |
| Q17 | varchar |  |  | SI | • Repeat STAMP screening weekly while the child is... |
| Q18 | varchar |  |  | SI | • Amend care plan as required |
| Q19 | varchar |  |  | SI | Guidelines to determine the nutritional implicatio... |
| Q20 | varchar |  |  | SI | Definite nutritional implications |
| Q21 | varchar |  |  | SI | • Bowel failure, intractable diarrhea |
| Q22 | varchar |  |  | SI | • Burns and major trauma |
| Q23 | varchar |  |  | SI | • Crohn's disease |
| Q24 | varchar |  |  | SI | • Cystic fibrosis |
| Q25 | varchar |  |  | SI | • Dysphagia |
| Q26 | varchar |  |  | SI | • Liver disease |
| Q27 | varchar |  |  | SI | • Major surgery |
| Q28 | varchar |  |  | SI | • Multiple food allergies / intolerances |
| Q29 | varchar |  |  | SI | • Oncology on active treatment |
| Q30 | varchar |  |  | SI | • Renal disease / failure |
| Q31 | varchar |  |  | SI | • Inborn errors of metabolism |
| Q32 | varchar |  |  | SI | Possible nutritional implications |
| Q33 | varchar |  |  | SI | • Behavioural eating problems |
| Q34 | varchar |  |  | SI | • Cardiology |
| Q35 | varchar |  |  | SI | • Cerebral palsy |
| Q36 | varchar |  |  | SI | • Cleft lip and palate |
| Q37 | varchar |  |  | SI | • Celiac disease |
| Q38 | varchar |  |  | SI | • Diabetes |
| Q39 | varchar |  |  | SI | • Gastroesophageal reflux |
| Q40 | varchar |  |  | SI | • Minor surgery |
| Q41 | varchar |  |  | SI | • Neuromuscular conditions |
| Q42 | varchar |  |  | SI | • Psychiatric disorders |
| Q43 | varchar |  |  | SI | • Respiratory Syncytial Virus (RSV) |
| Q44 | varchar |  |  | SI | • Single food allergy / intolerance |
| Q45 | varchar |  |  | SI | No nutritional implications |
| Q46 | varchar |  |  | SI | • Day case surgery |
| Q47 | varchar |  |  | SI | • Investigations |
| Q48 | varchar |  |  | SI | Guidelines for accurate measurement (step 3 above) |
| Q49 | varchar |  |  | SI | Tared weighing (infant or child will not lie or st... |
| Q50 | varchar |  |  | SI | 1. Weigh parent / carer barefoot and record in kg |
| Q51 | varchar |  |  | SI | 2. Weigh parent / carer and infant / child togethe... |
| Q52 | varchar |  |  | SI | 3. Subtract the parent / carer weight to obtain ch... |
| Q53 | varchar |  |  | SI | Infant (<2y) and child (≥2y) measuring requirement... |
| Q54 | varchar |  |  | SI | 1. Infant weighed unclothed |
| Q55 | varchar |  |  | SI | 2. Child weighed with minimal clothing |
| Q56 | varchar |  |  | SI | 3. Infant / child weight recorded to the nearest 0... |
| Q57 | varchar |  |  | SI | 4. Infant / child length / height recorded to near... |
| Q58 | varchar |  |  | SI | 5. Shoes and socks removed before length / height ... |
| Q59 | varchar |  |  | SI | 6. Child ≥ 2y that cannot stand: measure length an... |
| Q60 | varchar |  |  | SI | 7. Infant <2y that cannot lie down: measure standi... |
| Q61 | varchar |  |  | SI | Score |
| Q62 | varchar |  |  | SI | Classification |
| Q63 | varchar |  |  | SI | 0 - 1  |
| Q64 | varchar |  |  | SI | 2 - 3 |
| Q65 | varchar |  |  | SI | ≥ 4 |
| Q66 | varchar |  |  | SI | High risk |
| Q67 | varchar |  |  | SI | Medium risk |
| Q68 | varchar |  |  | SI | Low risk |
| Q69 | varchar |  |  | SI | The Screening Tool for the Assessment of Malnutrit... |
| Q70 | varchar |  |  | SI | and it designed for use with children in hospitals... |
| Q71 | date |  |  | SI | Date |
| Q72 | time |  |  | SI | Time os assessment |
| Q73 | time |  |  | SI | Time |
| Q74 | date |  |  | SI | Date |
| Q75 | time |  |  | SI | Time |
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