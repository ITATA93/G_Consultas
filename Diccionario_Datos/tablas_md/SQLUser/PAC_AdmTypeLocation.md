# SQLUser.PAC_AdmTypeLocation

**Schema:** SQLUser
**Columnas:** 165
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Tipos/categorías disponibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ADMLOC_RowId | bigint | PK |  | NO | - |
| ADMLOC_AdmType | varchar |  |  | SI | AdmType |
| ADMLOC_CTLOC_DR | bigint |  | FK | SI | Des Ref CTLOC_DR |
| ADMLOC_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| ADMLOC_CreatedDate | date |  |  | SI | Created Date |
| ADMLOC_CreatedTime | time |  |  | SI | Created Time |
| ADMLOC_CreatedUser_DR | bigint |  | FK | SI | Created User |
| ADMLOC_LocDesc | varchar |  |  | SI | Location Description |
| ADMLOC_Owner | varchar |  |  | SI | Owner |
| ADMLOC_UpdatedDate | date |  |  | SI | Updated Date |
| ADMLOC_UpdatedTime | time |  |  | SI | Updated Time |
| ADMLOC_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | 1. Plinth / Chair sitting |
| Q04 | - |  |  | SI | Can be over edge or on plinth / floor. Record best... |
| Q05 | - |  |  | SI | Can you sit on the plinth / chair without using yo... |
| Q06 | - |  |  | SI | Limited by contracture |
| Q07 | - |  |  | SI | Predominant spinal posture |
| Q08 | - |  |  | SI | 2.  Long sitting |
| Q09 | - |  |  | SI | Legs straight = knees maybe flexed, knee caps poin... |
| Q10 | - |  |  | SI | Can you sit on the plinth / chair without using yo... |
| Q100 | - |  |  | SI | Can you walk down the steps? You can use one raili... |
| Q101 | - |  |  | SI | Limited by contracture |
| Q102 | - |  |  | SI | 32. Ascends stairs without rail |
| Q103 | - |  |  | SI | Can you walk up the steps? This time try not to us... |
| Q104 | - |  |  | SI | Limited by contracture |
| Q105 | - |  |  | SI | 33. Descends stairs without rail |
| Q106 | - |  |  | SI | Can you walk down the steps? This time try not to ... |
| Q107 | - |  |  | SI | Limited by contracture |
| Q108 | - |  |  | SI | Score |
| Q109 | - |  |  | SI | Classification |
| Q11 | - |  |  | SI | Limited by contracture |
| Q110 | - |  |  | SI | 0 - 66 |
| Q111 | - |  |  | SI | Lower scores correspond to higher level of disabil... |
| Q112 | - |  |  | SI | 0 - 66: Lower scores correspond to higher level of... |
| Q113 | - |  |  | SI | Hammersmith Functional Motor Scale Expanded for SM... |
| Q12 | - |  |  | SI | Predominant leg posture |
| Q13 | - |  |  | SI | 3. One hand to head in sitting |
| Q14 | - |  |  | SI | Hand touch head above level of ears |
| Q15 | - |  |  | SI | Can you get one hand to your head without bending ... |
| Q16 | - |  |  | SI | Limited by contracture |
| Q17 | - |  |  | SI | 4. Two hands to head in sitting |
| Q18 | - |  |  | SI | Hands touch head above level of ear |
| Q19 | - |  |  | SI | Can you lift both hands up at the same time, to yo... |
| Q20 | - |  |  | SI | Limited by contracture |
| Q21 | - |  |  | SI | 5. Supine to side lying |
| Q22 | - |  |  | SI | Can you roll onto your side in both directions? Tr... |
| Q23 | - |  |  | SI | Limited by contracture |
| Q24 | - |  |  | SI | 6. Rolls prone to supine over R |
| Q25 | - |  |  | SI | Can you roll from your tummy to your back in both ... |
| Q26 | - |  |  | SI | Limited by contracture |
| Q27 | - |  |  | SI | 7. Rolls prone to supine over L |
| Q28 | - |  |  | SI | Can you roll from your tummy to your back in both ... |
| Q29 | - |  |  | SI | Limited by contracture |
| Q30 | - |  |  | SI | 8. Rolls supine to prone over R |
| Q31 | - |  |  | SI | Can you roll from your back to your front in both ... |
| Q32 | - |  |  | SI | Limited by contracture |
| Q33 | - |  |  | SI | 9. Rolls supine to prone over L |
| Q34 | - |  |  | SI | Can you roll from your back to your front in both ... |
| Q35 | - |  |  | SI | Limited by contracture |
| Q36 | - |  |  | SI | 10. Sitting to lying |
| Q37 | - |  |  | SI | Can you lie down in a controlled way from sitting? |
| Q38 | - |  |  | SI | Limited by contracture |
| Q39 | - |  |  | SI | 11. Props on forearms |
| Q40 | - |  |  | SI | Can you prop yourself on your forearms and hold fo... |
| Q41 | - |  |  | SI | Limited by contracture |
| Q42 | - |  |  | SI | 12. Lifts head from prone |
| Q43 | - |  |  | SI | Can you lift head up keeping your arms by your sid... |
| Q44 | - |  |  | SI | Limited by contracture |
| Q45 | - |  |  | SI | 13. Prop on extended arms |
| Q46 | - |  |  | SI | Can you prop yourself up with straight arms for a ... |
| Q47 | - |  |  | SI | Limited by contracture |
| Q48 | - |  |  | SI | 14. Lying to sitting |
| Q49 | - |  |  | SI | Can you get onto your hands and knees with your he... |
| Q50 | - |  |  | SI | Limited by contracture |
| Q51 | - |  |  | SI | 15. Four-point kneeling |
| Q52 | - |  |  | SI | Can you get onto your hands and knees with your he... |
| Q53 | - |  |  | SI | Limited by contracture |
| Q54 | - |  |  | SI | 16.  Crawling |
| Q55 | - |  |  | SI | Can you crawl forwards? |
| Q56 | - |  |  | SI | Limited by contracture |
| Q57 | - |  |  | SI | 17.  Lifts head from supine |
| Q58 | - |  |  | SI | Can you lift your head to look at your toes keepin... |
| Q59 | - |  |  | SI | Limited by contracture |
| Q60 | - |  |  | SI | 18. Supported standing |
| Q61 | - |  |  | SI | Can you stand using one hand for support for a cou... |
| Q62 | - |  |  | SI | Limited by contracture |
| Q63 | - |  |  | SI | 19. Stand unsupported |
| Q64 | - |  |  | SI | Can you stand without holding onto anything for a ... |
| Q65 | - |  |  | SI | Limited by contracture |
| Q66 | - |  |  | SI | 20. Stepping |
| Q67 | - |  |  | SI | Can you walk without using any help or aids? Show ... |
| Q68 | - |  |  | SI | Limited by contracture |
| Q69 | - |  |  | SI | 21. Right hip flexion in supine |
| Q70 | - |  |  | SI | Can you bring your right knee to your chest? Try t... |
| Q71 | - |  |  | SI | Limited by contracture |
| Q72 | - |  |  | SI | 22.  Left hip flexion in supine |
| Q73 | - |  |  | SI | Can you bring your left knee to your chest? Try to... |
| Q74 | - |  |  | SI | Limited by contracture |
| Q75 | - |  |  | SI | 23. High kneeling to right half kneel |
| Q76 | - |  |  | SI | Can you bring your left leg up so that your foot i... |
| Q77 | - |  |  | SI | Limited by contracture |
| Q78 | - |  |  | SI | 24. High kneeling to left half kneel |
| Q79 | - |  |  | SI | Can you bring your right leg up so that your foot ... |
| Q80 | - |  |  | SI | Limited by contracture |
| Q81 | - |  |  | SI | 25.  High kneeling to stand leading with left leg |
| Q82 | - |  |  | SI | Can you stand up from this position starting with ... |
| Q83 | - |  |  | SI | Limited by contracture |
| Q84 | - |  |  | SI | 26.  High keeling to stand leading with right leg |
| Q85 | - |  |  | SI | Can you stand up from this position starting with ... |
| Q86 | - |  |  | SI | Limited by contracture |
| Q87 | - |  |  | SI | 27. Stand to sit |
| Q88 | - |  |  | SI | Can you sit on the floor, in a controlled/safe way... |
| Q89 | - |  |  | SI | Limited by contracture |
| Q90 | - |  |  | SI | 28. Squat |
| Q91 | - |  |  | SI | Can you squat? Pretend you are going to sit in a v... |
| Q92 | - |  |  | SI | Limited by contracture |
| Q93 | - |  |  | SI | 29. Jump 12” forward |
| Q94 | - |  |  | SI | Can you jump as far as you can, with both feet, fr... |
| Q95 | - |  |  | SI | Limited by contracture |
| Q96 | - |  |  | SI | 30. Ascends stairs with rail |
| Q97 | - |  |  | SI | Can you walk up the steps? You can use one railing |
| Q98 | - |  |  | SI | Limited by contracture |
| Q99 | - |  |  | SI | 31. Descends stairs with rail |
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