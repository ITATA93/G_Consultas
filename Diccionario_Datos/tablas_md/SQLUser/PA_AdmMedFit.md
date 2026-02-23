# SQLUser.PA_AdmMedFit

**Schema:** SQLUser
**Columnas:** 137
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Admisión de Pacientes**. Registra episodios de atención hospitalaria.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| MF_ParRef | bigint | PK |  | NO | PA_Adm Parent Reference |
| MF_Childsub | double |  |  | NO | Childsub |
| MF_DateMedFit | date |  |  | SI | Date Med Fit |
| MF_DateMedUnfit | date |  |  | SI | Date Med Unfit |
| MF_ReasonDelDisch_DR | bigint |  | FK | SI | Des Ref ReasonDelDisch_DR |
| MF_RowId | varchar |  |  | NO | - |
| MF_TimeMedFit | time |  |  | SI | Time Med Fit |
| MF_TimeMedUnfit | time |  |  | SI | Time Med Unfit |
| MF_UpdateDate | date |  |  | SI | UpdateDate |
| MF_UpdateTime | time |  |  | SI | UpdateTime |
| MF_UpdateUserHospital_DR | bigint |  | FK | SI | Des Ref UpdateUserHospital |
| MF_UpdateUser_DR | bigint |  | FK | SI | Des Ref UpdateUser |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | Testing procedure: Each item is verbally explained... |
| Q04 | - |  |  | SI | In the starting position, the patient is instructe... |
| Q05 | - |  |  | SI | In the starting position, the patient lifts both a... |
| Q06 | - |  |  | SI | From the starting position, the therapist position... |
| Q07 | - |  |  | SI | Left side |
| Q08 | - |  |  | SI | Right side |
| Q09 | - |  |  | SI | From the starting position, the patient crosses on... |
| Q10 | - |  |  | SI | Left side |
| Q11 | - |  |  | SI | Right side |
| Q12 | - |  |  | SI | From the starting position, the patient abducts on... |
| Q13 | - |  |  | SI | Left side |
| Q14 | - |  |  | SI | Right side |
| Q15 | - |  |  | SI | Total Static Sitting Balance Score |
| Q16 | - |  |  | SI | Testing procedure: |
| Q17 | - |  |  | SI | First, each item is verbally explained and demonst... |
| Q18 | - |  |  | SI | Secondly, the item is demonstrated on the patient ... |
| Q19 | - |  |  | SI | Thirdly, the patient is asked to perform the expec... |
| Q20 | - |  |  | SI | Then, the patient performs the item on its own in ... |
| Q21 | - |  |  | SI | From the starting position with the arms crossed o... |
| Q22 | - |  |  | SI | Is compensation noted? |
| Q23 | - |  |  | SI | From the starting position with the arms crossed o... |
| Q24 | - |  |  | SI | Is compensation noted? |
| Q25 | - |  |  | SI | From the starting position, the patient is instruc... |
| Q26 | - |  |  | SI | (by shortening the ipsilateral side and lengthenin... |
| Q27 | - |  |  | SI | Left side |
| Q28 | - |  |  | SI | Right side |
| Q29 | - |  |  | SI | When completing for the left side, does the patien... |
| Q30 | - |  |  | SI | When completing for the right side, does the patie... |
| Q31 | - |  |  | SI | When completing for the left side, is compensation... |
| Q32 | - |  |  | SI | When completing for the right side, is compensatio... |
| Q33 | - |  |  | SI | From the starting position, the patient is instruc... |
| Q34 | - |  |  | SI | Left side |
| Q35 | - |  |  | SI | Right side |
| Q36 | - |  |  | SI | When completing for the left side, does the patien... |
| Q37 | - |  |  | SI | When completing for the right side, does the patie... |
| Q38 | - |  |  | SI | When completing for the left side, is compensation... |
| Q39 | - |  |  | SI | When completing for the right side, is compensatio... |
| Q40 | - |  |  | SI | From the starting position with the arms crossed o... |
| Q41 | - |  |  | SI | (The movement is initiated from the shoulder girdl... |
| Q42 | - |  |  | SI | Does the patient rotate the upper trunk |
| Q43 | - |  |  | SI | From the starting position with the arms crossed o... |
| Q44 | - |  |  | SI | (The movement is initiated from the pelvic girdle)... |
| Q45 | - |  |  | SI | Does the patient compensate during the motion? |
| Q46 | - |  |  | SI | From the starting position with the arms crossed o... |
| Q47 | - |  |  | SI | (Shuffle movement = combination of lateral flexion... |
| Q48 | - |  |  | SI | Does the patient compensate during the motion? |
| Q49 | - |  |  | SI | Dynamic Sitting Balance |
| Q50 | - |  |  | SI | Total Selective Movement Control Score out of 28 |
| Q51 | - |  |  | SI | Testing procedure: Each item is verbally explained... |
| Q52 | - |  |  | SI | From the starting position with arms straight forw... |
| Q53 | - |  |  | SI | corresponding with the forearm length and return t... |
| Q54 | - |  |  | SI | From the starting position with one arm straight s... |
| Q55 | - |  |  | SI | positioned at a distance that corresponds with the... |
| Q56 | - |  |  | SI | Left side |
| Q57 | - |  |  | SI | Right side |
| Q58 | - |  |  | SI | From the starting position with one arm straight s... |
| Q59 | - |  |  | SI | (reach to the opposite side)and return to the star... |
| Q60 | - |  |  | SI | Left side |
| Q61 | - |  |  | SI | Right side |
| Q62 | - |  |  | SI | Total Dynamic Reaching Score |
| Q63 | - |  |  | SI | Total Dynamic Reaching Score out of 10 |
| Q64 | - |  |  | SI | Total TCMS Score |
| Q65 | - |  |  | SI | Total TCMS Score out of 58 |
| Q66 | - |  |  | SI | Test instructions |
| Q67 | - |  |  | SI | Orthoses, shoes and/or a trunk brace should be tak... |
| Q68 | - |  |  | SI | The thighs make full contact with the table. The h... |
| Q69 | - |  |  | SI | The patient is asked to sit upright at the start o... |
| Q70 | - |  |  | SI | The term ‘upright’ refers to the most upright sitt... |
| Q71 | - |  |  | SI | This position is the reference position for identi... |
| Q72 | - |  |  | SI | The best performance is taken into account for sco... |
| Q73 | - |  |  | SI | If the child performs the tasks of subscale ‘stati... |
| Q74 | - |  |  | SI | Score |
| Q75 | - |  |  | SI | Classification |
| Q76 | - |  |  | SI | The Trunk Control Measurement Scale is a scored qu... |
| Q77 | - |  |  | SI | trunk control in patients aged 5 years old and old... |
| Q78 | - |  |  | SI | The clinical tool assesses static and dynamic sitt... |
| Q79 | - |  |  | SI | to produce a score that indicates whether a child ... |
| Q80 | - |  |  | SI | The total score is a measure of motor impairment o... |
| Q81 | - |  |  | SI | Total static sitting balance: 0 - 20 |
| Q82 | - |  |  | SI | Dynamic sitting balance: 0 - 28 |
| Q83 | - |  |  | SI | Dynamic reaching (equilibrium reactions): 0 - 10 |
| Q84 | - |  |  | SI | Total TCMS score: 0 - 58 |
| Q85 | - |  |  | SI | A higher score means less trunk motor impairment a... |
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