# SQLUser.PAC_WardTheatres

**Schema:** SQLUser
**Columnas:** 128
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| OTH_ParRef | bigint | PK |  | NO | PAC_Ward Parent Reference |
| OTH_CTLOC_DR | bigint |  | FK | SI | Des Ref CTLOC |
| OTH_Childsub | double |  |  | NO | Childsub |
| OTH_CreatedDate | date |  |  | SI | Created Date |
| OTH_CreatedTime | time |  |  | SI | Created Time |
| OTH_CreatedUser_DR | bigint |  | FK | SI | Created User |
| OTH_Resource_DR | bigint |  | FK | SI | Des Ref RBResource |
| OTH_RowId | varchar |  |  | NO | - |
| OTH_UpdatedDate | date |  |  | SI | Updated Date |
| OTH_UpdatedTime | time |  |  | SI | Updated Time |
| OTH_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | Sit to supine transition |
| Q04 | - |  |  | SI | The patient begins in the standard sitting positio... |
| Q05 | - |  |  | SI | Instructions: Please lie down on the mat. You may ... |
| Q06 | - |  |  | SI | Sit to supine transition |
| Q07 | - |  |  | SI | Supine to sit transition |
| Q08 | - |  |  | SI | The patient begins in a supine position on the mat... |
| Q09 | - |  |  | SI | Instructions: Please sit up on the edge of the mat... |
| Q10 | - |  |  | SI | Supine to sit transition |
| Q11 | - |  |  | SI | Scooting |
| Q12 | - |  |  | SI | The patient begins sitting on the mat table with f... |
| Q13 | - |  |  | SI | The goal is for the patient to scoot forward, whil... |
| Q14 | - |  |  | SI | Instructions: Please scoot forward so that you are... |
| Q15 | - |  |  | SI | Scooting |
| Q16 | - |  |  | SI | Quiet sitting - eyes open |
| Q17 | - |  |  | SI | The patient begins in the standard sitting positio... |
| Q18 | - |  |  | SI | Instructions: Please sit with your arms folded acr... |
| Q19 | - |  |  | SI | Quiet sitting - eyes open |
| Q20 | - |  |  | SI | Quiet sitting - eyes closed |
| Q21 | - |  |  | SI | The patient begins in the standard sitting positio... |
| Q22 | - |  |  | SI | Instructions: Please sit with your arms folded acr... |
| Q23 | - |  |  | SI | Quiet sitting - eyes closed |
| Q24 | - |  |  | SI | Turning to look over left shoulder: |
| Q25 | - |  |  | SI | The patient begins in the standard sitting positio... |
| Q26 | - |  |  | SI | Instructions: With your arms folded across your ch... |
| Q27 | - |  |  | SI | Turning to look over left shoulder |
| Q28 | - |  |  | SI | Turning to look over right shoulder: |
| Q29 | - |  |  | SI | The patient begins in the standard sitting positio... |
| Q30 | - |  |  | SI | Instructions: With your arms folded across your ch... |
| Q31 | - |  |  | SI | Turning to look over right shoulder |
| Q32 | - |  |  | SI | Picking up object from floor |
| Q33 | - |  |  | SI | The patient begins in the standard sitting positio... |
| Q34 | - |  |  | SI | Successful task complete involves forward reach to... |
| Q35 | - |  |  | SI | Instructions: Pick up the tennis ball from the flo... |
| Q36 | - |  |  | SI | Picking up object from floor - standard tennis bal... |
| Q37 | - |  |  | SI | Picking up object from floor - weighted tennis bal... |
| Q38 | - |  |  | SI | Lateral reaching |
| Q39 | - |  |  | SI | The patient begins in the standard sitting positio... |
| Q40 | - |  |  | SI | The examiner may provide active assistance and/or ... |
| Q41 | - |  |  | SI | From the distal aspect of the 3rd digit, 11 inches... |
| Q42 | - |  |  | SI | Instructions: Pick up the tennis ball from the mat... |
| Q43 | - |  |  | SI | Left lateral reaching - standard tennis ball |
| Q44 | - |  |  | SI | Right lateral reaching - standard tennis ball |
| Q45 | - |  |  | SI | Left lateral reaching - weighted tennis ball |
| Q46 | - |  |  | SI | Right lateral reaching - weighted tennis ball |
| Q47 | - |  |  | SI | External perturbation |
| Q48 | - |  |  | SI | The patient begins in the standard sitting positio... |
| Q49 | - |  |  | SI | Instructions: Please sit with your arms folded acr... |
| Q50 | - |  |  | SI | External perturbation |
| Q51 | - |  |  | SI | Lower extremity movement / changing base of suppor... |
| Q52 | - |  |  | SI | The patient begins in the standard sitting positio... |
| Q53 | - |  |  | SI | Instructions: Please sit with your arms folded acr... |
| Q54 | - |  |  | SI | Try to do this without using your arms on the mat ... |
| Q55 | - |  |  | SI | Lower extremity movement / changing base of suppor... |
| Q56 | - |  |  | SI | Sit to stand transfer |
| Q57 | - |  |  | SI | The patient begins in the standard sitting positio... |
| Q58 | - |  |  | SI | Instructions: Please stand up. Try to do this with... |
| Q59 | - |  |  | SI | Sit to stand transfer |
| Q60 | - |  |  | SI | General Instructions: Read each item and scoring c... |
| Q61 | - |  |  | SI | Circle the rating which best describes the patient... |
| Q62 | - |  |  | SI | Necessary equipment: Clinical mat table (hi-low id... |
| Q63 | - |  |  | SI | Standard Sitting Position: |
| Q64 | - |  |  | SI | 1) The patient sits symmetrically on a standard cl... |
| Q65 | - |  |  | SI | 2) ~50% of thigh length supported on the mat. |
| Q66 | - |  |  | SI | 3) Feet are on the floor with 8.5'' between medial... |
| Q67 | - |  |  | SI | 4) Hips, knees and ankles approximating 80-100 deg... |
| Q68 | - |  |  | SI | equipment must be safe for a sit to stand transfer... |
| Q69 | - |  |  | SI | 5) Hands should rest in the patient’s lap, with pa... |
| Q70 | - |  |  | SI | Interim Examiner Instructions: Orient the patient ... |
| Q71 | - |  |  | SI | Do not tell the patient which ball you will use fo... |
| Q72 | - |  |  | SI | Score |
| Q73 | - |  |  | SI | Classification |
| Q74 | - |  |  | SI | 0 - 64 |
| Q75 | - |  |  | SI | The higher the score the more independent the pati... |
| Q76 | - |  |  | SI | The Sitting Balance Assessment Tool is utilized by... |
| Q77 | - |  |  | SI | 0 - 64: The higher the score the more independent ... |
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