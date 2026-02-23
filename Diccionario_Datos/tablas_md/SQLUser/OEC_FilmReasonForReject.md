# SQLUser.OEC_FilmReasonForReject

**Schema:** SQLUser
**Columnas:** 139
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Entry Orders**. Tipos y estados de órdenes.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| FRR_RowId | bigint | PK |  | NO | - |
| ChildQ204DR | - |  |  | SI | Child Reference: Measurement |
| FRR_Code | varchar |  |  | NO | Code |
| FRR_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| FRR_CreatedDate | date |  |  | SI | Created Date |
| FRR_CreatedTime | time |  |  | SI | Created Time |
| FRR_CreatedUser_DR | bigint |  | FK | SI | Created User |
| FRR_Desc | varchar |  |  | NO | Description |
| FRR_Owner | varchar |  |  | SI | Owner |
| FRR_UpdatedDate | date |  |  | SI | Updated Date |
| FRR_UpdatedTime | time |  |  | SI | Updated Time |
| FRR_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q100 | - |  |  | SI | Method 1 |
| Q101 | - |  |  | SI | Method 2 |
| Q102 | - |  |  | SI | Method 3 |
| Q103 | - |  |  | SI | Result |
| Q104 | - |  |  | SI | Result |
| Q105 | - |  |  | SI | Result |
| Q106 | - |  |  | SI | Method |
| Q107 | - |  |  | SI | Right Eye |
| Q108 | - |  |  | SI | Left Eye |
| Q109 | - |  |  | SI | Right Eye |
| Q110 | - |  |  | SI | Left Eye |
| Q113 | - |  |  | SI | Right Eye |
| Q116 | - |  |  | SI | OD Inferior Oblique |
| Q131 | - |  |  | SI | Notes |
| Q145 | - |  |  | SI | Reflex - RAPD |
| Q146 | - |  |  | SI | Reflex - RAPD |
| Q151 | - |  |  | SI | Gaze |
| Q154 | - |  |  | SI | Amsler Grid |
| Q155 | - |  |  | SI | Size |
| Q190 | - |  |  | SI | Shape |
| Q200 | - |  |  | SI | Time |
| Q201 | - |  |  | SI | Posture |
| Q202 | - |  |  | SI | Abnormal head posture (AHP) |
| Q203 | - |  |  | SI | Specify abnormality |
| Q205 | - |  |  | SI | Notes |
| Q206 | - |  |  | SI | Notes |
| Q207 | - |  |  | SI | Diplopia Test |
| Q208 | - |  |  | SI | Annotated Image - Patterns of Cranial Nerve Palsie... |
| Q209 | - |  |  | SI | Diplopia notes |
| Q210 | - |  |  | SI | Diplopia test |
| Q38 | - |  |  | SI | Grading |
| Q39 | - |  |  | SI | Grading |
| Q40 | - |  |  | SI | Left Eye |
| Q41 | - |  |  | SI | Colour Vision |
| Q42 | - |  |  | SI | Reading |
| Q43 | - |  |  | SI | Amsler Grid |
| Q44 | - |  |  | SI | Stereopsis |
| Q45 | - |  |  | SI | Extra Ocular Movement (EOM) |
| Q46 | - |  |  | SI | Right Eye |
| Q47 | - |  |  | SI | Left eye |
| Q48 | - |  |  | SI | Right Eye |
| Q49 | - |  |  | SI | Left Eye |
| Q50 | - |  |  | SI | Right Left |
| Q51 | - |  |  | SI | Left Eye |
| Q52 | - |  |  | SI | OD Inferior Oblique |
| Q53 | - |  |  | SI | OD Inferior Oblique |
| Q53ObsDR | - |  |  | SI | OD Inferior Oblique DR |
| Q54 | - |  |  | SI | OD Lateral Rectus |
| Q54ObsDR | - |  |  | SI | OD Lateral Rectus DR |
| Q55 | - |  |  | SI | OS Lateral Rectus |
| Q55ObsDR | - |  |  | SI | OS Lateral Rectus DR |
| Q56 | - |  |  | SI | OD Medial Rectus |
| Q56ObsDR | - |  |  | SI | OD Medial Rectus DR |
| Q57 | - |  |  | SI | OD Superior Rectus |
| Q57ObsDR | - |  |  | SI | OD Superior Rectus DR |
| Q58 | - |  |  | SI | OS Superior Rectus |
| Q58ObsDR | - |  |  | SI | OS Superior Rectus DR |
| Q59 | - |  |  | SI | OS Medial Rectus |
| Q59ObsDR | - |  |  | SI | OS Medial Rectus DR |
| Q60 | - |  |  | SI | OD Inferior Rectus |
| Q60ObsDR | - |  |  | SI | OD Inferior Rectus DR |
| Q61 | - |  |  | SI | Notes |
| Q63 | - |  |  | SI | Size |
| Q64 | - |  |  | SI | OS Inferior Oblique |
| Q64ObsDR | - |  |  | SI | OS Inferior Oblique DR |
| Q65 | - |  |  | SI | Date |
| Q66 | - |  |  | SI | Shape |
| Q67 | - |  |  | SI | Size |
| Q69 | - |  |  | SI | Shape |
| Q70 | - |  |  | SI | OS Inferior Rectus |
| Q70ObsDR | - |  |  | SI | OS Inferior Rectus DR |
| Q71 | - |  |  | SI | OD Superior Oblique |
| Q71ObsDR | - |  |  | SI | OD Superior Oblique DR |
| Q72 | - |  |  | SI | OS Superior Oblique |
| Q72ObsDR | - |  |  | SI | OS Superior Oblique DR |
| Q82 | - |  |  | SI | OD Lateral Rectus |
| Q83 | - |  |  | SI | OS Lateral Rectus |
| Q84 | - |  |  | SI | OD Medial Rectus |
| Q85 | - |  |  | SI | OD Superior Rectus |
| Q86 | - |  |  | SI | OS Superior Rectus |
| Q87 | - |  |  | SI | OS Medial Rectus |
| Q88 | - |  |  | SI | OD Inferior Rectus |
| Q89 | - |  |  | SI | OS Inferior Rectus |
| Q90 | - |  |  | SI | OD Superior Oblique |
| Q91 | - |  |  | SI | OS Superior Oblique |
| Q92 | - |  |  | SI | OS Inferior Oblique |
| Q97 | - |  |  | SI | Cover test |
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