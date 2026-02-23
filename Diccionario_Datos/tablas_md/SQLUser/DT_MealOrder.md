# SQLUser.DT_MealOrder

**Schema:** SQLUser
**Columnas:** 117
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Dieta**. Gestión de alimentación de pacientes.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ORD_RowId | bigint | PK |  | NO | - |
| ORD_ARCIM_DR | varchar |  | FK | SI | Des Ref ARCIM |
| ORD_CTLOC_DR | bigint |  | FK | SI | Des Ref CTLOC |
| ORD_Date | date |  |  | SI | Date |
| ORD_MealType_DR | bigint |  | FK | SI | Des Ref MealType |
| ORD_Qty | double |  |  | SI | Qty |
| Q01 | - |  |  | SI | Follow up details |
| Q02 | - |  |  | SI | Follow up progress |
| Q03 | - |  |  | SI | Chest pain |
| Q04 | - |  |  | SI | Chest pain comments |
| Q05 | - |  |  | SI | Cough |
| Q06 | - |  |  | SI | Cough comments |
| Q07 | - |  |  | SI | Dyspnoea |
| Q08 | - |  |  | SI | Dyspnoea comments |
| Q09 | - |  |  | SI | Orthopnoea |
| Q10 | - |  |  | SI | Orthopnoea comments |
| Q11 | - |  |  | SI | Fever |
| Q12 | - |  |  | SI | Fever comments |
| Q13 | - |  |  | SI | Nausea and vomiting |
| Q14 | - |  |  | SI | Nausea and vomiting comments |
| Q15 | - |  |  | SI | Other symptoms |
| Q16 | - |  |  | SI | Objective findings |
| Q18 | - |  |  | SI | Physical Examination |
| Q19 | - |  |  | SI | Pale |
| Q20 | - |  |  | SI | Pale comment |
| Q21 | - |  |  | SI | Jaundice |
| Q22 | - |  |  | SI | Jaundice comment |
| Q23 | - |  |  | SI | Palpable lymph node |
| Q24 | - |  |  | SI | Palpable lymph node comment |
| Q25 | - |  |  | SI | HEENT other examination findings |
| Q26 | - |  |  | SI | Lungs clear |
| Q27 | - |  |  | SI | Lung comment |
| Q28 | - |  |  | SI | Fine crackles / rales |
| Q29 | - |  |  | SI | Fine crackles / rales  comment |
| Q30 | - |  |  | SI | Coarse crackles |
| Q31 | - |  |  | SI | Coarse crackles comment |
| Q32 | - |  |  | SI | Wheeze |
| Q33 | - |  |  | SI | Wheeze comment |
| Q34 | - |  |  | SI | Ronchi |
| Q35 | - |  |  | SI | Ronchi comments |
| Q36 | - |  |  | SI | Lungs other examination findings |
| Q37 | - |  |  | SI | Normal heart rate and sinus rhythm |
| Q38 | - |  |  | SI | Rate and rhythm comment |
| Q39 | - |  |  | SI | Normal S1 S2 |
| Q40 | - |  |  | SI | S1 S2 comment |
| Q41 | - |  |  | SI | Presence of S3 |
| Q42 | - |  |  | SI | S3 comment |
| Q43 | - |  |  | SI | Presence of S4 |
| Q44 | - |  |  | SI | S4 comment |
| Q45 | - |  |  | SI | Murmur |
| Q46 | - |  |  | SI | Murmur comment |
| Q47 | - |  |  | SI | CVS other examination findings |
| Q48 | - |  |  | SI | Soft to palpation |
| Q49 | - |  |  | SI | Abdominal palpation comment |
| Q50 | - |  |  | SI | Tenderness |
| Q51 | - |  |  | SI | Tenderness comment |
| Q52 | - |  |  | SI | Liver and spleen normal to palpation |
| Q53 | - |  |  | SI | Liver and spleen palpation comment |
| Q54 | - |  |  | SI | Bowel sounds normal |
| Q55 | - |  |  | SI | Bowel sounds comment |
| Q56 | - |  |  | SI | Abdomen other examination findings |
| Q57 | - |  |  | SI | Peripheral oedema |
| Q58 | - |  |  | SI | Peripheral oedema  comment |
| Q59 | - |  |  | SI | Clubbing |
| Q60 | - |  |  | SI | Clubbing comment |
| Q61 | - |  |  | SI | Phlebitis |
| Q62 | - |  |  | SI | Phlebitis comment |
| Q63 | - |  |  | SI | Extremities additional examination |
| Q64 | - |  |  | SI | Assessment additional details |
| Q65 | - |  |  | SI | Continue current medications and treatment plan |
| Q66 | - |  |  | SI | Plan additional details |
| Q67 | - |  |  | SI | Follow up in |
| Q68 | - |  |  | SI | Follow up date unit |
| Q69 | - |  |  | SI | I have discussed diagnosis and plan with patient /... |
| Q70 | - |  |  | SI | • Head, Eyes, Ears, Nose and Throat (HEENT) |
| Q71 | - |  |  | SI | Date |
| Q72 | - |  |  | SI | Time |
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