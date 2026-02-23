# SQLUser.DICOM_UnassocImgs

**Schema:** SQLUser
**Columnas:** 113
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Imágenes Diagnósticas**. Radiología y estudios de imagen.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| DCUNASSOC_RowId | bigint | PK |  | NO | - |
| DCUNASSOC_AccessionNo | varchar |  |  | SI | AccessionNo |
| DCUNASSOC_Date | date |  |  | SI | Date |
| DCUNASSOC_Description | varchar |  |  | SI | Description |
| DCUNASSOC_ImgNo | varchar |  |  | SI | ImgNo |
| DCUNASSOC_Modality | varchar |  |  | SI | Modality |
| DCUNASSOC_PatID | varchar |  |  | SI | PatID |
| DCUNASSOC_PatName | varchar |  |  | SI | PatName |
| DCUNASSOC_Physician | varchar |  |  | SI | Physician |
| DCUNASSOC_Reason | varchar |  |  | SI | Reason |
| DCUNASSOC_StyUID | varchar |  |  | SI | StyUID |
| DCUNASSOC_Time | time |  |  | SI | Time |
| Q01 | - |  |  | SI | Restlessness / agitation |
| Q02 | - |  |  | SI | Mood changes |
| Q03 | - |  |  | SI | Fear |
| Q04 | - |  |  | SI | Sleep |
| Q05 | - |  |  | SI | Hunger |
| Q06 | - |  |  | SI | Feelings of unreality |
| Q07 | - |  |  | SI | Racing thoughts |
| Q08 | - |  |  | SI | Drowsiness - observation |
| Q09 | - |  |  | SI | Appetite |
| Q10 | - |  |  | SI | Other symptoms |
| Q11 | - |  |  | SI | Temperature |
| Q11ObsDR | - |  |  | SI | Temperature DR |
| Q12 | - |  |  | SI | Pulse |
| Q12ObsDR | - |  |  | SI | Pulse DR |
| Q13 | - |  |  | SI | Respiration |
| Q13ObsDR | - |  |  | SI | Respiration DR |
| Q14 | - |  |  | SI | Systolic BP |
| Q14ObsDR | - |  |  | SI | Systolic BP DR |
| Q15 | - |  |  | SI | Diastolic BP |
| Q15ObsDR | - |  |  | SI | Diastolic BP DR |
| Q16 | - |  |  | SI | Pupil size (L) |
| Q16ObsDR | - |  |  | SI | Pupil size (L) DR |
| Q17 | - |  |  | SI | Pupil reaction (L) |
| Q17ObsDR | - |  |  | SI | Pupil reaction (L) DR |
| Q18 | - |  |  | SI | Pupil size (R) |
| Q18ObsDR | - |  |  | SI | Pupil size (R) DR |
| Q19 | - |  |  | SI | Pupil reaction (R) |
| Q19ObsDR | - |  |  | SI | Pupil reaction (R) DR |
| Q20 | - |  |  | SI | Weight |
| Q20ObsDR | - |  |  | SI | Weight DR |
| Q21 | - |  |  | SI | Symptom |
| Q22 | - |  |  | SI | Scoring |
| Q23 | - |  |  | SI | Questions |
| Q24 | - |  |  | SI | Do you feel more restless than you are normally? |
| Q25 | - |  |  | SI | Are your moods changing over a short period of tim... |
| Q26 | - |  |  | SI | Do you feel fearful? |
| Q27 | - |  |  | SI | How did you sleep last night? |
| Q28 | - |  |  | SI | Do you feel hungry? |
| Q29 | - |  |  | SI | Are your thoughts racing? |
| Q30 | - |  |  | SI | Do you feel sleepy or drowsy?	 |
| Q31 | - |  |  | SI | Have you noticed any changes in your appetite? |
| Q32 | - |  |  | SI | Do you feel that things around you are not real or... |
| Q33 | - |  |  | SI | Score |
| Q34 | - |  |  | SI | Classification |
| Q35 | - |  |  | SI | 0 - 63 |
| Q36 | - |  |  | SI | 0 is no withdrawal symptoms and 63 is the most sev... |
| Q37 | - |  |  | SI | 0 - 63: 0 is no withdrawal symptoms and 63 is the ... |
| Q38 | - |  |  | SI | 0 is no withdrawal symptoms and 63 is the most sev... |
| Q39 | - |  |  | SI | The Cannabis Withdrawal Scale is used to assess th... |
| Q40 | - |  |  | SI | The Cannabis Withdrawal Scale is used to assess th... |
| Q41 | - |  |  | SI | Date |
| Q42 | - |  |  | SI | Time |
| Q43 | - |  |  | SI | Restlessness / agitation |
| Q44 | - |  |  | SI | Mood changes |
| Q45 | - |  |  | SI | Fear |
| Q46 | - |  |  | SI | Sleep |
| Q47 | - |  |  | SI | Hunger |
| Q48 | - |  |  | SI | Feelings of unreality |
| Q49 | - |  |  | SI | Racing thoughts |
| Q50 | - |  |  | SI | Drowsiness - observation |
| Q51 | - |  |  | SI | Appetite |
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