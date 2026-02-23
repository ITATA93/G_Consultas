# questionnaire.QTCCFUA

> Cardiology Follow Up Assessment

**Schema:** questionnaire
**Columnas:** 112
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Cardiology Follow Up Assessment

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Follow up details |
| Q02 | varchar |  |  | SI | Follow up progress |
| Q03 | varchar |  |  | SI | Chest pain |
| Q04 | varchar |  |  | SI | Chest pain comments |
| Q05 | varchar |  |  | SI | Cough |
| Q06 | varchar |  |  | SI | Cough comments |
| Q07 | varchar |  |  | SI | Dyspnoea |
| Q08 | varchar |  |  | SI | Dyspnoea comments |
| Q09 | varchar |  |  | SI | Orthopnoea |
| Q10 | varchar |  |  | SI | Orthopnoea comments |
| Q11 | varchar |  |  | SI | Fever |
| Q12 | varchar |  |  | SI | Fever comments |
| Q13 | varchar |  |  | SI | Nausea and vomiting |
| Q14 | varchar |  |  | SI | Nausea and vomiting comments |
| Q15 | varchar |  |  | SI | Other symptoms |
| Q16 | varchar |  |  | SI | Objective findings |
| Q18 | varchar |  |  | SI | Physical Examination |
| Q19 | varchar |  |  | SI | Pale |
| Q20 | varchar |  |  | SI | Pale comment |
| Q21 | varchar |  |  | SI | Jaundice |
| Q22 | varchar |  |  | SI | Jaundice comment |
| Q23 | varchar |  |  | SI | Palpable lymph node |
| Q24 | varchar |  |  | SI | Palpable lymph node comment |
| Q25 | varchar |  |  | SI | HEENT other examination findings |
| Q26 | varchar |  |  | SI | Lungs clear |
| Q27 | varchar |  |  | SI | Lung comment |
| Q28 | varchar |  |  | SI | Fine crackles / rales |
| Q29 | varchar |  |  | SI | Fine crackles / rales  comment |
| Q30 | varchar |  |  | SI | Coarse crackles |
| Q31 | varchar |  |  | SI | Coarse crackles comment |
| Q32 | varchar |  |  | SI | Wheeze |
| Q33 | varchar |  |  | SI | Wheeze comment |
| Q34 | varchar |  |  | SI | Ronchi |
| Q35 | varchar |  |  | SI | Ronchi comments |
| Q36 | varchar |  |  | SI | Lungs other examination findings |
| Q37 | varchar |  |  | SI | Normal heart rate and sinus rhythm |
| Q38 | varchar |  |  | SI | Rate and rhythm comment |
| Q39 | varchar |  |  | SI | Normal S1 S2 |
| Q40 | varchar |  |  | SI | S1 S2 comment |
| Q41 | varchar |  |  | SI | Presence of S3 |
| Q42 | varchar |  |  | SI | S3 comment |
| Q43 | varchar |  |  | SI | Presence of S4 |
| Q44 | varchar |  |  | SI | S4 comment |
| Q45 | varchar |  |  | SI | Murmur |
| Q46 | varchar |  |  | SI | Murmur comment |
| Q47 | varchar |  |  | SI | CVS other examination findings |
| Q48 | varchar |  |  | SI | Soft to palpation |
| Q49 | varchar |  |  | SI | Abdominal palpation comment |
| Q50 | varchar |  |  | SI | Tenderness |
| Q51 | varchar |  |  | SI | Tenderness comment |
| Q52 | varchar |  |  | SI | Liver and spleen normal to palpation |
| Q53 | varchar |  |  | SI | Liver and spleen palpation comment |
| Q54 | varchar |  |  | SI | Bowel sounds normal |
| Q55 | varchar |  |  | SI | Bowel sounds comment |
| Q56 | varchar |  |  | SI | Abdomen other examination findings |
| Q57 | varchar |  |  | SI | Peripheral oedema |
| Q58 | varchar |  |  | SI | Peripheral oedema  comment |
| Q59 | varchar |  |  | SI | Clubbing |
| Q60 | varchar |  |  | SI | Clubbing comment |
| Q61 | varchar |  |  | SI | Phlebitis |
| Q62 | varchar |  |  | SI | Phlebitis comment |
| Q63 | varchar |  |  | SI | Extremities additional examination |
| Q64 | varchar |  |  | SI | Assessment additional details |
| Q65 | varchar |  |  | SI | Continue current medications and treatment plan |
| Q66 | varchar |  |  | SI | Plan additional details |
| Q67 | numeric |  |  | SI | Follow up in |
| Q68 | varchar |  |  | SI | Follow up date unit |
| Q69 | varchar |  |  | SI | I have discussed diagnosis and plan with patient /... |
| Q70 | varchar |  |  | SI | • Head, Eyes, Ears, Nose and Throat (HEENT) |
| Q71 | date |  |  | SI | Date |
| Q72 | time |  |  | SI | Time |
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