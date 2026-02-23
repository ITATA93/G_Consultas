# SQLUser.PAC_SynonymText

**Schema:** SQLUser
**Columnas:** 138
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| TXT_ParRef | bigint | PK |  | NO | PAC_Synonym Parent Reference |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | Condition |
| Q04 | - |  |  | SI | High risk condition |
| Q05 | - |  |  | SI | Age range |
| Q06 | - |  |  | SI | Criteria: |
| Q07 | - |  |  | SI | Heart Rate > 205 |
| Q08 | - |  |  | SI | Respiratory Rate: > 60 |
| Q09 | - |  |  | SI | Systolic BP: < 60 |
| Q10 | - |  |  | SI | Temperature: <36 or >38 |
| Q11 | - |  |  | SI | Criteria: |
| Q12 | - |  |  | SI | Heart Rate > 205 |
| Q13 | - |  |  | SI | Respiratory Rate: > 60 |
| Q14 | - |  |  | SI | Systolic BP: < 70 |
| Q15 | - |  |  | SI | Temperature: <36 or >38 |
| Q16 | - |  |  | SI | Criteria: |
| Q17 | - |  |  | SI | Heart Rate > 190 |
| Q18 | - |  |  | SI | Respiratory Rate: > 60 |
| Q19 | - |  |  | SI | Systolic BP: < 70 |
| Q20 | - |  |  | SI | Temperature: <36 or >38.5 |
| Q21 | - |  |  | SI | Criteria: |
| Q22 | - |  |  | SI | Heart Rate > 190 |
| Q23 | - |  |  | SI | Respiratory Rate: > 40 |
| Q24 | - |  |  | SI | Systolic BP: < 70 + (Age in yr x2) |
| Q25 | - |  |  | SI | Temperature: <36 or >38 |
| Q26 | - |  |  | SI | Criteria: |
| Q27 | - |  |  | SI | Heart Rate > 140 |
| Q28 | - |  |  | SI | Respiratory Rate: > 40 |
| Q29 | - |  |  | SI | Systolic BP: < 70 + (Age in yr x2) |
| Q30 | - |  |  | SI | Temperature: <36 or >38 |
| Q31 | - |  |  | SI | Criteria: |
| Q32 | - |  |  | SI | Heart Rate > 140 |
| Q33 | - |  |  | SI | Respiratory Rate: > 34 |
| Q34 | - |  |  | SI | Systolic BP: < 70 + (Age in yr x2) |
| Q35 | - |  |  | SI | Temperature: <36 or >38 |
| Q36 | - |  |  | SI | Criteria: |
| Q37 | - |  |  | SI | Heart Rate > 140 |
| Q38 | - |  |  | SI | Respiratory Rate: > 30 |
| Q39 | - |  |  | SI | Systolic BP: < 70 + (Age in yr x2) |
| Q40 | - |  |  | SI | Temperature: <36 or >38 |
| Q41 | - |  |  | SI | Criteria: |
| Q42 | - |  |  | SI | Heart Rate > 100 |
| Q43 | - |  |  | SI | Respiratory Rate: > 30 |
| Q44 | - |  |  | SI | Systolic BP: < 90 |
| Q45 | - |  |  | SI | Temperature: <36 or >38 |
| Q46 | - |  |  | SI | Criteria: |
| Q47 | - |  |  | SI | Heart Rate > 100 |
| Q48 | - |  |  | SI | Respiratory Rate: > 16 |
| Q49 | - |  |  | SI | Systolic BP: < 90 |
| Q50 | - |  |  | SI | Temperature: <36 or >38 |
| Q51 | - |  |  | SI | Temperature abnormal |
| Q52 | - |  |  | SI | Hypotension |
| Q53 | - |  |  | SI | Tachycardia |
| Q54 | - |  |  | SI | Capillary refill abnormal |
| Q55 | - |  |  | SI | Capillary refill (central vs. peripheral) |
| Q56 | - |  |  | SI | Mental status abnormal |
| Q57 | - |  |  | SI | Comment |
| Q58 | - |  |  | SI | Pulse abnormal |
| Q59 | - |  |  | SI | Pulse characteristics |
| Q60 | - |  |  | SI | Skin abnormal |
| Q61 | - |  |  | SI | Skin |
| Q62 | - |  |  | SI | Conclusion: (Positive or Negative based on the sco... |
| Q63 | - |  |  | SI | Patient will be positive if meets 3 or more risk f... |
| Q64 | - |  |  | SI | Patient will be positive if meets 2 or more risk f... |
| Q65 | - |  |  | SI | Score |
| Q66 | - |  |  | SI | Positive Low Risk |
| Q67 | - |  |  | SI | Positive High Risk |
| Q68 | - |  |  | SI | Negative High Risk |
| Q69 | - |  |  | SI | Negative Low Risk |
| Q70 | - |  |  | SI | Score |
| Q71 | - |  |  | SI | Classification |
| Q72 | - |  |  | SI | ≥ 3 |
| Q73 | - |  |  | SI | Positive Low Risk |
| Q74 | - |  |  | SI | <3 |
| Q75 | - |  |  | SI | Negative Low Risk |
| Q76 | - |  |  | SI | ≥ 2 |
| Q77 | - |  |  | SI | Positive High Risk |
| Q78 | - |  |  | SI | <2 |
| Q79 | - |  |  | SI | Negative High Risk |
| Q80 | - |  |  | SI | ≥ 3: 	Positive Low Risk |
| Q81 | - |  |  | SI | <3: Negative Low Risk |
| Q82 | - |  |  | SI | ≥ 2: Positive High Risk |
| Q83 | - |  |  | SI | <2: Negative High Risk |
| Q84 | - |  |  | SI | Pediatric Septic Shock Trigger Tool is used to all... |
| Q85 | - |  |  | SI | Tachypnea |
| Q86 | - |  |  | SI | Score |
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
| TXT_Childsub | double |  |  | NO | Childsub |
| TXT_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| TXT_CreatedDate | date |  |  | SI | Created Date |
| TXT_CreatedTime | time |  |  | SI | Created Time |
| TXT_CreatedUser_DR | bigint |  | FK | SI | Created User |
| TXT_RowId | varchar |  |  | NO | - |
| TXT_Sex_DR | bigint |  | FK | SI | Des Ref Sex |
| TXT_Text | varchar |  |  | SI | Text |
| TXT_UpdatedDate | date |  |  | SI | Updated Date |
| TXT_UpdatedTime | time |  |  | SI | Updated Time |
| TXT_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*