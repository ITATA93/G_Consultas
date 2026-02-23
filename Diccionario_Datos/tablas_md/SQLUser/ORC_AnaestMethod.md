# SQLUser.ORC_AnaestMethod

**Schema:** SQLUser
**Columnas:** 160
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Órdenes**. Parámetros de órdenes médicas.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ANMET_RowId | bigint | PK |  | NO | - |
| ANMET_ARCOS_DR | varchar |  | FK | SI | Des Ref ARCOS |
| ANMET_AvAnaesTime | double |  |  | SI | Average Anaesthetic Time (minutes), Anaesthetic Ti... |
| ANMET_Code | varchar |  |  | NO | Anaesth. Method Code |
| ANMET_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| ANMET_CodeTranslated | varchar |  |  | SI | - |
| ANMET_CreatedDate | date |  |  | SI | Created Date |
| ANMET_CreatedTime | time |  |  | SI | Created Time |
| ANMET_CreatedUser_DR | bigint |  | FK | SI | Created User |
| ANMET_DateFrom | date |  |  | SI | Date From |
| ANMET_DateTo | date |  |  | SI | Date To |
| ANMET_Desc | varchar |  |  | NO | Anaesth. Method Description |
| ANMET_DescTranslated | varchar |  |  | SI | - |
| ANMET_Owner | varchar |  |  | SI | Owner |
| ANMET_RequiresFasting | varchar |  |  | SI | Method Requires Fasting  |
| ANMET_Type_DR | bigint |  | FK | SI | Des Ref Type |
| ANMET_UpdatedDate | date |  |  | SI | Updated Date |
| ANMET_UpdatedTime | time |  |  | SI | Updated Time |
| ANMET_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | PRE-MORBID |
| Q02 | - |  |  | SI | Level of mobility |
| Q03 | - |  |  | SI | Falls within last 6/12 |
| Q04 | - |  |  | SI | History of falls |
| Q05 | - |  |  | SI | Home environment |
| Q06 | - |  |  | SI | Patient’s perceived problems |
| Q07 | - |  |  | SI | Patient’s goals for rehabilitation |
| Q08 | - |  |  | SI | Chest / Swallowing |
| Q09 | - |  |  | SI | Communication |
| Q10 | - |  |  | SI | Orientation / Cognition / Behaviour |
| Q100 | - |  |  | SI | Gait aid |
| Q100ObsDR | - |  |  | SI | Gait aid DR |
| Q11 | - |  |  | SI | Mini-Mental State Examination (MMSE) score |
| Q12 | - |  |  | SI | Vision / Hearing |
| Q13 | - |  |  | SI | Perceptual / Spatial / Neglect |
| Q14 | - |  |  | SI | Skin / Pressure |
| Q15 | - |  |  | SI | Braden score |
| Q16 | - |  |  | SI | BED MOBILITY |
| Q17 | - |  |  | SI | Rolling left |
| Q18 | - |  |  | SI | Rolling right |
| Q19 | - |  |  | SI | Bridging |
| Q20 | - |  |  | SI | Lie to sit to lie |
| Q21 | - |  |  | SI | SITTING |
| Q22 | - |  |  | SI | Static posture |
| Q23 | - |  |  | SI | Can sit unsupported |
| Q24 | - |  |  | SI | Time |
| Q25 | - |  |  | SI | Observation |
| Q26 | - |  |  | SI | Dynamic sitting balance & trunk control observatio... |
| Q27 | - |  |  | SI | SIT TO STAND |
| Q28 | - |  |  | SI | Sit to stand |
| Q29 | - |  |  | SI | Observation |
| Q30 | - |  |  | SI | STANDING / STANDING TRANSFERS |
| Q31 | - |  |  | SI | Can stand unsupported |
| Q32 | - |  |  | SI | Observation |
| Q33 | - |  |  | SI | MOBILITY |
| Q34 | - |  |  | SI | Mobility |
| Q35 | - |  |  | SI | Gait aid |
| Q36 | - |  |  | SI | Observation |
| Q37 | - |  |  | SI | STAIRS / OUTDOOR / RUNNING |
| Q38 | - |  |  | SI | Single step |
| Q39 | - |  |  | SI | Stairs |
| Q40 | - |  |  | SI | Slopes / Rough Ground |
| Q41 | - |  |  | SI | Cross road safely |
| Q42 | - |  |  | SI | Running / Sport |
| Q43 | - |  |  | SI | HiMAT indicated |
| Q44 | - |  |  | SI | Score |
| Q45 | - |  |  | SI | / 54 |
| Q46 | - |  |  | SI | CO-ORDINATION |
| Q47 | - |  |  | SI | Finger / Nose (x10) left |
| Q48 | - |  |  | SI | secs |
| Q49 | - |  |  | SI | Finger / Nose (x10) right |
| Q50 | - |  |  | SI | secs |
| Q51 | - |  |  | SI | Sup / Pron (x10) left |
| Q52 | - |  |  | SI | secs |
| Q53 | - |  |  | SI | Sup / Pron (x10) right |
| Q54 | - |  |  | SI | secs |
| Q55 | - |  |  | SI | Heel / Shin (x10) left |
| Q56 | - |  |  | SI | Heel / Shin (x10) right |
| Q57 | - |  |  | SI | secs |
| Q58 | - |  |  | SI | secs |
| Q59 | - |  |  | SI | Comments |
| Q60 | - |  |  | SI | Main problems identified |
| Q61 | - |  |  | SI | Physiotherapy plan / goals |
| Q62 | - |  |  | SI | UPPER LIMB |
| Q63 | - |  |  | SI | Hand dominance |
| Q64 | - |  |  | SI | Hand oedema |
| Q65 | - |  |  | SI | Shoulder subluxation |
| Q66 | - |  |  | SI | Distance |
| Q67 | - |  |  | SI | mm |
| Q68 | - |  |  | SI | Ritchie articular index - left |
| Q69 | - |  |  | SI | ROM |
| Q70 | - |  |  | SI | Ritchie articular index - right |
| Q71 | - |  |  | SI | ROM |
| Q72 | - |  |  | SI | (Test in supine, 30° Abduction) |
| Q73 | - |  |  | SI | Hand dominance |
| Q74 | - |  |  | SI | Hand oedema |
| Q75 | - |  |  | SI | Shoulder subluxation |
| Q76 | - |  |  | SI | BALANCE MEASURES |
| Q77 | - |  |  | SI | Left |
| Q78 | - |  |  | SI | Right |
| Q79 | - |  |  | SI | Pick up object from floor |
| Q80 | - |  |  | SI | Seated position |
| Q81 | - |  |  | SI | Standing position |
| Q82 | - |  |  | SI | Limits of stability (internal / external perturbat... |
| Q83 | - |  |  | SI | Ankle strategy |
| Q84 | - |  |  | SI | Hip strategy |
| Q85 | - |  |  | SI | Step strategy |
| Q86 | - |  |  | SI | Frequency |
| Q87 | - |  |  | SI | Cause(s) |
| Q88 | - |  |  | SI | Falls prevention strategies in place |
| Q89 | - |  |  | SI | Social |
| Q90 | - |  |  | SI | Supports |
| Q91 | - |  |  | SI | Services |
| Q92 | - |  |  | SI | Occupation / Leisure |
| Q93 | - |  |  | SI | Continence |
| Q94 | - |  |  | SI | If no, assistance required |
| Q95 | - |  |  | SI | Able to reach outside of base of support (BOS) and... |
| Q96 | - |  |  | SI | Functional reach |
| Q97 | - |  |  | SI | Comments |
| Q98 | - |  |  | SI | Date |
| Q99 | - |  |  | SI | Time |
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