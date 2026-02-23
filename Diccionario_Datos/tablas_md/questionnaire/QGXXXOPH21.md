# questionnaire.QGXXXOPH21

> Orthoptic Evaluations

**Schema:** questionnaire
**Columnas:** 128
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Orthoptic Evaluations

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q100 | varchar |  |  | SI | Method 1 |
| Q101 | varchar |  |  | SI | Method 2 |
| Q102 | varchar |  |  | SI | Method 3 |
| Q103 | varchar |  |  | SI | Result |
| Q104 | varchar |  |  | SI | Result |
| Q105 | varchar |  |  | SI | Result |
| Q106 | varchar |  |  | SI | Method |
| Q107 | varchar |  |  | SI | Right Eye |
| Q108 | varchar |  |  | SI | Left Eye |
| Q109 | varchar |  |  | SI | Right Eye |
| Q110 | varchar |  |  | SI | Left Eye |
| Q113 | varchar |  |  | SI | Right Eye |
| Q116 | varchar |  |  | SI | OD Inferior Oblique |
| Q131 | varchar |  |  | SI | Notes |
| Q145 | varchar |  |  | SI | Reflex - RAPD |
| Q146 | varchar |  |  | SI | Reflex - RAPD |
| Q151 | varchar |  |  | SI | Gaze |
| Q154 | varchar |  |  | SI | Amsler Grid |
| Q155 | varchar |  |  | SI | Size |
| Q190 | varchar |  |  | SI | Shape |
| Q200 | time |  |  | SI | Time |
| Q201 | varchar |  |  | SI | Posture |
| Q202 | varchar |  |  | SI | Abnormal head posture (AHP) |
| Q203 | varchar |  |  | SI | Specify abnormality |
| Q205 | varchar |  |  | SI | Notes |
| Q206 | varchar |  |  | SI | Notes |
| Q207 | varchar |  |  | SI | Diplopia Test |
| Q208 | varchar |  |  | SI | Annotated Image - Patterns of Cranial Nerve Palsie... |
| Q209 | varchar |  |  | SI | Diplopia notes |
| Q210 | varchar |  |  | SI | Diplopia test |
| Q38 | varchar |  |  | SI | Grading |
| Q39 | varchar |  |  | SI | Grading |
| Q40 | varchar |  |  | SI | Left Eye |
| Q41 | varchar |  |  | SI | Colour Vision |
| Q42 | varchar |  |  | SI | Reading |
| Q43 | varchar |  |  | SI | Amsler Grid |
| Q44 | varchar |  |  | SI | Stereopsis |
| Q45 | varchar |  |  | SI | Extra Ocular Movement (EOM) |
| Q46 | varchar |  |  | SI | Right Eye |
| Q47 | varchar |  |  | SI | Left eye |
| Q48 | varchar |  |  | SI | Right Eye |
| Q49 | varchar |  |  | SI | Left Eye |
| Q50 | varchar |  |  | SI | Right Left |
| Q51 | varchar |  |  | SI | Left Eye |
| Q52 | varchar |  |  | SI | OD Inferior Oblique |
| Q53 | varchar |  |  | SI | OD Inferior Oblique |
| Q53ObsDR | varchar |  | FK | SI | OD Inferior Oblique DR |
| Q54 | varchar |  |  | SI | OD Lateral Rectus |
| Q54ObsDR | varchar |  | FK | SI | OD Lateral Rectus DR |
| Q55 | varchar |  |  | SI | OS Lateral Rectus |
| Q55ObsDR | varchar |  | FK | SI | OS Lateral Rectus DR |
| Q56 | varchar |  |  | SI | OD Medial Rectus |
| Q56ObsDR | varchar |  | FK | SI | OD Medial Rectus DR |
| Q57 | varchar |  |  | SI | OD Superior Rectus |
| Q57ObsDR | varchar |  | FK | SI | OD Superior Rectus DR |
| Q58 | varchar |  |  | SI | OS Superior Rectus |
| Q58ObsDR | varchar |  | FK | SI | OS Superior Rectus DR |
| Q59 | varchar |  |  | SI | OS Medial Rectus |
| Q59ObsDR | varchar |  | FK | SI | OS Medial Rectus DR |
| Q60 | varchar |  |  | SI | OD Inferior Rectus |
| Q60ObsDR | varchar |  | FK | SI | OD Inferior Rectus DR |
| Q61 | varchar |  |  | SI | Notes |
| Q63 | varchar |  |  | SI | Size |
| Q64 | varchar |  |  | SI | OS Inferior Oblique |
| Q64ObsDR | varchar |  | FK | SI | OS Inferior Oblique DR |
| Q65 | date |  |  | SI | Date |
| Q66 | varchar |  |  | SI | Shape |
| Q67 | varchar |  |  | SI | Size |
| Q69 | varchar |  |  | SI | Shape |
| Q70 | varchar |  |  | SI | OS Inferior Rectus |
| Q70ObsDR | varchar |  | FK | SI | OS Inferior Rectus DR |
| Q71 | varchar |  |  | SI | OD Superior Oblique |
| Q71ObsDR | varchar |  | FK | SI | OD Superior Oblique DR |
| Q72 | varchar |  |  | SI | OS Superior Oblique |
| Q72ObsDR | varchar |  | FK | SI | OS Superior Oblique DR |
| Q82 | varchar |  |  | SI | OD Lateral Rectus |
| Q83 | varchar |  |  | SI | OS Lateral Rectus |
| Q84 | varchar |  |  | SI | OD Medial Rectus |
| Q85 | varchar |  |  | SI | OD Superior Rectus |
| Q86 | varchar |  |  | SI | OS Superior Rectus |
| Q87 | varchar |  |  | SI | OS Medial Rectus |
| Q88 | varchar |  |  | SI | OD Inferior Rectus |
| Q89 | varchar |  |  | SI | OS Inferior Rectus |
| Q90 | varchar |  |  | SI | OD Superior Oblique |
| Q91 | varchar |  |  | SI | OS Superior Oblique |
| Q92 | varchar |  |  | SI | OS Inferior Oblique |
| Q97 | varchar |  |  | SI | Cover test |
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