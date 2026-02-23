# questionnaire.QTCSITBAT

> Sitting Balance Assessment Tool (SitBAT)

**Schema:** questionnaire
**Columnas:** 118
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Sitting Balance Assessment Tool (SitBAT)

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date |  |  | SI | Date |
| Q02 | time |  |  | SI | Time |
| Q03 | varchar |  |  | SI | Sit to supine transition |
| Q04 | varchar |  |  | SI | The patient begins in the standard sitting positio... |
| Q05 | varchar |  |  | SI | Instructions: Please lie down on the mat. You may ... |
| Q06 | varchar |  |  | SI | Sit to supine transition |
| Q07 | varchar |  |  | SI | Supine to sit transition |
| Q08 | varchar |  |  | SI | The patient begins in a supine position on the mat... |
| Q09 | varchar |  |  | SI | Instructions: Please sit up on the edge of the mat... |
| Q10 | varchar |  |  | SI | Supine to sit transition |
| Q11 | varchar |  |  | SI | Scooting |
| Q12 | varchar |  |  | SI | The patient begins sitting on the mat table with f... |
| Q13 | varchar |  |  | SI | The goal is for the patient to scoot forward, whil... |
| Q14 | varchar |  |  | SI | Instructions: Please scoot forward so that you are... |
| Q15 | varchar |  |  | SI | Scooting |
| Q16 | varchar |  |  | SI | Quiet sitting - eyes open |
| Q17 | varchar |  |  | SI | The patient begins in the standard sitting positio... |
| Q18 | varchar |  |  | SI | Instructions: Please sit with your arms folded acr... |
| Q19 | varchar |  |  | SI | Quiet sitting - eyes open |
| Q20 | varchar |  |  | SI | Quiet sitting - eyes closed |
| Q21 | varchar |  |  | SI | The patient begins in the standard sitting positio... |
| Q22 | varchar |  |  | SI | Instructions: Please sit with your arms folded acr... |
| Q23 | varchar |  |  | SI | Quiet sitting - eyes closed |
| Q24 | varchar |  |  | SI | Turning to look over left shoulder: |
| Q25 | varchar |  |  | SI | The patient begins in the standard sitting positio... |
| Q26 | varchar |  |  | SI | Instructions: With your arms folded across your ch... |
| Q27 | varchar |  |  | SI | Turning to look over left shoulder |
| Q28 | varchar |  |  | SI | Turning to look over right shoulder: |
| Q29 | varchar |  |  | SI | The patient begins in the standard sitting positio... |
| Q30 | varchar |  |  | SI | Instructions: With your arms folded across your ch... |
| Q31 | varchar |  |  | SI | Turning to look over right shoulder |
| Q32 | varchar |  |  | SI | Picking up object from floor |
| Q33 | varchar |  |  | SI | The patient begins in the standard sitting positio... |
| Q34 | varchar |  |  | SI | Successful task complete involves forward reach to... |
| Q35 | varchar |  |  | SI | Instructions: Pick up the tennis ball from the flo... |
| Q36 | varchar |  |  | SI | Picking up object from floor - standard tennis bal... |
| Q37 | varchar |  |  | SI | Picking up object from floor - weighted tennis bal... |
| Q38 | varchar |  |  | SI | Lateral reaching |
| Q39 | varchar |  |  | SI | The patient begins in the standard sitting positio... |
| Q40 | varchar |  |  | SI | The examiner may provide active assistance and/or ... |
| Q41 | varchar |  |  | SI | From the distal aspect of the 3rd digit, 11 inches... |
| Q42 | varchar |  |  | SI | Instructions: Pick up the tennis ball from the mat... |
| Q43 | varchar |  |  | SI | Left lateral reaching - standard tennis ball |
| Q44 | varchar |  |  | SI | Right lateral reaching - standard tennis ball |
| Q45 | varchar |  |  | SI | Left lateral reaching - weighted tennis ball |
| Q46 | varchar |  |  | SI | Right lateral reaching - weighted tennis ball |
| Q47 | varchar |  |  | SI | External perturbation |
| Q48 | varchar |  |  | SI | The patient begins in the standard sitting positio... |
| Q49 | varchar |  |  | SI | Instructions: Please sit with your arms folded acr... |
| Q50 | varchar |  |  | SI | External perturbation |
| Q51 | varchar |  |  | SI | Lower extremity movement / changing base of suppor... |
| Q52 | varchar |  |  | SI | The patient begins in the standard sitting positio... |
| Q53 | varchar |  |  | SI | Instructions: Please sit with your arms folded acr... |
| Q54 | varchar |  |  | SI | Try to do this without using your arms on the mat ... |
| Q55 | varchar |  |  | SI | Lower extremity movement / changing base of suppor... |
| Q56 | varchar |  |  | SI | Sit to stand transfer |
| Q57 | varchar |  |  | SI | The patient begins in the standard sitting positio... |
| Q58 | varchar |  |  | SI | Instructions: Please stand up. Try to do this with... |
| Q59 | varchar |  |  | SI | Sit to stand transfer |
| Q60 | varchar |  |  | SI | General Instructions: Read each item and scoring c... |
| Q61 | varchar |  |  | SI | Circle the rating which best describes the patient... |
| Q62 | varchar |  |  | SI | Necessary equipment: Clinical mat table (hi-low id... |
| Q63 | varchar |  |  | SI | Standard Sitting Position: |
| Q64 | varchar |  |  | SI | 1) The patient sits symmetrically on a standard cl... |
| Q65 | varchar |  |  | SI | 2) ~50% of thigh length supported on the mat. |
| Q66 | varchar |  |  | SI | 3) Feet are on the floor with 8.5'' between medial... |
| Q67 | varchar |  |  | SI | 4) Hips, knees and ankles approximating 80-100 deg... |
| Q68 | varchar |  |  | SI | equipment must be safe for a sit to stand transfer... |
| Q69 | varchar |  |  | SI | 5) Hands should rest in the patient’s lap, with pa... |
| Q70 | varchar |  |  | SI | Interim Examiner Instructions: Orient the patient ... |
| Q71 | varchar |  |  | SI | Do not tell the patient which ball you will use fo... |
| Q72 | varchar |  |  | SI | Score |
| Q73 | varchar |  |  | SI | Classification |
| Q74 | varchar |  |  | SI | 0 - 64 |
| Q75 | varchar |  |  | SI | The higher the score the more independent the pati... |
| Q76 | varchar |  |  | SI | The Sitting Balance Assessment Tool is utilized by... |
| Q77 | varchar |  |  | SI | 0 - 64: The higher the score the more independent ... |
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