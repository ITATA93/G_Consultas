# SQLUser.OE_OrdExecStatus

**Schema:** SQLUser
**Columnas:** 165
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Órdenes Médicas**. Solicitudes de exámenes, procedimientos, etc. Estados posibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| STCH_ParRef | varchar | PK |  | NO | OE_OrdExec Parent Reference |
| ChildQ17DR | - |  |  | SI | Child Reference: Constant Symptom |
| Q01 | - |  |  | SI | Occupation |
| Q02 | - |  |  | SI | Work: Mechanical Stress |
| Q03 | - |  |  | SI | Other |
| Q04 | - |  |  | SI | Leisure: Mechanical Stress |
| Q05 | - |  |  | SI | Other |
| Q06 | - |  |  | SI | Pain Location |
| Q07 | - |  |  | SI | Mark the pain location |
| Q08 | - |  |  | SI | VAS Score |
| Q09 | - |  |  | SI | Is Your Pain |
| Q10 | - |  |  | SI | Pain Description |
| Q100 | - |  |  | SI | Walk a few blocks (300-400 m)? |
| Q101 | - |  |  | SI | Walk several kilometers? |
| Q102 | - |  |  | SI | Reach up to high shelves? |
| Q103 | - |  |  | SI | Throw a ball? |
| Q104 | - |  |  | SI | Run one block (about 100m)? |
| Q105 | - |  |  | SI | Take food out of the refrigerator? |
| Q106 | - |  |  | SI | Make your bed? |
| Q107 | - |  |  | SI | Put on socks (pantyhose)? |
| Q108 | - |  |  | SI | Bend over to clean the bathtub? |
| Q109 | - |  |  | SI | Move a chair? |
| Q11 | - |  |  | SI | Pain Present Since |
| Q110 | - |  |  | SI | Pull or push heavy doors? |
| Q111 | - |  |  | SI | Carry two bags of groceries? |
| Q112 | - |  |  | SI | Lift and carry a heavy suitcase? |
| Q113 | - |  |  | SI | Observation |
| Q114 | - |  |  | SI | Pelvic Landmarks |
| Q115 | - |  |  | SI | Tenderness on Palpation |
| Q116 | - |  |  | SI | Gait |
| Q117 | - |  |  | SI | Static Tests |
| Q118 | - |  |  | SI | Special Tests |
| Q12 | - |  |  | SI | Pain Progress |
| Q13 | - |  |  | SI | Current Pain History |
| Q14 | - |  |  | SI | Commenced as a Result of |
| Q15 | - |  |  | SI | Other |
| Q16 | - |  |  | SI | Symptoms At Onset |
| Q18 | - |  |  | SI | Pain Pattern Worse With the Following |
| Q19 | - |  |  | SI | Other |
| Q20 | - |  |  | SI | Pain Pattern Better With the Following |
| Q21 | - |  |  | SI | Other |
| Q22 | - |  |  | SI | Gait |
| Q23 | - |  |  | SI | Disturbed Sleep |
| Q24 | - |  |  | SI | Sleeping Postures |
| Q25 | - |  |  | SI | Surface |
| Q26 | - |  |  | SI | Previous Episodes |
| Q27 | - |  |  | SI | Year of First Episode |
| Q28 | - |  |  | SI | Cough / Sneeze / Strain |
| Q29 | - |  |  | SI | Night Pain |
| Q30 | - |  |  | SI | General Health |
| Q31 | - |  |  | SI | Medical History |
| Q32 | - |  |  | SI | Other |
| Q33 | - |  |  | SI | Medications |
| Q34 | - |  |  | SI | Other |
| Q35 | - |  |  | SI | Bladder |
| Q36 | - |  |  | SI | Previous Surgery |
| Q37 | - |  |  | SI | Comment |
| Q38 | - |  |  | SI | Previous Physical Therapy Treatment |
| Q39 | - |  |  | SI | X-ray |
| Q40 | - |  |  | SI | Report |
| Q41 | - |  |  | SI | Unexplained Weight Loss |
| Q42 | - |  |  | SI | Patient Goals |
| Q43 | - |  |  | SI | Sitting |
| Q44 | - |  |  | SI | Standing |
| Q45 | - |  |  | SI | Lordosis |
| Q46 | - |  |  | SI | Lateral Shift |
| Q47 | - |  |  | SI | Posture |
| Q48 | - |  |  | SI | Correction of Posture |
| Q49 | - |  |  | SI | Iliac Crest Front |
| Q50 | - |  |  | SI | Iliac Crest Back |
| Q51 | - |  |  | SI | Iliac Crest PSIS |
| Q52 | - |  |  | SI | Iliac Crest ASIS |
| Q53 | - |  |  | SI | Paraspinous muscles |
| Q54 | - |  |  | SI | Sacroiliac joints |
| Q55 | - |  |  | SI | Tip of coccyx |
| Q56 | - |  |  | SI | Percussion over spine |
| Q57 | - |  |  | SI | Other |
| Q63 | - |  |  | SI | Heel Walking |
| Q64 | - |  |  | SI | Toe Walking |
| Q65 | - |  |  | SI | Sitting Slouched |
| Q66 | - |  |  | SI | Sitting Erect |
| Q67 | - |  |  | SI | Standing Slouched |
| Q68 | - |  |  | SI | Standing Erect |
| Q69 | - |  |  | SI | Lying Prone in Extension |
| Q70 | - |  |  | SI | Long Sitting |
| Q71 | - |  |  | SI | Straight Leg Raise |
| Q72 | - |  |  | SI | Slump Test |
| Q73 | - |  |  | SI | Valsalva Maneuver |
| Q74 | - |  |  | SI | Other Special Test |
| Q75 | - |  |  | SI | Diagnosis |
| Q76 | - |  |  | SI | Derangement Pain Location |
| Q77 | - |  |  | SI | Other Diagnosis |
| Q78 | - |  |  | SI | Problems List |
| Q79 | - |  |  | SI | Rehabilitation Potential |
| Q80 | - |  |  | SI | Family / Patient involved in and verbalized unders... |
| Q81 | - |  |  | SI | Comment |
| Q82 | - |  |  | SI | Education |
| Q83 | - |  |  | SI | Short Term Goals |
| Q84 | - |  |  | SI | Long Term Goals |
| Q85 | - |  |  | SI | Number of Treatments per week |
| Q86 | - |  |  | SI | Number of weeks |
| Q87 | - |  |  | SI | Re Evaluation |
| Q88 | - |  |  | SI | Mechanical Therapy |
| Q89 | - |  |  | SI | Therapy Type |
| Q90 | - |  |  | SI | Others |
| Q91 | - |  |  | SI | Comment |
| Q92 | - |  |  | SI | Quebec Back Pain Disability Scale |
| Q93 | - |  |  | SI | Get out of bed? |
| Q94 | - |  |  | SI | Sleep through the night? |
| Q95 | - |  |  | SI | Turn over in bed? |
| Q96 | - |  |  | SI | Ride in a car? |
| Q97 | - |  |  | SI | Stand up for 20-30 minutes? |
| Q98 | - |  |  | SI | Sit in a chair for several hours? |
| Q99 | - |  |  | SI | Climb one flight of stairs? |
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
| STCH_AdminStatus_DR | bigint |  | FK | SI | Des Ref AdminStatus |
| STCH_ChangedAdminDate | date |  |  | SI | ChangedAdminDate |
| STCH_ChangedAdminTime | time |  |  | SI | ChangedAdminTime |
| STCH_Childsub | double |  |  | NO | Childsub |
| STCH_Date | date |  |  | SI | Date |
| STCH_OverseeUser_DR | bigint |  | FK | SI | Des Ref OverseeUser |
| STCH_Reason_DR | bigint |  | FK | SI | Des Ref Status Change Reason |
| STCH_RowId | varchar |  |  | NO | - |
| STCH_SetBySystem | varchar |  |  | SI | Is Set By System |
| STCH_Time | time |  |  | SI | Time |
| STCH_User_DR | bigint |  | FK | SI | Des Ref User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*